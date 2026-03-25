from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
 return "CI/CD Pipeline is Live! Version 2.0: Automated
Update Successful!"
if __name__ == '__main__':
 application.run(debug=True)
