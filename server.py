from flask_app import app

# Make sure to add your other controllers here!
from flask_app.controllers import users, dashboard, priorities

if __name__ == "__main__":
    app.run(debug=True)
