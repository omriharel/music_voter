import thread
import sys
import youtube
import semaphore
from flask import Flask
app = Flask(__name__)

songs = semaphore.Semaphore(1)
youtube_client = youtube.Client()

@app.route("/")
def hello():
    # globals are bad but fast check for development
    global songs
    global youtube_client
    thread.start_new_thread(youtube_client.start_new_video, (songs, 'https://www.youtube.com/watch?v=o0u4M6vppCI',))
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
