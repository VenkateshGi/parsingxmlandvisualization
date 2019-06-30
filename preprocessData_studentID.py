import re
tag_mapping = {
"&amp;" : "&",
"&quot;" : "\"",
"&apos;" : "'",
"&gt;" : ">",
"&lt;" : "<",
"&#xA;" : " ",
"&#xD;" : " "
}
def preprocessLine(inputLine):
	#preprocess the data in each line
	#write your code here
	for key,value in tag_mapping.items():
		inputLine = inputLine.replace(key,value)
	inputLine = re.search("Body=\"(.*)\"",inputLine).group(1)
	outputLine = ""
	flag = False
	for i in inputLine:
		if i == "<":
			flag = True
		elif i == ">":
			flag = False
		elif flag == False:
			outputLine+=i
	return outputLine

def splitFile(inputFile, outputFile_question, outputFile_answer):
	#preprocess the original file, and split them into two files.
	#please call preprocessLine() function within this function
	#write you code here
	raw_text = open(inputFile).read()
	questions = open(outputFile_question,"w")
	answers = open(outputFile_answer,"w")
	each_post = re.findall("<row(.*)/>",raw_text)
	updated_post = [re.search("PostTypeId=\"(\d+)\"",item).group(1) for item in each_post ]
	#print("updated -----------",updated_post)
	only_questions, only_answers = [], []
	for index,item in enumerate(each_post):
		item = preprocessLine(item)
		each_post[index] = item
		if updated_post[index] == "1":
			questions.write(item+"\n")
		elif updated_post[index] == "2":
			answers.write(item+"\n")


if __name__ == "__main__":

	f_data = "data.xml"
	f_question = "question.txt"
	f_answer = "answer.txt"

	splitFile(f_data, f_question, f_answer)
