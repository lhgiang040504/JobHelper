from fastapi import APIRouter, UploadFile, File, HTTPException, status, Request
from fastapi.encoders import jsonable_encoder
from utils.preprocessed_text import read_pdf
from services.CV_Infor_Extraction import CVsInfoExtraction
from utils.llm import get_CVs_parser
import os
import logging

# Logger để ghi lỗi
logger = logging.getLogger(__name__)

# Định nghĩa router
router = APIRouter()

# Định nghĩa hàm xử lý
@router.post(
    "/extract_cv_info",
    status_code=status.HTTP_201_CREATED,
    response_description="Extract CV information",
)
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    # Kiểm tra loại file
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Uploaded file must be a PDF")

    # Lưu file (xử lý tên file an toàn)
    safe_filename = os.path.basename(file.filename)
    file_location = f"./data/CVs/{safe_filename}"
    try:
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
    except Exception as e:
        logger.error(f"Failed to save file: {e}")
        raise HTTPException(status_code=500, detail="Failed to save file")

    # Đọc nội dung file CVs
    try:
        CVs_content = read_pdf(file_location)
    except Exception as e:
        logger.error(f"Failed to read PDF: {e}")
        raise HTTPException(status_code=500, detail="Cannot read file content")

    # Trích xuất thông tin CVs
    try:
        router.llm, router.cv_parser, router.cv_prompt = get_CVs_parser()
        cv_parser = CVsInfoExtraction(router.llm, router.cv_prompt, router.cv_parser)
        cv_info_extracted = cv_parser.extract_info(CVs_content)
    except Exception as e:
        logger.error(f"Failed to extract CV information: {e}")
        raise HTTPException(status_code=500, detail="Cannot extract CV information")
    
    # Lưu thông tin CV vào MongoDB
    try:
        # Đảm bảo lấy database từ app.mongodb
        database = request.app.mongodb.get_database()  # Database kết nối từ MongoDB
        candidates_collection = database['candidates']  # Truy cập collection 'candidates'
        
        candidate_json = jsonable_encoder(cv_info_extracted)  # Chuyển đổi dữ liệu thành JSON
        new_candidate = await candidates_collection.insert_one(candidate_json)  # Lưu vào MongoDB
        
        created_candidate = await candidates_collection.find_one({"_id": new_candidate.inserted_id})  # Lấy ứng viên vừa tạo
    except Exception as e:
        logger.error(f"Failed to save CV information: {e}")
        raise HTTPException(status_code=500, detail="Cannot save CV information")

    # Trả về kết quả thành công
    return created_candidate  # Trả về thông tin ứng viên đã được lưu vào MongoDB
