#!/usr/bin/env python

import sys
for line in sys.stdin:
	line = line.strip()
	data = line.split("\t")

	buy = data[0]
	data = data[1].split(" ")
	for unit in data:
		try:
			unit = unit.split(":")
			feature = unit[0]
			feature_id = unit[1]
			feature_value = unit[2]
			print "\t".join([feature_id, str(1)])
		except:
			pass 