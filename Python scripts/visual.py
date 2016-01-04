
import caffe
import caffe.draw
from caffe.proto import caffe_pb2
from google.protobuf import text_format

#If you have problems such as getting a blank image you have to change synatax in the proto file:
#http://stackoverflow.com/questions/31008493/caffe-drawing-cnn-net
# network file structure
input_net_proto_file ='path/to/deploy_draw.prototxt'
# output image file
output_image_file ='net_current_model.jpg'
#Arrangement of # network structure: LR, TB, RL etc.
rankdir ='TB'

net = caffe_pb2.NetParameter ()
text_format.Merge(open(input_net_proto_file).read(), net)
print('Net to %s Drawing'% output_image_file)
caffe.draw.draw_net_to_file (net, output_image_file, rankdir)
print('done... ')