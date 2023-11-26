from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')

from . import routes

# {% extends "base.html" %}
# {% block title %}Home{% endblock %}
# {% block content %}
# <style>
#     .hero-section {
#         height: 100vh;
#         display: flex;
#         flex-direction: column;
#         align-items: center;
#         justify-content: center;
#         background: linear-gradient(135deg, #6e8efb, #a777e3);
#         color: white;
#     }
#
#     .hero-title {
#         font-weight: bold;
#         font-size: 7rem;
#         text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
#     }
#
#     .hero-subtitle {
#         font-size: 1.5rem;
#         margin-top: 1rem;
#         opacity: 0.9;
#     }
#
#     .hero-button {
#         padding: 1rem 2rem;
#         margin-top: 2rem;
#         font-size: 1.2rem;
#         background-color: #fff;
#         color: #6e8efb;
#         border-radius: 8px;
#         text-decoration: none;
#         transition: background-color 0.3s, color 0.3s;
#     }
#
#     .hero-button:hover {
#         background-color: #a777e3;
#         color: white;
#     }
# </style>
#
# <div class="hero-section">
#     <h1 class="hero-title">Pet Playlists</h1>
#     <p class="hero-subtitle">Study more effectively than ever with the power of AI.</p>
#     <a href="{{ url_for('auth.login') }}" class="hero-button" type="button">LET'S GO</a>
# </div>
# {% endblock %}
