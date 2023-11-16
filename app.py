from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return "No data present, visit /form to submit a form."
    if request.method == 'POST':
        data = request.form
        return render_template('data.html', form_data = data)

if __name__ == "__main__":
    app.run(debug=True)