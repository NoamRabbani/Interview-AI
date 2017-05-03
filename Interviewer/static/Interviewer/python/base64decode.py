import re
import base64
from django.core.files.base import ContentFile

def base64ToWav(user_speech_base64encode):
    dataUrlPattern = re.compile('data:audio/wav;base64,(.*)$')
    user_speech_base64encode = dataUrlPattern.match(user_speech_base64encode).group(2)

    # If none or len 0, means illegal image data
    if (user_speech_base64encode == None or len(user_speech_base64encode) == 0):
        print("error, photo is invalid")

    # Decode the 64 bit string into 32 bit
    user_speech_base64encode = base64.b64decode(user_speech_base64encode)

    # Transform 32 bit string to png
    speech_file = ContentFile(user_speech_base64encode, 'speech_file.wav')

    return speech_file
