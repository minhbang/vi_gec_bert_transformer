import re


punctuation_marks = '.,?"\'()[]{}!:&;-+%/*#'
punctuation_marks_re = rf"([{re.escape(punctuation_marks)}])"


def split_sent_by_whitespace(sent: str):
    return re.sub(punctuation_marks_re, ' \\1 ', sent).lower().split()


def get_diff_position(i_words: list, t_words: list):
    """
    - Tách từ bằng khoảng trắng -> vị trí
    - Lấy các vị trí khác nhau giữa input và target
    """
    diff_pos = []
    t_words_len = len(t_words)
    for ix, w in enumerate(i_words):
        if ix < t_words_len and w != t_words[ix]:
            diff_pos.append(ix)
    return set(diff_pos)


# Evaluation
# ----------------------------------------------------------------------------------------------------------------------
def evaluate(inp: str, trg: str, prd: str):
    input_words = split_sent_by_whitespace(inp)
    target_words = split_sent_by_whitespace(trg)
    predict_words = split_sent_by_whitespace(prd)

    ref = get_diff_position(input_words, target_words)
    predict = get_diff_position(input_words, predict_words)
    predict_diff_target = get_diff_position(predict_words, target_words)

    detection_correct = ref.intersection(predict)
    detection_wrong = predict - ref
    detection_missing = ref - predict

    # Sửa lỗi chính xác
    correction_correct = ref - predict_diff_target
    # Sửa lỗi sai
    correction_wrong = ref.intersection(predict_diff_target)
    # Đúng mà sửa thành sai
    correction_correct2wrong = predict_diff_target - ref

    return (
        len(input_words),
        ref,  # List errors
        detection_correct,
        detection_wrong,
        detection_missing,
        correction_correct,
        correction_wrong,
        correction_correct2wrong
    )


INP = './output/evaluation1.input.txt'
TRG = './output/evaluation1.target.txt'
PRD = './output/evaluation1.predict.txt'

OUT1 = './output/evaluation1.analysis.txt'
OUT2 = './output/evaluation1.statistics.txt'

fileINP = open(INP, "r")
fileTRG = open(TRG, "r")
filePRD = open(PRD, "r")
inps = fileINP.readlines()
trgs = fileTRG.readlines()
prds = filePRD.readlines()
fileINP.close()
fileTRG.close()
filePRD.close()

fileOUT1 = open(OUT1, "w")
fileOUT2 = open(OUT2, "w")

count_errors = 0
count_detection_correct = 0
count_detection_wrong = 0
count_detection_missing = 0
count_correction_correct = 0
count_correction_wrong = 0
count_correction_correct2wrong = 0
max_sent_len = 0

statistics_errors = [0] * 200
statistics_detection_correct = [0] * 200
statistics_detection_wrong = [0] * 200
statistics_detection_missing = [0] * 200
statistics_correction_correct = [0] * 200
statistics_correction_wrong = [0] * 200
statistics_correction_correct2wrong = [0] * 200


def update_statistics(statistics: list, pos: set):
    for p in pos:
        statistics[p] += 1


def join_list(sep: str, l):
    return sep.join([str(i) for i in l])


fileOUT1.write('sent_index len | errors | detection_correct | detection_wrong | detection_missing | '
               'correction_correct | correction_wrong | correction_correct2wrong\n')
for i, sents in enumerate(zip(inps, trgs, prds)):
    print('evaluate sentence %d' % i)
    result = evaluate(*sents)
    max_sent_len = max(max_sent_len, result[0])

    count_errors += len(result[1])
    count_detection_correct += len(result[2])
    count_detection_wrong += len(result[3])
    count_detection_missing += len(result[4])
    count_correction_correct += len(result[5])
    count_correction_wrong += len(result[6])
    count_correction_correct2wrong += len(result[7])

    fileOUT1.write(str(i) + '\t' + str(result[0]) + '\t|\t' + '\t|\t'.join(
        list(map(lambda s: (','.join(str(x) for x in s)), result[1:]))) + '\n')

    update_statistics(statistics_errors, result[1])
    update_statistics(statistics_detection_correct, result[2])
    update_statistics(statistics_detection_wrong, result[3])
    update_statistics(statistics_detection_missing, result[4])
    update_statistics(statistics_correction_correct, result[5])
    update_statistics(statistics_correction_wrong, result[6])
    update_statistics(statistics_correction_correct2wrong, result[7])

fileOUT1.write('Sentences: %d\n' % len(inps))
fileOUT1.write('Total:\n')
fileOUT1.write(
    'errors %d\n'
    'detection_correct %d\n'
    'detection_wrong %d\n'
    'detection_missing %d\n'
    'correction_correct %d\n'
    'correction_wrong %d\n'
    'correction_correct2wrong %d\n' % (count_errors,
                                       count_detection_correct,
                                       count_detection_wrong,
                                       count_detection_missing,
                                       count_correction_correct,
                                       count_correction_wrong,
                                       count_correction_correct2wrong))

fileOUT2.write('Errors,' + join_list(',', statistics_errors[:max_sent_len]) + '\n')
fileOUT2.write('Detection correct,' + join_list(',', statistics_detection_correct[:max_sent_len]) + '\n')
fileOUT2.write('Detection missing,' + join_list(',', statistics_detection_missing[:max_sent_len]) + '\n')
fileOUT2.write('Detection wrong,' + join_list(',', statistics_detection_wrong[:max_sent_len]) + '\n')
fileOUT2.write('Correction correct,' + join_list(',', statistics_correction_correct[:max_sent_len]) + '\n')
fileOUT2.write('Correction wrong,' + join_list(',', statistics_correction_wrong[:max_sent_len]) + '\n')
# fileOUT2.write('Errors' + join_list(',', statistics_correction_correct2wrong[:max_sent_len]) + '\n')

fileOUT1.close()
fileOUT2.close()
print('Done')
