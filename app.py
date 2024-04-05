import json
import os

from flask import Flask, render_template

from formatter import get_md_screenings_html, sort_events_by_date
app = Flask(__name__)

@app.route("/")
def uk():
    filepath = os.path.join(app.root_path, 'static', 'json', 'events.json')
    try:
        with open(filepath, 'r') as json_file:
            content = json_file.read()
            content = json.loads(content)
    except FileNotFoundError:
        return "Events file not found."

    events_list = content["localizations"]["uk"]
    sorted_events = sort_events_by_date(events_list)
    md_screenings_html = get_md_screenings_html(sorted_events)

    return render_template('index.html', mobile_screenings=sorted_events, screenings_collection=md_screenings_html)

@app.route("/en")
def en():
    filepath = os.path.join(app.root_path, 'static', 'json', 'events.json')
    try:
        with open(filepath, 'r') as json_file:
            content = json_file.read()
            content = json.loads(content)
    except FileNotFoundError:
        return "Events file not found."

    events_list = content["localizations"]["en"]
    sorted_events = sort_events_by_date(events_list)
    md_screenings = get_md_screenings_html(sorted_events)
    print(md_screenings)

    return render_template('index_en.html', mobile_screenings=sorted_events, screenings_collection=md_screenings)

@app.route("/projects")
def projects_uk():
    return render_template('projects.html')

@app.route("/en/projects")
def projects_en():
    return render_template('projects_en.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=7777)