# Initial prompt would tell the model that it is a professor for the course it's given and it cna asnwer and generate any questions related to the course
# OPTIONAL: Have a separate prompt to deciper the topic of the question and input that as the description for the model (ex. You are a {physics, math, etc.} expert.)
        # This would scan the entire syllabus doc and find the subject based on the content

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


API_KEY = os.getenv('OPENAI_API_KEY')

os.environ['OPENAI_API_KEY'] = API_KEY

llm = OpenAI(openai_api_key=API_KEY, max_tokens=1000)

template = """You are a professor for the course {course} at {university}. \
            You can answer any qustion with great detail and are able to generate questions for any topic within the course to best help the student prepare for assessments. \
            The student will provide you with either the unit name, midterm prep, or final prep, and your job is to generate appropriate questions to help the student understand the topic better, as well as the best possible and most concise answer to that question. \
            Generate 10 such questions. The unit will be delimited by three backticks. ```{unit}```. \
             
            Provide the output in JSON format. The two main keys are component, which hold the value "flashcard", and info, which holds the following info: unit_name, topic, question, answer.
            
            
            """

prompt = PromptTemplate(template=template, input_variables=["course","university","unit"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

course = "PHYS 1401"
university = "University of Western Ontario"
unit = "circular motion"

response = llm_chain.run({'course': course, 'university': university, 'unit': unit})

print(response.encode('utf-8').decode('unicode-escape').json()) 