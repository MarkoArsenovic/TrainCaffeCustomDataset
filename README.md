# Train CaffeNet model on custom dataset

How to train CaffeNet on custom dataset

This is short description of training your own custom Net based on your image dataset using pre-trained CaffeNet model.

This repo contains all required Python and shell scripts  for pretraining and training stage, not optimized and could be cleaner code.

1. Collect all your images for test and valuation process and put them in Test and Train folder, each class of images should  be placed as subfolder in these two folders. Example, two classes used for your model, cars and bikes : Train/cars, Train/bikes etc.

2. First, create your own **train.txt** and **val.txt** files using **train_val.py** script. The content of these txt files will be as the example:
```
.
+-- train.txt
|   +-- Train/bike/bike.jpg 0
|   +-- Train/car/car.jpg 1
+-- test.txt
|   +-- Test/bike/bike.jpg 0
|   +-- Test/car/car.jpg 1
```	
The images are labeled as class numbers. If names of images contain spaces, could be removed using **remove_spaces.py**.

3. The second stage is to create *leveldb* libraries using **create_leveldb.sh**, just change the required paths inside the script.

4. After that, compute the mean using **make_imagenet_mean.sh**, the *imagenet_mean.binaryproto* file will be created.

5. Create your proto files, examples are provided, you should have *train* & *val* proto files and *solver* proto file for setting training parameters (momentum, decay, snapshots, no. of iterations etc.). Change the *num_output* in *fully-connected layer* for custom number of classes, for example if you are recognizing only bikes and cars *num_output = 2*.

6. The next step is to start training the Net, using **finetune_imagenet.sh**, gpu or cpu, the log of training will be placed in **output_finetune.txt**.

7. After the training is done, caffemodel files will be generated, *snapshots* after every *1000th iteration*.

8. To test the net you can write simpe Python script, bunch of examples are provided, [example](http://christopher5106.github.io/deep/learning/2015/09/04/Deep-learning-tutorial-on-Caffe-Technology.html).


There are few more Python scripts for plotting errors and accuracy out of the log file, for example **progres_plot.py** to plot accuracy, usage from terminal `python progress_plot.py /path/to/output_finetune.txt`.

Also, there is example of plotting *top-1* & *top-5* accuracy using **error_plot.py**, plots examples in the *Plots* directory.

Example visualizing filtered images throughout the layers, **visualize_layers.py**, usage of script provided with example of leaf as an input image. All layers in the Net model could be visualize using **visual.py**, example in *Plots* directory.


Further improvements and suggestions are welcome.






