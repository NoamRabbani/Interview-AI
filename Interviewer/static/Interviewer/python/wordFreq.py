from nltk.tokenize import word_tokenize
import re
import matplotlib.pyplot as plt
##removes non non-alphanumeric characters based on re
def re_nalpha(str):
	pattern = re.compile(r'[^\w\s]', re.U)
	return re.sub(r'_', '', re.sub(pattern, '', str))

def wfreq (text):
	word_dic = {}
	if isinstance(text,str):
		#preprocessing module is used to tokenize the text
		text = word_tokenize(re_nalpha(text))
		for word in text:
			if word not in word_dic:
				word_dic[word] = 1
			else:
				word_dic[word] +=1
	else:
		for sent in text:
			sent_str = word_tokenize(re_nalpha(sent[0]))
			for word in sent_str:
				if word not in word_dic:
					word_dic[word] = 1
				else:
					word_dic[word] +=1
	sorted_list = sorted(word_dic.items(), key=lambda d: d[1],reverse=True)
	return sorted_list
def create_pic(input_text):
	sorted_list=wfreq(input_text)
	print (sorted_list)
	x_list = []
	y_list = []
	for item in sorted_list:
		x_list.append(item[0])
		y_list.append(item[1])
	x=range(len(x_list[:5]))
	plt.bar(x, y_list[:5],width=0.9)
	plt.xticks((x),x_list)
	plt.savefig('freq.png')
