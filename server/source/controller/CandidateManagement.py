from fastapi import UploadFile, File, Request, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from source.utils.preprocessed_text import read_pdf
from source.services.Resume_Infor_Extraction import CVsInfoExtraction
from source.utils.llama3_model import get_CVs_parser
from source.models.candidate import Candidate
import os
import logging

# Logger để ghi lỗi
logger = logging.getLogger(__name__)

async def postExtractCVInfo(request: Request, file: UploadFile = File(...)):
    if not file.filename:
        return JSONResponse(
            status_code=400,
            content={"status": 400, "success": False, "message": "No file uploaded"}
        )
    if file.content_type != "application/pdf":
        return JSONResponse(
            status_code=400,
            content={"status": 400, "success": False, "message": "Invalid file type"}
        )

    # Check file size before saving
    if file.size > 2 * 1024 * 1024:  # 2 MB limit
        return JSONResponse(
            status_code=400,
            content={"status": 400, "success": False, "message": "File size exceeds limit"}
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
    # Xử lý limit file size
    if len(CVs_content.split()) > 15000:
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "success": False,
                "message": "File size exceeds limit"
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
    try:
        # Lưu vào database
        database = request.app.mongodb.get_database()
        collection = database["candidates"]

        new_candidate = await collection.insert_one(cv_info_extracted)
        created_candidate = await collection.find_one({"_id": new_candidate.inserted_id})
    except Exception as e:
        logger.error(f"Failed to save candidate: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to save candidate"
            }
        )
    
    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "CV information extracted successfully",
            "data": created_candidate
        }
    )

async def createCandidate(request: Request, candidate: Candidate = Body(...)):
    try:
        # Lấy dữ liệu từ Body
        candidate_data = jsonable_encoder(candidate)

        # Truy cập cơ sở dữ liệu và collection
        database = request.app.mongodb.get_database()
        candidates_collection = database["candidates"]

        # Chèn dữ liệu vào collection
        new_candidate = await candidates_collection.insert_one(candidate_data)
        created_candidate = await candidates_collection.find_one({"_id": new_candidate.inserted_id})

        return JSONResponse(
            status_code=200,
            content={
                "status": 200,
                "success": True,
                "message": "Candidate created successfully",
                "data": created_candidate
            }
        )
    except Exception as e:
        logger.error(f"Failed to create candidate: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to create candidate"
            }
        )

async def getAllCandidates(request: Request):
    try:
        # Truy cập cơ sở dữ liệu và collection
        database = request.app.mongodb.get_database()
        candidates_collection = database["candidates"]

        # Lấy danh sách tất cả các ứng viên
        candidates_cursor = candidates_collection.find()
        candidates = await candidates_cursor.to_list(length=100)  # Giới hạn số lượng kết quả trả về

        # Kiểm tra nếu danh sách ứng viên trống
        if len(candidates) <= 0:
            return JSONResponse(
                status_code=404,
                content={
                    "status": 404,
                    "success": False,
                    "message": "No candidates found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "status": 200,
                "success": True,
                "message": "Candidates retrieved successfully",
                "data": candidates
            }
        )
    except Exception as e:
        logger.error(f"Failed to retrieve candidates: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to retrieve candidates"
            }
        )
    
async def getCandidateById(request: Request, candidate_id: str):
    try:
        # Truy cập cơ sở dữ liệu và collection
        database = request.app.mongodb.get_database()
        candidates_collection = database["candidates"]

        # Lấy thông tin ứng viên
        candidate = await candidates_collection.find_one({"_id": candidate_id})
        if not candidate:
            return JSONResponse(
                status_code=404,
                content={
                    "status": 404,
                    "success": False,
                    "message": "Candidate not found"
                }
            )

        return JSONResponse(
            status_code=200,
            content={
                "status": 200,
                "success": True,
                "message": "Candidate retrieved successfully",
                "data": candidate
            }
        )
    except Exception as e:
        logger.error(f"Failed to retrieve candidate: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to retrieve candidate"
            }
        )

async def deleteCandate(request: Request, candidate_id: str):
    try:
        # Truy cập cơ sở dữ liệu
        database = request.app.mongodb.get_database()  # Thay tên database
        candidates_collection = database["candidates"]

        # Kiểm tra nếu ứng viên tồn tại
        candidate = await candidates_collection.find_one({"_id": candidate_id})
        if not candidate:
            return JSONResponse(
                status_code=404,
                content={
                    "status": 404,
                    "success": False,
                    "message": "Candidate not found"
                }
            )

        # Xóa ứng viên
        result = await candidates_collection.delete_one({"_id": candidate_id})
        if result.deleted_count == 1:
            return JSONResponse(
                status_code=200,
                content={
                    "status": 200,
                    "success": True,
                    "message": "Candidate deleted successfully"
                }
            )
        else:
            raise Exception("Failed to delete candidate")

    except Exception as e:
        logger.error(f"Failed to delete candidate: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to delete candidate"
            }
        )