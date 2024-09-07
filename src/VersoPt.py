import sqlite3
from src.livro import livro

class VersoPt:
    def __init__(self, id_livro, nr_cap, nr_vs):
        if isinstance(id_livro, int):
            self.livro=id_livro
        else:
            self.livro = livro[id_livro].value
        self.cap = nr_cap
        self.nr_vs = nr_vs
        self.vs = self.set_vs()

    def set_vs(self):
        pass
        # TODO
        # sql = 'SELECT text FROM verse WHERE book_id = {} AND chapter = {} AND verse = {}'.format(self.livro, self.cap, self.nr_vs)

        # try:
        #     with sqlite3.connect('/Users/davison/Software/almeida-semantica/db/ARA.sqlite') as cnx:
        #         cursor = cnx.cursor()
        #         rs = cursor.execute(sql).fetchone()
        # except sqlite3.Error as er:
        #     print(er)

        # return rs[0]
    
