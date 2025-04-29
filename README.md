# 🖐️ Touchless Drag-and-Drop Interface

This project allows users to **grab** and **move** on-screen objects **without touching the screen** — just by using **hand gestures** in front of a webcam.

Built with **Python**, **OpenCV**, and **MediaPipe**, it demonstrates how gesture-based interaction can power futuristic user interfaces.

---

## 🎯 Features
- Touchless interaction using webcam
- Grab and move images naturally using hand gestures
- Real-time hand detection and finger tracking
- Works with any image type (JPG, PNG)

---

## 🚀 How It Works
- The webcam captures your hand using MediaPipe HandTracking.
- When your **index finger** and **middle finger** tips come **close together**, the system recognizes a **"grab"**.
- Move your hand ➔ The selected image follows.
- Separate your fingers ➔ The image is **dropped** in place.

---

## 🧠 Technologies Used
- Python 3.10
- OpenCV
- MediaPipe
- CVZone

---

## 📥 Installation Instructions
1. **Clone this repository** or download the project files.
2. **Install required packages** inside a virtual environment:
    ```bash
    pip install opencv-python mediapipe cvzone
    ```
3. **Make sure your folder structure is:**
    ```
    TouchlessDragDrop/
    ├── images/
    │   └── box.png
    ├── drag_image.py
    ├── main.py
    ├── README.md
    └── venv/ (your virtual environment)
    ```

4. **Run the application:**
    ```bash
    python main.py
    ```

---

## 📸 Demo
(Insert a screenshot or short GIF of your webcam running the project.)

---

## 📢 Why This Project Matters
- Enables **hygienic** user interaction (important for public kiosks, museums, hospitals)
- Prepares for **AR/VR interfaces** where touchless gestures are key
- Shows practical application of **Computer Vision + Real-Time Interaction**
- Opens doors for **accessibility solutions** (for users unable to use a mouse/keyboard)

---

## 🙌 Future Upgrades
- Drag and drop **multiple images** simultaneously
- Add **visual feedback** (glowing box on grab)
- Create a **multi-user system** (detect multiple hands)
- Port to **AR headsets** (e.g., Hololens)

---
