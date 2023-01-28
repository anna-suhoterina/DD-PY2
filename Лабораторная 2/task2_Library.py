from typing import Optional

from pydantic import BaseModel, conint


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book(BaseModel):
    id_: conint(gt=0)
    name: str
    pages: conint(gt=0)


class Library(BaseModel):
    books: Optional[list[Book]] = []  # если аргумент не передан, инициализируем библиотеку с пустым списком книг

    def get_next_book_id(self) -> int:
        """ Возвращение идентификатора для добавления новой книги в библиотеку"""
        if self.books:  # если в библиотеке есть книги
            return (max(self.books, key=lambda book: book.id_)).id_ + 1  # увеличиваем id последней книги на 1
        else:
            return 1  # если книг нет, возвращаем id = 1

    def get_index_by_book_id(self, search_id: int) -> int:
        """ Возвращение индекса книги в списке со значением запрашиваемого id"""
        for book_index, current_book in enumerate(self.books):  # перебираем все книги и их индексы в списке
            if search_id == current_book.id_:  # если книга с запрашиваемым id существует
                return book_index  # возвращаем ее индекс в списке
            if search_id not in [book.id_ for book in self.books]:  # если книги с запрашиваемым id не существует
                raise ValueError("Книги с запрашиваемым id не существует")  # вызываем ошибку


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

