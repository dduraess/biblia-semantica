from src.ConectorBD import *
from src.VersoGg import *

class PalavraGg: 
    def __init__(self, palavra):
        self.literal = palavra
        self.ocorrencias = self.set_ocorrencias()
        self.ocorrencias_lxx = self.set_ocorrencias_lxx()
        self.strong = self.set_strongs()
        self.lemma = self.set_lemma()

    def set_ocorrencias(self):
        sql = "SELECT nr_sq_livro, chapter, verse FROM bible WHERE content like '%{}%'".format(self.literal)
        sbl = '/Users/davison/Software/almeida-semantica/db/sbl.db'
        
        # cursor = ConectorBD(sbl).con.cursor()
        rs = ConectorBD(sbl).con.cursor().execute(sql).fetchall()

        # atributo de verso contendo lista de XML cujos filhos são atributos
        # TODO alterar para retornar apenas as referências (atentar pelo nr da palavra)
        # e não o conteúdo do versículo
        lst_ocorrencias = [VersoGg(id_livro, nr_cap, nr_vs).vs for id_livro, nr_cap, nr_vs in rs]
        return lst_ocorrencias
    
    def set_ocorrencias_lxx(self):
        sql = """
            select 
                -- id, 
                src_name, 
                book_name, 
                chapter_nr, 
                verse_nr
                , word_nr
                , word
                , word_root --lemma
                , morphology
            from 
                content
            where 
                word_root like '%{}%'
            """
        lxx = '/Users/davison/Software/almeida-semantica/db/lxx.db'

        rs = ConectorBD(lxx).con.cursor().execute(sql.format(self.literal)).fetchall()
        return rs
    
    def set_strongs(self):
        # abaixo é como feito no hebraico
        # TODO
        # ls_rs = list()
        # # removendo as duplicatas para as definições dicionário strong
        # for cd_strong in list(dict.fromkeys(strong_ocorrencias)):
        #     strongs = '/Users/davison/Software/almeida-semantica/db/strongs.sqlite'
        #     sql = "SELECT number, description FROM strongs WHERE number like '{}'".format(cd_strong)
        #     cursor = ConectorBD(strongs).cursor()
        #     rs = cursor.execute(sql).fetchone()
        #     ls_rs.append(rs)
        pass
        
        # return ls_rs

    def set_lemma(self):
        pass
    