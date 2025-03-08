# DigiZest-1.0 Hackathon - Smart Home Automation (Face Recognition Module)

This repository contains a crucial component of our **Smart Home Automation System**, developed during the **DigiZest 1.0 Hackathon**. This module focuses on **real-time face recognition** to identify known individuals and automate home appliances based on their preferences.

## 🚀 Overview

Our system uses **OpenCV** and **DeepFace** to detect and recognize faces in real time. It captures video from a webcam, detects faces, and compares them with pre-loaded reference images to identify specific individuals. Based on the recognition results, the system can trigger specific actions (e.g., turning on lights, adjusting thermostat settings, etc.) as part of the larger home automation system.

## 🛠️ Technologies Used
- **Python**
- **OpenCV** - For real-time video capture and face detection.
- **DeepFace** - For deep learning-based face recognition.
- **Threading** - To optimize face recognition performance.

## ⚙️ How It Works
1. Captures a video feed from the webcam.
2. Detects faces using OpenCV's **Haar Cascade Classifier**.
3. Compares the detected faces with stored reference images using **DeepFace**.
4. Displays recognition results:
   - ✅ `"RMATCH!"` (Recognized Person 1)
   - ✅ `"PMATCH!"` (Recognized Person 2)
   - ❌ `"NO PERSON!"` (No face detected)
   - 🚨 `"INTRUDER!"` (Unknown person detected)
5. Based on the recognition results, the **home automation system** can trigger specific actions.

## 📌 Dependencies
Ensure you have the following installed:
```bash
pip install opencv-python deepface
