from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from source.services.Job_Info_Extraction import JobInfoExtraction
from utils.llm import get_Jobs_parser
import logging

# Logger để ghi lỗi
logger = logging.getLogger(__name__)

async def postExtractJobInfo(request: Request):
    # Lấy nội dung text từ request
    try:
        body = await request.json()
        Jobs_content = body.get("text", "").strip()

        # Kiểm tra nếu không có text
        if not Jobs_content:
            return JSONResponse(
                status_code=400,
                content={
                    "status": 400,
                    "success": False,
                    "message": "No text provided"
                }
            )

    except Exception as e:
        logger.error(f"Failed to parse request body: {e}")
        return JSONResponse(
            status_code=400,
            content={
                "status": 400,
                "success": False,
                "message": "Invalid request body"
            }
        )

    # Trích xuất thông tin Job
    try:
        llm, job_parser, job_prompt = get_Jobs_parser()
        job_parser = JobInfoExtraction(llm, job_prompt, job_parser)
        job_info_extracted = job_parser.extract_info(Jobs_content)

        # Kiểm tra xem có dữ liệu trích xuất hay không
        if not job_info_extracted:
            raise ValueError("No job information extracted")

    except Exception as e:
        logger.error(f"Failed to extract Job information: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to extract Job information"
            }
        )

    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "Job information extracted successfully",
            "data": job_info_extracted
        }
    )
