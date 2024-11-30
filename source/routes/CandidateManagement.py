from fastapi import APIRouter, status, UploadFile, File, Request
from source.controller.CandidateManagement import postExtractCVInfo
# Định nghĩa router
router = APIRouter()


@router.post("/extract_cv_info")
async def extract_cv_info(request: Request, file: UploadFile = File(...)):
    return await postExtractCVInfo(request, file)
