#!/opt/homebrew/bin/python3

# [1] Fonte; [2] livro; [3] cap_ini; [4] cap_fim

import sqlite3
import sys
from pathlib import Path
from translate import Translator

home = str(Path.home())
hb_at = 'OSHB.db'

def retornar_texto_vs_hb(livro, cap, verso):
    sql ='SELECT Verse, Form FROM Words WHERE BookName like "{}" and Chapter = {} and Verse = {}'.format(livro, cap, verso)
    with sqlite3.connect(hb_at) as cnx:
        cursor = cnx.cursor()
        rs = cursor.execute(sql).fetchall()
        nr_versiculo = rs[0][0]
        palavras_vs_hb = ''.join([p[1].replace('/', '') + ' ' for p in rs])
    return (nr_versiculo, palavras_vs_hb)

def retornar_txt_cap_hb(livro, cap):
    sql = 'select max(Verse) from Words where BookName like "{}" and Chapter = {}'.format(livro, cap)
    with sqlite3.connect(hb_at) as cnx:
        cursor = cnx.cursor()
        rs = cursor.execute(sql).fetchone()
        txt_cap_hb = []
        for vs in range(1, rs[0]+1):
            txt_cap_hb.append(retornar_texto_vs_hb(livro, cap, vs))
    return (cap, txt_cap_hb)

def retornar_livros_at():
    sql = 'select distinct BookName from Words'

    try:
        with sqlite3.connect(hb_at) as cnx:
            cursor = cnx.cursor()
            rs = cursor.execute(sql).fetchall()
    except sqlite3.Error as er:
        print(er)

    return [l[0] for l in rs]

def traduzir(fonte, livro, cap_ini, cap_fim):
    livros_at = retornar_livros_at()
    transl=Translator(from_lang=fonte, to_lang='pt')
    if livro in livros_at:
        texto_traduzido = ''
        for cap in range(cap_ini, cap_fim+1):
            nr_vs = 1
            for verso in [vs[1] for vs in retornar_txt_cap_hb(livro, cap)[1]]:
                texto_traduzido += str(nr_vs) + ' '
                texto_traduzido += ''.join(transl.translate(verso) + ' ')
                nr_vs=nr_vs+1
            texto_traduzido += ''.join('\n\n' + livro + ' ' + str(cap+1) + '\n')
    else:
        print('Livro informado não corresponde a nenhum dos do Antigo Testamento')

    return texto_traduzido

with open('texto_traduzido', 'a') as saida:
    saida.write(traduzir(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))