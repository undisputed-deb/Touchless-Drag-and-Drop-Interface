# 🖐️ Touchless Drag-and-Drop Interface (Advanced Version)

This project allows users to **grab**, **move**, **resize**, **spawn**, and experience **smooth animated transitions** for on-screen objects — using just **hand gestures** and a webcam.

Built with **Python**, **OpenCV**, and **MediaPipe**, it showcases futuristic, touchless user interface designs with modern visual feedback.

---

<div align="center">
  
![Touchless Interface Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWZvY2V0dWJ0a2V2bGJ4a2Q3c2J6dW1qZ3V4eWp6cWp6b3o0eGZ6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7kn27lnYSA3GJYW5ZV/giphy.gif)

*Demo showing grab, move, resize, and spawn functionality with smooth animations*

</div>

---

## ✨ Features

| Feature | Description | Visual |
|---------|-------------|--------|
| **Multiple Draggable Images** | Move different objects separately | ![Drag](https://img.icons8.com/fluency/48/000000/drag.png) |
| **Pinch to Resize** | Shrink or enlarge objects naturally | ![Resize](https://img.icons8.com/fluency/48/000000/resize.png) |
| **Glow Effect** | Visual highlight while holding an object | ![Glow](https://img.icons8.com/fluency/48/000000/glow.png) |
| **Animated Transitions** | Smooth scale animation for realistic UX | ![Animation](https://img.icons8.com/fluency/48/000000/animation.png) |
| **Boundary Protection** | Objects stay within screen boundaries | ![Boundary](https://img.icons8.com/fluency/48/000000/boundary.png) |
| **Gesture Spawning** | Open palm creates new draggable objects | ![Spawn](https://img.icons8.com/fluency/48/000000/plus.png) |

---

## 🚀 How It Works

<div align="center">
  
![Gesture Mapping](https://i.imgur.com/5K5f7Eo.png)

*Hand gesture mapping for different interactions*

</div>

1. **Webcam captures** your hand via MediaPipe HandTracking
2. **Pinch fingers** (index + thumb close) → **Grab** object
3. **Move hand** → Object follows cursor with smooth animation
4. **Stretch pinch** → Resize (zoom in/out) the object
5. **Open palm** → **Spawn new** draggable object
6. **Grab/release** → Smooth animated scaling for visual feedback

---

## 🛠️ Technologies Used

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5CB3FF?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-FF6F00?style=for-the-badge&logo=google&logoColor=white)
![CVZone](https://img.shields.io/badge/CVZone-4285F4?style=for-the-badge&logo=google&logoColor=white)

</div>

---

## 📥 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- Webcam
- Git

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/touchless-drag-drop.git
   cd touchless-drag-drop
   ```

2. **Create and activate virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Project Structure**
   ```
   TouchlessDragDrop/
   ├── images/
   │   ├── box.png
   │   └── object2.png
   ├── main.py
   ├── drag_image.py
   ├── requirements.txt
   ├── README.md
   └── demo.gif
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

---

## 🎮 Usage Guide

<div align="center">
  
![Usage Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2Z3dWJ6c3lqZ2h2N2N0eGZ6dG5xZ2V5dGJ6ZzZ0dGZ6ZzZ0dGZ6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4Vtk43fQzSqZaGJ5dR/giphy.gif)

*Demonstration of different gestures and interactions*

</div>

| Gesture | Action | Visual Feedback |
|---------|--------|-----------------|
| 👌 Pinch with thumb and index | Grab and move object | Glow effect + smooth following |
| 👌 Pinch and move fingers apart | Resize object | Smooth scaling animation |
| 🖐 Open palm for 2 seconds | Spawn new object | Particle effect at spawn point |
| ✋ Release pinch | Drop object | Bounce animation on placement |

---

## 🔧 Customization

### Adding New Objects
Place your image files in the `images/` folder and update the code:
```python
# In main.py
object_paths = ["images/box.png", "images/your_image.png", "images/another_object.png"]
```

### Adjusting Animation Parameters
Modify animation properties in `drag_image.py`:
```python
# Animation settings
self.animation_speed = 0.2  # Adjust for faster/slower animations
self.glow_intensity = 15    # Increase for more prominent glow
self.max_scale = 2.0        # Maximum resize scale
self.min_scale = 0.5        # Minimum resize scale
```

---

## 🌟 Why This Project Matters

- **Hygienic Interaction**: No physical contact required
- **Natural User Interfaces**: Intuitive hand gesture control
- **Real-time Computer Vision**: Combines advanced tracking with user-friendly UX
- **Prototype Potential**: Foundation for AR/VR applications, smart devices, and accessibility technologies

<div align="center">
  
![Application Areas](https://i.imgur.com/r8BQ5aP.png)

*Potential application areas for touchless interfaces*

</div>

---

## 🔮 Future Enhancements

| Feature | Status | Description |
|---------|--------|-------------|
| Multi-object dragging | Planned | Drag multiple objects simultaneously |
| Advanced physics | In Progress | Bounce/drop effects with gravity simulation |
| Collision detection | Planned | Detect and respond to object collisions |
| Multi-user support | Research | Track multiple users simultaneously |
| Layout persistence | Planned | Save/load object positions between sessions |

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## 🙌 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for robust hand tracking
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [CVZone](https://github.com/cvzone/cvzone) for helpful computer vision utilities

---

<div align="center">

**Experience the future of interaction today!** 🚀

</div>
