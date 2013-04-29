#!/usr/bin/env python
# coding: utf-8
import codecs
import sys
from nltk import bigrams
from nltk import trigrams
import fileinput
import re
import csv
from nltk.corpus import stopwords
import nltk


def gen_ML_postag(text):
	out = codecs.open("unigram_pos.txt",'w','utf8')
	out_bi = codecs.open("bigram_pos.txt",'w','utf8')
	out_tri = codecs.open("trigram_pos.txt",'w','utf8')
	out_file = codecs.open("tweets_pos.txt",'w','utf8')
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
			line = line.replace('barack','obama')
			line = line.replace('mitt','romney')
			line = line.replace('mrpresident','obama')
			verdict = verdict.replace('!!!!','2')
			wordtokens = nltk.word_tokenize(line)
			pos = nltk.pos_tag(wordtokens)	
			
			newline = ""
			if "obama" in line: 
				newline = newline + " obama"
			if "romney" in line: 
				newline = newline + " romney"

			for pair in pos:				
				if pair[1] == "JJ" or pair[1] == "JJR" or pair[1] == "JJS" or pair[1] == "RB" or pair[1] == "RBR" or pair[1] == "RBS":
					newline = newline + " " + pair[0]
			
			if newline == "":				
				for word in line.split( ):		
					if word not in stopwords.words('english'):
						newline = newline + " " + word			
						
			out_file.write(newline + "," + verdict)
			out_file.write("\n")
			print newline + "," + verdict

			unigrams = newline.split()        		
			for ml in unigrams:        			
				out.write(ml)
        			out.write("\n")

			tokens = newline.split()
			ml_bigram = bigrams(tokens)       		
        		for ml in ml_bigram:
        			out_bi.write(" ".join(ml))
        			out_bi.write("\n")

			ml_trigrams = trigrams(tokens)       		
        		for ml in ml_trigrams:
        			out_tri.write(" ".join(ml))
        			out_tri.write("\n")

inp = sys.argv[1]

gen_ML_postag(inp)
