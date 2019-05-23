""" Python test for PBIL implementation,
	See the Github: 
	https://github.com/albert118/Population-Based-Incremental-Learning

	Author: Albert Ferguson """

from random import randint

class Epoch():
	def __init__(self, debug, **kwargs):
	# kwargs dict: 4 vals
	# learnRate, numTerminals, numConcentrators, maxConcentrators
		try:
			if(debug):
				argDict = {
					'numTerminals': 12, 'numConcentrators': 8, 
					'maxConcentrators': 3,'learnRate': 0.05 
					}

				debugEpoch = self.__init__(0, argDict)
				debugEpoch.printEpoch()

			elif (not debug):
				self.generation = 0
				self.probVec = [0.5] * kwargs[numTerminals]
				self.LR = kwargs[learnRate]
				self.terminalCount = kwargs[numTerminals]
				self.conentratorCount = kwargs[numConcentrators]
				self.maxConcCount = kwargs[maxConcentrators]

				self.chromosomes = []
				self.numChromosomes = kwargs[numTerminals]
				self.initSolutions()
			else:
				raise Exception(list(kwargs))
		except Exception as inst:
			print(type(inst))
			print(inst.args)
			print(inst)
			print("Bad argument format")

	def initSolutions(self):
		for i in range(self.numChromosomes):
			self.chromosomes.append(Solution(numTerminals, numConcentrators, maxConcentrators))

	def __str__(self):
		return self.generation

	def updateProbVec(self):
		for i in range(len(probVec)):
			newProbVec[i] = self.probVec[i] + self.chromosomes[i] * self.LR
		self.probVec = newProbVec

	def nextGen(self, chromosomeIDs):
		self.generation += 1
		self.numChromosomes = len(chromosomeIDs)
		self.chromosomes = chromosomeIDs

	def printEpoch(self):
		print("Generation: {}\t Chromosome Count: {}".format(self.generation, self.numChromosomes))
		for i in range(self.numChromosomes):
			self.chromosomes[i].printSolutionSet()

class Chromosome():
	""" The parent class for all solution children classes. """
	def __init__(self, chromID):
		self.ID = chromID

	def __str__(self):
		return self.ID

class Solution(Chromosome):
	def __init__(self, numTerminals, numConcentrators, maxConcentrators):
		self.terminalCount = numTerminals
		self.conentratorCount = numConcentrators
		
		self.network = self.createNetwork(numTerminals)
		while(not self.validNet(self.network, self.conentratorCount, maxConcentrators)):
			self.network = self.createNetwork(numTerminals)

	def createNetwork(self, x):
		network = []
		for i in range(x):
			concBit = ''
			for j in range(3): # TODO: dynamically determine number of bits in range!
				# generate bitwise int value for the concentrator
				concBit += str(randint(0, 1))
			network.append(str(concBit))
		return network

	def validNet(self, network, y, argCheck):
		# if a concBit occurs more than three times: invalid
		concCounter = [0] * y
		for i in range(len(network)):
			# int takes a string value and base to determine decimal
			concCounter[int(network[i], 2)]

		if max(concCounter) > argCheck:
			return 0
		return 1

	def printSolutionSet(self):
		print("Terminals: {}\t Concentrators: {}\t".format(self.terminalCount, self.conentratorCount))
		print("Network Connections:\n{}\n".format(self.network))

test = Epoch(1)