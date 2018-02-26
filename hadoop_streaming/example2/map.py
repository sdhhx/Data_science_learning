#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	line = line.split("\t")

	for i in range(len(line)):
		line[i] = line[i].strip()
	print "\t".join(line)
#test : cat testdata.txt | python map.py | sort -k 2 | sort -k 3 | sort > output.txt