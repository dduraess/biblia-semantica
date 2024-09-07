from translate import Translator
from src.PalavraHb import *
from src.VersoHb import *
from src.PalavraGg import *
from src.VersoGg import *

class ServicoTraducao:
    def __init__(self, periodo):
        self.periodo = periodo
        self.texto_traduzido_pt = self.set_traducao_pt()

    def set_traducao_pt(self):
        if isinstance(self.periodo, PalavraHb):
            self.tradutor = Translator(from_lang='he', to_lang='pt')
            txt = self.tradutor.translate(self.periodo.ocorrencia)
            return txt
        elif isinstance(self.periodo, VersoHb):
            self.tradutor = Translator(from_lang='he', to_lang='pt')
            txt = self.tradutor.translate(self.periodo.texto)
            return txt
        elif isinstance(self.periodo, PalavraGg):
            self.tradutor = Translator(from_lang='el', to_lang='pt')
            txt = self.tradutor.translate(self.periodo.ocorrencia)
            return txt
        elif isinstance(self.periodo, VersoGg):
            self.tradutor = Translator(from_lang='el', to_lang='pt')
            txt = self.tradutor.translate(self.periodo.get_txt_vs())
            return txt

    def traduzir_expressao(self):
        # TODO 
        pass