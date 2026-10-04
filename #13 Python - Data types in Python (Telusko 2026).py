Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x = 10
type(x)
<class 'int'>
pi = 3.14
type(pi)
<class 'float'>
c = 6+8j
c
(6+8j)
type(c)
<class 'complex'>
a = 2
b = 3
c = complex(a,b)
c
(2+3j)
k = int(pi)
type(k)
<class 'int'>
k
3
p = float(k)
type(p)
<class 'float'>
p
3.0
name = 'navin'
type(name)
<class 'str'>
a = 7
b = 6
greater = b > a
greater
False
greater = b < a
greater
True
is_it = True
is_it
True
k = int(true)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    k = int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
k = int(True)
k
1
k = int(False)
k
0
result
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    result
NameError: name 'result' is not defined
print(result)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined
>>> result = None
>>> print(result)
None
>>> l = [4,5,6,7]
>>> typr(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    typr(l)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(l)
<class 'list'>
>>> t = (4,5,6,7)
>>> type(t)
<class 'tuple'>
>>> s = {4,5,6,4}
>>> type(s)
<class 'set'>
>>> r = range(0,10)
>>> type(r)
<class 'range'>
>>> list(r)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> set(r)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> r
range(0, 10)
>>> set(r)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> set(range(2,11,2))
{2, 4, 6, 8, 10}
>>> 
>>> 
>>> 
>>> ls = [4,5,6]
>>> tup = (7,8)
>>> x = list(tup)
>>> print(x)
[7, 8]
