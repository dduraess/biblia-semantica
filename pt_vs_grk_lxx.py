import sys
sys.path.append('/Users/davison/Software/almeida-semantica')
from src.ConectorBD import *
import cltk as cltk
import pandas as pd
from pandasql import sqldf
import os

class pt_vs_grk_lxx():
    
    ara= '/Users/davison/Software/almeida-semantica/db/ARA.sqlite'

    sql_pt= """
                SELECT 
                    book_id as nr_sq_livro, 
                    chapter
                    , verse 
                    , text
                FROM 
                    verse
                ORDER BY 
                    nr_sq_livro,
                    chapter,
                    verse
                """

    pt_df = pd.read_sql_query(sql_pt, ConectorBD(ara).con)

    def exportar_vs_rng_pt():
        vs_rng = pt_df.loc[(pt_df['nr_sq_livro'] == 5) & (pt_df['chapter'] == 32) & (pt_df['verse'] >= 1) & (pt_df['verse'] <= 176)]
        vs_rng.to_csv('/Users/davison/Desktop/vs_rng.csv', index=False)
        os.system('open ' + '/Users/davison/Desktop/vs_rng.csv')