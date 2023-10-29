from flask import Flask, render_template
import requests
import json
import os
#import time

app = Flask(__name__)

# Load environment variables from the .env file
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

# Access environment variables
api_key=os.environ["API_KEY"]

def get_memes():
    url = ("https://meme-api.com/gimme")    
    response = json.loads(requests.request("GET",url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def meme_index():
    #time.sleep(5)
    meme_pic, subreddit = get_memes()    
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/map")
def map():    
    location = "Calgary, Ab"
    iframe_src = f"https://www.google.com/maps/embed/v1/place?key={api_key}&q={location}"
    return render_template("map.html", iframe_src=iframe_src)

@app.route("/navbar")
def navbar():
    return render_template("bootstrap_navbar.html")


app.run("0.0.0.0", port=8080)