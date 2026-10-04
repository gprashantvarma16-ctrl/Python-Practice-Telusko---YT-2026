Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 3
b = 2
a + b
5
a - b
1
a * b
6
a / b
1.5
a // b
1
a % b
1
a = (a+2)
a
5
a += 2
a
7
a ++
SyntaxError: invalid syntax
a += 1
a
8
x = 6
y = 5
x,y = 6,5
x
6
y
5
-a
-8
a
8
a = -a
a
-8
a = 4
b = 3
a > b
True
a < b
False
a <= b
False
b = 4
a <= b
True
a >= b
True
a == b
True
a != b
False
a
4
b
4
b = 5
a < 10
True
>>> b > 1
True
>>> a < 10 b > 1
SyntaxError: invalid syntax
>>> a < 10 and b > 1
True
>>> a < 10 or b > 1
True
>>> a < 10 or b > 10
True
>>> a < 10 and b > 10
False
>>> a > 10 and b > 10
False
>>> result = true
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    result = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> result
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> not result
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    not result
NameError: name 'result' is not defined
>>> a = 3
>>> b = 4
>>> a *= 2
>>> b -= a
>>> print(a > b and b > 0)
False
>>> a
6
>>> b
-2
