from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route("/quiz")
def quiz():
    return render_template('quiz.html')


if __name__ == '__main__':
    app.run()
