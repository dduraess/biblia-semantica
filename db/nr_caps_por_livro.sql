select max(chapter)
from verse
inner join book on verse.book_id = book.id
where book.name like '%{}%'