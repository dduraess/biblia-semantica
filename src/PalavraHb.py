from src.ConectorBD import *

class PalavraHb:
    def __init__(self, palavra):
        self.ocorrencia = palavra
        self.ocorrencias = self.set_ocorrencias()
        self.strongs = self.set_strongs()
        # TODO self.stemm/lemma = self.set_lemma()
        # TODO self.para_gg = set_lemma_gg(self.lemma)

    def set_ocorrencias(self):
        sql = """
            select 
                WordID, BookName, Chapter, Verse, WordIndex, Lemma, Morphology
            from 
                Words
            where 
                Form like '%{}%'
            """

        oshb = '/Users/davison/Software/almeida-semantica/db/OSHB.db'
        rs = ConectorBD(oshb).con.cursor().execute(sql.format(self.ocorrencia)).fetchall()
        return rs
    
    # TODO método para obter stemm/lemma e reduzir as ocorrências/restringir a semântica
    # (atentar que a raiz da palavra hebraica (como nas línguas semíticas) não funciona com prefixo/sufixo)
    # def set_lemma(self):

    # TODO método para obter stemm/lemma no grego, para encontrar refs no NT (ver se esse 
    # método é útil no contexto semântico do hebraico para o grego)
    # def set_lemma_gg(self):
    

    def set_strongs(self):
        # a 5a coluna da tabela Words do Open Scriptures (OSHB.db) é o código da palavra 
        # pelo James Strong, às vezes (2x), com alguma informação (talvez a morfologia) antes da '/' 
        strong_ocorrencias = [i[5].split('/', 1)[-1].split('/', 1)[-1] for i in self.ocorrencias]
        
        ls_rs = []
        strongs_db = '/Users/davison/Software/almeida-semantica/db/strongs.sqlite'
        sql_strongs = "SELECT number, description FROM strongs WHERE number like '{}'"
        # removendo as duplicatas para as definições dicionário strong
        for cd_strong in list(dict.fromkeys(strong_ocorrencias)):
            rs = ConectorBD(strongs_db).con.cursor().execute(sql_strongs.format(cd_strong)).fetchone()
            ls_rs.append(rs)
        
        return ls_rs
