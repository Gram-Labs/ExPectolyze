# ExPectolyze

Analysis suite for use with the ExPecto deep learning variant expression prediction model. This README serves as a writeup of my 2019 work in the [Ruderfer lab](https://github.com/RuderferLab) + some thoughts on potential further development of a project integrating multiple pipelines of deep learning functional SNV annotation for non-coding DNA sequences. Utilizes the [ExPecto](https://github.com/functionlab/expecto) tissue-specific, deep learning framework using variants + sequence data to predict significant functional variants. 


## Motivation [Background]

### Variant annotation / deep learning

- Important clinical significance in looking for cases where genes of recurrence have been definitively implicated in disease phenotype - however, in non-coding sequences there's no visible enrichment because we can't interpret their effect
- The main goal of new ML methods is to interpret likely functional effects of point mutations in NC regions
- We need to be able to annotate regions to elucidate functional significance
- We've never thought previously about methods to integrate analysis of common and rare variants, but with new ways to combine them in terms of observable phenotype this should be a good outlook moving forward
- Question: can we find new rare variants that can be validated with RNA seq data afterwards?

### Integrating functional prediction methods

- Integrating methods in an easily accessible and combinatorial fashion would be a significant next step in the ease of use of the plethora of resources in the current literature
- Existing web APIs for using open-source deep learning methods
    - none of these offer a way to analyze the same data (if possible) across multiple methods/approaches
    - would be interesting to be able to compare data thru analysis this way


## ExPecto [Present]

### Important commands (3 steps)

chromatin.py step

```
python chromatin.py ../first1k_final.vcf
```

Intermediate/precursor step to prediction (decides associated gene for predicted expression effect)

```
closest-features --delim '\t' --closest --dist <(awk '{printf $1"\t"$2-1"\t"$2"\n"}' first1k_final.vcf|sed s/chr//g|sed s/^/chr/g|sort-bed - ) ./resources/geneanno.pc.sorted.bed > first1k_final.vcf.bed.sorted.bed.closestgene
```

predict.py step

```
python predict.py --coorFile ../first1k_final.vcf --geneFile first1k_final.vcf.bed.sorted.bed.closestgene --snpEffectFilePattern first1k_final.vcf.shift_SHIFT.diff.h5 --modelList ./resources/modellist --output output.csv
```


### Output

Contents of output.csv:

- 'Name': Table of common and rare variants with strong predicted expression effects (used with hg19 genome build version)
- First 7 columns the same as .vcf file
- Additional columns include predicted expression effect (log fold change) for each of the input models in the order given by the `modelList` file (contains model names and associated tissues)

    `Chr, Position, Ref, Alt, MAF, is_gtexv6_eqt1, expecto predicted max expression effect`


### Flow / Analysis

- Use ExPecto output to compare to existing data for the purpose of validating model in the context of our research
- Overall steps: 
	1. Get reasonable set of good previously-annotated variants (effect coding seq) - whole-genome .vcf file
	2. Look at prediction outputs from ExPecto 
	3. Map expression [validation data?] to see if:
		i.  predictions are correct
		ii. how well they line up with our data
	4. Figure out how to streamline steps 2 and 3 as the initial step
	5. Figure out future examples
        i. Ex. promoter/enhancer data: find variants in this region and check if we see effects in expression on the gene that these promoters/enhancers impact 


### TO-DO (analysis)

- [ ] Find out which variants of the set that ExPecto marked as strong predictors are 'rare' and noncoding (unless the original dataset is all noncoding anyway?) since that's an important part of overall research focus
	- Non-coding variants = ones located in regions classified as non-coding
	- Rare variants = ???
	- Need to find a database that can be parsed with script to make comparisons to ExPecto-indicted strong variants

- [ ] Carry out ExPecto analysis over and over till 10k worth of input datafile variants have been processed through the system and stored in a single output file - IN PROGRESS

- [ ] Write script to map RNA-seq data to ExPecto results for another method of model validation in our lab's context
    - Filename: `HBCC_DLPFC_eqtlResidualExpression_WithoutSVbasedOutierIndividualsV2.tsv`
        - HBCC: Human Brain Collection Core; DLPFC: Dorsolateral Prefronal Cortex; PFC: Perfluorocarbon 
    - More info: https://kbase.us/data-upload-download-guide/expression-matrix/
    - This file is a matrix of relative RNA-seq readouts (actual values) across different sample observations (x-axis legend) and across different ENSEMBL gene IDs (y-axis legend)
    - Match gene IDs to ones in the intermediate ExPecto/BEDOPS step (only for ones in the final output that were considered strong)
    - Evaluate whether significance from ExPecto carries over to significance in expression matrix and vice versa

### TO-DO (non-analysis)

- [x] trim modelList to only include brain/dorsolateral prefrontal cortex tissue models
- [x] overall clean up code in chromatin.py and predict.py
- [ ] add some more logging + script runtime and memory usage reporting to `chromatin.py` and `predict.py`
    - start of script, after major steps, etc
    - timing of major steps as well as total time (will need to import package)
- [x] improve requirements.txt as well as another list of other packages (bedops) that require additional installation steps
- [ ] write main executable python script that combines all the steps in one (with some basic error handling)
    - should be able to take raw input (whole-genome, compressed) file and desired number of variants and do all the steps up to final input



## Prediction Pipeline [Future]

### Ideas

- Online resource that functions like Kipoi (downloadable API + online user interface) but for simultaneous integration of multiple methods of NCSV functional prediction instead of a showcase of methods that aren't otherwise similar to one another
    - Example of something cool: https://hb.flatironinstitute.org/expecto/ 
    - Kipoi API docs: https://github.com/kipoi/kipoi

### Components

- Better multiprocessing/subprocessing of larger data inputs since it takes way too much time now
    - divide by x number of cores per task available to make process more efficient
