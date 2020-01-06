import os,csv,json

with open ('/data/ruderferlab/sandbox/grahame/expecto/data/ids_dna.json', 'r') as f1:
    json_dna_ids = json.load(f1)

output2 = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/filtered_expecto_input.tsv', 'w'), delimiter = '\t')
output2.writerow(['variant'] + ['list_of_DNA_ids_with_1/1_allelic_match'])

with open ('/data/ruderferlab/sandbox/grahame/expecto/data/first25k_formatted.vcf', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    counter = 0

    for line in reader:
        if len(line) > 1:
            indexList = []
            #indexList.append(line[1])
            for item in line:
                if (':' in item and ',' in item and item.split(":")[0] == '1/1'):
                    counter = counter+1
                    itemindex = line.index(item)
                    actualName = json_dna_ids[itemindex]['individual_DNA_ID']
                    indexList.append(actualName)
                    print (line[1] + ' - ' + str(itemindex) + ' - ' + actualName)
                else:
                    continue
            print (' ')
            
            if len(indexList) > 1:
                output2.writerow([line[1]] + [indexList])