# 3.6 Tasks

### 3.6.1 Rubber matrix - 2
> Last week you solved the problem of writing functions for a program that works with two-dimensional matrices. In this assignment, you will write a Matrix class that implements a similar functionality.

### 3.6.2 Hierarchy of exceptions
> In the next few tasks you will need to write classes for working with different books (notebooks, magazines), inheriting the basic **Book** class for all books.
>
> When working with these classes (reading, writing and others) exceptional situations can occur. In this task you need to implement a hierarchy of custom exceptions that you will use later: **BookIOErrors** - (basic exception class), **PageNotFoundError** - for situations when methods address a page that doesn't exist, **TooLongTextError** - for situations when the text you write doesn't fit on the page, **PermissionDeniedError** - for situations when writing to the book is not allowed, **NotExistingExtensionError** - if the called method in the book class is missing.

### 3.6.3 Write-read
> A book and a notebook, despite their differences, have some things in common. They have pages and can be read. Write an implementation of classes **Novel** and **Notebook**, which are inherited from the base class Book. The distinctive feature of Novel is the ability to add bookmarks and find page number by them. In the book you also can't make notes (write). In a notebook, on the contrary, you can make notes, but there is no bookmarking functionality.

### 3.6.4 Table of contents book
> In this task you need to extend the functionality of the **Novel** and **Person** classes.
