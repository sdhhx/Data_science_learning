#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
import sys

current_letter = None
letter = None
current_count = 0

for line in sys.stdin:
	line = line.strip().split('\t')
	try:
		letter = line[0]
		count = int(line[1])
	except:
		continue
	if current_letter == letter:
		current_count = current_count + count
	else:
		if current_letter:
			print current_letter + '\t' + str(current_count)
		current_letter = letter
		current_count = 1
if current_letter == letter:
	print current_letter + '\t' + str(current_count)
#cat testdata.txt | python question3_maps2.py | sort | python question3_reduces2.py > result.txt
