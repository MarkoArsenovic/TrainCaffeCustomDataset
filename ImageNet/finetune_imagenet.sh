#!/usr/bin/env sh

TOOLS=~/caffe/build/tools

GLOG_logtostderr=1  $TOOLS//caffe train -solver finetune_solver.prototxt -weights ~/caffe/examples/imagenet/caffe_reference_imagenet_model -gpu 0 >> output_finetune.txt 2>&1

echo "Done."
