class Rule(object):
    """ Rule Base class
    Một luật Tìm/Thay thế, ví dụ D/GI/V thay thế lẫn nhau
    """

    @staticmethod
    def get_all_patterns():
        return []

    def __init__(self, pattern: str = None) -> None:
        self.search_replace = []
        if pattern is not None:
            ps = pattern.split('/')
            if len(ps) > 1:
                self.add_pair(ps[0], ps[1])
                if len(ps) > 2:
                    # Chỉ xử lý đến trường hợp A/B/C
                    self.add_pair(ps[1], ps[2])
                    self.add_pair(ps[0], ps[2])
            else:
                raise Exception('Error: Pattern like "A/B"')

    def add_pair(self, p1: str, p2: str):
        c1 = self.preprocess_search_str(p1)
        c2 = self.preprocess_search_str(p2)
        self.search_replace.append((c1, c2))
        self.search_replace.append((c2, c1))

    def preprocess_search_str(self, c: str):
        return c

    def before_replace(self, word: str):
        return word

    def after_replace(self, word: str):
        return word

    def replace(self, old: str, new: str, word: str):
        """ Tìm/Thay thế old bằng new trong từ word,
        tự động phát hiện lower, upper hay capitalize để biến đổi phù hợp trước khi thay vào

        Parameters
        ----------
        old
        new
        word

        Returns
        -------
        str
        """
        sr = [
            (old.upper(), new.upper()),
            (old.capitalize(), new.capitalize()),
            (old.lower(), new.lower())
        ]
        new_word = word = self.before_replace(word)
        for s, r in sr:
            new_word = word.replace(s, r)
            if new_word != word:
                break
        new_word = self.after_replace(new_word)

        return new_word

    def apply(self, word: str) -> list:
        """ Áp dụng rule này cho từ word duy nhất 1 lần random
        Parameters
        ----------
        word:str

        Returns
        -------
        list
            Danh sách từ đã bị thay đổi
        """
        result = []
        for sr in self.search_replace:
            new_word = self.replace(sr[0], sr[1], word)
            if new_word != word:
                result.append(new_word)
        return result
