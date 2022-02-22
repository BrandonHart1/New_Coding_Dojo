from flask_app import app
# -----------------  ninjas  ???  ---------------
from flask_app.controllers import ninjas, dojos



if __name__ == "__main__":
    app.run(debug=True)
