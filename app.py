from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from summarize_video import summarize_video

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/summarize", methods=["POST"])
def summarize():
    url = request.form["url"]
    title, summary = summarize_video(url=url)
    return jsonify(
        {
            "title" : title,
            "summary" : summary.to_dict()        
        }
    )