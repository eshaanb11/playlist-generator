from flask import Flask, render_template, request
import requests
from waitress import serve
from dotenv import load_dotenv
import os
# from pprint import pprint

load_dotenv()

app = Flask(__name__)

BASE_URL = "https://ws.audioscrobbler.com/2.0/"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")

        params = {
            "method": "tag.gettoptracks",
            "tag": genre,
            "api_key": os.getenv("API_KEY"),
            "format": "json",
            "limit": 15
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return render_template(
                "index.html",
                error="Genre not found. Please try another name."
            )
        # pprint(data)

        tracks = []
        for track in data["tracks"]["track"]:
            tracks.append({
                "name": track["name"],
                "url": track["url"]
            })

        return render_template(
            "playlist.html",
            genre=genre.title(),
            tracks=tracks
        )

    return render_template("index.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)