from watson_developer_cloud import SpeechToTextV1
import json

stt = SpeechToTextV1(username="5ff4851b-de60-45c5-9fdb-e0d7d9b866c2", password="3siYdkUyzVoj")

audio_file = open("clinton_200003_genome.wav", "rb")

result = json.dumps(stt.recognize(audio_file, content_type="audio/wav",model="en-UK_NarrowbandModel",continuous="true",timestamps="true",word_confidence="True",keywords=["completion","this"],keywords_threshold="0.1"), indent=2)

print result
wjdata = json.loads(result)


for subs in wjdata["results"]:
	print "transcript"
	print subs["alternatives"][0]["transcript"]
	print "timestamps"
	print subs["alternatives"][0]["timestamps"]
	print "confidence"
	print subs["alternatives"][0]["confidence"]
	print "word_confidence"
	print subs["alternatives"][0]["word_confidence"]
	print "keywords_result"
	print subs["keywords_result"]
# https://www.ibm.com/watson/developercloud/doc/speech-to-text/input.html#models can select model