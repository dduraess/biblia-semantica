import xml.etree.ElementTree as ET
import sqlite3
from src.livro import livro

class Vers_gg:
    def __init__(self, nm_livro, nr_cap, nr_vs):
        self.livro = livro[nm_livro].value
        self.cap = nr_cap
        self.nr_vs = nr_vs
        self.vs = self.set_vs()
        self.qtde_palavras = len(self.vs)

    def set_vs(self):

        sql = 'SELECT content FROM bible WHERE nr_sq_livro = {} AND chapter = {} AND verse = {}'.format(self.livro, self.cap, self.nr_vs)

        try:
            with sqlite3.connect('/Users/davison/Software/almeida-semantica/db/sbl.db') as cnx:
                cursor = cnx.cursor()
                rs = cursor.execute(sql).fetchone()[0]
        except sqlite3.Error as er:
            print(er)

        return rs
    
    def get_txt_vs(self):

        # como faz lista enumerada com if else 
        # return str(vs) + " " + "".join([child.text + " " if i!=len(verso) else child.text + child.tail for i, child in enumerate(verso)])
        return str(self.nr_vs) + " " + "".join([child.text + child.tail for child in ET.fromstring(self.vs)]).strip()
    
