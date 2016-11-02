import cv2
import os
import random
import numpy as np


def loadMEMEs(path):
    meme_classes = os.listdir(path)
    original_memes = []

    for meme_class in meme_classes:
        meme = cv2.imread(path + meme_class)
        original_memes.append(meme)

    return len(original_memes), original_memes, meme_classes


def createMEMEs(path, original_memes, meme_classes):
    for i in range(0, len(original_memes), 1):
        # Create class folder
        class_dir = path + str(i) + '/'
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)

        # Read original MEME image
        original_meme = original_memes[i]

        # ADD TEXT
        # Font types: original_meme, rage_meme
        font_type = "original_meme"
        addText(original_meme, class_dir, font_type)

        # CREATE RAGE COMIC

        print "Created new MEMEs."

def createRageComic(path, original_memes, meme_classes, nRageComics):
    # RESIZE IMAGES TO 250 x 250 or 250 x 750


    for i in range(0, nRageComics, 1):
        nRows = 3
        row = []

        for ii in range (0, nRows, 1):
            image1_width = 0
            image2_width = 0

            while image1_width != 250 and image2_width != 250:
                row_img1 = random.choice(original_memes)
                image1_width = row_img1.shape[1]
                row_img2 = random.choice(original_memes)
                image2_width = row_img2.shape[1]

            # ADD TEXT
            # Font types: original_meme, rage_meme
            font_type = "rage_meme"
            row_img1 = addText(row_img1, font_type)
            row_img2 = addText(row_img2, font_type)

            row.append(np.hstack([row_img1, row_img2]))

        comic = np.vstack([row[0], row[1], row[2]])

    print "Created new MEMEs."


def addText(original_meme, font_type):
    if font_type == "original_meme":
        text = "RANDOM TEXT"
        fontFace = cv2.FONT_HERSHEY_TRIPLEX
        fontScale = 1.0
        thickness = 2

    elif font_type == "rage_meme":
        text = "RANDOM TEXT"
        fontFace = cv2.FONT_HERSHEY_TRIPLEX
        fontScale = 1.0
        thickness = 2

    textSize = cv2.getTextSize(text, fontFace, fontScale, thickness)

    # Original image size
    h = original_meme.shape[0]
    w = original_meme.shape[1]

    # Center the text
    # y = (h + textSize[0][1])/2
    y = int(h - h*0.85)
    x = int((w - textSize[0][0])/2)

    # Put text on the top
    # Put text on the bottom
    # Put text on top and bottom
    cv2.putText(original_meme, text, (x, y), fontFace, fontScale, (255, 255, 255), thickness)

    return original_meme
