import json
from flask import render_template, redirect, url_for
from flask_login import login_required
from . import main, llm
from .forms import NewCollectionForm


@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    cards_data = [
        {
            'title': '',
            'image': ''},
    ]
    form = NewCollectionForm()
    if form.validate_on_submit():
        response = llm.generate_questions(form.collection_course.data, form.collection_description.data)
        print(response)
        data = json.loads(response)

        # Step 2: Organize and Display the Data
        for flashcard in data['info']:
            print(f"Unit Name: {flashcard['unit_name']}")
            print(f"Topic: {flashcard['topic']}")
            print(f"Question: {flashcard['question']}")
            print(f"Answer: {flashcard['answer'].encode('utf-8')}")

            print("\n")  # Adds a newline for better readability between flashcards
        return redirect(url_for('flashcards.carousel'))
    return render_template('home.html', cards=cards_data, form=form)
