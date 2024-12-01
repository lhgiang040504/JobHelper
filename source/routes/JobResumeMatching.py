from fastapi import APIRouter, Request, Body
from source.models.candidate import Candidate
from source.models.job import JobDescription
from source.controller.JobResumeMatching import createJobResumeMatching

router = APIRouter()

@router.post("/createJobResumeMatching")
async def create_job_resume_matching(request: Request, Candidate: Candidate = Body(...), JobDescription: JobDescription = Body(...)):
     return await createJobResumeMatching(request, Candidate, JobDescription)