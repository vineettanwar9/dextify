from PIL import Image, ImageEnhance
import page
import words
from PIL import Image
import cv2
import numpy as np
import os
import shutil
image = cv2.cvtColor(cv2.imread("page.jpg"), cv2.COLOR_BGR2RGB)
crop = page.detection(image)
boxes = words.detection(crop)   
lines = words.sort_words(boxes)

i = 0

path = r"C:\Users\funky\OneDrive\Desktop\Personal\Project\segmented"

#removing a folder
shutil.rmtree(path, ignore_errors=True)

#adding a folder
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)

for line in lines:
    text = crop.copy()
    for (x1, y1, x2, y2) in line:
        # roi = text[y1:y2, x1:x2]
        save = Image.fromarray(text[y1:y2, x1:x2])
        save = cv2.cvtColor(np.asarray(save), cv2.COLOR_BGR2GRAY)
        #th, save = cv2.threshold(save, 128, 192, cv2.THRESH_OTSU)
        #kernel = np.ones((2,2),np.uint8)
        #save = cv2.erode(save,kernel,iterations = 1)
        #save = cv2.dilate(save,kernel,iterations = 1)
        # print(i)
        
        save = Image.fromarray(save)
        save.save("segmented/word" + str(i) + ".png")
        i += 1



