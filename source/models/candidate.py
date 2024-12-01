from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
import uuid

# Contact model with email validation
class Contact(BaseModel):
    name: str = Field(None, description="The full name of the candidate")
    phone_number: str = Field(None, description="The phone number of the candidate")
    email: Optional[EmailStr] = Field(None, description="Email address")
    linkedin: str = Field(None, description="The LinkedIn profile of the candidate")
    location: str = Field(
        default_factory=str,
        description="Complete street address wherever possible."
    )

class Role(BaseModel):
    name: str = Field(description="The position the candidate is applying for")
    num_experience: float = Field(description='Years of experience deducted from the (number of days between the dates)/365 in title "Kinh nghiệm"')

# Candidate model containing all information about the candidate
class Candidate(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")     
    contact: Contact
    role: Role = Field(description="The position the candidate is applying for")
    language: List[str] = Field(description="The spoken/written language")
    skills: List[str] = Field(description="Extract the technical tools in the following text. Technical tools are generally in 2-3 words")
    major: List[str] = Field(description="The major of the candidate")   

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id" : '066de609-b04a-4b30-b46c-32537c7f1f6e',
                "contact": {
                    "name": "Nguyen Van A",
                    "phone_number": "0123456789",
                    "email": "exampl1@gmail.com",  # Email will be validated
                    "linkedin": "https://www.linkedin.com/in/nguyenvana",
                    "location": "Thu Duc, Ho Chi Minh"
                },
                    "role":{
                         "name": "Software Engineer",
                         "num_experience": 3.5
                },
                    "language": ["English", "Vietnamese"],
                    "skills": ["Python", "Java", "C++"],
                    "major": ["Computer Science"]
            }
        }
