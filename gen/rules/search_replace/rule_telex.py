from .rule import Rule


class RuleTelex(Rule):
    """
    Bỏ dấu tiếng Việt + thêm ký tự tương ứng kiểu gõ TELEX => Lỗi bỏ dấu bằng bộ gõ TELEX
    """

    @staticmethod
    def get_all_patterns():
        return [
            # a
            'à/af', 'á/as', 'ạ/aj', 'ả/ar', 'ã/ax', 'â/aa', 'ầ/aaf', 'ấ/aas', 'ậ/aaj', 'ẩ/aar', 'ẫ/aax', 'ă/aw',
            'ằ/awf', 'ắ/aws', 'ặ/awj', 'ẳ/awr', 'ẵ/awx',
            # e
            'è/ef', 'é/es', 'ẹ/ej', 'ẻ/er', 'ẽ/ex', 'ê/ee', 'ề/ee', 'ế/ees', 'ệ/eej', 'ể/eer', 'ễ/eex',
            # i
            'ì/if', 'í/is', 'ị/ij', 'ỉ/ir', 'ĩ/ix',
            # o
            'ò/of', 'ó/os', 'ọ/oj', 'ỏ/or', 'õ/ox', 'ô/oo', 'ồ/oof', 'ố/oos', 'ộ/ooj', 'ổ/oor', 'ỗ/oox', 'ơ/ow',
            'ờ/owf', 'ớ/ows', 'ợ/owj', 'ở/owr', 'ỡ/owx',
            # u
            'ù/uf', 'ú/us', 'ụ/uj', 'ủ/ur', 'ũ/ux', 'ư/uw', 'ừ/uwf', 'ứ/uws', 'ự/uwj', 'ử/uwr', 'ữ/uwx',
            # y
            'ỳ/yf', 'ý/ys', 'ỵ/yj', 'ỷ/yr', 'ỹ/yx',
            # d
            'đ/dd'
        ]

    def add_pair(self, p1: str, p2: str):
        c1 = self.preprocess_search_str(p1)
        c2 = self.preprocess_search_str(p2)
        self.search_replace.append((c1, c2))
        # xử lý trường hợp vd ầ/aaf thì tạo ra ầ/afa luôn
        if len(c2) == 3 and c2[1] != c2[2]:
            self.search_replace.append((c1, c2[0] + c2[2] + c2[1]))
