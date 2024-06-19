import sqlite3

class palavra_gg: 
    def __init__(self, palavra):
        self.ocorrencia = palavra
        self.ocorrencias = self.set_ocorrencias()
        self.strongs = self.set_strongs()
        self.lemma = self.set_lemma()

    def set_ocorrencias(self):
        sql = """
            select 
                WordID, BookName, Chapter, Verse, WordIndex, Lemma, Morphology
            from 
                Words
            where 
                Form like '%{}%'
            """

        with sqlite3.connect('/Users/davison/Software/almeida-semantica/db/OSHB.db') as cnx:
            cursor = cnx.cursor()
            rs = cursor.execute(sql.format(self.ocorrencia)).fetchall()
        return rs
    
    def set_ocorrencias_lxx(self):
        sql = """
            select 
                WordID, BookName, Chapter, Verse, WordIndex, Lemma, Morphology
            from 
                Words
            where 
                Form like '%{}%'
            """

        with sqlite3.connect('/Users/davison/Software/almeida-semantica/db/OSHB.db') as cnx:
            cursor = cnx.cursor()
            rs = cursor.execute(sql.format(self.ocorrencia)).fetchall()
        return rs
    
    def set_lemma(self):
        pass
    