from bug_fixing_1 import *
import calendar


class CalendarBookmark:

    """класс дескриптор - закладка для ежедневника"""
    def __init__(self, bookmark=0):
        self.bookmark = bookmark

    def __get__(self, obj, obj_type):
        return self.bookmark

    def __set__(self, obj, value):
        if value > len(obj) or value < 1:
            raise PageNotFoundError
        self.bookmark = value


class CalendarBook(Book):
    """класс книги - ежедневник с закладкой"""

    bookmark = CalendarBookmark()

    def __init__(self, title, content=None):
        super().__init__(title, content)
        self.title = title
        self._content = [] if content is None else content

        if content is None:
            cl = calendar.TextCalendar(firstweekday=0)
            for month in range(1, 13):
                self._content.append(cl.formatmonth(int(self.title), month))
                for day in [d for d in cl.itermonthdates(int(self.title), month) if d.month == month]:
                    self._content.append(str(day))
        else:
            self._content = content

    def __len__(self):
        return len(self._content)

    def __getitem__(self, num_page):
        if num_page > len(self._content) or num_page <= 0:
            raise PageNotFoundError
        return self._content[num_page - 1]

    def __setitem__(self, num_page, new_page):
        if num_page > len(self._content) or num_page <= 0:
            raise PageNotFoundError
        self._content[num_page - 1] = Page(str(new_page))
