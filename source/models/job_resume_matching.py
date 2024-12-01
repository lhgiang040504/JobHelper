from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class JobResumeMatching(BaseModel):
     id : str = Field(default_factory=uuid.uuid4, alias="_id")
     job_id: str = Field(..., description="The job id")
     resume_id: str = Field(..., description="The resume id")
     matching_skill_score: float
     # matching_major_score: float
     # matching_role_score: float
     # matching_experience_score: float
     list_matching_skills: List[str] = Field(description="The list of matching skills between the job and the resume")

     class Config:
           populate_by_name = True
           json_schema_extra = {
                "example": {
                     "job_id": '066de609-b04a-4b30-b46c-32537c7f1f6e',
                     "resume_id": '066de609-b04a-4b30-b46c-32537c7f1f6e',
                     "matching_skill_score": 0.8,
                    #  "matching_major_score": 0.9,
                    #  "matching_role_score": 0.7,
                    #  "matching_experience_score": 0.5,
                     "list_matching_skills": ["Python", "Java", "C++"]
                }
           }

