from fastapi import UploadFile, File, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from utils.preprocessed_text import read_pdf
from source.services.CV_Infor_Extraction import CVsInfoExtraction
from utils.llm import get_CVs_parser
import os
import logging

# Logger để ghi lỗi
logger = logging.getLogger(__name__)

async def postExtractCVInfo(request: Request, file: UploadFile = File(...)):
    # Kiểm tra loại file
    if not file.filename:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "success": False,
                "message": "No file uploaded"
            }
        )
    if file.content_type != "application/pdf":
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "success": False,
                "message": "Invalid file type"
            }
        )

    # Lưu file (xử lý tên file an toàn)
    safe_filename = os.path.basename(file.filename)
    file_location = f"./data/CVs/{safe_filename}"
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
    except Exception as e:
        logger.error(f"Failed to save file: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to save file"
            }
        )

    # Đọc nội dung file CVs
    try:
        CVs_content = read_pdf(file_location)
    except Exception as e:
        logger.error(f"Failed to read PDF: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to read PDF"
            }
        )

    # Trích xuất thông tin CVs
    try:
        llm, cv_parser, cv_prompt = get_CVs_parser()
        cv_parser = CVsInfoExtraction(llm, cv_prompt, cv_parser)
        cv_info_extracted = cv_parser.extract_info(CVs_content)
    except Exception as e:
        logger.error(f"Failed to extract CV information: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to extract CV information"
            }
        )
    
    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "CV information extracted successfully",
            "data": cv_info_extracted
        }
    )
