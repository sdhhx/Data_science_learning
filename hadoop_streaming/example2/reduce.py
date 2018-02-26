#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	for i in range(len(line)):
		line[i] = line[i].strip()
	print "\t".join(line)