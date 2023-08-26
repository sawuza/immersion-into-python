# 4.6 Tasks

### 4.6.1 Bug fixing 1
> In the previous week, you solved several assignments to create "book" classes. These assignments were of a tutorial nature and the classes created have flaws.
>
> First, storing a page as a string is not a good idea. A page may have more complex logic for adding text than just writing to the end of a line. As such an example, consider a school journal, where adding a grade occurs on a line with a particular last name.
>
> Secondly, the table of contents is essentially a subtype of a page and accordingly should be passed and stored not in a separate attribute, but in the content (first or last page, as it is done in real books). 
>
> Third, the max_sign attribute of the Notebook class refers to page characteristics rather than to the book.
>
> Fourth, the write, read methods in the Book class do not look natural, for reading it would be more suitable to refer to a page as a list element - book[page], and to add a record to a page as book[page] += 'string'
>
> Fifth, note that books can be compared to each other, for example by the number of pages in them.
>
> Sixth, bookmarks can be set in all books (including notebooks).
>
> In this task, you need to start working on bugs. The corrections will not concern the bookmarks and table of contents functionality. Write a "correct" implementation of Book and Page classes.

### 4.6.2 Bug fixing 2
> In this task, we continue to deal with the disadvantages of "book" classes. As already mentioned, the peculiarity of bookmarks is that you can put them in any book. In addition, it is worth noting that there are quite a large number of their types. As examples of varieties we can mention such characteristics as the possibility of bookmarks to have or not to have markings (for example, by whom it was put or tags for quick search on bookmarks), bookmarks connectivity (when bookmarks mark the beginning and end of certain pages, for example: to highlight a chapter in a book), a bookmark can be installed in a book initially without the ability to completely remove it (remember the diary, with its ribbon bookmark). Therefore, one possible solution might be to use descriptors to create a bookmarking mechanism.
> 
> As an assignment, we suggest you to write an implementation of the daily planner class - CalendarBook(Book) and the CalendarBookmark descriptor class. In the descriptor, you need to implement two methods to get and set the value of the bookmark attribute of the CalendarBook class.  The bookmark for the diary is set in the book initially, the page number it refers to is 0. The same value is returned when the bookmark attribute of the CalendarBook class is accessed when the book content is missing. One more remark concerning bookmark indexing - the reader cannot set a bookmark to the default position or to a missing position in the book. In such cases, a PageNotFoundError exception is thrown. If you try to delete a bookmark, the AttributeError exception is thrown.
> 
> Since a diary is essentially a kind of notebook, its constructor is almost identical to the Notebook class constructor you implemented earlier. The only difference is the way of content generation. The year (string) is passed as the title parameter. The pages of the new diary have the following structure and content: for each month (starting from January) the first page contains the calendar for the current month, each next page represents a certain day of the current month with the date content in the format - " 2011-01-02" (year, month, number written through the sign "-" (minus)). The order of months and numbers of the month correspond to the normal flow of time. To create pages containing a calendar, use the formatmonth method of the TextCalendar class from the calendar module of the Python standard library. Generating the date for the rest of the pages uses the itermonthdates method from the class above. For more information on how the classes work, see the examples below.

### 4.6.3 Bug fixing 3
> This is the final task for implementing "book" classes. In it, you will have to implement the PageTableContents class of the table of contents page and add the initialization of the table of contents page to the constructor of the CalendarBook class. In addition, you need to fix defects in the implementation of Person and AdvancedPerson classes.