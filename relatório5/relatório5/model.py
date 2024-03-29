from pymongo import MongoClient
from bson.objectid import ObjectId

class bookModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_book(self, name: str, autor: str) -> str:
        try:
            result = self.collection.insert_one({"name": name, "autor": autor})
            livro_id = str(result.inserted_id)
            print(f"book {name} created with id: {livro_id}")
            return livro_id
        except Exception as error:
            print(f"An error occurred while creating book: {error}")
            return None

    def read_book_by_id(self, book_id: str) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(book_id)})
            if book:
                print(f"book found: {book}")
                return book
            else:
                print(f"No book found with id {book_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading book: {error}")
            return None

    def update_book(self, book_id: str, name: str, autor: str) -> str:
        try:
            result = self.collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"name": name, "autor": autor}})
            if result.modified_count:
                print(f"book {book_id} updated with name {name} and autor {autor}")
            else:
                print(f"No book found with id {book_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None

    def delete_book(self, book_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            if result.deleted_count:
                print(f"book {book_id} deleted")
            else:
                print(f"No book found with id {book_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
            return None