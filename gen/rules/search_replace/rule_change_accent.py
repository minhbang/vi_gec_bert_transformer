from .rule import Rule


class RuleChangeAccent(Rule):
    """
    Thay đổi dấu hỏi <-> ngã ==> Lỗi sử dụng dấu hỏi ngã
    """

    @staticmethod
    def get_all_patterns():
        return [
            "ẻ/ẽ", "ể/ễ",
            "ỷ/ỹ",
            "ủ/ũ", "ử/ữ",
            "ỉ/ĩ",
            "ỏ/õ", "ổ/ỗ",
            "ả/ã", "ẩ/ẫ", "ẳ/ẵ",
        ]
