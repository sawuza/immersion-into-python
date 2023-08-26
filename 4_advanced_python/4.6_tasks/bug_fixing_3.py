from bug_fixing_2 import *
from abc import ABC, abstractmethod
import calendar
import re


class NotExistingExtensionError(BaseException):
    pass


class PermissionDeniedError(BaseException):
    pass


class Person(ABC):
    """класс описывающий человека"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def set_bookmark(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_bookmark(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_bookmark(self, *args, **kwargs):
        pass


class Reader:
    def read(self, book, num_page):
        return book[num_page]


class Writer:
    def write(self, book, num_page, text):
        book[num_page] += text


class AdvancedPerson(Person, Reader, Writer):
    """класс человека умеющего читать, писать, пользоваться закладками"""

    def set_bookmark(self, book, num_page):
        book.bookmark[self.name] = num_page

    def get_bookmark(self, book):
        return book.bookmark[self.name]

    def del_bookmark(self, book, person):
        del book.bookmark[person]

    def search(self, book, page):
        if not hasattr(book, "_table"):
            raise NotExistingExtensionError
        return book._table.search(page)

    def read(self, book, page):
        if not hasattr(book, "_table"):
            raise NotExistingExtensionError
        if type(page) == int:
            reader = Reader()
            return reader.read(book, page)
        else:
            return book[self.search(book, page)]

    def write(self, book, page, text):
        writer = Writer()
        writer.write(book, page, text)


class PageTableContents(Page):
    def __init__(self, text=None, max_sign=2000):
        super().__init__(text, max_sign)
        self.max_sign = max_sign
        if text is None:
            self.text = "TABLE OF CONTENT\n"
        else:
            self.text = text

    def __str__(self):
        return self.text

    def search(self, chapter):
        regexp = re.compile('^{}:(\d+)$'.format(chapter), re.MULTILINE)
        res = re.search(regexp, self.text)
        if res is not None:
            return int(res[1])
        raise PageNotFoundError

    def __add__(self, other):
        raise PermissionDeniedError

    def __radd__(self, obj):
        raise PermissionDeniedError

    def __iadd__(self, other):
        raise PermissionDeniedError


class CalendarBook(Book):
    """класс ежедневник с закладкой"""

    def __init__(self, title, content=None):
        super().__init__(title, content)
        self.title = title
        self._content = [] if content is None else content
        self.bookmark = None

        index = 1
        cl = calendar.TextCalendar(firstweekday=0)
        table_of_content = "TABLE OF CONTENT\n"
        for month in range(1, 13):
            self._content.append(Page(cl.formatmonth(int(self.title), month)))
            table_of_content += "{}:{}\n".format(calendar.month_name[month], index)
            index += 1
            for day in [d for d in cl.itermonthdates(int(self.title), month) if d.month == month]:
                self._content.append(Page(str(day)))
                index += 1
        self._table = PageTableContents(table_of_content)
        self._content.append(self._table)

    def __len__(self):
        return len(self._content)

    def __getitem__(self, num_page):
        if num_page > len(self._content) or num_page <= 0:
            raise PageNotFoundError
        return self._content[num_page - 1]

    def __setitem__(self, num_page, new_page):
        if num_page > len(self._content) or num_page <= 0:
            raise PageNotFoundError
        self._content[num_page - 1] = new_page
