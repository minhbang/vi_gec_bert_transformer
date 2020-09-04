from transformers import BertTokenizer
from src import TransformerWithBertModel
import os


path = os.getcwd()

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = TransformerWithBertModel.from_pretrained(
    "%s/model_stage2" % path,
    checkpoint_file='checkpoint_best.pt',
    data_name_or_path="%s/data" % path,
    bert_model="bert-base-multilingual-cased",
)
model.eval()  # disable dropout

while True:
    print('Nhập câu sai chính tả (q để thoát):')
    line = input()
    if 'q' == line.rstrip():
        break

    tokens = " ".join(['[CLS]'] + tokenizer.tokenize(line.strip()) + ['[SEP]'])
    # print("Tokenized: %s" % tokens)

    result = model.translate(tokens)
    # print("Output: %s" % result)

    detokenized = ''.join(result).replace(' ', '').replace('▁', ' ')
    # print("Detokenized: %s" % detokenized)

    print(detokenized[1:])
    print('---------------------------------------------------------')
