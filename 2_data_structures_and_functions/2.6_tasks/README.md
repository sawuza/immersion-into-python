# 2.6 Tasks

### 2.6.1 Lottery - 2
> You work for a company that organizes lotteries. This time the task is to write a program for generating all the ticket numbers that will be printed in the printing house for the next draw. The number of tickets, the number of digits in the ticket number and the series number are determined by the lottery organizers and are known in advance. During some lotteries, there may be cases when the number of required tickets exceeds the possible number of numbers in the specified series. The program shall take that situation into account and, if necessary, automatically change the series to another one, according to the rules of series generation. The input data for the program are such that it is guaranteed: the number of required tickets is greater than 0 and the number of series is enough to generate the required number of tickets. The program must generate exactly the specified number of numbers.
> 
> Series generation rules: The series number is changed when all possible numbers of the current series have already been generated. If the letter on the right in the current series is "Z", it is changed to "A", and the letter on the left is changed to the letter that is next in order in the alphabet after it. For example: KZ -> LA, TZ -> UA. In all other cases, the letter to the right of the current series changes to the letter that is next in order in the alphabet after the current one. For example: RD -> RE, HO -> HP.
> 
> Ticket series numbers can take values from "AA" to "ZZ". Possible numbers for the number of digits in a ticket number equal to 6, will take all possible values from 000001 to 999999. Extreme values in the above examples must be included. 

### 2.6.2 Rubber matrix
> You and your friends are writing a program for working with two-dimensional matrices. Part of the functionality necessary for the normal operation of the program is assigned to you to write. Namely:
> - a function to create an "empty" matrix of size: size x size, filled with "zero" elements (None)
> - a function for adding an element to a matrix with the ability to extend the matrix itself
> - function to convert a matrix into a string representation
>
> Rules for adding elements to a matrix:
> - the matrix is filled in line by line, from left to right, from the first row to the last one
> - element to be added takes the position of the first free "zero" element
> - a "zero" element (None) is ignored
> - in case a matrix element being added takes the position of the first element in the last matrix row, the matrix needs to be "expanded" by increasing the matrix size by 1 (adding one column and one row), while the elements added to the matrix are shifted to the beginning so that there are no "null" elements between them.

### 2.6.3 Ingredients
> In the work of cafes that do not have electronic accounting, sometimes there are situations when, after taking an order 
waiter finds out that there are not enough products in the kitchen to prepare the required number of servings. In this task you need to implement a function that solves this problem. Write a function check_portions that takes two mandatory arguments food (name of dish), count (number of servings) and two optional arguments recipes, store (products available) with default values - recipes and store, respectively. Data on the number of products needed to prepare one portion of a dish and the number of available products in the kitchen are stored in dictionaries:
> - **recipes**, where keys: names of dishes, values: dictionaries like {'product1':'amount_of_product1_in_portion', 'product2': 'amount_of_product2_in_portion', ...}
> - **store**, where keys: product names, values: amount of product available for cooking
>
> The function should return a tuple of two integers(response_code, count), if there is enough food to cook the specified number of servings: **response_code=1, count** is the number of servings from the request, otherwise: **response_code=0, count** is the maximum possible number of servings of the given dish that can be cooked from the food stored in the kitchen. The unit of measure for all products is grams. For dishes missing from the menu the function returns tuple (0,0).

### 2.6.4 Collecting statistics
> In the previous task, you took the first step toward organizing electronic accounting in the cafe by writing the check_portions function. The next step can be the collection of statistics about the orders. In the future, the obtained information will be used by the management staff (for example: to analyze the situations when the orders cannot be fulfilled due to the lack of necessary products and to take measures to prevent such situations). In this task, you need to write the collect_statistics decorator for the check_portions function, which will collect and save data about the orders.  The decorator saves collected data into a dictionary (the defaultdict type from the collections module) passed to it as an argument. The keys in the dictionary are the names of dishes, the values are lists of named tuples Order. Each named tuple Order corresponds to one order and contains two fields: success - the success of the order (executed (1) / rejected (0) ), portions - the number of portions of the order (if the order is rejected - you must store the number of portions which are NOT enough to fulfill the order). The type of data stored in both fields is int. If you are not yet familiar with namedtuple and defaultdict from the collections module of the Python standard library, check out the documentation or read the article.  To pass the assignment, you need to add to the code template:
> - your implementation of the collect_statistics decorator
> - your check_portions function (which you implemented in the "Ingredients" task)
> - decorate the check_portions function in any of the ways.
