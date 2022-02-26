from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template('Home.html')


@app.route("/quiz")
def quiz():
    return render_template('Quiz.html')


@app.route("/info")
def info():
    return render_template('Info.html')


if __name__ == '__main__':
    app.run()
