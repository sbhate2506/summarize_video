from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from summarize_video import summarize_video
from custom_exception import InvalidUsage
import sys, os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/summarize", methods=["POST"])
def summarize():
    url = request.form["url"]
    try:
        title, summary = summarize_video(url=url)
    except:
        raise InvalidUsage('Something went wrong', 500)
    else:
        return jsonify(
            {
                "title" : title,
                "summary" : summary.to_dict()        
            }
        )

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    return response