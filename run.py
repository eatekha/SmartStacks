from app import app

if __name__ == "__main__":
    # Create some test users
    from app.models import User
    app.run(debug=True)
