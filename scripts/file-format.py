'''
VCF File Editor for use with ExPecto's chromatin.py

- Final file only has the first five columns
- Enforces tab separation as the delimiter
- Removes mutation entries without PASS score
 
'''

import os,sys
from logger import logger
log = logger().log


def format(file):

    newName = (str(file).split('/')[-1]).split('.vcf')[0] + '_formatted.vcf'
    #cmd = 'touch %s' % newName
    #os.system(cmd)
    finalName = (str(file).split('/')[-1]).split('.vcf')[0] + '_final.vcf'
    #cmd = 'touch %s' % finalName
    #os.system(cmd)


    infile = open(file,'r').readlines()
    with open(newName,'w+') as outfile:
        for line in infile:
            linesplit = line.split("\t")
            if linesplit[6] == 'PASS':
                if len(linesplit[3]) == 1:
                    if len(linesplit[4]) == 1:
                        outfile.write(line)
    outfile.close()
    
    
    #cmd = "awk '{ OFS=\"\t\"; print $1, $2, $3, $4, $5 }' %s > %s" % (newName, finalName)
    #os.system(cmd)

    print ("Formatting complete!")


if __name__ == '__main__':
    file = input('File to convert: ')
    format(file)
    
