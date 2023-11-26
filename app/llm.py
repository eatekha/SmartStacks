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

def generate_questions(course, school, topic):

        template = """You are a professor for the course {course} at {school}. \
                You can answer any qustion with great detail and are able to generate questions for any topic within the course to best help the student prepare for assessments. \
                The student will provide you with either the unit name, midterm prep, or final prep, and your job is to generate appropriate questions to help the student understand the topic better, as well as the best possible and most concise answer to that question. \
                Generate 10 such questions. The unit will be delimited by three backticks. ```{topic}```. \
                
                Provide the output in JSON format. The two main keys are component, which hold the value "flashcard", and info, which holds the following info: unit_name, topic, question, answer.
                
                
                """

        q_prompt = PromptTemplate(template=template, input_variables=["course","school","topic"])
        q_llm_chain = LLMChain(prompt=q_prompt, llm=llm)

        course = "PHYS 1401"
        school = "University of Western Ontario"
        topic = "circular motion" # user input 


        response = q_llm_chain.run({'course': course, 'school': school, 'topic': topic})
        print(response)

        response = json.dumps(response, ensure_ascii=False)
        with open('output.json', 'w', encoding='utf8') as f:
                json.dump(response, f)



final_res = generate_questions("PHYS 1401", "University of Western Ontario", "circular motion")

def check_answers(response):  
        user_answer = input("Enter your answer: ")
        template = """You are a smart professor with the following information: {response}. \
        The student will provide you with their answer for a question, which is delimited by three angled brackets. \
        Your job is to check if the user's answer is similar to the answer you were given or not. \
        Check for both exact values and synonyms. Use your professional judgement as a professor and check thorouoghlt whether the answer is mostly right or not. \
        If the answer is wrong, provide the correct answer, as well as an elaborate description, explaining why it's wrong. If the answer is right, provide a short description of why the answer is right \ 
        ```{user_answer}```. <<<What is the power rule?>>> 
        
        
        """
        # we can get the question by taking the text of the parent element of the answer component in the flashcard
        a_prompt = PromptTemplate(template=template, input_variables=["response","user_answer"])
        a_llm_chain = LLMChain(prompt=a_prompt, llm=llm)

        response = a_llm_chain.run({'user_answer': user_answer, 'response': final_res})

        return response


print(generate_questions(final_res))