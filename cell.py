#/usr/bin/python!

import sys
import numpy as np

class test:

	def __init__(self, number):
		self.number=number
		self.mult=0	
	def func(self):
		self.mult= self.number*2


#u.func()
#u.func()
#print u.mult

#Class cell
#con ... connections,
class cell:
	
	def __init__(self,con):
		self.con=con		#con are its connections
		self.mem=[]		#mem ist the memory of one particular cell
		self.weight=[]
		self.desic=""
	def init_mem(self):			#get es much mems as there are cons for one cell
		for i in self.con:
			self.mem.append(1)
#	init_mem(self)
#	def interact(self):

	def choose_weight(self):	#get the weight of random desicion
	        
		summem=sum(self.mem) 		#sum of rememberd actions
		if len(self.con)==len(self.mem):	#if length of 
			if summem > 0:
				for i in self.mem:
					self.weight.append(float(i)/float(summem))
				self.desic=np.random.choice(self.con,p=self.weight)
			else:
				self.desic=np.random.choice(self.con)
		else:
			print "Error ChooseWeight: length of Arguments must be equal"
	#	print weight
		self.desic=np.random.choice(self.con)
	def call(self,goallist):

        opts=self.con
        respT=self.mem
        choose_weight(self)
#       print cellnum
#       print opts
#       print respT
#       print desi
        if self.desic in goallist:				#if desicion is in goallist
                self.mem[self.con.index(self.desic)]+=1		#add one to the memory at the index of con in which the desicion is
                return True
        elif self.desic in self.con:
#               print desi
                ret=call(self,goallist)
                if ret==True:
                        self.mem[self.con.index(desi)]+=1
                        return True
                else:
                        return False
        else:
                return False

	

liste=[]
i=0
while i <10:
	
	liste.append(cell([i,i+1]))
	liste[i].init_mem()
	liste[i].choose_weight()
	print liste[i].desic
	i+=1
