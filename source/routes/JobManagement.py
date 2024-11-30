from fastapi import APIRouter, status, Request
from source.controller.JobManagement import postExtractJobInfo
# Định nghĩa router
router = APIRouter()


@router.post("/extract_job_info")
async def extract_job_info(request: Request):
    return await postExtractJobInfo(request)
