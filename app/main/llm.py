from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

os.environ['OPENAI_API_KEY'] = API_KEY

llm = OpenAI(openai_api_key=API_KEY, max_tokens=2000)


def generate_questions(course, topic):
    template = """You are a professor for the course {course}. \
                You can answer any question with great detail and are able to generate questions for any topic within the course to best help the student prepare for assessments. \
                The student will provide you with the course name and relevant topics related to the course, and your job is to generate appropriate questions to help the student understand the topic better, as well as the best possible and most concise answer to that question. \
                Generate 10 such questions. The unit will be delimited by three backticks. ```{topic}```. \
                
                Provide the output in JSON format. The main key is "topic". Topic holds an array of JSON objects, with the following keys: question and answer, which store the question and answer.
                """

    q_prompt = PromptTemplate(template=template, input_variables=["course", "topic"])
    q_llm_chain = LLMChain(prompt=q_prompt, llm=llm)

    response = q_llm_chain.run({'course': course, 'topic': topic})
    response = json.dumps(response)
    return response

# def check_answers(response):
#     user_answer = input("Enter your answer: ")
#     template = """You are a smart professor with the following information: {response}. \
#         The student will provide you with their answer for a question, which is delimited by three angled brackets. \
#         Your job is to check if the user's answer is similar to the answer you were given or not. \
#         Check for both exact values and synonyms. Use your professional judgement as a professor and check thorouoghlt whether the answer is mostly right or not. \
#         If the answer is wrong, provide the correct answer, as well as an elaborate description, explaining why it's wrong. If the answer is right, provide a short description of why the answer is right \
#         ```{user_answer}```. <<<What is the power rule?>>>
#
#
#         """
#     # we can get the question by taking the text of the parent element of the answer component in the flashcard
#     a_prompt = PromptTemplate(template=template, input_variables=["response", "user_answer"])
#     a_llm_chain = LLMChain(prompt=a_prompt, llm=llm)
#
#     response = a_llm_chain.run({'user_answer': user_answer, 'response': final_res})
#
#     return response
#
#
# print(check_answers(final_res))

print(generate_questions("Calculus", "Derivatives"))