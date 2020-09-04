import re

from underthesea import pos_tag


class SearchReplace(object):
    def __init__(self, rule_classes: list) -> None:
        self.rules = []
        self.words = []
        self.sentences = []
        self.limit = 0
        self.words_count = 0
        self.word_changed_count = 0
        for rule_class in rule_classes:
            self.add_rule(rule_class)
        super().__init__()

    def add_rule(self, rule_class):
        rules = rule_class().get_all_patterns()
        for rule in rules:
            self.rules.append(rule_class(rule))

    @staticmethod
    def postprocess_sentence(sent: str):
        """Xóa các khoảng trắng trước các dấu"""
        return re.sub(r"\s+([.,!?\"'()\[\]])", r"\1", sent)

    @staticmethod
    def allwed(word: str):
        """Từ cho phép search/replace không?"""
        # return not (word.startswith('N') or word.startswith('CH'))
        return not word.startswith('CH')

    def export(self):
        new_sentence = self.postprocess_sentence(' '.join(list(list(zip(*self.words))[0])))
        self.sentences.append(new_sentence)

    def apply_word(self, word: str) -> list:
        new_words = []
        if self.allwed(word):
            for rule in self.rules:
                new_words = list(set(new_words + rule.apply(word)))
        return new_words

    def apply_at(self, i: int):
        """Thực hiện ở vị trí i """
        if i < self.words_count and self.word_changed_count < self.limit:
            word = self.words[i][0]
            new_words = self.apply_word(word)
            for new_word in new_words:
                self.words[i] = (new_word, self.words[i][1])
                self.word_changed_count += 1
                if i == (self.words_count - 1) or self.word_changed_count == self.limit:
                    self.export()
                else:
                    self.apply_at(i + 1)
                self.words[i] = (word, self.words[i][1])
                self.word_changed_count -= 1
            self.apply_at(i + 1)

    def apply(self, sentence: str, limit: int = 1) -> list:
        """ Áp dụng mẫu tìm/thay thế cho một câu
        Parameters
        ----------
        limit: int
            Giới hạn số lỗi tối đa trong một câu
        sentence: str
           Câu đầu vào
        Returns
        -------
        str
            Câu đã áp dụng mẫu tìm/thay thế
        """
        # Gán nhãn từ loại
        self.words = pos_tag(sentence)
        self.words_count = len(self.words)
        self.sentences = []
        self.limit = limit
        self.word_changed_count = 0
        self.apply_at(0)
        return self.sentences
