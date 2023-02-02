from exceptions import *

class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.author = author
        self.year = year
        self.bookmark = {}

    def read(self, page):
        if page < 0 or page > self.size:
            raise PageNotFoundError

        return self.content[page]

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise PermissionDeniedError

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        if page < 0 or page > self.size:
            raise PageNotFoundError

        self.bookmark.update({person: page})

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        if person not in self.bookmark:
            raise PageNotFoundError

        return self.bookmark[person]

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        del self.bookmark[person]


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=[]):
        """конструктор"""
        if len(content) > 0:
            self.size = len(content)
        else:
            self.size = size
            content = ['' for _ in range(size)]

        super().__init__(title, content)
        self.max_sign = max_sign

    def read(self, page):
        """возвращает страницу с номером page"""
        if page < 0 or page > self.size:
            raise PageNotFoundError

        return self.content[page]

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        if page < 0 or page > self.size:
            raise PageNotFoundError

        if len(self.content[page] + text) > self.max_sign:
            raise TooLongTextError

        self.content[page] += text

class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        return book.read(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""
        book.write(page, text)

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        if not isinstance(book, Novel):
            raise NotExistingExtensionError

        book.set_bookmark(self, page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        if not isinstance(book, Novel):
            raise NotExistingExtensionError

        return book.get_bookmark(self)

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        if not isinstance(book, Novel):
            raise NotExistingExtensionError

        book.del_bookmark(self)


# person = Person('Igor')
# print(person.name)

# from string import ascii_lowercase as alphabet
# content = [sign for sign in alphabet]
# notebook = Notebook('note', 24, 100, content)
# print(notebook.title)
# print(notebook.max_sign)
# print(notebook.size)
# print(notebook.content)
# print(person.read(notebook, 100))
# person.write(notebook, 10, '+new_value')
# print(person.read(notebook, 10))

# person.read(notebook, 100)

# too_long_text = alphabet * 1000
# person.write(notebook, 0, too_long_text)

# novel = Novel('Grin', 1925, 'Gold chain')
# print(novel.size)
# print(novel.author)
# print(novel.year)
# print(novel.title)

# novel = Novel('Grin', 1925, 'Gold chain', content)
# user1 = Person('Dima')
# user2 = Person('Dima')
# user1.set_bookmark(novel, 5)
# user2.set_bookmark(novel, 7)
# print(user1.get_bookmark(novel) == user2.get_bookmark(novel))
# print(user1.get_bookmark(novel))
# print(user2.get_bookmark(novel))

# person.write(novel, 10, 'new_value')
# person.set_bookmark(novel, 10)
# print(person.get_bookmark(novel))
# person.del_bookmark(novel)
# print(person.get_bookmark(novel))
