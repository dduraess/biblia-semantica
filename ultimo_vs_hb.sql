select 
    max(Verse) ultimo_vers
from 
	Words
where 
    BookName = '{}'
and Chapter = {}