from translate import Translator
from src.PalavraHb import *
from src.VersoHb import *
from src.PalavraGg import *
from src.VersoGg import *

class ServicoTraducao:
    def __init__(self, periodo):
        self.periodo = periodo
        self.texto_traduzido = self.set_traducao()

    def set_traducao(self):
        if isinstance(self.periodo, PalavraHb):
            self.tradutor = Translator(from_lang='he', to_lang='pt')
            return self.tradutor.translate(self.periodo.ocorrencia)
        elif isinstance(self.periodo, VersoHb):
            self.tradutor = Translator(from_lang='he', to_lang='pt')
            return self.tradutor.translate(self.periodo.texto)
        elif isinstance(self.periodo, PalavraGg):
            self.tradutor = Translator(from_lang='el', to_lang='pt')
            return self.tradutor.translate(self.periodo.ocorrencia)
        elif isinstance(self.periodo, VersoGg):
            self.tradutor = Translator(from_lang='el', to_lang='pt')
            return self.tradutor.translate(self.periodo.get_txt_vs())

    def traduzir_expressao(self):
        # TODO 
        pass