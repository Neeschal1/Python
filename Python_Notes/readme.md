###Loops###

while using for loop, we use it in 2 different ways.
1. using range functions
2. using pre-defined list or tuple or dict.


1. When we are using range function inside for loop, we use the index value or looping variable(for i in range()). Here, i determines the starting and ending numeric values present inside range function.
Point to remember: Range function only allows integer value to it.


2. Let us write a demo program for better understanding:

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    print(i)

Here, we are using a list named arr. and when we use arr in loop with a variable i, the i variable denotes the list elements present inside the list. So, this program gives the output as:
1
2
3
4
5
6
7
8
9
10

Wonder, why these outputs are not in sequential manner? Its due to missing of end=' ' after print() function inside the loop.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in arr:
    print(i, end=' ')

Now, this will give the sequencial output as:
1 2 3 4 5 6 7 8 9 10


Note:
For range function,

for i in range(a, b, c):
  print(i)

Here, a, b and c inside range function denotes special meanings within it. 
a: represents the starting of the loop
b: represents the ending of the loop
c: represents the steps of occuring the second or third loop after its previous loop

for eg:
for i in range(1, 20, 3):
  print(i)

Output will be:
1, 4, 7, 10, 13, 16, 19


While using a loop, we might have to use if ___ else conditon.
sometimes, we may need to terminate the program whenever one of the result satisfies a single command. we use break keyword