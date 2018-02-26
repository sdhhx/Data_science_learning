#!/usr/bin/env python

import sys

current_feature_id = None
current_count = 0
feature_id = None
count = 0

for line in sys.stdin:
	try:
		line = line.strip()
		line = line.split("\t")
		feature_id = line[0]
		count = int(line[1])
		if feature_id == current_feature_id:
			current_count = current_count + 1
		else:
			if current_feature_id:
				print "\t".join([current_feature_id, str(current_count)])
			current_feature_id = feature_id
			current_count = count
	except:
		pass
#last one must be true
if current_feature_id == feature_id:
	print "\t".join([current_feature_id, str(current_count)])