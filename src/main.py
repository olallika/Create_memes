from functions import loadMEMEs, createMEMEs, createRageComic, resizeNEGATIVES

# # CREATE ORIGINAL MEMES
# memes_path = "../../datasets/memes/"
# n_classes, original_memes, meme_classes = loadMEMEs(memes_path)
# memes_path = "../../datasets/syn_memes/"
# createMEMEs(memes_path, original_memes, meme_classes)

# # CREATE RAGE COMICS
memes_path = "../../../datasets/rage_memes/"

# # RESIZE ALL IMAGES TO 250x250 AND 250x500
# original_image_path = memes_path + 'large_memes/'
# new_image_path = memes_path + 'large_memes_resized/'
# new_size = (500, 250)
# resizeNEGATIVES(original_image_path, new_size, new_image_path)
# original_image_path = memes_path + 'small_memes/'
# new_image_path = memes_path + 'small_memes_resized/'
# new_size = (250, 250)
# resizeNEGATIVES(original_image_path, new_size, new_image_path)

_, large_memes, large_meme_classes = loadMEMEs(memes_path + 'large_memes_resized/')
_, small_memes, small_meme_classes = loadMEMEs(memes_path + 'small_memes_resized/')

memes_path = "../../../datasets/syn_memes/"
nRageComics = 20
createRageComic(memes_path, large_memes, small_memes, nRageComics)

print "Detected " + str(large_meme_classes + small_meme_classes) + " meme classes.\n"
