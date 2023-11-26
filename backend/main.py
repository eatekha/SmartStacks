# This is the API manager for the backend. It handles all the requests from the frontend and




# TODO - Add authentication to the endpoints
# TODO - Add error handling to the endpoints
# TODO -a wAY TO ADD FLASHCARDS TO THE DATABASE
# TODO - ADD A WAY TO RETRIEVE PAST Q'A;S 


from flask import Flask, jsonify, request
import psycopg2
#Get password for .env
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

#1. Connect to Database
#2. Check if user is authenticated
#3. If authenticated, return data
#4. If not authenticated, return 401

# Before we do anything, call these things need to be met
def connect_to_database():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='{}' password='{}'".format(os.getenv("DB_HOST"), os.getenv("DB_PASSWORD")))
        print("Connected to Database")
        return conn
    except:
        print("I am unable to connect to the database")
        return False

conn = connect_to_database()
cur = conn.cursor()

username = "admin"
user_id = "2"

'''
This file manages all the endpoints for the backend
'''
@app.route('/')
# Connect to database first, if this is possible then return 200, start calling functions, else return 401
def index():
    if conn:
        return jsonify("I WORK"), 200
    else:
        return jsonify("I DON'T WORK"), 401

'''
ALL THESE ENDPOINTS ARE RELATED TO THE COURSES
adding pdf/syllabus is confusing rn
'''


#Add a course to the database and personal sector
@app.route('/courses/addCourse', methods=['POST'])
def addCourse():
        try:
            # Get coursename from request
            coursename = request.json['coursename']
            # Add course to database
            cur.execute("INSERT INTO course (coursename) VALUES (%s)", (coursename,))
            cur.execute("INSERT INTO usercourses (userid, courseid) VALUES (%s, %s)", (user_id, cur.lastrowid))
            conn.commit()
            # Return success
            return jsonify("Course Added"), 200
        except:
            # Return error
            return jsonify("Course Not Added, Problem With Server"), 401




'''
ALL THESE ENDPOINTS ARE RELATED TO THE USERS
'''

# Get all courses a user is registered in from the database
@app.route('/users/retrieveEnrolled', methods=['GET'])
def getCourses():
    try:
        courses = []
        # Return courses
        cur.execute("SELECT courseid FROM usercourses WHERE user_id = %s", (user_id,))
        for course in cur.fetchall():
            cur.execute("select coursename from course where courseid = {}".format(course[0]))
            courses.append(cur.fetchone()[0])
        return jsonify(courses), 200
    
    except:
        # Return error
        return jsonify("Courses Not Retrieved, Problem With Server"), 401



@app.route('/users/getFlashCards', methods=['POST'])
def llm():
        from langchain.chains import LLMChain
        from langchain.llms import OpenAI
        from langchain.prompts import PromptTemplate
        from dotenv import load_dotenv
        import os
        import streamlit as st

        load_dotenv()

        data = request.json  # Assuming the data is sent as JSON
        course = data.get('course')
        school = data.get('school')
        topic = data.get('topic')


        API_KEY = os.getenv('OPENAI_API_KEY')

        os.environ['OPENAI_API_KEY'] = API_KEY

        llm = OpenAI(openai_api_key=API_KEY, max_tokens=1000)

        template = """You are a professor for the course {course} at {school}. \
                You can answer any qustion with great detail and are able to generate questions for any topic within the course to best help the student prepare for assessments. \
                The student will provide you with either the unit name, midterm prep, or final prep, and your job is to generate appropriate questions to help the student understand the topic better, as well as the best possible and most concise answer to that question. \
                Generate 10 such questions. The unit will be delimited by three backticks. ```{topic}```. \
                
                Provide the output in JSON format. The two main keys are component, which hold the value "flashcard", and info, which holds the following info: unit_name, topic, question, answer.
                
                
                """

        prompt = PromptTemplate(template=template, input_variables=["course","school","topic"])
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        '''
        course = "PHYS 1401"
        school = "University of Western Ontario"
        topic = "circular motion" # user input 
        '''
        import json
        response = llm_chain.run({'course': course, 'school': school, 'topic': topic})


        return jsonify(response), 200





def addToHistory(flashcards):
     pass



if __name__ == '__main__':
    app.run(debug=True, port=3000)



