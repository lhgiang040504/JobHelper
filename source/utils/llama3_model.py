from langchain_groq import ChatGroq
import dotenv
import os
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from source.models.candidate import Candidate
from source.models.job import JobDescription
from source.models.job_resume_matching import JobResumeMatching

dotenv.load_dotenv()

LLAMA_3_API_KEY = os.getenv("LLAMA_3_API_KEY")

def get_CVs_parser():
    llm = ChatGroq(
        temperature=0,
        groq_api_key = LLAMA_3_API_KEY,
        model_name = "llama-3.1-70b-versatile"
    )

    # Set up a parser + inject instructions into the prompt template.
    cv_parser = JsonOutputParser(pydantic_object=Candidate)

    cv_prompt = PromptTemplate(
        template="""
            #Intruduction#
            You are a good CV filter. You are provided with a CV text.\n
            {data}
            #Context#
            Currently, I am working on a project that requires extracting structured information from CVs. I need to extract the following structured information from the provided CV text. If information is missing, leave it blank.
            #Task#
            Extract the following structured information from the provided CV text. If information is missing, leave it blank. 
            #Requirment# 
            1. If information is missing, leave it blank.
            2. Convernt the extracted information into English. 
            #Format_instructions# : {format_instructions}
        """,
        input_variables=["data"],
        partial_variables={"format_instructions": cv_parser.get_format_instructions()},
    )
    return llm, cv_parser, cv_prompt

def get_Jobs_parser():
    llm = ChatGroq(
        temperature=0,
        groq_api_key = LLAMA_3_API_KEY,
        model_name = "llama-3.3-70b-versatile"
    )

    # Set up a parser + inject instructions into the prompt template.
    job_parser = JsonOutputParser(pydantic_object=JobDescription)

    job_prompt = PromptTemplate(
        template="""        
        #Intruduction#
        You are a good Job Decription filter. You are provided with a Job Decription text: \n
        {data}
        #Context#
        Currently, I am working on a project that requires extracting structured information from JDs. I need to extract the following structured information from the provided JDs text. If information is missing, leave it blank.
        #Task#
        Extract the following structured information from the provided CV text.
        #Requirment# 
        1. If information is missing, leave it blank.
        2. Convernt the extracted information into English. 
        #Format Instructions#\n
        {format_instructions}
         """,
     input_variables=["data"],
     partial_variables={"format_instructions": job_parser.get_format_instructions()},
    )
    return llm, job_parser, job_prompt


def matching_CVs_JDs():
    llm = ChatGroq(
        temperature=0,
        groq_api_key = LLAMA_3_API_KEY,
        model_name = "llama-3.1-70b-versatile"
    )

    parser = JsonOutputParser(pydantic_object=JobResumeMatching)

    # Set up a parser + inject instructions into the prompt template.
    prompt = PromptTemplate(
        template="""        
        #Intruduction#
        You are a good CV-JD matcher. You are provided with a CV text and a JD text: \n
        {data}
        #Context#
        Currently, I am working on a project that requires matching CVs with JDs. I need to extract the following structured information from the provided CVs and JDs text.
        #Task#
        Match the following structured information from the provided CVs and JDs text.
        #Format Instructions#\n
        {format_instructions}
         """,
     input_variables=["data"],
     partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return llm, parser, prompt
    