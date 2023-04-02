from save_json import writeAJson
from database import Database
from model import bookModel

db = Database(database="relatorio5", collection="livros")
db.resetDatabase()
data = db.collection.find()

book_model = bookModel(db)

livro_id = book_model.create_book("Moby Dick", "Herman Melville")

book1 = book_model.read_book_by_id(livro_id)

book_model.update_book(livro_id, "Mobie Dick", "Herman Melville")

book_model.delete_book(livro_id)


