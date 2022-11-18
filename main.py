import shutil
from fastapi import FastAPI,UploadFile,File

app = FastAPI()

@app.post("/files")
async def upload(file: UploadFile = File(...)):
    with open(f'{file.filename}','wb') as buffer:
        shutil.copyfileobj(file.file,buffer)


    return {"file uploaded successfully"}
