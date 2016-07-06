#!/usr/bin/env sh
# Create the imagenet leveldb inputs
# N.B. set the path to the imagenet train + val data dirs

TOOLS=~/caffe/build/tools
DATA=/path/to/images/

echo "Creating leveldb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset.bin -resize_width 256 -resize_height 256 -shuffle \
    "" \
    $DATA/train.txt \
    train_leveldb

GLOG_logtostderr=1 $TOOLS/convert_imageset.bin -resize_width 256 -resize_height 256 -shuffle \
    "" \
    $DATA/val.txt \
    val_leveldb
    
echo "Done."
