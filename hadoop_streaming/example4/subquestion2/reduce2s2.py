#!/usr/bin/env python

import sys

current_feature = None
current_count = 0
feature = None
count = 0

for line in sys.stdin:
	try:
		line = line.strip()
		line = line.split("\t")
		feature = line[0]
		count = int(line[1])
		if feature== current_feature:
			current_count = current_count + 1
		else:
			if current_feature:
				print "\t".join([current_feature, str(current_count)])
			current_feature = feature
			current_count = count
	except:
		pass
if feature== current_feature:
	print "\t".join([current_feature, str(current_count)])