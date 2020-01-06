import os,csv

geneOfInterest = ''
    tissueIndex = 15
    newfile1 = '/data/ruderferlab/sandbox/grahame/expecto/data/newfile1.tsv'

    # STEP 1

    output1 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/newfile1.tsv', 'w'), delimiter = '\t')
    output1.writerow(['variant'] + ['gene'] + ['expectoValue'] + ['distanceToTSS'])

    with open(expectoOutput, 'r') as expectoOutputFile:
        expectoOutputReader = csv.reader(expectoOutputFile, delimiter=',')

        for outputLine in expectoOutputReader:
            gene = outputLine[8]
            variantOfInterest = outputLine[3]
            expectoValue = outputLine[tissueIndex]
            distanceToTSS = outputLine[7]     
            output1.writerow([variantOfInterest] + [gene] + [expectoValue] + [distanceToTSS])

    expectoOutputFile.close()
    # STEP 2