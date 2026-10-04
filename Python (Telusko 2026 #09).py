Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
tup = [23,45,67,43]
type(tup)
<class 'list'>
tup = 23,45,67,43
type(tup)
<class 'tuple'>
tup (23,45,67,43)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup (23,45,67,43)
TypeError: 'tuple' object is not callable
tup = (23,45,67,43)
type(tup)
<class 'tuple'>
min(tup)
23
max(tup)
67
sum(tup)
178
tup [2]
67
tuo[2] = 65
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    tuo[2] = 65
NameError: name 'tuo' is not defined. Did you mean: 'tup'?
tup [2] = 65
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    tup [2] = 65
TypeError: 'tuple' object does not support item assignment
>>> len(tup)
4
>>> tupA = (2,'navin',7.9)
>>> tupA
(2, 'navin', 7.9)
>>> num = tupA [0]
>>> num, name, num1 = tupA
>>> num
2
>>> name
'navin'
>>> num1
7.9
>>> num, name, num1, num2 = tupA
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    num, name, num1, num2 = tupA
ValueError: not enough values to unpack (expected 4, got 3)
>>> tupB = (34, 'navin', [3,4,5,6])
>>> tupB [0] = 34
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tupB [0] = 34
TypeError: 'tuple' object does not support item assignment
>>> tupB [2] [1] = 9
>>> tupB
(34, 'navin', [3, 9, 5, 6])
>>> 34 in tupB
True
>>> 'Navin' in tupB
False
>>> 
>>> 
>>> 
>>> tup = (50,70,90)
>>> x = tup [0]
>>> y = tup[2]
>>> print(x+y)
140
