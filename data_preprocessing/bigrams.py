#!/usr/bin/env python
# coding: utf-8
import codecs
import sys
from nltk import bigrams
import fileinput
import re
import csv
from nltk.corpus import stopwords

#def gen_ML_Bigram(text):
#        texfbig = codecs.open(text,'r','utf8').read()
#        tokens = texfbig.split()
#        ml_bigram = bigrams(tokens)
#        out = codecs.open("ml_bigram.txt",'w','utf8')
#        for ml in ml_bigram:
#                out.write(" ".join(ml))
#                out.write("\n")


def gen_ML_Bigram(text):
	out = codecs.open("bigram.txt",'w','utf8')
	out_file = codecs.open("tweets.txt",'w','utf8')
	#for line in open(text,'r'):
	with open(text, 'rb') as f:
		reader = csv.reader(f, delimiter=',')
		for row in reader:
			line = row[3]
			verdict = row[6]
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
			verdict = verdict.replace('!!!!','2')
			
			newline = ""
			for word in line.split( ):
				if word not in stopwords.words('english'):
					newline = newline + " " + word			
			out_file.write(newline + "," + verdict)
			out_file.write("\n")
			print newline + "," + verdict

			tokens = newline.split()
			ml_bigram = bigrams(tokens)       		
        		for ml in ml_bigram:
        			out.write(" ".join(ml))
        			out.write("\n")

inp = sys.argv[1]

gen_ML_Bigram(inp)
