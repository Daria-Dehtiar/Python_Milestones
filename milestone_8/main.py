from typing import List, Dict

class Shelf:
    def __init__(self, _id: int):
        self._id = _id
        self.content = {}

    def create_category(self, name: str) -> str:
        if name not in self.content:
            self.content[name] = []
            return f"Category {name} created successfully"
        else:
            return f"Category {name} already exists"

    def delete_category(self, name: str) -> str:
        if name in self.content:
            del self.content[name]
            return f"Category {name} was deleted"
        return f"Category {name} does not exist"

    def get_categories(self):
        return list(self.content.keys())

    def get_all_content(self) -> Dict:
        return self.content

    def get_books_by_category(self, category_name: str):
        if category_name in self.content:
            return self.content[category_name]
        return f"Category {category_name} does not exist"

    def add_book(self, category_name: str, book_title: str) -> str:
        if category_name in self.content:
            self.content[category_name].append(book_title)
            category.books = self.content[category_name]
            return f"Book {book_title} was added to category {category_name}"
        return f"Category {category_name} does not exist. Create this category first."

    def delete_book(self, category_name: str, book_title: str) -> str:
        if category_name in self.content:
            for book in self.content[category_name]:
                if book == book_title:
                    self.content[category_name].remove(book_title)
                    category.books = self.content[category_name]
                    return f"Book {book_title} was deleted"
        return f"Book {book_title} not found"

    def get_book(self, category_name: str, book_title: str):
        if category_name in self.content:
            for book in category.books:
                    if book == book_title:
                        return book
        return f"Book {book_title} not found"

class Book():
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.info = {"title": self.title, "author": self.author, "year": self.year}
        self.location = {}

    def get_info(self) -> Dict:
        return self.info

    def set_category(self, category, shelf):
        if isinstance(category, Category):
            self.location["category"] = category.name
            self.location["shelf"] = category.shelf_id
            category.books.append(book.title)
            shelf.content[category.name] = category.books
            return f"Book {self.title} was added to the {category} category", self.location
        else:
            return f"Category {category} does not exist"

class Category():
    def __init__(self, name: str, shelf_id: int):
        self.name = name
        self.shelf_id = shelf_id
        self.books = []

    def books_in_alphabetical_order(self) -> List:
        sorted_books = sorted(self.books, key=lambda book: book)
        return sorted_books

    def get_book(self, book_title):
        for book in self.books:
            if book == book_title:
                return book
            else:
                return "No book with that name in this category"

    def delete_book(self, book_title: str):
        for book in self.books:
            if book == book_title:
                self.books.remove(book)
                return f"Book {book_title} deleted"
        return "No book with that name in this category"

    def search_by_title(self, string: str):
        matching_titles = []
        for book in self.books:
            if book.startswith(string):
                matching_titles.append(book)
        for book in matching_titles:
            print (book + "\n")


if __name__ == "__main__":

    import random
    from faker import Faker

    fake = Faker()

    def create_category():
        categories = ["Science", "Poetry", "Legends", "Tragedy", "Fantasy", "Fairy tale", "Adventure", "Religion", "History", "Thriller", "Detective"]
        category = random.choice(categories)
        return category

    pile_of_books = [Book(title = (fake.sentence(nb_words = 4)[:-1]), author = fake.name(), year = fake.year()) for _ in range(50)]
    shelves = [Shelf(_id = _) for _ in range(1, 6)]
    categories = [Category(name = create_category(), shelf_id = random.randint(1, 5)) for _ in range(10)]

    for book in pile_of_books:
        category = random.choice(categories)
        shelf = next((s for s in shelves if s._id == category.shelf_id), None)
        if shelf:
            book.set_category(category, shelf)

    for shelf in shelves:
        print(shelf._id, shelf.content)
