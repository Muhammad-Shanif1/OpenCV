import cv2
import json
import numpy as np

IMAGE_PATH = "/home/muhammad-shanif/Downloads/border.jpeg"
MIN_AREA = 3000

img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Image not found at {IMAGE_PATH}")

h, w = img.shape[:2]

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

def is_image_border(cnt):
    x, y, cw, ch = cv2.boundingRect(cnt)
    # Exclude outer frame and image border
    # Check if rectangle takes up more than 30% of image area
    area_ratio = (cw * ch) / (w * h)
    if area_ratio > 0.30:
        return True
    return False

def rect_from_contour(cnt):
    x, y, cw, ch = cv2.boundingRect(cnt)
    return [
        {"x": int(x),      "y": int(y)},
        {"x": int(x),      "y": int(y + ch)},
        {"x": int(x + cw), "y": int(y + ch)},
        {"x": int(x + cw), "y": int(y)},
        {"x": int(x),      "y": int(y)}
    ]

boundaries = []
processed_areas = []  # Track similar rectangles to avoid duplicates

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < MIN_AREA:
        continue

    if is_image_border(cnt):
        continue

    x, y, cw, ch = cv2.boundingRect(cnt)
    
    # Check for duplicate/overlapping rectangles
    is_duplicate = False
    for px, py, pw, ph in processed_areas:
        # If centers are very close and sizes similar, it's likely a duplicate
        center_diff = abs((x + cw/2) - (px + pw/2)) + abs((y + ch/2) - (py + ph/2))
        size_diff = abs(cw - pw) + abs(ch - ph)
        if center_diff < 10 and size_diff < 10:
            is_duplicate = True
            break
    
    if is_duplicate:
        continue
    
    processed_areas.append((x, y, cw, ch))
    boundary = rect_from_contour(cnt)
    boundaries.append(boundary)

with open("boundary_clean.json", "w") as f:
    json.dump({"boundaries": boundaries}, f, indent=2)

print(f"✅ boundary_clean.json created with {len(boundaries)} rectangles")
