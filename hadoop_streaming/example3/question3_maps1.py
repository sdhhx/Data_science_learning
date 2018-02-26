#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    last_letter = line.split(",")
    print last_letter[-1].strip()