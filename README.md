# Face Verification App (DLASSV1)

A simple Flask web app to verify faces using deep learning models (FaceNet or VGGFace).

## Features
- Upload an image via browser
- Compare it with stored face images
- Supports FaceNet and VGGFace models

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/face-verification-app.git
cd face-verification-app

python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python app.py

