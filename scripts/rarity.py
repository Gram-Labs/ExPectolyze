import csv,os,json

# Rarity index = 78 from the front, 35 from the back
# ex. for the first line, value = 0.5929

rarityFile = '/data/ruderferlab/sandbox/grahame/expecto/data/allchroms.genome_annovar.vcf'
data = '/data/ruderferlab/sandbox/grahame/expecto/data/postmap_filtered.tsv'
outputFile = '/data/ruderferlab/sandbox/grahame/expecto/data/postmap_plusrarity.tsv'

output = csv.writer(open(outputFile, 'w'), delimiter='\t')
output.writerow(['variant'] + ['gene'] + ['expectoValue'] + ['distance_to_tss'] + ['gnomad_score_all'] + ['dna_rna_ids'])

with open (rarityFile, 'r') as rarefile, open(data, 'r') as datafile:
    rarereader = csv.reader(rarefile, delimiter='\t')
    datareader = csv.reader(datafile, delimiter='\t')

    for line in datareader:
        variant = line[0]
        gene = line[1]
        expectoValue = line[2]
        tss = line[3]
        ids = line[4]

        for line1 in rarereader: 
            rVariant = line1[1]
            if rVariant == variant:
                gnomad_score = line1[83]
                output.writerow([variant] + [gene] + [expectoValue] + [tss] + [gnomad_score] + [ids])
                break
