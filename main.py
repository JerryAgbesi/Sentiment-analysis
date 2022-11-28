import shutil
import os.path
from fastapi import FastAPI,UploadFile,File,HTTPException
from transcriber import transcribe_audio

app = FastAPI()

save_path = '/media/jerry/463A06993A068661/Sentiment-analysis/uploaded_files'


@app.post("/files")
async def upload(file: UploadFile = File(...)):
    audio_path = os.path.join(save_path,file.filename)
    with open(audio_path,'wb') as buffer:
        shutil.copyfileobj(file.file,buffer)

    # try:

    await transcribe_audio(audio_path)

    # except:
    #     return("something went wrong")




    

    return {"file uploaded successfully"}
