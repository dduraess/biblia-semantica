select 
    WordID, BookName, Chapter, Verse, WordIndex, Lemma, Morphology
from 
    Words
where 
    Form like '%{}%'