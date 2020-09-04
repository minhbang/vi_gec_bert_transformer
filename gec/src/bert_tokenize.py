#! /usr/bin/env python3 -u
# -*- Coding: utf-8; -*-
#
# Copyright (c) 2019 National Institute of Information and Communications Technology.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
"""
Tokenize raw sentences with the BERT tokenizer.
"""

import sys
import argparse
from transformers import BertTokenizer


def main(args):
    tokenizer = BertTokenizer.from_pretrained(args.bert_model, cache_dir='./cache')
    for line in sys.stdin:
        tokens = tokenizer.tokenize(line.strip())
        print(" ".join(['[CLS]'] + tokens + ['[SEP]']))


def cli_main():
    parser = argparse.ArgumentParser(description="Tokenize raw sentences with the BERT tokenizer")
    parser.add_argument("-m", "--model", type=str, dest="bert_model", required=True, help="BERT model name")
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    cli_main()
