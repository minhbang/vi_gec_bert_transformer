import os
from datetime import datetime

from config import DATA_DIR
from rules import search_replace


inputFilename = os.path.join(DATA_DIR, 'sents.txt')
outpuFilename = os.path.join(DATA_DIR, 'data_' + datetime.now().strftime('%H-%M-%S_%d-%m-%y') + '.txt')

if os.path.exists(inputFilename):
    inputFile = open(inputFilename, "r")
    outputFile = open(outpuFilename, "a")
    sents = inputFile.readlines()
    sents_count = len(sents)
    result_count = 0
    print("Tạo câu sai chính tả từ câu đúng:")
    print('--------------------------------------')
    print("File dữ liệu: ", inputFilename)
    print("Số câu đúng: ", sents_count)
    print('--------------------------------------')
    print('Đang thực hiện...')
    for i, sent in enumerate(sents, start=1):
        sentences = search_replace.apply(sent.strip())
        result_count += len(sentences)
        outputFile.write('*' + sent)
        outputFile.writelines(map(lambda s: '+' + s + '\n', sentences))
        print("Thực hiện xong %d câu, %.2f%%" % (i, i * 100 / sents_count))

    inputFile.close()
    outputFile.close()
    print('KẾT QUẢ')
    print('Số câu sai chính tả tạo được: ', result_count)
    print("File dữ liệu kết quả: ", outpuFilename)
    print('--------------------------------------')
else:
    print('Error: input file "data/sents.txt" not found!')
