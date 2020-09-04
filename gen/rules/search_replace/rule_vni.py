from .rule import Rule


class RuleVni(Rule):
    """
    Bỏ dấu tiếng Việt + thêm số tương ứng kiểu gõ VNI => Lỗi bỏ dấu bằng bộ gõ VNI
    """

    @staticmethod
    def get_all_patterns():
        return [
            # a
            'à/a2', 'á/a1', 'ạ/a5', 'ả/a3', 'ã/a4', 'â/a6', 'ầ/a62', 'ấ/a61', 'ậ/a65', 'ẩ/a63', 'ẫ/a64', 'ă/a8',
            'ằ/a82', 'ắ/a81', 'ặ/a85', 'ẳ/a83', 'ẵ/a84',
            # e
            'è/e2', 'é/e1', 'ẹ/e5', 'ẻ/e3', 'ẽ/e4', 'ê/e6', 'ề/e62', 'ế/e61', 'ệ/e65', 'ể/e63', 'ễ/e64',
            # i
            'ì/i2', 'í/i1', 'ị/i5', 'ỉ/i3', 'ĩ/i4',
            # o
            'ò/o2', 'ó/o1', 'ọ/o5', 'ỏ/o3', 'õ/o4', 'ô/o6', 'ồ/o62', 'ố/o61', 'ộ/o65', 'ổ/o63', 'ỗ/o64', 'ơ/o7',
            'ờ/o72', 'ớ/o71', 'ợ/o75', 'ở/o73', 'ỡ/o74',
            # u
            'ù/u2', 'ú/u1', 'ụ/u5', 'ủ/u3', 'ũ/u4', 'ư/u7', 'ừ/u72', 'ứ/u71', 'ự/u75', 'ử/u73', 'ữ/u74',
            # y
            'ỳ/y2', 'ý/y1', 'ỵ/y5', 'ỷ/y3', 'ỹ/y4',
            # d
            'đ/d9'
        ]

    def add_pair(self, p1: str, p2: str):
        c1 = self.preprocess_search_str(p1)
        c2 = self.preprocess_search_str(p2)
        self.search_replace.append((c1, c2))
        # xử lý trường hợp vd ầ/a62 thì tạo ra ầ/a26 luôn
        if len(c2) == 3:
            self.search_replace.append((c1, c2[0] + c2[2] + c2[1]))
