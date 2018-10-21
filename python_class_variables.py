class InstanceCreationCounter:
	instance_counter = 0
	def __init__(self, name):
		self.name = name
		InstanceCreationCounter.instance_counter += 1
		
	def printNumInstances(self):
		print "Current instance {0}, instance count is {1}".format(self.name, InstanceCreationCounter.instance_counter)

if __name__ == '__main__':
	isntance_to_create = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	for name in isntance_to_create:
		tmp = InstanceCreationCounter(name)
		tmp.printNumInstances()
