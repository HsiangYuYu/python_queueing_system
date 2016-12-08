# encoding: utf-8
import random
import math
countBlock = 0
def getQueueingLength(queueing_list):
	sum = 0
	for i in queueing_list:
		sum += i.packetLength
	return sum


class Packet(object):
	def __init__(self,arrivalRate,id):
		self.id = id
		self.arrivalRate = arrivalRate
		self.nextTimeInterval = math.log(random.uniform(0,1))/-arrivalRate
		#self.packetLength = (math.log(random.uniform(0,1))/-arrivalRate)*100*10**6
		self.serviceTime = (math.log(random.uniform(0,1))/-12500)
		self.packetLength = self.serviceTime*100*10**6
		self.arrivalTime = 0
		self.startProcessingTime = 0
		self.dwellingTime = 0


packet_list = []
arrRate = int(input("Enter arrivalRate:"))
memeoryCapacity = int(input("Enter memeoryCapacity:"))

for i in range(10000):
	packet_list.append(Packet(arrRate,i))


i = 0
buffer = 0
while i < len(packet_list):
	buffer += packet_list[i].nextTimeInterval
	packet_list[i].arrivalTime = buffer;
	#print 'packet id:',packet_list[i].id,'	Arrives at: ',packet_list[i].arrivalTime
	i+=1

underProcessing_list = []
queueing_list = []
completed_list = []

j = 0 
currentTime = packet_list[0].arrivalTime
while j < len(packet_list):
	if packet_list[j] not in queueing_list:
		queueing_list.append(packet_list[j])
		if getQueueingLength(queueing_list)> memeoryCapacity:
			countBlock+=1
	
	if len(underProcessing_list) == 0:
		underProcessing_list.append(queueing_list[0])
		packet_list[j].startProcessingTime = currentTime
		del queueing_list[0]

	if len(underProcessing_list) == 1:
		currentTime = currentTime + underProcessing_list[0].serviceTime
		i = underProcessing_list[0].id+1
		count = 0
		
		while i < len(packet_list):
			if packet_list[i].arrivalTime < currentTime and packet_list[i] not in queueing_list:
				queueing_list.append(packet_list[i])
				count+=1
				if getQueueingLength(queueing_list)< memeoryCapacity:
					#print getQueueingLength(queueing_list)
					pass
				else:
					countBlock += 1
					#print "countBlock", countBlock
					queueing_list.pop()
					break
			else:
				break
			i+=1
		if count == 0 and j!=len(packet_list)-1:
			currentTime = packet_list[j+1].arrivalTime			
		del underProcessing_list[0]
	j+=1


sum = 0

totaltime = packet_list[-1].startProcessingTime + packet_list[-1].serviceTime


#for x in packet_list:
#	print x.packetLength
rate = countBlock*1.0/10000
print "blocking rate:",rate
#print "average dwelling time:",sum/len(packet_list)













