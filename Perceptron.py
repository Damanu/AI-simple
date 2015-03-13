#/usr/bin/python!
import sys
import numpy as np

#code from website: http://natureofcode.com/book/chapter-10-neural-networks/
#At the middle of the Site.

class Perceptron:
	def __init__(self,learning,inpnum): #learning.. val for speed of learning, inpnum... nuber of inputs
		self.learning=learning
		self.weigths=[]
		self.inpnum=inpnum
		i=0
		while True:
			self.weight.append(np.random.choice([1,-1])
			i+=1
			if i==self.inpnum:
				break
	def feedforward(self,inputs):
		su=0
		for i in self.weights:
			su+= i
		return activate(su)
	def activate(self,su):
		if su > 0:
			return(1)
		else: 
			return(-1)
	def train(self,inputs,desired):
		guess = feedforward(inputs)
		error = desired - guess
		i=0
		for x in self.weights:
			self.weights[i]+=self.learning*error*inputs[i]
	
