"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base
import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)  # create tables in the database

session = Session()

# Add a new user
User.add_user(session, 'testuser', 'testpassword')

# Retrieve the user
user = User.get_user(session, 'testuser')
if user is not None:
    print('User retrieved successfully')

# Check the password
if user.check_password('testpassword'):
    print('Password is correct')

session.close()"""