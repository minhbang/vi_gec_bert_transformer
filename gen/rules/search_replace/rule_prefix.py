from .rule import Rule


class RulePrefix(Rule):
    """
    - Giọng Bắc
        - Bắt đầu với CH/TR: trăn trối => chăn chối
        - Bắt đầu với S/X: năng suất => năng xuất
        - Bắt đầu với D/GI:	dang dở => giang giở
    - Giọng Nam và Trung
        - Bắt đầu với D/GI/V: vang danh => dang danh
        - Bắt đầu với U/H/QU: uy quyền => quy quyền
    """
    @staticmethod
    def get_all_patterns():
        return ["CH/TR", "S/X", "D/GI", "D/GI/V", "U/H/QU"]

    def preprocess_search_str(self, c: str):
        return ' %s' % c

    def before_replace(self, word: str):
        return ' %s' % word

    def after_replace(self, word: str):
        return word.strip()
