import cv2

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img, strength=15):
    return cv2.GaussianBlur(img, (strength, strength), 0)

def resize(img, ratio=0.5):
    new_width = int(img.shape[1] * ratio)
    new_height = int(img.shape[0] * ratio)
    return cv2.resize(img, (new_width, new_height))