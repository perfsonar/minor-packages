#!/usr/bin/python

'''
minimal 2to3 coverter that touches only u'' literals
'''

import sys
from lib2to3.fixes.fix_unicode import FixUnicode

FixUnicode.PATTERN = 'STRING'
sys.argv[1:1] = ['-f', 'unicode']
execfile('/usr/bin/2to3')
