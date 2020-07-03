from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json
from find_real_news import get_real_news  # get real news from NewsAPI

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
    # returns dictionary with language, original text and translated text
    translated_query = lang_translate(query_news)
    query = get_all_query(translated_query["final_text"])
    pred = pipeline.predict(query)
    print(pred)

    # if news is fake, display alternative real news using NewsAPI
    if pred == ['FAKE']:
        real_news = get_real_news(translated_query["final_text"])
        if real_news["totalResults"] != 0:
            print(real_news)
            return f'<html> <body> <h1> {pred} </h1> <h4> Text: {translated_query["original_text"]} </h4><h4> Language: {translated_query["source_lang"]} </h4><h4> Translated Text: {translated_query["final_text"]} </h4><h2> Real News Alternative: </h2><p> Title: {real_news["title"]} </p><p> Text: {real_news["text"]} </p><p> Link: {real_news["link"]} </p><p> Source: {real_news["source"]} </p><form action="/"> <button type="submit"> Fact Check another Article </button> </form> </body ></ html>'

    return f'<html> <body> <h1> {pred} </h1> <h4> Text: {translated_query["original_text"]} </h4><h4> Language: {translated_query["source_lang"]} </h4><h4> Translated Text: {translated_query["final_text"]} </h4><form action="/"> <button type="submit"> Fact Check another Article </button> </form> </body ></ html>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
