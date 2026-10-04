Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 5
a
5
b = 5
b
5
id(s)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    id(s)
NameError: name 's' is not defined
>>> id(a)
140724392486136
>>> id(b)
140724392486136
>>> b = 6
>>> id(b)
140724392486168
>>> k = 5
>>> b = 9
>>> id(k)
140724392486136
>>> id(b)
140724392486264
>>> 
>>> name = 'navin'
>>> name1 = 'navin'
>>> id(name)
2654957692192
>>> id(name1)
2654957692192
>>> a = 'My fav color is black'
>>> b = 'My fav color is black'
>>> id(a)
2654957826160
>>> id(b)
2654957825968
>>> a = 1000
>>> b = 1000
>>> id(b)
2654952986160
>>> id(a)
2654921846992
>>> 
>>> 
>>> 
>>> a = 'telusko'
>>> b = 'telusko'
>>> print(id(a) == id(b))
True
