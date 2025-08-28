```markdown
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&weight=700&size=32&duration=1&pause=1000&color=00F5D4&center=true&width=600&lines=Touchless+Drag+%26+Drop" alt="Typing">
</p>

<p align="center">
  <em>Move, resize and spawn objects with nothing but your hand ✋✨</em>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-4.x-5D3FD3?style=flat-square&logo=opencv&logoColor=white"/>
  <img alt="MediaPipe" src="https://img.shields.io/badge/MediaPipe-0.10+-0F9D58?style=flat-square&logo=google&logoColor=white"/>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
</p>

---

## 🎬 15-Second Demo
<p align="center">
  <img src="https://i.imgur.com/4iE3HqL.gif" width="85%" alt="Touchless interaction demo"/>
  <br/>
  <sub>Grab • Move • Resize • Spawn — all without touching the screen.</sub>
</p>

---

## 🚀 Quick Start (30 s)

```bash
# 1️⃣ Clone & jump in
git clone https://github.com/yourname/TouchlessDragDrop.git
cd TouchlessDragDrop

# 2️⃣ One-liner install
pip install -r requirements.txt      # opencv-python mediapipe cvzone

# 3️⃣ Go!
python main.py
```

<details open>
<summary>🖥️ Recommended Setup</summary>

- **Camera**: 720 p or better  
- **Lighting**: Even, front-facing light (avoid back-light)  
- **Distance**: 40-80 cm from webcam  
</details>

---

## 🎛️ Hand-Gesture Cheatsheet

| Gesture | Action | Preview |
|---------|--------|---------|
| 👌 **Pinch** (index + thumb) | Grab object | ![grab](https://i.imgur.com/8x9n3uC.gif) |
| ✋ **Open Palm** (all fingers) | Spawn new box | ![spawn](https://i.imgur.com/7q4Vw9P.gif) |
| 🤏 **Stretch Pinch** | Resize grabbed object | ![resize](https://i.imgur.com/y5zQ8YH.gif) |

---

## 🛠️ Tech Stack

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,opencv" height="50" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="50" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="50" />
</div>

- **Python 3.10+** — Rapid prototyping  
- **OpenCV + MediaPipe** — Real-time hand tracking & rendering  
- **CVZone** — High-level gesture abstractions  

---

## 🧪 Features Deep-Dive

<details>
<summary>✨ Smooth Animated Transitions</summary>

Every grab / release triggers a 200 ms ease-out scale animation so the interaction feels tactile and responsive.

```python
# pseudo-snippet
if grabbing:
    animate_scale(obj, 1.2, duration=200, easing="easeOutCubic")
else:
    animate_scale(obj, 1.0, duration=200)
```
</details>

<details>
<summary>🚧 Boundary Protection</summary>

Objects are clamped to screen edges so they never get “lost”.

```python
x = max(0, min(x, frame_w - w))
y = max(0, min(y, frame_h - h))
```
</details>

<details>
<summary>🎨 Glow Effect While Grabbing</summary>

A soft neon outline appears only when an object is currently held.

```python
cv2.rectangle(img, (x,y), (x+w,y+h), color, 2, cv2.LINE_AA)
cv2.GaussianBlur(img[y:y+h, x:x+w], (15,15), 0)
```
</details>

---

## 🏗️ Project Structure

```
TouchlessDragDrop/
├── images/
│   └── box.png
├── utils/
│   ├── hand_tracker.py
│   └── animator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔮 Roadmap

- [ ] Multi-object simultaneous drag  
- [ ] Collision detection & physics  
- [ ] Save / load workspace layout (JSON)  
- [ ] Multi-user support (up to 2 hands each)  
- [ ] Voice commands (“spawn red box”)  

---

## 🤝 Contributing

We ❤️ pull requests!  
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the dev setup and coding style.

---

## 📄 License

MIT © [Your Name](https://github.com/yourname)

---

## 🖼️ Media Kit

| Still Image | GIF |
|-------------|-----|
| ![still](https://i.imgur.com/JpKzP7m.png) | ![gif](https://i.imgur.com/4iE3HqL.gif) |

Right-click → “Save link as” to download.

---

<p align="center">
  <i>Made with 🖐️ and a pinch of Python.</i>
</p>
```
