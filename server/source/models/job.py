from pydantic import BaseModel, Field
from typing import List
import uuid

class JobDescription(BaseModel):
    id : str = Field(..., default_factory=uuid.uuid4, alias="_id")
    role: str = Field(..., description="Job title")
    experience: float = Field(..., description="Experience level required for the job")
    acceptable_majors: List[str] = Field(..., description="Acceptable majors for the job")
    skills: List[str] = Field(..., description="Skills required for the job")
    degree: List[str] = Field(..., description="Degree required for the job")
    class Config:
            populate_by_name = True
            json_schema_extra = {
               "example": {
                     "_id" : '066de609-b04a-4b30-b46c-32537c7f1f6e',
                     "role": "Software Engineer",
                     "experience": 3.5,
                     "acceptable_majors": ["Computer Science"],
                     "skills": ["Python", "Java", "C++", "Toeic"],
                     "degree": ["Bachelor"]
               }
            }
