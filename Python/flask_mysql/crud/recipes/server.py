from flask_app import app
from flask_app.controllers import users_controller, recipes_controller

# -----------import controllers here--------------

if __name__ == '__main__':
    app.run(debug=True)