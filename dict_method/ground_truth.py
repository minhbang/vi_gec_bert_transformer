import re


class GroundTruth:
    def __init__(self, punctuation_marks: str):
        self.punctuation_marks_re = rf"([{re.escape(punctuation_marks)}])"

    def split_sent_by_whitespace(self, sent: str):
        return re.sub(self.punctuation_marks_re, ' \\1 ', sent).lower().split()

    def get_wrong_position(self, inp: str, trg: str):
        """
        - Tách từ bằng khoảng trắng -> vị trí
        - Lấy các vị trí khác nhau giữa input và target => có lỗi ở đó
        :param inp: str
        :param trg: str
        :return: list vị trí lỗi
        """
        input_words = self.split_sent_by_whitespace(inp)
        target_words = self.split_sent_by_whitespace(trg)
        wrong_pos = []
        target_words_len = len(target_words)
        for i, w in enumerate(input_words):
            if i < target_words_len and w != target_words[i]:
                wrong_pos.append(i)
        return set(wrong_pos)
