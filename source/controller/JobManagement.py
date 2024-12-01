from fastapi import Request, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from source.services.Job_Info_Extraction import JobInfoExtraction
from utils.llama3_model import get_Jobs_parser
from source.models.job import JobDescription
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

async def createJob(request: Request, job: JobDescription = Body(...)):
    try:
        # Lấy dữ liệu từ Body
        job_data = jsonable_encoder(job)

        database = request.app.mongodb.get_database()
        jobs_collection = database["jobs"]

        new_job = await jobs_collection.insert_one(job_data)
        created_job = await jobs_collection.find_one({"_id": new_job.inserted_id})

    except Exception as e:
        logger.error(f"Failed to create job: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to create job"
            }
        )

    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "Job created successfully",
            "data": created_job
        }
   )

async def getAllJobs(request: Request):
    try:
        database = request.app.mongodb.get_database()
        jobs_collection = database["jobs"]
        jobs = await jobs_collection.find().to_list(length=1000)

    except Exception as e:
        logger.error(f"Failed to get all jobs: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to get all jobs"
            }
        )

    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": "Jobs retrieved successfully",
            "data": jobs
        }
    )

async def deleteJob(request: Request, job_id: str):
    try:
        database = request.app.mongodb.get_database()
        jobs_collection = database["jobs"]
        
        # Kiểm tra xem job có tồn tại hay không
        job = await jobs_collection.find_one({"_id": job_id})
        if not job:
            return JSONResponse(
                status_code=404,
                content={
                    "status": 404,
                    "success": False,
                    "message": "Job not found"
                }
            )
        result = await jobs_collection.delete_one({"_id": job_id})
        if result.deleted_count == 1:
            return JSONResponse(
                status_code=200,
                content={
                    "status": 200,
                    "success": True,
                    "message": "Job deleted successfully"
                }
            )
        else:
            raise Exception("Failed to delete job")
        
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
        
    