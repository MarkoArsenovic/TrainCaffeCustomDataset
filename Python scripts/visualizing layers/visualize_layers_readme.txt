in the folder /../caffe/models/bvlc_googlenet place the custom deploy.prototxt file and the custom trained model renamed as bvlc_googlenet.caffemodel,
or change the source code...
in the input folder place the image for visulization, in the output/jp folder the output images will be placed

aftwer that, from the root folder where the visualize_layers.py script is located run the script from terminal:

python visualize_layers.py --base-model /home/devf13/caffe/models/bvlc_googlenet \
	--image images/jp.jpg --output output/jp


initital source code :
http://www.pyimagesearch.com/2015/08/03/deep-dream-visualizing-every-layer-of-googlenet/

