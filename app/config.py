from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#import databaseuri from .env
import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("DATABASE_URI")
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)



'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(uri)
Session = sessionmaker(bind=engine)
from sqlalchemy import text


def test_connection():
    session = Session()
    try:
        session.execute(text('SELECT * FROM usertable'))
        print('Database connection successful')
    except Exception as e:
        print('Database connection failed:', e)
    finally:
        session.close()

test_connection()

'''
