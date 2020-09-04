# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import re
from datetime import datetime

from scrapy.utils.markup import remove_tags

from tuoitre_vn.lib.sent_tokenize import SentTokenizer
from . import DATA_DIR, MIN_LEN, MAX_LEN


class RemoveHtmlPipeline(object):

    def open_spider(self, spider):
        print('Download from https://tuoitre.vn/van-hoa')
        print('Parameters:')
        print('-a start_date= Start date, default = now')
        print('-a days= Number of days backward, default = 1')
        print('Downloading...')
        print(
            '--------------------------------------------------------------------------------------------------------')

    def process_item(self, item, spider):
        item['content'] = re.sub(r'<p>\s*<b>[^<]+</b>\s*</p>', '', item['content'])
        item['content'] = remove_tags(item['content'])
        return item


class CleanPipeline(object):
    """
        https://github.com/nusnlp/crosentgec/blob/master/scripts/clean_data.py
        """

    @staticmethod
    def clean_sentence(line):
        # replace - unicode - punctuation
        line = re.sub(r'\\"', r'"', line)
        line = re.sub(r'\\t', ' ', line)
        line = re.sub(r'，', r',', line)
        line = re.sub(r'。 *', r'. ', line)
        line = re.sub(r'、', r',', line)
        line = re.sub(r'”', r'"', line)
        line = re.sub(r'“', r'"', line)
        line = re.sub(r'∶', r':', line)
        line = re.sub(r'：', r':', line)
        line = re.sub(r'？', r'?', line)
        line = re.sub(r'《', r'"', line)
        line = re.sub(r'》', r'"', line)
        line = re.sub(r'）', r')', line)
        line = re.sub(r'！', r'!', line)
        line = re.sub(r'（', r'(', line)
        line = re.sub(r'；', r';', line)
        line = re.sub(r'１', r'"', line)
        line = re.sub(r'」', r'"', line)
        line = re.sub(r'「', r'"', line)
        line = re.sub(r'０', r'0', line)
        line = re.sub(r'３', r'3', line)
        line = re.sub(r'２', r'2', line)
        line = re.sub(r'５', r'5', line)
        line = re.sub(r'６', r'6', line)
        line = re.sub(r'９', r'9', line)
        line = re.sub(r'７', r'7', line)
        line = re.sub(r'８', r'8', line)
        line = re.sub(r'４', r'4', line)
        line = re.sub(r'． *', r'. ', line)
        line = re.sub(r'～', r'~', line)
        line = re.sub(r'’', '\'', line)
        line = re.sub(r'…', r'...', line)
        line = re.sub(r'━', r'-', line)
        line = re.sub(r'〈', r'<', line)
        line = re.sub(r'〉', r'>', line)
        line = re.sub(r'【', r'[', line)
        line = re.sub(r'】', r']', line)
        line = re.sub(r'％', r'%', line)

        # remove - non - printing - char
        line = re.sub(r'[\x00-\x09\x0B-\x1F\x7F-\x9F\xAD]', r' ', line)
        line = re.sub(r'[\u0600-\u0605\u2060-\u206f\u202a-\u202e\u200b-\u200f]', r' ', line)
        line = re.sub(r'[\ufeff\ufff9\ufffa\ufffb]', r' ', line)
        line = re.sub(r'[\ue000-\uf8ff]', r' ', line)

        # normalize - punctuation
        line = re.sub(r'\r', r'', line)
        line = re.sub(r'\(', r' (', line)
        line = re.sub(r'\)', r') ', line)
        line = re.sub(r' +', r' ', line)
        line = re.sub(r'\) ([\.\!\:\?\;\,])', r')\1', line)
        line = re.sub(r'\( ', r'(', line)
        line = re.sub(r' \)', r')', line)
        line = re.sub(r'(\d) \%', r'\1%', line)
        line = re.sub(r' :', r':', line)
        line = re.sub(r' ;', r';', line)
        line = re.sub(r'\`', '\'', line)
        line = re.sub(r'\'\'', r' " ', line)
        line = re.sub(r'„', r'"', line)
        line = re.sub(r'“', r'"', line)
        line = re.sub(r'”', r'"', line)
        line = re.sub(r'–', r'-', line)
        line = re.sub(r'—', r' - ', line)
        line = re.sub(r' +', r' ', line)
        line = re.sub(r'´', '\'', line)
        line = re.sub(r'([a-zA-Z])‘([a-zA-Z])', '\\1\'\\2', line)
        line = re.sub(r'([a-zA-Z])’([a-zA-Z])', '\\1\'\\2', line)
        line = re.sub(r'‘', r'"', line)
        line = re.sub(r'‚', r'"', line)
        line = re.sub(r'’', r'"', line)
        line = re.sub(r'\'\'', r'"', line)
        line = re.sub(r'´´', r'"', line)
        line = re.sub(r'…', r'...', line)
        line = re.sub(r' « ', r' "', line)
        line = re.sub(r'« ', r'"', line)
        line = re.sub(r'«', r'"', line)
        line = re.sub(r' » ', r'" ', line)
        line = re.sub(r' »', r'"', line)
        line = re.sub(r'»', r'"', line)
        line = re.sub(r' \%', r'%', line)
        line = re.sub(r'nº ', r'nº ', line)
        line = re.sub(r' :', r':', line)
        line = re.sub(r' ºC', r' ºC', line)
        line = re.sub(r' cm', r' cm', line)
        line = re.sub(r' \?', r'?', line)
        line = re.sub(r' \!', r'!', line)
        line = re.sub(r' ;', r';', line)
        line = re.sub(r', ', r', ', line)
        line = re.sub(r' +', r' ', line)
        line = re.sub(r'\"([,\.]+)', r'\1"', line)
        return line

    def process_item(self, item, spider):
        item['content'] = self.clean_sentence(item['content'])
        return item


class SentencesSplitPipeline(object):
    def open_spider(self, spider):
        self.st = SentTokenizer()

    def process_item(self, item, spider):
        item['content'] = self.st.split(item['content'])
        return item


# pipeline bo cac cau kha nang khong dung chính tả
# Bỏ tât cả dấu " ở đầu và đuôi
# câu chỉ có 1 dấu " bỏ
# bỏ dấu câu
# Bỏ cân ngắn hơn 9 ký tự


class RemoveUnnecessaryCharacters(object):
    def process_item(self, item, spider):
        content = []
        for s in item['content']:
            if MIN_LEN <= len(s) <= MAX_LEN:
                content.append(s.strip('-_ ').replace('"', ''))
        item['content'] = content
        return item


class ToTxtFilePipeline(object):

    def __init__(self) -> None:
        super().__init__()
        self.file = None
        self.sentences_count = 0
        self.output_filepath = ''

    def open_spider(self, spider):
        path = DATA_DIR
        if not os.path.exists(path):
            os.makedirs(path)
        filename = 'tuoitre_vn_' + datetime.now().strftime('%H-%M-%S_%d-%m-%y') + '.txt'
        self.output_filepath = os.path.join(path, filename)
        self.file = open(self.output_filepath, 'w')
        self.sentences_count = 0

    def close_spider(self, spider):
        self.file.close()
        print(
            '--------------------------------------------------------------------------------------------------------')
        print('Has taken %d sentences' % self.sentences_count)
        print('Output File: %s' % self.output_filepath)
        print('Done...')

    def process_item(self, item, spider):
        self.sentences_count += len(item['content'])
        self.file.write("\n".join(item['content']))
        return item
