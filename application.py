from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "1Your Flask App Works  from docker container!"

@application.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    application.run(host='0.0.0.0',port=8080, debug=True)
