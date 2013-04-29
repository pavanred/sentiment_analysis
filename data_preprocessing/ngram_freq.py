#!/usr/bin/env python
# coding: utf-8
import codecs
import sys
import operator
from collections import defaultdict
import re

def gen_ML_ngram_freq(text):
	d = defaultdict(int)
	out = codecs.open("ngram_freq.txt",'w','utf8')
        for line in open(text,'r'):
        	d[line.replace('\n','')] += 1
	s = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
	for line in s:
		line = re.sub('[^a-zA-Z ]','',str(line))
		out.write(line)
                out.write("\n")	

inp = sys.argv[1]

gen_ML_ngram_freq(inp)
