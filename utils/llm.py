from dotenv import load_dotenv
from langchain_groq import ChatGroq
import dotenv
import os
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from source.database.models import Candidate
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
        template="""Extract the following structured information from the provided CV text. If information is missing, leave it blank. 
        **Important:** Do not modify the `id` field; it should remain as it is (it can be either provided or left blank for MongoDB to auto-generate).
        \n{format_instructions}\n{query}\n""",
        input_variables=["query"],
        partial_variables={"format_instructions": cv_parser.get_format_instructions()},
    )
    return llm, cv_parser, cv_prompt
