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
          
          database = request.app.mongodb.get_database()
          job_resume_matching = database["job_resume_matching"]

          new_job_resume_matching = JobResumeMatching(**result)
          new_job_resume_matching = jsonable_encoder(new_job_resume_matching)
          new_job_resume_matching['matching_skill_score'] = len(new_job_resume_matching['list_matching_skills']) / len(job.skills)
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
async def getTopKJobResumeMatching(request: Request, job_id: str):
    try:
        database = request.app.mongodb.get_database()
        job_resume_matching = database["job_resume_matching"]
        candidates = database["candidates"]
        job_resume_matching_list = []

        # Aggregation pipeline để lấy Top K job resume matching
        pipeline = [
            {
                '$match': {
                    'job_id': job_id  # Lọc theo job_id
                }
            },
            {
                '$group': {
                    '_id': None,  # Không nhóm theo trường nào
                    'topK': {
                        '$topN': {
                            'output': '$$ROOT',  # Lấy toàn bộ tài liệu
                            'sortBy': {'total_score': -1},  # Sắp xếp giảm dần theo total_score
                            'n': 10  # Số lượng tài liệu cần lấy
                        }
                    }
                }
            }
        ]

        # Lấy danh sách top K job resume matching
        list_candidate_matching = await job_resume_matching.aggregate(pipeline).to_list(length=1)
        result = []

        for candidate in list_candidate_matching[0]['topK']:
            candidate_id = candidate['resume_id']
            find_candidate = await candidates.find_one({"_id": candidate_id})
            result.append(candidate|find_candidate)
        
        job_resume_matching_list = result
            

    except Exception as e:
        logger.error(f"Failed to get top {10} job resume matching: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "success": False,
                "message": "Failed to get top job resume matching"
            }
        )

    # Trả về kết quả thành công
    return JSONResponse(
        status_code=200,
        content={
            "status": 200,
            "success": True,
            "message": f"Top {10} Job Resume Matching",
            "data": job_resume_matching_list
        }
    )