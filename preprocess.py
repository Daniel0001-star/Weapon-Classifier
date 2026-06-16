import cv2 #open computer vision?????

IMG_SIZE = 64

def preprocess_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) #This loads the images and converts to black andn white
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) # We need to resize the images
    img = img / 255.0 #This is to reducet the brightness to 
    return img.flatten()