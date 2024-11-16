from flask import Flask, render_template, jsonify
from threading import Thread
from streaming import start_streaming  # Ensure this module is implemented correctly
import time

app = Flask(__name__)

# Thread-safe shared data structure
from threading import Lock

processed_data = []
data_lock = Lock()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/data")
def data():
    API_KEY = "AIzaSyAXD4UtUwto_Eo6HKCs4lAeMDh3Z8BFy8k"  # Ensure this is valid
    VIDEO_ID = "4gulVzzh82g"

    # Start streaming in a separate thread
    def stream_comments():
        global processed_data
        data = start_streaming(API_KEY, VIDEO_ID)  # Assumes start_streaming returns data
        with data_lock:
            processed_data.extend(data)  # Safely update the shared list

    comment_thread = Thread(target=stream_comments, daemon=True)
    comment_thread.start()

    # Let the user know the process has started
    return jsonify({"message": "Streaming started!", "processed_data": processed_data})


if __name__ == "__main__":
    app.run(debug=True)
