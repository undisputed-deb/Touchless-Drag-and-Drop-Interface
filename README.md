# 🖐️ Touchless Drag-and-Drop Interface (Advanced Version)

This project allows users to **grab**, **move**, **resize**, **spawn**, and now experience **smooth animated transitions** for on-screen objects — using just **hand gestures** and a webcam.

Built with **Python**, **OpenCV**, and **MediaPipe**, it showcases futuristic, touchless user interface designs.

---

## 🎯 Features
- 🖼️ **Multiple draggable images** — Move different objects separately
- 📏 **Pinch to resize images** — Shrink or enlarge objects naturally
- ✨ **Glow effect when grabbing** — Visual highlight while holding an object
- 🎬 **Animated transitions on grab/release** — Smooth scale animation for realistic UX
- 🚧 **Boundary protection** — No dragging objects outside the screen
- ✋ **Gesture to spawn new object** — Open palm creates a new draggable box

---

## 🚀 How It Works
- Webcam captures your hand via MediaPipe HandTracking.
- **Pinch fingers** (index + middle close) ➔ **Grab** object.
- **Move hand** ➔ Object follows cursor.
- **Stretch pinch** ➔ Resize (zoom in/out) the object.
- **Open all fingers** ➔ **Spawn new** draggable object.
- **Grab/release** ➔ Smooth animated scaling for better visual feedback.

---

## 🧠 Technologies Used
- Python 3.10
- OpenCV
- MediaPipe
- CVZone

---

## 📥 Installation Instructions
1. Clone this repository or download the project files.
2. Create a virtual environment and install the required packages:
    ```bash
    pip install opencv-python mediapipe cvzone
    ```
3. Project Structure:
    ```
    TouchlessDragDrop/
    ├── images/
    │   └── box.png
    ├── drag_image.py
    ├── main.py
    ├── README.md
    └── venv/
    ```

4. Run the application:
    ```bash
    python main.py
    ```

---

## 📸 Demo Screenshot / GIF
(Add a GIF or image showing grab, move, resize, spawn new object.)

---

## 📢 Why This Project Matters
- Enables **hygienic** interaction (no physical contact).
- Demonstrates the power of **natural user interfaces**.
- Combines **real-time Computer Vision** with **user-friendly UX**.
- Excellent prototype for **AR/VR applications**, **smart devices**, or **accessibility technologies**.

---

## 🙌 Future Upgrades
- Drag multiple objects simultaneously
- Animated bounce/drop effects
- Detect object collisions
- Multi-user support (track 2 people at once)
- Save the layout persistently

