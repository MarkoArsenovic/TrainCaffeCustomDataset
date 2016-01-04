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
    parser.add_argument('output_file1', help='file of captured stdout and stderr')
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



    f1 = open(args.output_file1, 'r')

    training_iterations1 = []
    training_loss1 = []

    test_iterations1 = []
    test_top11 = []
    test_top51 = []
    test_loss1 = []

    check_test1 = False
    check_test21 = False
    for line in f1:

    	if 'Test net output #1' in line:
	    	test_top11.append(float(line.strip().split(' = ')[-1]))

    	if 'Test net output #2' in line:
		test_top51.append(float(line.strip().split(' = ')[-1]))



        if 'Test net output' in line and 'valid_log_loss' in line:
                test_loss1.append(float(line.strip().split(' ')[-2]))
                check_test21 = False
        else:
                test_loss1.append(0)
                check_test21 = False

        if '] Iteration ' in line and 'loss = ' in line:
              arr = re.findall(r'ion \b\d+\b,', line)
              training_iterations1.append(int(arr[0].strip(',')[4:]))
              training_loss1.append(float(line.strip().split(' = ')[-1]))

        if '] Iteration ' in line and 'Testing net' in line:
              arr = re.findall(r'ion \b\d+\b,', line)
              test_iterations1.append(int(arr[0].strip(',')[4:]))
              check_test1 = True

    print 'train iterations len: ', len(training_iterations1)
    print 'train loss len: ', len(training_loss1)
    print 'test loss len: ', len(test_loss1)
    print 'test iterations len: ', len(test_iterations1)
    print 'test accuracy len: ', len(test_top11)

    if len(test_iterations1) != len(test_top11): #awaiting test...
        print 'mis-match'
        print len(test_iterations1[0:-1])
        test_iterations1 = test_iterations1[0:-1]

    f1.close()


    y = np.array(test_top1)
    x = np.array(test_iterations)
    y1 = np.array(test_top11)
    x1 = np.array(test_iterations1)
    print len(x)
    print len(y)
    plt.xlabel('iterations')
    plt.ylabel('top-1 [%] of success')
    plt.title('top-1 through the iterations')
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.legend(['original model', 'fine tuned model'], loc='lower right')  
    plt.show()


    y = np.array(test_top5)
    x = np.array(test_iterations)
    y1 = np.array(test_top51)
    x1 = np.array(test_iterations1)
    print len(x)
    print len(y)
    plt.xlabel('iterations')
    plt.ylabel('top-5 [%] of success')
    plt.title('top-5 through the iterations')
    plt.plot(x,y) 
    plt.plot(x1,y1)
    plt.legend(['original model', 'fine tuned model'], loc='lower right')  
    plt.show()




