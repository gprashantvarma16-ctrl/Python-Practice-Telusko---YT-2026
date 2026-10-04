Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
45
45
navin
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    navin
NameError: name 'navin' is not defined
num = 8
num
8
'navin'
'navin'
print(navin)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(navin)
NameError: name 'navin' is not defined
print('navin')
navin
print('navin telusko')
navin telusko
print('navin's telusko')
      
SyntaxError: unterminated string literal (detected at line 1)
>>> print('navin's telusko'')
...       
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> print("navin's telusko")
...       
navin's telusko
>>> print('navin\'s "telusko"')
...       
navin's "telusko"
>>> pint('navin\'s telusko')
...       
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pint('navin\'s telusko')
NameError: name 'pint' is not defined. Did you mean: 'print'?
>>> print('navin\'s telusko')
...       
navin's telusko
>>> 'navin'
...       
'navin'
>>> 'navin ' 'navin '
...       
'navin navin '
>>> 'navin ' * 10
...       
'navin navin navin navin navin navin navin navin navin navin '
>>> print('c:\users\navin')
...       
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> print('c:\\users\\navin')
...       
c:\users\navin
>>> 
>>> 
>>> print("path: C:\\new_folder\\notes\\\"day1\".txt")
...       
path: C:\new_folder\notes\"day1".txt
