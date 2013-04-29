#!/usr/bin/env python
# coding: utf-8
import codecs
import sys
from nltk import trigrams
import fileinput
import re
import csv

#def gen_ML_Bigram(text):
#        texfbig = codecs.open(text,'r','utf8').read()
#        tokens = texfbig.split()
#        ml_bigram = bigrams(tokens)
#        out = codecs.open("ml_bigram.txt",'w','utf8')
#        for ml in ml_bigram:
#                out.write(" ".join(ml))
#                out.write("\n")


def gen_ML_Trigram(text):
	out = codecs.open("trigram.txt",'w','utf8')
	out_file = codecs.open("tweets.txt",'w','utf8')
	#for line in open(text,'r'):
	with open(text, 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			line = row[3]
			verdict = row[6]
			print line
			print verdict
			line = line.lower()
			line = line.replace(':)','positive')
			line = line.replace(':-)','positive')
			line = line.replace(':(','negative')
			line = line.replace(':-(','negative')
			line = re.sub('[àáâãäçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ]','',line)
			line = re.sub('<a>',' ',line)
			line = re.sub('<e>',' ',line)
			line = re.sub('</a>','',line)
			line = re.sub('</e>','',line)
			line = re.sub('http://t\.co/\w*','',line)
			line = re.sub('https://t\.co/\w*','',line)
			line = re.sub('#\w*','',line)
			line = re.sub('@\w*','',line)
			line = re.sub('[^a-zA-Z ]','',line)
			line = line.replace('barak','obama')
			line = line.replace('mitt','romney')
			line = line.replace('mrpresident','obama')
			out_file.write(line + "," + verdict)
			out_file.write("\n")
	
			tokens = line.split()
			ml_trigram = trigrams(tokens)       		
        		for ml in ml_trigram:
        			out.write(" ".join(ml))
        			out.write("\n")

inp = sys.argv[1]

gen_ML_Trigram(inp)
