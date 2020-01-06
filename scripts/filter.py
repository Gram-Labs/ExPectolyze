
import csv

# Step 1
# Filter geneanno list to only include genes in the rnaSeq file

def filter1(geneannoFile,rnaSeqFile,chr):

    tsvList = []

    with open(rnaSeqFile, 'r') as tsvfile:  
        reader1 = csv.reader(tsvfile, delimiter='\t') 
        for line in reader1:
            for item in line:
                if (len(item) > 4 and item[2] == 'S'):
                    tsvList.append(item)
    tsvfile.close()
    print ('tsv parsing complete')
    print (len(tsvList))

    #outputFile = csv.writer(open('modified.geneanno.pc.sorted.bed', 'w'))
    write1 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/resources/modified.geneanno.pc.sorted.bed', 'w'), delimiter=' ',quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    # 18625 lines initially 
    with open (geneannoFile, 'r') as annofile:  
        reader1 = csv.reader(annofile, delimiter='\t')
        for line in reader1:
            if line[4] in tsvList:
                if line[0] == chr:
                    write1.writerow([line[0]] + [line[1]] + [line[2]] + [line[3]] + [line[4]])
    annofile.close()

    yuh1 = '/data/ruderferlab/sandbox/grahame/expecto/resources/modified.geneanno.pc.sorted.bed'
    yuh2 = '/data/ruderferlab/sandbox/grahame/expecto/resources/final.geneanno.pc.sorted.bed'

    cmd = "awk '{ OFS=\"\t\"; print $1, $2, $3, $4, $5 }' %s > %s" % (yuh1, yuh2)
    os.system(cmd)
    print ('new geneanno file created and delimited')












def filter2(rnaSeqFile,manualfile):

    tsvList = []
    with open(rnaSeqFile, 'r') as tsvfile:  
        reader1 = csv.reader(tsvfile, delimiter='\t') 
        for line in reader1:
            for item in line:
                if (len(item) > 4 and item[2] == 'S'):
                    tsvList.append(item)
    tsvfile.close()
    tsv1 = str(len(tsvList))
    print ('tsv parsing complete, length %s' % tsv1)

    write1 = csv.writer(open('modified_initial.vcf', 'w'), delimiter='\t')

    varList = []
    with open (manualfile, 'r') as f1:
        reader1 = csv.reader(f1, delimiter='\t')
        for line in reader1:
            variant = line[2]
            gene = line[7]
            if gene in tsvList:
                varList.append(variant)
    f1.close()
    len1 = str(len(varList))
    print ('got list of vars: length %s' % len1)

    bigfile = '/data/ruderferlab/sandbox/grahame/first100k_final.vcf'
    with open(bigfile, 'r') as big:
        reader2 = csv.reader(big, delimiter='\t')
        for line in reader2:
            if line[1] in varList:
                write1.writerow([line[0]] + [line[1]] + [line[2]] + [line[3]] + [line[4]])
    big.close()
    print ('done')


def idmap(dnainput,rnainput,mapfile,mapoutput)

    mapDNAIndex = 8     # name = WGS.DataID
    mapRNAIndex = 11    # name = RNAseq.dlpfc.DataID

    with open(dnainput) as f1:
        dnacontent = f1.readlines()
    
    with open(rnainput) as f2: 
        rnacontent = f2.readlines()
    
    write1 = csv.writer(open(mapoutput, 'w'), delimiter = ',')

    with open(mapfile, 'r') as mapf:
        mapreader = csv.reader(mapf, delimiter='\t')
        for line in mapreader:
            if line[8] 
        








if __name__ == '__main__':

    rnaSeqFile = '/data/ruderferlab/sandbox/grahame/data/HBCC_DLPFC_eqtlResidualExpression_WithoutSVbasedOutierIndividualsV2.tsv'
    geneannoFile = '/data/ruderferlab/sandbox/grahame/expecto/resources/geneanno.pc.sorted.bed'
    filteredgennannoFile = '/data/ruderferlab/sandbox/grahame/expecto/resources/modified.geneanno.pc.sorted.bed'
    chromosome = 'chr1'
    bedopsOutputFile = '/data/ruderferlab/sandbox/grahame/first25k_final.vcf.bed.sorted.bed.closestgene'
    manualfile = '/data/ruderferlab/sandbox/grahame/manual_bedops.vcf.bed.sorted.bed.closestgene'
    dnainput = '/data/ruderferlab/sandbox/grahame/expecto/data/ids_dna.csv'
    rnainput = '/data/ruderferlab/sandbox/grahame/expecto/data/ids_rna.csv'
    idmap = '/data/ruderferlab/sandbox/grahame/expecto/data/CMC-ID.map'
    mapoutput = '/data/ruderferlab/sandbox/grahame/expecto/data/condensed_map.map'
    
    choice = input('Which filter process (1/2): ')
    
    if choice == '1':
        filter1(geneannoFile,rnaSeqFile,chromosome)
    if choice == '2':
        filter2(rnaSeqFile,manualfile)
    if choice == '3':
        idmap(dnainput,rnainput,mapfile,mapoutput)



