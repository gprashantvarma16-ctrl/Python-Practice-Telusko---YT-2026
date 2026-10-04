Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
set1 = {23,56,78,21,56}
set1
{56, 21, 78, 23}
21 in set1
True
22inset2
SyntaxError: invalid syntax
22 in set1
False
>>> len(set1)
4
>>> type(set1)
<class 'set'>
>>> set2 = {}
>>> type(set2)
<class 'dict'>
>>> set2 = set()
>>> type(set2)
<class 'set'>
>>> set2 = set('abcdmnop')
>>> set3 = set('aeioupd')
>>> set2
{'n', 'c', 'p', 'a', 'o', 'b', 'd', 'm'}
>>> set3
{'p', 'e', 'u', 'a', 'i', 'o', 'd'}
>>> set1 - set2
{56, 21, 78, 23}
>>> set2 - set3
{'n', 'c', 'b', 'm'}
>>> set2 | set3
{'n', 'c', 'p', 'e', 'u', 'a', 'i', 'o', 'b', 'd', 'm'}
>>> set2 & set3
{'p', 'a', 'd', 'o'}
>>> set2 ^ set3
{'c', 'u', 'e', 'b', 'n', 'i', 'm'}
>>> tup = (45)
>>> type(tup)
<class 'int'>
>>> tup = (45,)
>>> type(tup)
<class 'tuple'>
>>> 
>>> 
>>> a = set("python")
>>> b = set("telusko")
>>> print(a&b)
{'t', 'o'}
