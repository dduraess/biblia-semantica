from src.ConectorBD import *
from src.livro import livro

class VersoHb:
    def __init__(self, id_livro, nr_cap, nr_vs):
        if isinstance(id_livro, int):
            self.livro=id_livro
        else:
            self.livro = livro[id_livro].value
        self.nr_cap = nr_cap
        self.nr_vs = nr_vs
        self.texto = self.set_texto()
        # self.qtde_palavras = len(self.vs)

    def set_texto(self):
        sql ='SELECT Verse, Form FROM Words WHERE nr_sq_livro like "{}" and Chapter = {} and Verse = {}'.format(self.livro, self.nr_cap, self.nr_vs)
        oshb = '/Users/davison/Software/almeida-semantica/db/OSHB.db'
        rs = ConectorBD(oshb).con.cursor().execute(sql).fetchall()
        # nr_versiculo = rs[0][0]
        palavras_vs_hb = ''.join([p[1].replace('/', '') + ' ' for p in rs])
        return palavras_vs_hb