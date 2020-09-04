import glob
import os


DICT = './corpus/dict.txt'
if os.path.exists(DICT):
    print('Files dict.txt is exists...')
else:
    fileDICT = open(DICT, "w")

    for file in glob.glob("./corpus/vi-wordnet/*.csv"):
        fileTEMP = open(file, "r")
        words = fileTEMP.read().replace(', ', '\n')
        fileTEMP.close()
        fileDICT.write(words)

    fileDICT.close()
    print('Done')
