from write_read import *


class AdvancedPerson(Person):
    def __init__(self, name):
        super().__init__(name)

    def search(self, book, name_page):
        """возвращает номер страницы name_page из книги book"""
        return book.search(name_page)

    def read(self, book, page):
        if isinstance(page, str):
            page = book.search(page)

        return book.read(page)

    def write(self, book, page, text):
        raise PermissionDeniedError


class NovelWithTable(Novel):
    """класс - книга с оглавлением"""

    def __init__(self, author, year, title, content=None, table=None):
        super().__init__(author, year, title, content)
        if table is None:
            self.table = {}
        else:
            self.table = table

    def search(self, name_page):
        if name_page in self.table:
            return self.table[name_page]

        raise PageNotFoundError

    def add_chapter(self, chapter, page):
        self.table.update({chapter: page})

    def remove_chapter(self, chapter):
        if chapter not in self.table:
            raise PageNotFoundError

        del self.table[chapter]


# person = AdvancedPerson('Ivan')
# from string import ascii_lowercase as alphabet

# content = [sign for sign in alphabet]
# table = {'start_page': 0}
# novel = NovelWithTable('Grin', 1925, 'Gold chain', content, table)
# print(novel.table)
# print(person.search(novel, 'start_page'))

# print(person.search(novel, 'non-exist_page'))
# novel.add_chapter('last_page', 26)
# print(person.search(novel, 'last_page'))
# novel.remove_chapter('start_page')
# print(novel.table)

# person.write(novel, 1, 'abcabc')
# print(person.read(novel, 1))
