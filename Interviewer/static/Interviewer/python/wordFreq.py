from nltk.tokenize import word_tokenize
import re
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
	return  word_dic,sorted_list

#add sign filter
s = 'Note: The service capitalizes many proper nouns for the US English language models, en-US_BroadbandModel and en-US_NarrowbandModel. For example, for US English transcriptions, the service returns text that reads "Barack Obama graduated from Columbia University" instead of "barack obama graduated from columbia university," as it does for other language models.'
my_list,sorted_list=wfreq(s)
print (my_list)
print (sorted_list)
print (sorted_list[1][0])
print (sorted_list[1][1])