from flask import render_template
from flask_login import login_required
from . import flashcards


@flashcards.route('/flashcards')
@login_required
def carousel():
    flashcards_data = [
        {
            'question': 'What is the principle of superposition in physics?',
            'answer': 'The principle of superposition states that when two or more waves overlap, the total displacement at any point is equal to the sum of the individual displacements at that point.'
        },
        {
            'question': "What is Newton's third law of motion?",
            'answer': 'Newton\'s third law of motion states that for every action, there is an equal and opposite reaction. This means that in every interaction, there is a pair of forces acting on the two interacting objects with equal magnitude and opposite direction.'
        },
        {
            'question': 'What is the speed of light in a vacuum?',
            'answer': 'The speed of light in a vacuum is approximately 299,792,458 meters per second (often rounded to 300,000 kilometers per second). This speed is a fundamental constant of nature and is the maximum speed at which all energy, matter, and information in the universe can travel.'
        },
        {
            'question': 'What is the difference between kinetic and potential energy?',
            'answer': 'Kinetic energy is the energy an object possesses due to its motion, whereas potential energy is the stored energy of an object due to its position or state. For example, a moving car has kinetic energy, while a ball at the top of a hill has potential energy.'
        },
        {
            'question': "What is Heisenberg's Uncertainty Principle?",
            'answer': 'Heisenberg\'s Uncertainty Principle is a fundamental theory in quantum mechanics that states it is impossible to simultaneously know both the exact position and exact momentum of a particle. The more precisely one property is measured, the less precisely the other can be known.'
        }
    ]

    return render_template('carousel.html', flashcards=flashcards_data)
