import shutil
from fastapi import FastAPI,UploadFile,File
from transcriber import transcribe_audio

app = FastAPI()

@app.post("/files")
async def upload(file: UploadFile = File(...)):
    with open(f'{file.filename}','wb') as buffer:
        shutil.copyfileobj(file.file,buffer)
    
    await transcribe_audio(file.filename)

    

    return {"file uploaded successfully"}
