from functions import loadMEMEs, createMEMEs, createRageComic

# CREATE ORIGINAL MEMES
memes_path = "../../datasets/memes/"
n_classes, original_memes, meme_classes = loadMEMEs(memes_path)
memes_path = "../../datasets/syn_memes/"
createMEMEs(memes_path, original_memes, meme_classes)

# CREATE RAGE COMICS
memes_path = "../../datasets/rage_memes/"
_, original_memes, meme_classes = loadMEMEs(memes_path)
memes_path = "../../datasets/syn_memes/"

nRageComics = 50000
createRageComic(memes_path, original_memes, meme_classes, nRageComics)

print "Detected " + str(n_classes) + " meme classes.\n"
