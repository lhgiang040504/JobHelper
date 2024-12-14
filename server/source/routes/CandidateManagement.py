from fastapi import APIRouter, status, UploadFile, File, Request, Body
from source.controller.CandidateManagement import postExtractCVInfo, createCandidate, getAllCandidates, deleteCandate, getCandidateById
from source.models.candidate import Candidate
# Định nghĩa router
router = APIRouter()


@router.post("/extract_cv_info")
async def extract_cv_info(request: Request, file: UploadFile = File(...)):
    print(file)
    return await postExtractCVInfo(request, file)

@router.post("/create_candidate")
async def create_candidate(request: Request, candidate: Candidate = Body(...)):
    return await createCandidate(request, candidate)

@router.get("/get_all_candidates")
async def get_all_candidates(request: Request):
    return await getAllCandidates(request)

@router.get("/get_candidate/{candidate_id}")
async def get_candidate_by_id(request: Request, candidate_id: str):
    return await getCandidateById(request, candidate_id)

@router.delete('/delete/{candidate_id}')
async def delete_candidate(request: Request, candidate_id: str):
    return await deleteCandate(request, candidate_id)
