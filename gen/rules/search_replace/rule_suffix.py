from .rule import Rule


class RuleSuffix(Rule):
    """
    - Giọng Nam và Trung
        - Phụ âm cuối C/T: hờn mát => hờn mác
        - Phụ âm cuối N/NG: khốn cùng => khốn cùn
        - Phụ âm cuối I/Y: trình bày => trình bài
    """
    @staticmethod
    def get_all_patterns():
        return ["C/T", "N/NG", "I/Y"]

    def preprocess_search_str(self, c: str):
        return '%s ' % c

    def before_replace(self, word: str):
        return '%s ' % word

    def after_replace(self, word: str):
        return word.strip()
