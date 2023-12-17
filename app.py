from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is Lavanya here'


@app.route('/problems')
def problems():
    return 'This is my list of problems'

if __name__ == '__main__':
    app.run(debug=True)
