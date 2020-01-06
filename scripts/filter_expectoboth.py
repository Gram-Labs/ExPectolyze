import csv

output3 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/exp_inputANDoutput.tsv', 'w'), delimiter = '\t')
output3.writerow(['variant'] + ['gene'] + ['expectoValue'] + ['distanceToTSS'] + ['list_of_heterozygous_DNA_ids'])

with open ('/data/ruderferlab/sandbox/grahame/expecto/data/filtered_expecto_input.tsv', 'r') as input4k, open('/data/ruderferlab/sandbox/grahame/expecto/data/filtered_expecto_output.tsv', 'r') as output20k:
    inputreader = csv.reader(input4k, delimiter='\t')
    outputreader = csv.reader(output20k, delimiter='\t')

    for line in inputreader:
        variant = line[0]
        listOfPpl = line[1]
        for line1 in outputreader:
            variant1 = line1[0]
            gene = line1[1]
            expectoValue = line1[2]
            tss = line1[3]
            if variant == variant1:
                output3.writerow([variant] + [gene] + [expectoValue] + [tss] + [listOfPpl])
                break
            else:
                continue