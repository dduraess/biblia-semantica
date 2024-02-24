from cltk.stem.lemma import LemmaReplacer
from cltk.corpus.utils.formatter import cltk_normalize
from cltk.tokenize.word import WordTokenizer

lemmatizer = LemmaReplacer('greek')
word_tokenizer = WordTokenizer('greek')

def extract_stem(text):
    normalized_text = cltk_normalize(text, rm_punct=True, rm_numbers=True)
    tokens = word_tokenizer.tokenize(normalized_text.lower())
    stems = [lemmatizer.lemmatize(token)[0] for token in tokens]
    return stems
