from nltk.corpus.reader import WordListCorpusReader
from underthesea import word_tokenize
import re

from model import DictionaryBasedSpellingDetection
from ground_truth import GroundTruth


punctuation_marks = '.,?"\'()[]{}!:&;-+%/*#'

model = DictionaryBasedSpellingDetection(punctuation_marks, './corpus', ['dict.txt'])
ground_truth = GroundTruth(punctuation_marks)


# Evaluation
# ----------------------------------------------------------------------------------------------------------------------
def evaluate(inp: str, trg: str):
    """
    :param inp: str
    :param trg: str
    :return: (Số lỗi phát hiện đúng, Số lỗi phát hiện sai, Số lỗi bỏ sót)
    """
    ref = ground_truth.get_wrong_position(inp, trg)
    predict = model.predict(inp)
    total_ = len(ref)
    correct_ = 0
    wrong_ = 0
    for w in predict:
        # Có vị trí của w xuất hiện trong ref
        if len(w - ref) < len(w):
            correct_ += 1
            ref = ref - w
        else:
            wrong_ += 1
    missing_ = len(ref)
    return total_, correct_, wrong_, missing_


INP = './data/test.input.txt'
TRG = './data/test.target.txt'
OUT = './output/evaluate_log.txt'

fileINP = open(INP, "r")
fileTRG = open(TRG, "r")
inps = fileINP.readlines()
trgs = fileTRG.readlines()
fileINP.close()
fileTRG.close()

fileOUT = open(OUT, "w")
fileOUT.write('index (total, correct, wrong, missing)\n')
total, correct, wrong, missing = (0, 0, 0, 0)
for i, sents in enumerate(zip(inps, trgs)):
    print('evaluate sentence %d' % i)
    result = evaluate(*sents)
    fileOUT.write(str(i) + ' (%d, %d, %d, %d)\n' % result)
    total += result[0]
    correct += result[1]
    wrong += result[2]
    missing += result[3]
fileOUT.write('Sentences: %d\n' % len(inps))
fileOUT.write('Result:\n')
fileOUT.write('(%d, %d, %d, %d)' % (total, correct, wrong, missing))
fileOUT.close()
print('Done')
