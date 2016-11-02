import PIL
import cv2
import os
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv


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


def resizeNEGATIVES(negative_images, new_size, save_folder):
    neg_files = os.listdir(negative_images)

    if not os.path.exists(save_folder + '/'):
        os.mkdir(save_folder + '/')

    cont = 0
    for neg_file in neg_files:
        print 'Resized: ' + str(cont) + '/' + str(len(neg_files))
        if neg_file.endswith(".jpg"):
            try:
                img = Image.open(negative_images + '/' + neg_file)
                img = img.resize(new_size, PIL.Image.ANTIALIAS)
                img.save(save_folder + '/' + neg_file)

            except IOError:
                print neg_file

        cont += 1


def createRageComic(path, large_memes, small_memes, nRageComics):
    for i in range(0, nRageComics, 1):
        nRows = 3
        row = []
        border_color = [0, 0, 0]
        border_size = 1

        for ii in range(0, nRows, 1):
            row_type = random.random()

            if row_type >= 0.2:
                # two small rage memes
                meme_1 = random.choice(small_memes)
                meme_1 = cv2.copyMakeBorder(meme_1, border_size, border_size, border_size, border_size,
                                            cv2.BORDER_CONSTANT, value=border_color)

                meme_2 = random.choice(small_memes)
                meme_2 = cv2.copyMakeBorder(meme_2, border_size, border_size, border_size, border_size,
                                            cv2.BORDER_CONSTANT, value=border_color)

                row.append(np.hstack([meme_1, meme_2]))

            elif row_type < 0.2:
                # one large rage meme
                meme = random.choice(large_memes)
                meme = cv2.copyMakeBorder(meme, border_size, border_size, border_size*2, border_size*2,
                                          cv2.BORDER_CONSTANT, value=border_color)

                row.append(np.hstack([meme]))

        comic = np.vstack([row[0], row[1], row[2]])
        comic = comic[3:752, 5:499]

        if not os.path.exists(path + 'rage_comics/'):
            os.mkdir(path + 'rage_comics/')
        cv2.imwrite(path + 'rage_comics/' + str(i) + '.jpg', comic)

        print "Created " + str(i) + '/' + str(nRageComics)

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
    y = int(h - h * 0.85)
    x = int((w - textSize[0][0]) / 2)

    # Put text on the top
    # Put text on the bottom
    # Put text on top and bottom
    cv2.putText(original_meme, text, (x, y), fontFace, fontScale, (255, 255, 255), thickness)

    return original_meme
