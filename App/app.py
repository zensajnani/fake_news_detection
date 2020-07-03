from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

pipeline = joblib.load('./pipeline1.sav')

app = Flask(__name__)


@app.route('/')
def home():
    name = "TechnologIQ"
    return render_template('index.html', name=name)


@app.route('/api', methods=['POST'])
def get_delay():

    result = request.form
    query_news = result['news']
    translated_query = lang_translate(
        "कोरोना वायरस (COVID 19) महामारी की वजह से भारत समेत")
    query = get_all_query(query_news)
    pred = pipeline.predict(query)
    print(pred)
    return f'<html><body><h1>{pred}</h1> <br> <h3>{query}</h3><h4>{translated_query}</h4><form action="/"> <button type="submit">back </button> </form></body></html>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
