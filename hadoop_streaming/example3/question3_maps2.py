#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
lastword = []
lwFile = open('lastword.txt', 'r')
for line in lwFile.readlines():
	line = line.strip()
	lastword.append(line)

for line in sys.stdin:
	words = line.strip().split(",")
	for word in words:
		word = word.strip()
		if word in lastword:
			print word + "\t" + str(1)