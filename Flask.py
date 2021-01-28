from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello there, I am Jesse. I develop softwares in Python3, HTML, JavaScript, CSS, Angular, React, Nodejs, SQL, mySQL, postgreSQL, C#, Java, Flutter and Arduino. Check out: 'https://github.com/jessedeveloperinvestor'"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
