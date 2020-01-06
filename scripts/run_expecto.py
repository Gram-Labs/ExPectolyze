'''
Author: Grahame Evans - Ruderfer Lab
Last updated: 17 December 2019
Python version: 3.6.3
Documentation: see README.md

Purpose: Executable python file that combines the .vcf file editing steps and the two ExPecto scripts into a better-logged framework.

'''

import os,sys
import file_format, run, run_analysis  # scripts
from logger import logger
log = logger().log


print('\n      O       o O       o O       o')
print('      | O   o | | O   o | | O   o |')
print('      | | O | | | | O | | | | O | |')
print('      | o   O | | o   O | | o   O |')
print('      o       O o       O o       O')
print('\n' + '-'*42 + '\n      ExPecto CLI Executable Wrapper\n' + '-'*42)
print(' Developed by Grahame - Ruderfer Lab')
print('    Documentation - refer to README.md')
print('       Last updated - 13 Dec 2019')
print('-'*42 + '\n')

##################################################################################

file = input('Filename: ')
input1 = file_format.format(file)
cmd = 'cd expecto'
os.system(cmd)
cmd = 'python chromatin.py %s' % input1
os.system(cmd)

# switch this to subprocess, add rest of the commands

