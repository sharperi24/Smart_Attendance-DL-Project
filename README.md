# Smart Attendance App
A simple Flask web app to verify faces and mark attendance using deep learning models (FaceNet or VGGFace).
## Features
- Upload an image via browser
- Compare it with stored face images
- Supports FaceNet and VGGFace models

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/face-verification-app.git
cd face-verification-app
```
### 2. Create a virtual environment 
```bash
python -m venv venv
```
### 3. Activate the virtual environment 
```bash
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```
### 4. Install the requirements 
```bash
pip install -r requirements.txt
```
### 5. Run the app using the following command
```bash
python app.py
```

