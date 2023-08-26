class TooLongTextError(BaseException):
    pass


class PageNotFoundError(BaseException):
    pass


class Page:
    """класс страница"""

    def __init__(self, text=None, max_sign=2000):
        self._text = '' if text is None else text
        self.max_sign = max_sign

    def __str__(self):
        return self._text

    def __len__(self):
        return len(self._text)

    def __add__(self, obj):
        if not isinstance(obj, (Page, str)):
            raise TypeError
        if len(self._text + obj) > self.max_sign:
            raise TooLongTextError
        self._text += obj
        return self

    def __radd__(self, obj):
        if not isinstance(obj, (Page, str)):
            raise TypeError
        return obj + self._text

    def __gt__(self, obj):
        if isinstance(obj, (Page, str)):
            return len(self) > len(obj)
        raise TypeError

    def __ge__(self, obj):
        if isinstance(obj, (Page, str)):
            return len(self) >= len(obj)
        raise TypeError

    def __eq__(self, obj):
        if isinstance(obj, (Page, str)):
            return len(self) == len(obj)
        raise TypeError


class Book:
    """класс книга"""

    def __init__(self, title, content=None):
        self.title = title
        self._content = [] if content is None else content

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

    def __gt__(self, obj):
        if isinstance(obj, Book):
            return len(self._content) > len(obj)
        raise TypeError

    def __ge__(self, obj):
        if isinstance(obj, Book):
            return len(self._content) >= len(obj)
        raise TypeError

    def __eq__(self, obj):
        if isinstance(obj, Book):
            return len(self._content) == len(obj)
        raise TypeError
