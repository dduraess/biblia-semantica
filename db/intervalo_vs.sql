select verse, text 
from verse
inner join book on verse.book_id = book.id
where book.name like '%{}%'
and chapter between {} and {}
-- and verse between {} and {}
