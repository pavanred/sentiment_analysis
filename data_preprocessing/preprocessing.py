#!/usr/bin/env python

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
	

if __name__ == '__main__':
    main()


