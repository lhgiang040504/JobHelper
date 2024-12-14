from source.models.job import JobDescription
from source.models.candidate import Candidate
from sklearn.metrics.pairwise import cosine_similarity
from source.utils.llama3_model import matching_CVs_JDs
from dotenv import dotenv_values
import numpy as np
import requests

config = dotenv_values(".env")

class Rule:
     def __init__(self, job = JobDescription, resume = Candidate):
          self.job = job
          self.resume = resume
     
     def get_match(self):
          data = f"Candidate: {self.resume} \n Job: {self.job}"
          llm, parser, prompt = matching_CVs_JDs()
          chain = prompt | llm | parser
          result = chain.invoke(input={"data": data})
          return result