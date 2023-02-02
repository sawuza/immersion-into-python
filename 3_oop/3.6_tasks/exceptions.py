class BookIOErrors(Exception):
    pass


class NotExistingExtensionError(BookIOErrors):
    pass


class PermissionDeniedError(BookIOErrors):
    pass


class PageNotFoundError(BookIOErrors):
    pass


class TooLongTextError(BookIOErrors):
    pass
