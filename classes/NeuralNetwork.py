import numpy as np;
import timeit;
from modules.graph_utils import *;
from classes.HiddenLayer import *;
from pybrain.datasets.supervised import SupervisedDataSet;
from pybrain.tools.shortcuts import buildNetwork;
from pybrain.supervised.trainers.backprop import BackpropTrainer;

class NeuralNetwork:
	""" Neural network class """
	def __init__(self, num_inputs, num_outputs, num_hidden_layers):
		self.num_inputs = num_inputs;
		self.num_outputs = num_outputs;
		self.num_hidden_layers = num_hidden_layers;
		self.dataset = None;
		self.network = None;
		self.backprop = None;
		self.epochs = 10;
		print("[NeuralNetwork]: New neural network object created.");

	def buildDataset(self):
		self.dataset = SupervisedDataSet(self.num_inputs, self.num_outputs);
		print("[buildDataset]: Dataset object built.");
		return True;

	def addData(self, data_in, data_out):
		self.dataset.addSample(data_in, data_out);
		print("[addData]: Data appended.");
		return True;

	def buildNetwork(self):
		self.network = buildNetwork(self.num_inputs, self.num_hidden_layers, self.num_outputs);
		print("[buildNetwork]: Network created.");
		return True;

	def backProp(self):
		self.backprop = BackpropTrainer(self.network, learningrate = 0.01, momentum = 0.99);
		print("[backProp]: Back propogation trainer created.");
		return True;

	def testData(self):
		print('[testData]: MSE:', self.backprop.testOnData(self.dataset));

	def trainData(self):
		start = timeit.default_timer();
		self.backprop.trainOnDataset(self.dataset, self.epochs);
		stop = timeit.default_timer();
		print("[trainData]: Training time: "+str(stop - start));
		return True;
