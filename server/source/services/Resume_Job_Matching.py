import uuid
from typing import List, Optional
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Predefined dictionary for major relatedness
MAJOR_DICT = {
    "computer science": ["software engineering", "data science", "artificial intelligence", "kỹ thuật phần mềm", "khoa học dữ liệu", "trí tuệ nhân tạo"],
    "electrical engineering": ["electronics", "telecommunications", "embedded systems", "điện tử", "viễn thông", "hệ thống nhúng"],
    "economics": ["business administration", "finance", "accounting", "marketing", "quản trị kinh doanh", "tài chính", "kế toán", "tiếp thị"],
    # Add more majors and their related fields here
}

# Define a skill matching algorithm
def calculate_match(job_skills, candidate_skills):
    matched_skills = []
    unmatched_skills = []

    # Direct matches
    for skill in candidate_skills:
        if skill in job_skills:
            matched_skills.append(skill)
        else:
            unmatched_skills.append(skill)

    # Cosine similarity for unmatched skills
    tfidf_vectorizer = TfidfVectorizer().fit(job_skills + unmatched_skills)
    job_vectors = tfidf_vectorizer.transform(job_skills)
    candidate_vectors = tfidf_vectorizer.transform(unmatched_skills)

    similar_skills = []
    for idx, candidate_vector in enumerate(candidate_vectors):
        similarities = cosine_similarity(candidate_vector, job_vectors)
        max_similarity = max(similarities[0]) if similarities.size > 0 else 0
        if max_similarity > 0.7:  # Threshold for similarity
            similar_skills.append(unmatched_skills[idx])

    matched_skills.extend(similar_skills)

    return matched_skills

def calculate_degree_match(job_degree, candidate_degree):
    if isinstance(job_degree, list):
        return 1.0 if candidate_degree in [deg.lower() for deg in job_degree] else 0.0
    return 1.0 if candidate_degree.lower() == job_degree.lower() else 0.0

def calculate_major_match(job_major, candidate_major):
    candidate_major_lower = candidate_major.lower()
    if isinstance(job_major, list):
        if candidate_major_lower in [maj.lower() for maj in job_major]:
            return 1.0
        # Check relatedness using MAJOR_DICT
        for major in job_major:
            related_majors = MAJOR_DICT.get(major.lower(), [])
            if candidate_major_lower in related_majors:
                return 0.5
        return 0.0
    return 1.0 if candidate_major_lower == job_major.lower() else 0.0

# Define the Rule class
class Rule:
    def __init__(self, job, resume):
        self.job = job.dict()
        self.resume = resume.dict()

    def get_match(self):
        job_skills = self.job.get("skills", [])
        candidate_skills = self.resume.get("skills", [])
        job_degree = self.job.get("degree", [])
        candidate_degree = self.resume.get("degree", "").lower()
        job_major = self.job.get("acceptable_majors", [])
        candidate_major = self.resume.get("major", [""])[0].lower()

        matched_skills = calculate_match(job_skills, candidate_skills)
        degree_match_score = calculate_degree_match(job_degree, candidate_degree)
        major_match_score = calculate_major_match(job_major, candidate_major)

        result = {
            "_id": str(uuid.uuid4()),
            "job_id": self.job.get("id", ""),
            "resume_id": self.resume.get("id", ""),
            "list_matching_skills": matched_skills,
            "matching_degree_score": degree_match_score,
            "matching_major_score": major_match_score,
            "matching_skill_score": round(len(matched_skills) / len(job_skills), 2),
        }
        return result
    

# Example usage
if __name__ == "__main__":
    job_description = {
        "id": "job123",
        "role": "Embedded Software Developer",
        "experience": 1,
        "acceptable_majors": [
            "Computer Science",
            "Electrical Engineering"
        ],
        "skills": [
            "C/C++",
            "Python",
            "Shell Script",
            "RTOS",
            "Linux",
            "ARM architecture",
            "Microprocessor/Computer architectures",
            "Debugging",
            "ML/DL",
            "OpenCV",
            "PyTorch",
            "TensorFlow",
            "Caffe"
        ],
        "degree": ["Bachelor"]
    }

    candidate_resume = {
        "id": "resume456",
        "contact": {
            "name": "Nguyen Duy Tam Anh",
            "phone_number": "0935592852",
            "email": "nguyenduytamanh03012004@gmail.com",
            "linkedin": "https://www.linkedin.com/in/t%C3%A2m-anh-nguy%E1%BB%85n-duy-bb33942b7",
            "location": "Thu Duc, Ho Chi Minh"
        },
        "role": {
            "name": "AI Engineer",
            "num_experience": 0
        },
        "language": [
            "English",
            "Vietnamese"
        ],
        "skills": [
            "Python",
            "C/C++",
            "Machine Learning",
            "numpy",
            "pandas",
            "matplotlib",
            "SQL Server",
            "FastAPI",
            "MongoDB",
            "Langchain",
            "Pytorch",
            "Transformer",
            "scikit-learn"
        ],
        "major": ["Computer Science"],
        "degree": "Bachelor",
        "file_name": "CV Nguyễn Duy Tâm Anh - AI Engineer Intern-TopCV.vn.pdf"
    }
    print("Job Description:", job_description)
    rule = Rule(job=job_description, resume=candidate_resume)
    match_result = rule.get_match()

    print("Match Result:", match_result)
