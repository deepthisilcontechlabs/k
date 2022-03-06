from flask import Flask
application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/hello")
def hello():
    name = "SilconTechLabs"
    return "Hello !" + name + "!\n"


if __name__ == "__main__":
    application.debug = True
    application.run(port=8080, host="0.0.0.0")