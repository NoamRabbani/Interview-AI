from watson_developer_cloud import SpeechToTextV1
import json, base64
from nltk.tokenize import word_tokenize
import re
import matplotlib.pyplot as plt
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
from wordcloud import WordCloud
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
	plt.savefig('Interviewer/static/Interviewer/userMedia/freq.png')
	plt.close()

def create_emo(input_text):
	natural_language_understanding = NaturalLanguageUnderstandingV1(
		version='2017-02-27',
		username='6a28fa30-2bd7-4981-9037-09e3e8a3a691',
		password='ZtUrPvaSmxKL')

	response = natural_language_understanding.analyze(
		text=input_text,
		features=[features.Emotion()])
	result=json.loads(json.dumps(response, indent=2))
	print(result)
	emo_rate=result["emotion"]["document"]["emotion"]
	labels = ['sadness', 'joy', 'fear', 'disgust','anger']
	sizes = [emo_rate['sadness'], emo_rate['joy'], emo_rate['fear'], emo_rate['disgust'],emo_rate['anger']]
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','black']
	patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
	plt.legend(patches, labels, loc="best")
	plt.tight_layout()
	plt.savefig('Interviewer/static/Interviewer/userMedia/emo.png')
	plt.close()
def word_could(text):
# Generate a word cloud image
	wordcloud = WordCloud().generate(text)
	wordcloud = WordCloud(max_font_size=40).generate(text)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig('Interviewer/static/Interviewer/userMedia/wordcloud.png')
	plt.close()




def speech_to_text(b64code):

	stt = SpeechToTextV1(username="5ff4851b-de60-45c5-9fdb-e0d7d9b866c2", password="3siYdkUyzVoj")

	audio_file = base64.b64decode(b64code)

	result = json.dumps(stt.recognize(audio_file, content_type="audio/wav",continuous="true",timestamps="true",word_confidence="True",model="en-UK_NarrowbandModel"), indent=2)

	# print result
	wjdata = json.loads(result)

	temp_str = ''
	for subs in wjdata["results"]:
		# print "transcript"
		temp_str+=subs["alternatives"][0]["transcript"]
	print(temp_str)
	timestamps = subs["alternatives"][0]["timestamps"]
	average_velocity = (timestamps[-1][2]-timestamps[0][1])/len(timestamps)
	print (average_velocity)
	create_pic(temp_str)
	create_emo(temp_str)
	word_could(temp_str)
	result = {'speech_str': temp_str, 'average_velocity': average_velocity}

	return result

# print speech_to_text("clinton_200003_genome.wav")



	# print "timestamps"
	# print subs["alternatives"][0]["timestamps"]
	# print "confidence"
	# print subs["alternatives"][0]["confidence"]
	# print "word_confidence"
	# print subs["alternatives"][0]["word_confidence"]
	# print "keywords_result"
	# print subs["keywords_result"]
# https://www.ibm.com/watson/developercloud/doc/speech-to-text/input.html#models can select model
