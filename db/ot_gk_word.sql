select 
    -- id, 
    src_name, 
    book_name, 
    chapter_nr, 
    verse_nr
    , word_nr
    , word
    , word_root
    , morphology
from 
    content
where 
    word_root like '%{}%'