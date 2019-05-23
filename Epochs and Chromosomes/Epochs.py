""" Python test for PBIL implementation,
	See the Github: 
	https://github.com/albert118/Population-Based-Incremental-Learning

	Author: Albert Ferguson """

from random import randint
from inspect import getargvalues
from sys import _getframe

class Epoch():
	def __init__(self, debug, **kwargs):
	# kwargs dict: 4 vals
	# learnRate, numTerminals, numConcentrators, maxConcentrators
		try:
			# debug default values, sanity check if debug enabled
			if(debug):
				print("Running the debug Epoch!")
				self.generation = 0
				self.probVec = [0.5] * 12
				self.LR = 0.05
				self.terminalCount = 12
				self.conentratorCount = 8
				self.maxConcCount = 3

				self.chromosomes = []
				self.numChromosomes = 12
				# init the chromosomes (bit list)
				self.initSolutions() 
				# print the data back to stdout
				self.printEpoch()

			elif (not debug):
				self.generation = 0
				self.probVec = [0.5] * kwargs[numTerminals]
				self.LR = kwargs[learnRate]
				self.terminalCount = kwargs[numTerminals]
				self.conentratorCount = kwargs[numConcentrators]
				self.maxConcCount = kwargs[maxConcentrators]

				self.chromosomes = []
				self.numChromosomes = kwargs[numTerminals]
				# init the chromosomes (bit list)
				self.initSolutions()

			else:
				raise Exception(list(kwargs))
		except Exception as inst:
			print(type(inst))
			print(inst)
			print("Bad argument format")
			print()
			print(getargvalues(_getframe()))

	def __str__(self):
		return self.generation

	# initialise the solution set (bit list of concentrators
	# connected to terminals)
	def initSolutions(self):
		for i in range(self.numChromosomes):
			self.chromosomes.append(Solution(self.terminalCount, self.conentratorCount, self.maxConcCount))

	# update prob_vec using the learning rate
	def updateProbVec(self):
		for i in range(len(probVec)):
			newProbVec[i] = self.probVec[i] + self.chromosomes[i] * self.LR
		self.probVec = newProbVec

	# increment generation and update prob_vec
	def nextGen(self, chromosomeIDs):
		self.generation += 1
		self.numChromosomes = len(chromosomeIDs)
		self.chromosomes = chromosomeIDs

	# formatted epoch and solution set printing
	def printEpoch(self):
		print("Generation: {}\t Chromosome Count: {}".format(self.generation, self.numChromosomes))
		for i in range(self.numChromosomes):
			self.chromosomes[i].printSolutionSet()

# the base class solution sets inherit from
class Chromosome():
	""" The parent class for all solution children classes. """
	def __init__(self, chromID):
		self.ID = chromID

	def __str__(self):
		return self.ID

# solution set class defintion 
# for the terminal-concentrator problem
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
