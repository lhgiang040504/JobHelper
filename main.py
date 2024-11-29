from fastapi import FastAPI, UploadFile, File, HTTPException
import os
from utils.preprocessed_text import read_pdf
from dotenv import dotenv_values
from source.database.db_connection import MongoDB

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb = MongoDB(uri=config['MONGODB_URI'], db_name=config['MONGODB_DB'])
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb.close()
    print("Disconnected to the MongoDB database!")

@app.post('/upload-CVs/')
async def upload_pdf(file: UploadFile = File(...)):
     # Kiểm tra loại file
     if file.content_type != 'application/pdf':
         raise HTTPException(status_code=400, detail='File must be a pdf')
     # Lưu file
     file_location = f'./data/CVs/{file.filename}'
     with open(file_location, 'wb+') as file_object:
         file_object.write(await file.read())

     # Đọc nội dung file CVs
     try:
        CVs_content = read_pdf(file_location)
     except Exception as e:
        raise HTTPException(status_code=500, detail='Cannot read file content')
          
     return {'file_name': file.filename, 'content': CVs_content}