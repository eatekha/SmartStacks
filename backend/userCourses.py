# Connect to PostgreSQL Database

import psycopg2
import sys
import pprint
#Get password for .env
import os
from dotenv import load_dotenv
load_dotenv()

def connect_to_database():
    try:
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='{}' password='{}'".format(os.getenv("DB_HOST"), os.getenv("DB_PASSWORD")))
    except:
        print("I am unable to connect to the database")
    return conn


conn = connect_to_database()

'''
Placeholder for How We Authenticate Users

'''

#Assume we have userToken
userToken = "123456"

# User Pages -> User Courses

def getUserCourses(userToken):
    cur = conn.cursor()
    # Get User ID
    user_id = 1
    courses = []
    # Return courses
    cur.execute("SELECT courseid FROM usercourses WHERE user_id = %s", (user_id,))
    for course in cur.fetchall():
        cur.execute("select coursename from course where courseid = {}".format(course[0]))
        courses.append(cur.fetchone()[0])
    return courses

getUserCourses(userToken)


def addUserCourse(userToken, courseID):
    cur = conn.cursor()
    # Get User ID
    cur.execute("SELECT user_id FROM usertable WHERE user_token = %s", (userToken,))
    userID = cur.fetchone()[0]
    # Add User's Course
    cur.execute("INSERT INTO usercourses (user_id, course_id) VALUES (%s, %s)", (userID, courseID))
    conn.commit()
    return cur.fetchall()



