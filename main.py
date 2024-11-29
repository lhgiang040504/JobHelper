from fastapi import FastAPI, UploadFile, File, HTTPException
from PyPDF2 import PdfReader
import os

app = FastAPI()

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
         reader = PdfReader(file_location)
         CVs_content = ''
         for page in reader.pages:
             CVs_content += page.extract_text()
     except Exception as e:
           raise HTTPException(status_code=500, detail='Cannot read file content')
          
     return {'file_name': file.filename, 'content': CVs_content}