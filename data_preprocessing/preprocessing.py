#!/usr/bin/env python
# coding: utf-8

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
			return os.path.join(tmpDir,filename)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise
   
def main():
	print "data processing..."

	filename = raw_input("Enter the training data file name:") 
	filepath = os.path.join(__filepath__ , "data")
	filepath = os.path.join(filepath, filename)

	tmpfilepath = DataProcessing.createTmpDir(__filepath__,filename)  
	shutil.copy2(filepath, tmpfilepath)
	
	tmpfilepath = tmpfilepath.replace(" ","\\ ")
	print "temp file path: " + tmpfilepath

	print "ascii encoding..."
	os.system("sed -i \"s|[àáâãäçèéêëìíîïñòóôõöùúûüýÿÀÁÂÃÄÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ]||g\" " + tmpfilepath)
		
	print "replacing tags <a>, </a>, <e> and </e>..."
	os.system("sed -i \"s|<a>| |g\" " + tmpfilepath)
	os.system("sed -i \"s|<e>| |g\" " + tmpfilepath)
	os.system("sed -i \"s|</a>||g\" " + tmpfilepath)
	os.system("sed -i \"s|</e>||g\" " + tmpfilepath)
	
	print "remove urls..."
	os.system("sed -i \"s|http://t\.co/\w*||g\" " + tmpfilepath)
	os.system("sed -i \"s|https://t\.co/\w*||g\" " + tmpfilepath)
	
	print "basic stemming - removing \"'s\", \"'re\" replaced with \"are\", removing \"'\"..."
	os.system("sed -i \"s|'s||g\" " + tmpfilepath)
	os.system("sed -i \"s|'re| are|g\" " + tmpfilepath)
	os.system("sed -i \"s|'||g\" " + tmpfilepath)
	
	print "removing twitter @usernames..."
	os.system("sed -i \"s|@\w*||g\" " + tmpfilepath)
	
	print "transform all text to lower case..."
	os.system("tr '[:upper:]' '[:lower:]' " + tmpfilepath)
	
	print "removing #tags..."
	os.system("sed -i \"s|#\w*||g\" " + tmpfilepath)
	
	
	
if __name__ == '__main__':
    main()


