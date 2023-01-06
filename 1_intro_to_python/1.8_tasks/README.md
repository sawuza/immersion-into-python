# 1.8 Tasks

## 1.8.1 Letters positions

> __Letter positions.__ The program inputs two non-empty strings containing at least one character. 
For each letter in the second line, determine at what positions it occurs in the first line and print them in the format: <letter> <position numbers separated by space>. If the letter has no occurrences, print None instead of position numbers. The sequence of letters must correspond to the sequence in which they occur in the second line (that is, they must not change). Letters in different registers should be considered equivalent. If some letter enters the second line several times, output should be done only for the first occurrence. Letters include only letters of the Latin alphabet a-z, A-Z.
> 
> __Note:__ It is guaranteed that only Latin characters, numbers, punctuation, and special characters are fed into the program.

## 1.8.2 Just the letters

> __Just the letters.__ Write a program with a string as input. The program must select all the letters occurring in the string and output them in alphabetical order in one line (the letters must be in lower case), without spaces and repetitions to the standard output. Letters include only characters of the Latin alphabet (A-Z, a-z). The program must not be case-sensitive for letters.
>
> __Note:__ it is guaranteed that only Latin characters, punctuation, and special characters are fed into the program.

## 1.8.3 Electronic Range

> __Electronic Range.__ The target of the electronic shooting gallery outputs data about the shot as a pair of x, y coordinates. The reference point of the coordinate system coincides with the center of the target (as in the picture below) . Your task is to write a program that will calculate the sum of scores of all hits. Data input format: the first line contains number k (the number of shots), the next k lines contain the coordinates of hits x, y (two real numbers separated by a space).
It is guaranteed that x, y are in the range from -15 to 15.
>
> The program should print the number of points scored for all shots.
>
> __Note:__ In cases where the hit coordinates are exactly on the line of the circle dividing the zones, fewer points are scored. For example for the coordinates: (0, -8) - 2 points, (10, 0) - 0 points.


## 1.8.4 Lottery

> __Lottery.__ You work for a company that organizes lotteries. The lottery ticket number is "002345 AZ" (the serial number of the ticket, consisting of 6 digits, and a series of two capital letters of the Latin alphabet).
>
> Write a program that generates ticket numbers of winners. The program inputs: the number of winners, and the number of the last ticket sold.  The program must generate the specified number of unique numbers (if the number of tickets sold allows it) and print them in the format - Winner number 1 - "002345 AZ". Winners can be displayed in any order.
>
> It is guaranteed that all ticket numbers from "000001" through the number of the last ticket sold (inclusive) will participate in the draw, and the series number in the current draw is unique. If the number of tickets sold is less than or equal to the number of scheduled winners in the drawing, all numbers of tickets sold shall be deemed winners.
>
> __Note:__ if you already know Python well enough and you know about sys.stdin.read(), use input() for data input in this task. This requirement is due to the peculiarities of the test implementation for this task. Use the randint function from the random module of the Python standard library to generate random numbers.

## 1.8.5 Simple Substitution Cipher

> __Simple Substitution Cipher__ Write a program to decrypt messages encrypted with the simple substitution cipher. The program is inputted with an encrypted string and a decryption table.
>
> A decryption table is a sequence of symbols, each of which corresponds to the corresponding (in order) symbol of the original alphabet. For clarity, you can write the decryption table and the alphabet under each other:

`cdefghijklmnopqrstuvwxyzab  # decryption table`
`abcdefghijklmnopqrstuvwxyz  # original alphabet`

> This arrangement shows that the letters from the encrypted text correspond to the letters of the original text. For example: the character j in the encrypted text corresponds to h in the original text.
>
> Decode the message and print it out. The program must be case insensitive (all letters of the original message must be converted to lower case).
