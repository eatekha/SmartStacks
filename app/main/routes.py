from flask import render_template
from flask_login import login_required
from . import main
import requests


# Fetch this Route @app.route('/users/retrieveEnrolled', methods=['GET'])
def getCourses():

    # Define the API endpoint URL
    api_url = 'http://127.0.0.1:3000/users/retrieveEnrolled'  # Replace with the actual API endpoint URL

    try:
        # Make a GET request to the API
        response = requests.get(api_url)
        print(response)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON data
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


@main.route('/home')
@login_required
def home():
    cards_data = [
        {
            'title': '',
            'image': ''},
    ]

        # Your dynamic data
    data_array = getCourses()

    # Pass the dynamic data as a variable to the template
    return render_template('home.html', cards=cards_data, card_titles=data_array)
