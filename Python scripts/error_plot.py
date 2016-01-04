__author__ = 'Marko Arsenovic'


import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import pylab
import sys
import argparse
import re
from pylab import figure, show, legend, ylabel

from mpl_toolkits.axes_grid1 import host_subplot


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='makes a plot from Caffe output')
    parser.add_argument('output_file', help='file of captured stdout and stderr')
    args = parser.parse_args()

    f = open(args.output_file, 'r')

    training_iterations = []
    training_loss = []

    test_iterations = []
    test_top1 = []
    test_top5 = []
    test_loss = []

    check_test = False
    check_test2 = False
    for line in f:

    	if 'Test net output #1' in line:
	    	test_top1.append(float(line.strip().split(' = ')[-1]))

    	if 'Test net output #2' in line:
		test_top5.append(float(line.strip().split(' = ')[-1]))



        if 'Test net output' in line and 'valid_log_loss' in line:
                test_loss.append(float(line.strip().split(' ')[-2]))
                check_test2 = False
        else:
                test_loss.append(0)
                check_test2 = False

        if '] Iteration ' in line and 'loss = ' in line:
              arr = re.findall(r'ion \b\d+\b,', line)
              training_iterations.append(int(arr[0].strip(',')[4:]))
              training_loss.append(float(line.strip().split(' = ')[-1]))

        if '] Iteration ' in line and 'Testing net' in line:
              arr = re.findall(r'ion \b\d+\b,', line)
              test_iterations.append(int(arr[0].strip(',')[4:]))
              check_test = True

    print 'train iterations len: ', len(training_iterations)
    print 'train loss len: ', len(training_loss)
    print 'test loss len: ', len(test_loss)
    print 'test iterations len: ', len(test_iterations)
    print 'test accuracy len: ', len(test_top1)

    if len(test_iterations) != len(test_top1): #awaiting test...
        print 'mis-match'
        print len(test_iterations[0:-1])
        test_iterations = test_iterations[0:-1]

    f.close()

    y = np.array(test_top1)
    x = np.array(test_iterations)
    print len(x)
    print len(y)
    plt.xlabel('iterations')
    plt.ylabel('top-1 [%] of success')
    plt.title('top-1 through the iterations')
    plt.plot(x,y) 
    plt.show()


    y = np.array(test_top5)
    x = np.array(test_iterations)
    print len(x)
    print len(y)
    plt.xlabel('iterations')
    plt.ylabel('top-5 [%] of success')
    plt.title('top-5 through the iterations')
    plt.plot(x,y) 
    plt.show()





