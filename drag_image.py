import cv2

class DragImage:
    def __init__(self, path, pos):
        self.imgOriginal = cv2.imread(path)
        self.img = self.imgOriginal.copy()
        self.pos = pos
        self.size = self.img.shape[:2]  # (height, width)
        self.dragging = False
        self.scale = 1
        self.target_scale = 1
        self.smoothness = 0.08  # Animation speed

    def update(self, cursor, grabbing, pinch_distance):
        x, y = self.pos
        h, w = self.size
        cx, cy = cursor

        if x < cx < x + w and y < cy < y + h:
            if grabbing:
                self.dragging = True

        if not grabbing:
            self.dragging = False

        if self.dragging:
            self.pos = (cx - w // 2, cy - h // 2)

            # Resize while dragging based on pinch
            new_scale = max(0.5, min(pinch_distance / 100, 2))  # Limit zoom
            if abs(new_scale - self.scale) > 0.05:
                self.target_scale = new_scale

        # Animation: Smoothly move toward target scale
        self.scale += (self.target_scale - self.scale) * self.smoothness
        self.img = cv2.resize(self.imgOriginal, (0, 0), fx=self.scale, fy=self.scale)
        self.size = self.img.shape[:2]

    def draw(self, background, grabbed):
        x, y = self.pos
        h, w = self.size

        # Boundary checking
        h_bg, w_bg = background.shape[:2]
        x = max(0, min(x, w_bg - w))
        y = max(0, min(y, h_bg - h))
        self.pos = (x, y)

        if h > 0 and w > 0:
            try:
                background[y:y+h, x:x+w] = self.img
            except:
                pass

        # Glow effect
        if grabbed:
            cv2.rectangle(background, (x, y), (x+w, y+h), (0, 255, 255), 4)

        return background
