# Convert all this to a function to add to database assume we have data

def add_flashcards(data):
    for flashcard in data['info']:
        unit_name = flashcard['unit_name']
        topic = flashcard['topic']
        question = flashcard['question']
        answer = flashcard['answer'].encode('utf-8')

        conn = connect_to_database()
        cur = conn.cursor()

        cur.execute("INSERT INTO flashcards (flashcard_unit, flashcard_topic, flashcard_question, flashcard_answer) VALUES (%s, %s, %s, %s)", (unit_name, topic, question, answer))
        conn.commit()

add_flashcards(data)



def add_Course()