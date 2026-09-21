import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #тест 2 - книга с менее 0 или более 41 символа не добавится
    @pytest.mark.parametrize('name',['', 'A' * 41])
    def test_add_new_book_name_lenght_boundaries(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    #тест 3 - установка жанра из списка genre
    @pytest.mark.parametrize('books_genre',['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_from_genre_list(self, books_genre):
        book_Name = 'Преступление и наказание'
        collector = BooksCollector()
        collector.add_new_book(book_Name)
        collector.set_book_genre(book_Name, books_genre)
        assert collector.books_genre[book_Name] == books_genre

    #тест 4 - получение жанра по существующей книге
    def test_get_book_genre_by_exist_book_name(self):
        book_Name = 'Гарри Поттер'
        books_genre = 'Фантастика'
        collector = BooksCollector()
        collector.add_new_book(book_Name)
        collector.set_book_genre(book_Name, books_genre)
        assert collector.get_book_genre(book_Name) == books_genre

    #тест 5 - получение списка книг по существующему жанру
    def test_get_books_with_specific_genre_by_exist_genre(self):
        book_Name_1 = 'Гарри Поттер и филосовский камень'
        book_Name_2 = 'Гарри Поттер и кубок огня'
        book_Name_3 = 'Шерлок Холмс'
        books_genre_1 = 'Фантастика'
        books_genre_2 = 'Детективы'

        collector = BooksCollector()
        collector.add_new_book(book_Name_1)
        collector.add_new_book(book_Name_2)
        collector.add_new_book(book_Name_3)

        collector.set_book_genre(book_Name_1, books_genre_1)
        collector.set_book_genre(book_Name_2, books_genre_1)
        collector.set_book_genre(book_Name_3, books_genre_2)

        assert len(collector.get_books_with_specific_genre(books_genre_1)) == 2

    #тест 6 - получение списка книг для детей
    def test_get_books_for_children_one_book_for_children(self):
        book_Name_1 = 'Гарри Поттер и филосовский камень'
        book_Name_2 = 'Стивен кинг'

        collector = BooksCollector()
        collector.add_new_book(book_Name_1)
        collector.add_new_book(book_Name_2)

        collector.set_book_genre(book_Name_1, 'Фантастика')
        collector.set_book_genre(book_Name_2, 'Ужасы')

        assert len(collector.get_books_for_children()) == 1

    #тест 7 - добавляем книгу в Избранное
    def test_add_book_in_favorites_two_books(self):
        book_Name_1 = 'Гарри Поттер и филосовский камень'
        book_Name_2 = 'Преступление и наказание'

        collector = BooksCollector()
        collector.add_new_book(book_Name_1)
        collector.add_new_book(book_Name_2)

        collector.set_book_genre(book_Name_1, 'Фантастика')
        collector.set_book_genre(book_Name_2, 'Детективы')

        collector.add_book_in_favorites(book_Name_1)
        collector.add_book_in_favorites(book_Name_2)

        assert len(collector.favorites) == 2

    #тест 8 - добавляем книгу в Избранное
    def test_delete_book_from_favorites_one_book(self):
        book_Name_1 = 'Гарри Поттер и филосовский камень'
        book_Name_2 = 'Преступление и наказание'

        collector = BooksCollector()
        collector.add_new_book(book_Name_1)
        collector.add_new_book(book_Name_2)

        collector.set_book_genre(book_Name_1, 'Фантастика')
        collector.set_book_genre(book_Name_2, 'Детективы')

        collector.add_book_in_favorites(book_Name_1)
        collector.add_book_in_favorites(book_Name_2)

        collector.delete_book_from_favorites(book_Name_1)

        assert len(collector.favorites) == 1