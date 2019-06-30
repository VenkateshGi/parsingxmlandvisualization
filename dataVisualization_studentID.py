from parser_studentID import *
import matplotlib.pyplot as plt
import pandas as pd
def visualizeWordDistribution(inputFile, outputImage="o"):
	#write your code here
	inp = open(inputFile).read()
	each_post = re.findall("<row(.*)/>",inp)
	vocab_count = []
	for item in each_post:
		visualize = Parser(item)
		vocab_count.append(visualize.getVocabularySize())
	plt.hist(vocab_count,bins=range(0, 110, 10))
	plt.xticks(range(5, 115, 10),["0-10","10-20","20-30","30-40","40-50",\
	"50-60","60-70","70-80","80-90","90-100"],rotation = 90)
	plt.xlabel("Vocabulary words length")
	plt.ylabel("no.of posts")
	plt.title("Vocabulary length vs no.of posts")
	plt.savefig(outputImage)


def visualizePostNumberTrend(inputFile, outputImage):
	#write your code here
	inp = open(inputFile).read()
	each_post = re.findall("<row(.*)/>",inp)
	empty_dict={}
	for item in each_post:
		question_or_answer = re.search("PostTypeId=\"(\d+)\"",item).group(1)
		if question_or_answer in ["1","2"]:
			quarter = Parser(item).getDateQuarter()
			if quarter in empty_dict:
				if question_or_answer == "1":
					empty_dict[quarter]["question"]+=1
				else:
					empty_dict[quarter]["answer"]+=1
			else:
				empty_dict[quarter] = {"question" : 0, "answer" : 0}
	print(empty_dict)
	main_update = []
	for key,item in empty_dict.items():
		main_update.append([key,item["question"],item["answer"]])
	print(main_update)
	df = pd.DataFrame(main_update,columns = ["ID","question","answer"])
	print(df.head())
	ax = df.plot()
	ax.set_xticklabels(df.ID, rotation=90)
	plt.xlabel('quarters')
	plt.title("Quarters vs no.of POSTS ")
	plt.ylabel('posts', fontsize=16)
	plt.savefig(outputImage)
	print("***************figures are stored***************")

if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"

	visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
