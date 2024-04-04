from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def uk():
    return render_template('index.html')

@app.route("/en")
def en():
    return render_template('index_en.html')

@app.route("/projects")
def projects_uk():
    return render_template('projects.html')

@app.route("/en/projects")
def projects_en():
    return render_template('projects_en.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)