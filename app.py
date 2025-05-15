from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import os
import cv2
import base64
from datetime import datetime
import numpy as np

app = Flask(__name__)
FACES_FOLDER = "faces"
ATTENDANCE_FILE = "attendance.txt"

os.makedirs(FACES_FOLDER, exist_ok=True)

def log_attendance(name):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ATTENDANCE_FILE, "a") as f:
        f.write(f"{name} - {timestamp}\n")

def get_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        return []
    with open(ATTENDANCE_FILE, "r") as f:
        return f.readlines()

@app.route("/")
def index():
    return render_template("index.html", attendance=get_attendance())

@app.route("/verify", methods=["POST"])
def verify():
    try:
        data = request.json['image']
        encoded_data = data.split(',')[1]
        img_bytes = base64.b64decode(encoded_data)
        img_array = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        temp_path = "temp.jpg"
        cv2.imwrite(temp_path, img)

        result = DeepFace.find(temp_path, db_path=FACES_FOLDER, enforce_detection=False)

        if len(result) > 0 and not result[0].empty:
            identity = os.path.basename(result[0].iloc[0]['identity'])
            name = os.path.splitext(identity)[0]
            log_attendance(name)
            return jsonify({"status": "success", "message": f"Welcome, {name}!"})
        else:
            return jsonify({"status": "fail", "message": "Face not recognized."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
