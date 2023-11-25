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
        return True
    except:
        print("I am unable to connect to the database")
        return False

conn = connect_to_database()
cur = conn.cursor()

@app.route('/')
# Connect to database first, if this is possible then return 200, start calling functions, else return 401
def index():
    if conn:
        return jsonify("I WORK"), 200
    else:
        return jsonify("I DON'T WORK"), 401



@app.route('/users/addCourse', methods=['POST'])
def addCourse():
    # Get userID and courseID from request
    userID = request.json['userID']
    courseID = request.json['courseID']


@app.route('/users/retrieveCourses', methods=['POST'])
def getCourses():
    # Get userID from request
    userID = request.json['userID']
    # Get courses from database
    courses = []
    # Return courses
    cur.execute("SELECT course_id FROM usercourses WHERE user_id = %s", (userID,))






if __name__ == '__main__':
    app.run(debug=True)


