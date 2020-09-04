"""
- Đọc file gec.txt, tách thành 2 file gec.target.txt và gec.input.txt
- Tách gec.target.txt và gec.input.txt thành tập train và tập test
- Trích một phần từ tập train thành tập validation
"""
import os


def preprocess_sentence(s):
    return s
    # return s.lower()


CORPUS_DIR = 'corpus'


def get_set_filename(set_name, input_target):
    return os.path.join(CORPUS_DIR, '%s.%s.txt' % (set_name, input_target))


GEC = os.path.join(CORPUS_DIR, 'gec.txt')
INP = os.path.join(CORPUS_DIR, 'gec.input.txt')
TRG = os.path.join(CORPUS_DIR, 'gec.target.txt')

TRAIN_PERCENT = 0.7
VAL_PERCENT = 0.2

if os.path.exists(INP):
    print('Files gec.input.txt, gec.target.txt is exists...')
else:
    print('Start split gec.txt file...')
    fileGEC = open(GEC, "r")
    sents = fileGEC.readlines()
    fileGEC.close()

    fileINP = open(INP, "w")
    fileTRG = open(TRG, "w")
    correct_sent = ''
    for line in sents:
        sent = preprocess_sentence(line[1:])
        if line[0] == "*":
            correct_sent = sent
        else:
            fileINP.write(sent)
            fileTRG.write(correct_sent)

    fileINP.close()
    fileTRG.close()


def split_dataset(source_name, set1_percent, set1_name, set2_name):
    if os.path.exists(get_set_filename(set1_name, 'input')):
        print('%s, %s set is exists...' % (set1_name.capitalize(), set2_name.capitalize()))
    else:
        print('Start split %s, %s set from %s...' % (set1_name, set2_name, source_name))

        file_input = open(get_set_filename(source_name, 'input'), "r")
        file_target = open(get_set_filename(source_name, 'target'), "r")
        inputs = file_input.readlines()
        targets = file_target.readlines()
        file_input.close()
        file_target.close()

        total_len = len(inputs)
        set1_len = int(set1_percent * total_len)
        set2_len = total_len - set1_len

        set1_input = open(get_set_filename(set1_name, 'input'), "w")
        set1_target = open(get_set_filename(set1_name, 'target'), "w")
        set2_input = open(get_set_filename(set2_name, 'input'), "w")
        set2_target = open(get_set_filename(set2_name, 'target'), "w")

        set1_input.writelines(inputs[:set1_len])  # train_len first sents
        set1_target.writelines(targets[:set1_len])
        set2_input.writelines(inputs[-set2_len:])  # set2_len last sents
        set2_target.writelines(targets[-set2_len:])

        set1_input.close()
        set1_target.close()
        set2_input.close()
        set2_target.close()

        print('Done:')
        print('- total: %d sents' % total_len)
        print('- %s: %d sents' % (set1_name, set1_len))
        print('- %s: %d sents' % (set2_name, set2_len))


split_dataset('gec', TRAIN_PERCENT, 'train', 'test')
split_dataset('train', VAL_PERCENT, 'val', 'train')

print('Done')
