from typing import List

from pymongo import MongoClient
from bson.objectid import ObjectId

from main import Habitat


class AnimalModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_Animal(self, nome: str, especie: str, idade: int, habitat: List[Habitat]) -> str:
        try:
            result = self.collection.insert_one({"id": id, "nome": nome, "especie": especie, "idade": idade, "habitat": habitat})
            animal_id = str(result.inserted_id)
            print(f"Animal {nome} created with id: {animal_id}")
            return animal_id
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None

    def read_animal_by_id(self, animal_id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def update_animal(self, animal_id: str, nome: str, especie: str, idade: int, habitat: Habitat) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {nome: str, especie: str, idade: int, habitat: Habitat}})
            if result.modified_count:
                print(f"animal {animal_id} updated with name {nome}, age{idade}, especie {especie} and habitat{habitat}")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None