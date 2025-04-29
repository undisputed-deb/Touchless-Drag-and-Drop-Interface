import cv2

class DragImage:
    def __init__(self, path, pos):
        self.img = cv2.imread(path)
        self.pos = pos
        self.size = self.img.shape[:2]  # (height, width)
        self.dragging = False

    def update(self, cursor, grabbing):
        x, y = self.pos
        h, w = self.size
        cx, cy = cursor

        if x < cx < x + w and y < cy < y + h:
            if grabbing:
                self.dragging = True

        if not grabbing:
            self.dragging = False

        if self.dragging:
            self.pos = cx - w // 2, cy - h // 2

    def draw(self, background):
        x, y = self.pos
        h, w = self.size

        # Handle boundary clipping
        h_bg, w_bg = background.shape[:2]
        if y + h > h_bg:
            h = h_bg - y
        if x + w > w_bg:
            w = w_bg - x

        if h > 0 and w > 0:
            background[y:y+h, x:x+w] = self.img[:h, :w]

        return background
