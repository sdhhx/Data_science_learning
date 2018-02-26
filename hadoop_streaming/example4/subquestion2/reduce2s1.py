#!/usr/bin/env python

import sys

current_feature = None
current_feature_id = None
current_count = 0
feature = None
feature_id = None
count = 0

for line in sys.stdin:
	try:
		line = line.strip()
		line = line.split("\t")
		feature = line[0]
		feature_id = line[1]
		count = int(line[2])
		if (feature, feature_id) == (current_feature, current_feature_id):
			current_count = current_count + 1
		else:
			if current_feature:
				print "\t".join([current_feature, current_feature_id, str(current_count)])
			current_feature = feature
			current_feature_id = feature_id
			current_count = count
	except:
		pass
if (feature, feature_id) == (current_feature, current_feature_id):
	print "\t".join([current_feature, current_feature_id, str(current_count)])