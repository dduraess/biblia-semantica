import sqlite3

class ConectorBD:
    def __init__(self, arq):
        self.con=self.getConexao(arq)

    def getConexao(self, arq):
        try:
            with sqlite3.connect(arq) as con:
                return con
        except sqlite3.Error as er:
            return er