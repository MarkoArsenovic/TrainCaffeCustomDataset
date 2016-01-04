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
                filesList.append(str(x[0]) + "/" + filename + " " + str(classCount))
                #print join(x[0], filename)
                filescount += 1
        if filescount > 0:
            labels.append(str(x[0]) + " " + str(classCount))
            classCount += 1
        else:
            continue
        print classCount-1, filescount

models_root = root_path 
print 'Creating train labels'
f = open(join(models_root, "train.txt"), 'wb')
for lbl in filesList:
    f.write(lbl + '\n')
f.close()

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
                filesList.append(str(x[0]) + "/" + filename + " " + str(classCount))
                #print join(x[0], filename)
                filescount += 1
        if filescount > 0:
            labels.append(str(x[1]) + " " + str(classCount))
            classCount += 1
        else:
            continue
        print classCount-1, filescount

models_root = root_path 
print 'Creating test labels'
f = open(join(models_root, "val.txt"), 'wb')
for lbl in filesList:
    f.write(lbl + '\n')
f.close()
