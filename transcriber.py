import whisper
import random

async def transcribe_audio(audio_filepath):
    ran_num = random.randint(1,100)

    audio_file = open(audio_filepath,'r')

  
    model = whisper.load_model('base')
    response = model.transcribe(audio_file,fp16=False)

    response_byte = response['text'].encode('utf-8')

    with open(f"Transcribed{ran_num}.txt","wb") as file:
        file.write(response_byte)
