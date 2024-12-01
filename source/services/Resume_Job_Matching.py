from source.models.job import JobDescription
from source.models.candidate import Candidate
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import dotenv_values
import numpy as np
import requests

config = dotenv_values(".env")

class Rule:
     def __init__(self, job = JobDescription, resume = Candidate):
          self.job = job
          self.resume = resume
          self.job_skills = job.skills
          self.resume_skills = resume.skills
     @staticmethod
     def get_cls(data):
          response = requests.post(config['URL_GET_CLS'], json=data)
          list_cls = response.json()
          return list_cls.get('cls_tokens')
     
     def get_similarity(self, job_skills, resume_skills):
          emb_job_skills = np.array(self.get_cls({"texts" : job_skills}))
          emb_resume_skills = np.array(self.get_cls({"texts" : resume_skills}))
          return cosine_similarity(emb_resume_skills, emb_job_skills)
     
     def get_match(self):
          list_similar_skill = self.get_similarity(self.job_skills, self.resume_skills)
          result = {
               "job_id": self.job.id,
               "resume_id": self.resume.id,
               "matching_skill_score" : 0,
               "list_matching_skills": []
          }
          average_score = 0
          for score in list_similar_skill:
               for j, value in enumerate(score):
                    if value > 0.9:
                         average_score += 1
                         if self.job_skills[j] not in result["list_matching_skills"]:
                             result["list_matching_skills"].append(self.job_skills[j])

          result["matching_skill_score"] = average_score / len(self.job_skills)
          return result