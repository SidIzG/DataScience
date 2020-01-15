import numpy as npy
from functools import partial
import PIL.Image
import tensorflow as tf 
import urllib.request
import os
import zipfile

#1. Download google's pre-trained neural network (I'm using the neural network called Inception)
#2. Create a TensorFlow session
#3. Pick a layer in the pre-trained network to enhance the input image
#4. Apply Gradient Ascent algorithm to the layer
#5. Output Deep Dreamed Image

def main():
	url = 'https://storage.googleapis.com/download.tensorflow.org/models/inception5h.zip'
	#data directory where we are extracting the neural network to
	data_dir = '../data'
	#use os module to get the model name and make a local zip file path
	model_name = os.path.split(url)[-1]
	local_zip_file = os.path.join(data_dir, model_name)
	#if there is nothing at that path we can download it using the urllib module and store it in the model url variable
	if not os.path.exists(local_zip_file):
		#Download
		model_url = urllib.request.urlopen(url)
		with open(local_zip_file, 'wb') as output:
			output.write(model_url.read())

		#extract
		with zipfile.ZipFile(local_zip_file, 'r') as zip_ref:
			zip_ref.extractall(data_dir)

	#Create TensorFlow session and load the model
	model_fn = 'tensorflow_inception_graph.pb'

	#initialize graph using Graph() of TensorFlow
	graph = tf.Graph()
	#initialize session using the graph
	session = tf.InteractiveSession(graph=graph)

	#open existing saved inception graph
	with tf.gfile.FastGFile(os.path.join(data_dir, model_fn), 'rb') as f:
		#read graph and parse
		graph_def = tf.GraphDef()
		graph_def.ParseFromString(f.read())

	#define input using an input tensor
	tensor_input = tf.placeholder(npy.float32, name='input')	
	#define image net mean value
	imagenet_mean = 117.0
	tensor_preprocessed = tf.expand_dims(tensor_input-imagenet_mean, 0)
	tf.import_graph_def(graph_def, {'input': tensor_preprocessed})

	#load all the layers into an array called layers
	layers = [op.name for op in graph.get_operations() if op.type=='Conv2D' and 'import/' in op.name]
	#the convolutional layer will output feature channels which we store in feature_nums
	feature_nums = [int(graph.get_tensor_by_name(name+':0').get_shape()[-1]) for name in layers]
	
	def render_deepdream(tensor_obj, image=image_noise, iter_n=10, step = 1.5, oct_n=4, oct_scale=1.4):
		#optimization objective
		tensor_score = tf.reduce_mean(tensor_obj)
		tensor_grad = tf.gradients(tensor_score, tensor_input)[0]

		#split image into a bunch of octaves
		img = image
		octaves = []
		for o in range(octave_n-1):
			hw = image.shape[:2]
			lo = resize(image, npy.int32(npy.float32(hw)/octave_scale))
			high = image-resize(lo, hw)
			image = lo
			octaves.append(high)

		#generate details 
		for oct in range(octave_n):
			if oct > 0:
				high = octaves[-oct]
				image = resize(image, high.shape[:2])+high
			for i in range(iter_n):
				#essentially applying gradient asent
				grad = calc_grad_tiled(image, tensor_grad)
				image += grad*(step / (npy.abs(grad).mean()+1e-7))

			#Output the deep dream image
			showarray(img/255.0)

	#Picking a lower level layer and a feature channel
	layer = 'mixed4d_3x3_bottlenech_pre_relu'
	channel = 139

	#load our input image
	image = PIL.Image.open('jedi_fallen_order.jpg')

	#format the image using numpy and apply deep dream 
	image = npy.float32(image)

	#Apply gradient ascent algorithm to the layer we choose
	render_deepdream(T(layer)[:,:,:,139] image)





