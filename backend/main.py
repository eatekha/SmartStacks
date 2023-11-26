# This is the API manager for the backend. It handles all the requests from the frontend and

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

username = "Eseosa"
user_id = "1"

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


#Add a course to the database
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



if __name__ == '__main__':
    app.run(debug=True)


