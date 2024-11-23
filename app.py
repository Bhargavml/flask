from flask import Flask

### WSGI Application
app=Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to this Best Flask course. this course is amazing"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__=="__main__":
    app.run(debug=True)
