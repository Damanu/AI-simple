#/usr/bin/python!

import sys
import numpy as np

#Program to choose between Options randomly
#Input: List of Options
#Output: Option wich was decided
def ChooseSimple(opts): 		#opts is the list of options to choose from
	thinknp=np.random.rand(len(opts))
	think=[]
	for i in thinknp:
		think.append(i)
	optind=think.index(max(think))
	return(opts[optind])


#Weightet random choosing
#Input: opts: options to choose, respT: list how often to one Option true responded
#Output: descision
def ChooseWeight(opts,respT):
	weight=[]
	sumrespT=sum(respT)
	if len(opts)==len(respT):
		if sumrespT > 0:
			for i in respT:
				weight.append(float(i)/float(sumrespT))
			return(np.random.choice(opts,p=weight))
		else:
			return(np.random.choice(opts))
		#	retnp=np.random.choice(opts)
			#ret=[]
			#for item in retnp:
			#	ret.append(i)
			#return(ret)
	else:
		print "Error ChooseWeight: length of Arguments must be equal"
	print weight
	return(np.random.choice(opts))
	#retnp=np.random.choice(opts,weight)
	#ret=[]
	#for i in retnp:
	#	ret.append(i)
	#return(ret)

def Cell(Brain,Memory,cellnum,goallist):
	
	opts=Brain[cellnum]
	respT=Memory[cellnum]
	desi=ChooseWeight(Brain[cellnum],Memory[cellnum])
	print cellnum
#	print opts
#	print respT
#	print desi
	if desi in goallist:
		Memory[cellnum][Brain[cellnum].index(desi)]+=1
		return True
	elif desi in Brain:
#		print desi
		ret=Cell(Brain,Memory,desi,goallist)
		if ret==True:
			Memory[cellnum][Brain[cellnum].index(desi)]+=1
			return True
		else:
			return False
	else:
		return False

Memory=[]
Brain={0:[1,2],1:[3,2],2:[4,5],3:[0,"N"],4:[1,"Food"],5:["Food","N"]}
for i in Brain:
	Memory.append([1,1])
#print Memory
#print Brain
ii=0
count=0
while ii < 10:
	ii+=1
	erg= Cell(Brain,Memory,0,["Food"])
	print erg
	if erg:
		count+=1
print Brain
print Memory
print count
#print ChooseSimple(["A","B"])
#ChooseWeight(["A","B"],[0,0])
