Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = {0:34,1:35,2:67,3:8}
data[2]
67
data = {'kiran':34, 'sushil':35, 'harsh':67, 'navin':8}
data[1]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    data[1]
KeyError: 1
data['harsh']
67
data.get('harsh')
67
data.get(1)
print(data.get(1))
None
data.get('kiran', 'not found')
34
data.get('gaurav', 'not found')
'not found'
data = {'kiran':34,'sushil':35,'harsh':67,'navin':8,'harsh':34}
data
{'kiran': 34, 'sushil': 35, 'harsh': 34, 'navin': 8}
keys = {'navin', 'hitesh', 'shramik'}
values = [34,64,87]
dict1 = dict(zip(keys,values))
dict1
{'hitesh': 34, 'shramik': 64, 'navin': 87}
data
{'kiran': 34, 'sushil': 35, 'harsh': 34, 'navin': 8}
data.pop('navin')
8
data
{'kiran': 34, 'sushil': 35, 'harsh': 34}
del dta['sushil']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del dta['sushil']
NameError: name 'dta' is not defined. Did you mean: 'data'?
del data['sushil']
data
{'kiran': 34, 'harsh': 34}

data = {'js':'vscode', 'python':['vscode','pycharm'], 'java':{'core':'vscode','spring':'iij'}\}
...         
SyntaxError: unexpected character after line continuation character
>>> data = {'js':'vscode', 'python':['vscode','pycharm'], 'java':{'core':'vscode','spring':'iij'}}
...         
>>> data['python']
...         
['vscode', 'pycharm']
>>> data['python']
...         
['vscode', 'pycharm']
>>> data['python'][0]
...         
'vscode'
>>> dta['java']
...         
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dta['java']
NameError: name 'dta' is not defined. Did you mean: 'data'?
>>> data['java']
...         
{'core': 'vscode', 'spring': 'iij'}
>>> data['java']['spring']
...         
'iij'
>>> 
>>> 
>>> 
>>> 
>>> data = {'harsh': ['java','python','AI'], 'navin': {'frontend': 'React', 'backend': 'spring'}, 'kiran': ('JS', 'Flask')}
...         
>>> print(data['navin']['backend'])
...         
spring
>>> print(data['navin']['frontend'])
...         
React
