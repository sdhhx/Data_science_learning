# -*- coding: utf-8 -*-

fc_file = open('./output/NotbuyOutput2/part-00000', 'r')
#fc_file = open('./output/BuyOutput2/part-00000', 'r')
feature_count = {}
for line in fc_file.readlines():
	line = line.split("\t")
	feature = line[0]
	try:
		count = int(line[1])
	except:
		continue
	feature_count[feature] = count

faid_file = open('./output/NotbuyOutput1/part-00000', 'r')
#faid_file = open('./output/BuyOutput1/part-00000', 'r')
f = open('notbuy_result.txt','w')
for line in faid_file.readlines():
	line = line.split("\t")
	try:
		feature = line[0]
		feature_id = line[1]
		count = int(line[2])
		if feature in feature_count:
			pct = 1.0 * count / feature_count[feature] * 100
			#print "\t".join([feature, feature_id, str(count), str(pct) + "%"])
			f.write("\t".join([feature, feature_id, str(count), str(pct) + "%"]) + "\n")
	except:
		pass
f.close()