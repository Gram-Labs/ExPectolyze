import csv

filteredBothFile = '/data/ruderferlab/sandbox/grahame/expecto/data/exp_inputANDoutput.tsv'

with open (filteredBothFile, 'r') as f, open('/data/ruderferlab/sandbox/grahame/expecto/data/postmap_filtered.tsv', 'w') as f1:

    f1.write('variant' + '\t' + 'gene' + '\t' + 'expectoValue' + '\t' + 'distanceToTSS' + '\t' + 'combined_valid_ids')

    for line in f:
        if ':' in line:
            f1.write(line)