from datetime import datetime
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import smtplib
import threading
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# --- Stage 1: Loading Screen ---
@app.route("/")
def loading():
    return render_template("loading.html")


# --- Stage 2: Live Calendar Counter ---
@app.route("/counter")
def counter():
    return render_template(
        "counter.html",
        birth_iso="2008-11-16T00:00:00",
        birth_label="November 16, 2008"
    )


# --- Stage 3: Interactive Chocolate Cake ---
@app.route("/cake")
def cake():
    return render_template("cake.html")

# --- Stage 4: Personal Note ---
@app.route("/note")
def note():
    heading = "Happy 18th Birthday Maidam Ji"
    paragraph = (
        "Aapko birthday mubarak ho, Madam ji! 🎂✨ Main chahta hoon ki aap yun hi hamesha muskurati rahein aur zindagi mein aage badhti rahein. 🌸 Aapka yeh naya saal dher saari khushiyon se bhara rahe aur aap kamyabi ki nayi unchaiyon tak pahunchein! 🌟💖"
    )
    youtube_url = "https://youtu.be/K2aJTT29ZdU?si=t6_RYU2_hcH4r8ko"
    return render_template(
        "note.html",
        heading=heading,
        paragraph=paragraph,
        youtube_url=youtube_url
    )


# --- Background Checkpoint Endpoint ---
@app.route("/checkpoint", methods=["POST"])
def checkpoint():
    data = request.get_json(silent=True) or {}
    stage_name = data.get("stage", "Unknown Action")
    timestamp = datetime.now().strftime("%d %b %Y, %I:%M:%S %p")

    threading.Thread(
        args=(stage_name, timestamp),
        daemon=True
    ).start()

    return jsonify({"status": "queued"}), 202


if __name__ == "__main__":
    app.run()