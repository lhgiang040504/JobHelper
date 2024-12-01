from fastapi import APIRouter, status, Request, Body
from source.controller.JobManagement import postExtractJobInfo, createJob, getAllJobs, deleteJob
from source.models.job import JobDescription
# Định nghĩa router
router = APIRouter()


@router.post("/extract_job_info")
async def extract_job_info(request: Request):
    return await postExtractJobInfo(request)

@router.post("/create_job")
async def create_job(request: Request, job: JobDescription = Body(...)):
    return await createJob(request, job)

@router.get("/get_all_jobs")
async def get_all_jobs(request: Request):
    return await getAllJobs(request)

@router.delete("/{job_id}")
async def delete_job(request: Request, job_id: str):
    return await deleteJob(request, job_id)