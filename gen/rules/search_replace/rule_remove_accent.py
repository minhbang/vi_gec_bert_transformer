from .rule import Rule


class RuleRemoveAccent(Rule):
    """Bỏ dấu tiếng Việt => Lỗi quên gõ dấu"""

    @staticmethod
    def get_all_patterns():
        return [
            'à|á|ạ|ả|ã|â|ầ|ấ|ậ|ẩ|ẫ|ă|ằ|ắ|ặ|ẳ|ẵ/a',
            'è|é|ẹ|ẻ|ẽ|ê|ề|ế|ệ|ể|ễ/e',
            'ì|í|ị|ỉ|ĩ/i',
            'ò|ó|ọ|ỏ|õ|ô|ồ|ố|ộ|ổ|ỗ|ơ|ờ|ớ|ợ|ở|ỡ/o',
            'ù|ú|ụ|ủ|ũ|ư|ừ|ứ|ự|ử|ữ/u',
            'ỳ|ý|ỵ|ỷ|ỹ/y',
            'đ/d'
        ]

    def add_pair(self, p1: str, p2: str):
        c1s = p1.split('|')
        c2 = self.preprocess_search_str(p2)
        for c1 in c1s:
            c1 = self.preprocess_search_str(c1)
            self.search_replace.append((c1, c2))