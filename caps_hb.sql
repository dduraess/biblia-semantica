select 
    distinct BookName livro
    , max(Chapter) ultimo_cap
from 
    Words
group by 
    1