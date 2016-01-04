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
    test_accuracy = []
    test_loss = []

    check_test = False
    check_test2 = False
    for line in f:

        if check_test:
            test_accuracy.append(float(line.strip().split(' = ')[-1]))
            check_test = False
            check_test2 = True
        elif check_test2:
            if 'Test net output' in line and 'valid_log_loss' in line:
                #print line
                #print line.strip().split(' ')
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
    print 'test accuracy len: ', len(test_accuracy)

    if len(test_iterations) != len(test_accuracy): #awaiting test...
        print 'mis-match'
        print len(test_iterations[0:-1])
        test_iterations = test_iterations[0:-1]

    f.close()
    #plt.plot(training_iterations, training_loss, '-', linewidth=2)
    #plt.plot(test_iterations, test_accuracy, '-', linewidth=2)
    #plt.show()

    host = host_subplot(111)#, axes_class=AA.Axes)
    plt.subplots_adjust(right=0.75)

    par1 = host.twinx()

    host.set_xlabel("iterations")
    host.set_ylabel("loss [%]")
    par1.set_ylabel("validation accuracy [%]") 
    plt.title('accuracy and loss through the iterations')

    p1, = host.plot(training_iterations, training_loss, label="training log loss")
    #p3, = host.plot(test_iterations, test_loss, label="valdation log loss")
    p2, = par1.plot(test_iterations, test_accuracy, label="validation accuracy")

    host.legend(loc=4)

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())



    f1 = open(args.output_file1, 'r')

    training_iterations1 = []
    training_loss1 = []

    test_iterations1 = []
    test_accuracy1 = []
    test_loss1 = []

    check_test1 = False
    check_test21 = False
    for line in f1:

        if check_test1:
            test_accuracy1.append(float(line.strip().split(' = ')[-1]))
            check_test1 = False
            check_test21 = True
        elif check_test21:
            if 'Test net output' in line and 'valid_log_loss' in line:
                #print line
                #print line.strip().split(' ')
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
    print 'test accuracy len: ', len(test_accuracy1)

    if len(test_iterations1) != len(test_accuracy1): #awaiting test...
        print 'mis-match'
        print len(test_iterations1[0:-1])
        test_iterations1 = test_iterations1[0:-1]

    f1.close()
    #plt.plot(training_iterations, training_loss, '-', linewidth=2)
    #plt.plot(test_iterations, test_accuracy, '-', linewidth=2)
    #plt.show()



    p11, = host.plot(training_iterations1, training_loss1, label="training log loss finetune")
    #p3, = host.plot(test_iterations, test_loss, label="valdation log loss")
    p21, = par1.plot(test_iterations1, test_accuracy1, label="validation accuracy finetune")

    host.legend(loc=4)

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())

    host.axis["left"].label.set_color(p11.get_color())
    par1.axis["right"].label.set_color(p21.get_color())



    plt.draw()
    plt.show()
