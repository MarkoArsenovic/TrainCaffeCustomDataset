__author__ = 'Marko Arsenovic'

#!/usr/bin/python

from os import walk
from os.path import join
import os

classCount = 0
labels = []
filesList = []
X0 = []
y = []
k = 0


root_path = "/path/to/images/"
#"""
for x in walk(join(root_path, "Train/")):  
    filescount = 0
    fc = 0
    if x[0].__contains__("missclassified"):
        continue
    if len(x[2]) > 0:
        print "Processing class %i..."% (k)
        k += 1
        for filename in x[2]:
            if filename.endswith(".jpg") or filename.endswith(".JPG"):

                fnampe_path = str(x[0]) + "/" + filename
                print fnampe_path
                os.rename(fnampe_path, fnampe_path.replace(" ","_"))
                #print join(x[0], filename)
                filescount += 1

        print classCount-1, filescount

k = 0
X1 = []
y1 = []
classCount = 0
labels = []
filesList = []
for x in walk(join(root_path, "Test/")):
    filescount = 0
    fc = 0
    if x[0].__contains__("missclassified"):
        continue
    if len(x[2]) > 0:
        print "Processing class %i..."% (k)
        k += 1
        for filename in x[2]:
            if filename.endswith(".jpg") or filename.endswith(".JPG"):
                fnampe_path = str(x[0]) + "/" + filename
                print fnampe_path
                os.rename(fnampe_path, fnampe_path.replace(" ","_"))
                filescount += 1

        print classCount-1, filescount

