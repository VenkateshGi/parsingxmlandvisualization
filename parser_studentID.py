import re
from preprocessData_studentID import preprocessLine
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()

	def __str__(self):
		return """ ID : {} \n Post Type : {}\n Date Quarter : {}\n Clean Body : {}\n"""\
		.format(self.ID, self.type, self.dateQuarter,self.cleanBody)

	def getID(self):
		return re.search("Id=\"(\d+)\"",self.inputString).group(1)


	def getPostType(self):
		return re.search("PostTypeId=\"(\d+)\"",self.inputString).group(1)

	def getDateQuarter(self):
		CreationDate = re.search("CreationDate=\"(\d+)-(\d+)",self.inputString)
		year = CreationDate.group(1)
		month = int(CreationDate.group(2))
		if month < 4:
			month = "Q1"
		elif month < 7:
			month = "Q2"
		elif month < 10:
			month = "Q3"
		else:
			month = "Q4"
		return year+month


	def getCleanedBody(self):
		
		return preprocessLine(self.inputString)


	def getVocabularySize(self):
		vocabulary = self.cleanBody.lower()
		for i in punctuations:
			vocabulary.replace(i," ")
		print(vocabulary)
		return len(set(vocabulary.split()))
