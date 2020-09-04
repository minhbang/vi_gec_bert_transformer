import argparse
from transformers import BertTokenizer


def main(args):
    tokenizer = BertTokenizer.from_pretrained(args.bert_model, cache_dir='./cache')
    tokenizer.save_vocabulary(args.data_dir)


def cli_main():
    parser = argparse.ArgumentParser(description="Extract vocab.txt file of pretrained BERT model")
    parser.add_argument("-m", "--model", type=str, dest="bert_model", required=True, help="BERT model name")
    parser.add_argument("-d", "--dir", type=str, dest="data_dir", required=True, help="Data Dir")
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    cli_main()
