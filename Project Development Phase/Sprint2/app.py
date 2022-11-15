from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Home Page
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    # logic yet to be built
    if request.method == 'GET':
        return ("Here the logic is defined")
    if request.method == 'POST':
        return ("Here the logic is defined")
if __name__ == '__main__':
    app.run()
