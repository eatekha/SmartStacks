from app import app

if __name__ == "__main__":
    # Create some test users
    from app.models import User

    User.add_user('admin', 'admin')

    app.run(debug=True)
