from nltk.tokenize.punkt import PunktSentenceTokenizer
# , PunktParameters
import pickle
import string
import os


class SentTokenizer(object):
    def __init__(self):
        self.spliter = self.get_spliter()
        super().__init__()

    def get_spliter(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/sent_tokenize_model_v1.0.pkl', 'rb') as fs:
            punkt_param = pickle.load(fs)

        punkt_param.sent_starters = {}
        abbrev_types = ['g.m.t', 'e.g', 'dr', 'dr', 'vs', "000", 'mr', 'mrs', 'prof', 'inc', 'tp', 'ts', 'ths',
                        'th', 'vs', 'tp', 'k.l', 'a.w.a.k.e', 't', 'a.i', '</i', 'g.w',
                        'ass',
                        'u.n.c.l.e', 't.e.s.t', 'ths', 'd.c', 've…', 'ts', 'f.t', 'b.b', 'z.e', 's.g', 'm.p',
                        'g.u.y',
                        'l.c', 'g.i', 'j.f', 'r.r', 'v.i', 'm.h', 'a.s', 'bs', 'c.k', 'aug', 't.d.q', 'b…', 'ph',
                        'j.k', 'e.l', 'o.t', 's.a']
        abbrev_types.extend(string.ascii_uppercase)
        for abbrev_type in abbrev_types:
            punkt_param.abbrev_types.add(abbrev_type)
        for abbrev_type in string.ascii_lowercase:
            punkt_param.abbrev_types.add(abbrev_type)
        return PunktSentenceTokenizer(punkt_param)

    def split(self, str_input: string):
        sentences = str_input.replace("\n", " ")
        return self.spliter.sentences_from_text(sentences)
