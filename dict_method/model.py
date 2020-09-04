from nltk.corpus.reader import WordListCorpusReader
from underthesea import word_tokenize
import re


class DictionaryBasedSpellingDetection:
    def __init__(self, punctuation_marks: str, corpus_dir: str, corpus_files: list):
        reader = WordListCorpusReader(corpus_dir, corpus_files)
        self.vi_dict = set(reader.words())
        # Thêm các dấu vào từ điển, xem như nó đúng chỉnh tả
        self.vi_dict.update(list(punctuation_marks))
        # Thêm một số từ đặc biệt
        self.vi_dict.update(['m', 'g', 'gt', 'kg', 'km', 'mm', 'cm', 'c', 'f', 't'])
        self.re_d = re.compile(r'\d')

    @staticmethod
    def preprocess_sent(sent: str):
        return word_tokenize(sent.strip().lower())

    def not_has_digits(self, s: str):
        return self.re_d.search(s) is None

    def is_wrong(self, w: str):
        return self.not_has_digits(w) and (w not in self.vi_dict)

    def predict(self, inp: str):
        """
        Dự đoán các vị trí sai, nếu 1 từ không có trong từ điển -> đánh dấu tất cả các chử của từ đó khả năng là sai

        :param inp: str
        :return: list các list vị trí sai của từ
        """
        words = self.preprocess_sent(inp)
        pos = 0
        wrong_words = []
        for word in words:
            new_pos = pos + len(word.split())
            if self.is_wrong(word):
                wrong_words.append(set(range(pos, new_pos)))
            pos = new_pos

        return wrong_words
