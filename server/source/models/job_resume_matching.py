from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

class JobResumeMatching(BaseModel):
     id : str = Field(default_factory=uuid.uuid4, alias="_id")
     job_id: str = Field(..., description="The job id")
     resume_id: str = Field(..., description="The resume id")
     list_matching_skills: List[str] = Field(description="The list of matching skills between the job and the resume")
     matching_skill_score: Optional[float] = Field(description="len(list_matching_skills) / len(job.skills)")
     matching_degree_score: Optional[float] = Field(description="1 if the degree of the resume is acceptable for the job, else 0")
     matching_major_score: Optional[float] = Field(description="1 if the major of the resume is acceptable for the job, else 0 and 0.5 if the major of the resume related to the major of the job")
     total_score: Optional[float] = Field(description="matching_skill_score + matching_degree_score + matching_major_score")
                                          

     class Config:
           populate_by_name = True
           json_schema_extra = {
                "example": {
                     "job_id": '066de609-b04a-4b30-b46c-32537c7f1f6e',
                     "resume_id": '066de609-123-4b30-b46c-32537c7f1f6e',
                     "matching_skill_score": 0.8,
                     "matching_degree_score": 1,
                     "matching_major_score": 0.5,
                     "list_matching_skills": ["Python", "Java", "C++"],
                     "total_score": 2.3
                }
           }

