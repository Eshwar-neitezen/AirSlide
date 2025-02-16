# Airslide: Hand-Gesture-Based Scrolling

Airslide is a Python project that uses hand gestures to control screen scrolling. It utilizes OpenCV, MediaPipe, and PyAutoGUI to track hand movements from the webcam and simulate scrolling actions.

---

## Features
- Real-time hand tracking using MediaPipe.  
- Detects palm facing the camera.  
- Processes only right-hand gestures.  
- Scrolls based on thumb and index finger positions.  
- Displays live video with hand landmarks.  

---

## Requirements
- Python 3.10+  
- OpenCV (`cv2`)  
- MediaPipe  
- PyAutoGUI  

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/airslide.git
   cd airslide
