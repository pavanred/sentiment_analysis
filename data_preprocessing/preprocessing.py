#!/usr/bin/env python
# coding: utf-8
#

__filepath__ = "/media/Data1/workspace/git/sentiment analysis/data_preprocessing/"

import os
import errno
import time
import shutil

class DataProcessing:
	
	@staticmethod
	def createTmpDir(path,filename):
		tmpDir = os.path.join(path,"tmp" + str(time.time())) 		
		try:
			os.makedirs(tmpDir)
			#return os.path.join(tmpDir,filename)
			return tmpDir
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
				
	@staticmethod
	def asciiEncoding(tmpfilepath):
		print "ascii encoding..."
		os.system("sed -i \"s|[àáâãäçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ]||g\" " + tmpfilepath)
		
	@staticmethod
	def removeHtmlTags(tmpfilepath):
		print "replacing tags <a>, </a>, <e> and </e>..."
		os.system("sed -i \"s|<a>| |g\" " + tmpfilepath)
		os.system("sed -i \"s|<e>| |g\" " + tmpfilepath)
		os.system("sed -i \"s|</a>||g\" " + tmpfilepath)
		os.system("sed -i \"s|</e>||g\" " + tmpfilepath)

	@staticmethod
	def removeUrls(tmpfilepath):
		print "remove urls..."
		os.system("sed -i \"s|http://t\.co/\w*||g\" " + tmpfilepath)
		os.system("sed -i \"s|https://t\.co/\w*||g\" " + tmpfilepath)
		
	@staticmethod
	def basicStemming(tmpfilepath):
		#removing "'s", "'re" replaced with "are", removing "'"
		print "basic stemming..."
		os.system("sed -i \"s|'s||g\" " + tmpfilepath)
		os.system("sed -i \"s|'re| are|g\" " + tmpfilepath)
		os.system("sed -i \"s|'||g\" " + tmpfilepath)	
		
	@staticmethod
	def removeTagsAndUsers(tmpfilepath):
		print "removing #tags and @usernames..."
		os.system("sed -i \"s|#\w*||g\" " + tmpfilepath)
		os.system("sed -i \"s|@\w*||g\" " + tmpfilepath)
		
	@staticmethod
	def toLowerCase(tmpfilepath):
		print "all text to lower case..."
		os.system("tr '[:upper:]' '[:lower:]' < " + tmpfilepath)
		
	@staticmethod
	def normalizeEntityNames(tmpfilepath):
		print "normalizing entitiy names..."
		os.system("sed -i \"s|barak|obama|g\" " + tmpfilepath)
		os.system("sed -i \"s|barak obama|obama|g\" " + tmpfilepath)
		os.system("sed -i \"s|mitt|romney|g\" " + tmpfilepath)
		os.system("sed -i \"s|mitt romney|romney|g\" " + tmpfilepath)
		os.system("sed -i \"s|mr.president|obama|g\" " + tmpfilepath)
		os.system("sed -i \"s|mr. president|obama|g\" " + tmpfilepath)
		
	@staticmethod
	def trimAll(tmpDir):
		print "removing extra spaces ..."
		os.system("sed -i \"s|[ ]{2,}||g\" " + tmpDir + "/tweets.txt")		
		
	@staticmethod
	def retainOnlyText(tmpfilepath, tmpDir):
		print "retain only text ..."
		os.system("awk -F \",\" '{print $4}' " + tmpfilepath + " >> " + tmpDir + "/tweets.txt")
		os.system("sed -i \"s|[^a-zA-Z]| |g\" " + tmpDir + "/tweets.txt")
		
	@staticmethod
	def getWordList(tmpDir):
		print "creating word count file..."
		#os.system("tr ' ' '\12' <$4.txt | sort | uniq -c | sort -nr >> wordcount.txt")
		#wordlistfile = os.path.join(tmpDir,"wordlist.txt")
		os.system("tr ' ' '\12' < " + tmpDir + "/tweets.txt | uniq >> " + tmpDir + "/wordlist.txt")
		
	   
def main():
	print "data processing..."

	filename = raw_input("Enter the training data file name:") 
	filepath = os.path.join(__filepath__ , "data")
	filepath = os.path.join(filepath, filename)

	tmpDir = DataProcessing.createTmpDir(__filepath__,filename)  
	tmpfilepath = os.path.join(tmpDir,filename)
	shutil.copy2(filepath, tmpfilepath)
	
	tmpDir = tmpDir.replace(" ","\\ ")
	tmpfilepath = tmpfilepath.replace(" ","\\ ")
	print "temp file path: " + tmpfilepath

	DataProcessing.asciiEncoding(tmpfilepath)
	
	DataProcessing.removeHtmlTags(tmpfilepath)
	DataProcessing.removeUrls(tmpfilepath)
	
	DataProcessing.basicStemming(tmpfilepath)
	
	DataProcessing.removeTagsAndUsers(tmpfilepath)
	
	DataProcessing.toLowerCase(tmpfilepath)
	DataProcessing.normalizeEntityNames(tmpfilepath)
	
	DataProcessing.retainOnlyText(tmpfilepath, tmpDir)
	
	DataProcessing.trimAll(tmpDir)
	DataProcessing.getWordList(tmpDir)
	
	print "temp file path: " + tmpfilepath
	
if __name__ == '__main__':
    main()


