#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	friends = line.split(" ")

	toge_friend = friends[0]
	friends = friends[1:]
	length = len(friends)
	for i in range(length):
		for j in range(i + 1, length):
			print friends[i] + "," + friends[j] + "\t" + toge_friend
			print friends[j] + "," + friends[i] + "\t" + toge_friend