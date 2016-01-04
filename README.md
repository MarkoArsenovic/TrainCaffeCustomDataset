# Train-Caffe-ImageNet-on-custom-dataset

How to train Caffe ImageNet on custom dataset

This is short description on training your own custom Net based on your image dataset using pre-trained CaffeNet model.

This repo contains all required python and shell scripts  for pretraining and training stage, not optimized and could be cleaner code, sorry...

Collect all your images for test and valuation process and put them in Test and Train folders, each class of images should  be placed as subfolder in these two folders. Example, two classes expected for your model, cars and bikes : Train/cars, Train/bikes etc.

First, create your own train.txt and val.txt files using train_val.py script. The content of these txt files will be as example :

Train/bike/bike.jpg 0                    Test/bike/bike.jpg 0    
Train/car/car.jpg 1                      Test/car/car.jpg 1

The images are labeled as class numbers. If names contain spaces, could be removed using remove_spaces.py.

The second stage is to create leveldb libraries using create_leveldb.sh, just change the required paths inside the script.

After that, compute the mean using make_imagenet_mean.sh, the imagenet_mean.binaryproto file will be crated.

Create your proto files, examples are provoded, you should have train & val proto files and soler proto file for setting training parameters. Change the num_output in fully-connected layer for custom number of classe, example of bikes and cars num_output = 2.

The next step is to start training the Net, using finetune_imagenet.sh, gpu or cpu, the log of training will be placed in output_finetune.txt.

After the training is done, caffemodel files will be generated.

To test the net you can write simpe python script, bunch of tutorials are provided, example:

http://christopher5106.github.io/deep/learning/2015/09/04/Deep-learning-tutorial-on-Caffe-Technology.html

There are few more python script for plotting errors and accuracy out of the log file, for example progres_plot.py to plot accuracy, usage from terminal python progress_plot.py /path/to/output_finetune.txt, examples in the Plots directory.

Also, there is example of plotting top-1 & top-5 accuracy using error_plot.py.

Further improvments and suggestions are welcome.






Also, there is the example visualizing filtered images throughout the layers, visualize_layers.py, usage of script provided with example of leaf as an input image.
