#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
import sys

current_letter = None
letter = None

for line in sys.stdin:
	letter = line.strip()
	if current_letter == letter:
		pass
	else:
		if current_letter:
			print current_letter
		current_letter = letter
if current_letter == letter:
	print current_letter
#cat testdata.txt | python question3_maps1.py | sort | python question3_reduces1.py > lastword.txt
