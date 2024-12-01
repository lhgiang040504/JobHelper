from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from source.models.candidate import Candidate
from fastapi.encoders import jsonable_encoder
from source.models.job import JobDescription
from source.services.Resume_Job_Matching import Rule
from source.models.job_resume_matching import JobResumeMatching
import logging
import uuid

# Logger để ghi lỗi
logger = logging.getLogger(__name__)


async def createJobResumeMatching(request: Request, candidate: Candidate = Body(...), job: JobDescription = Body(...)):
     try:
          rule = Rule(job, candidate)
          result = rule.get_match()
          print(result)
          
          database = request.app.mongodb.get_database()
          job_resume_matching = database["job_resume_matching"]

          new_job_resume_matching = JobResumeMatching(**result)
          new_job_resume_matching = jsonable_encoder(new_job_resume_matching)
          new_job_resume_matching = await job_resume_matching.insert_one(new_job_resume_matching)
          created_job_resume_matching = await job_resume_matching.find_one({"_id": new_job_resume_matching.inserted_id})
     except Exception as e:
        logger.error(f"Failed to create job resume macthing: {e}")
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
               "message": "Job Resume Matching created successfully",
               "data": created_job_resume_matching
          }
     )