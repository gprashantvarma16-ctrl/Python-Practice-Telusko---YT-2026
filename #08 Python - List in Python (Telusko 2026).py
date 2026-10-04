Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1 = 65
num1
65
nums = [45,87,21,24,99]
nums
[45, 87, 21, 24, 99]
nums[0]
45
nums[5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nums[5]
IndexError: list index out of range
nums[4]
99
nums[-1]
99
nums [-1]
99
nums[2:4]
[21, 24]
nums[2:]
[21, 24, 99]

names = ['navin','harsh','kiran']
names
['navin', 'harsh', 'kiran']
mix = ['navin',67,6.5]
mix
['navin', 67, 6.5]
mix = [nums, names]
mix
[[45, 87, 21, 24, 99], ['navin', 'harsh', 'kiran']]
mix[0]
[45, 87, 21, 24, 99]
len(mix)
2
mix[0][0]
45
mix[1:1]
[]
mix[1][2]
'kiran'
mix = nums+names
mix
[45, 87, 21, 24, 99, 'navin', 'harsh', 'kiran']

nums = [23,56,14,36,45]
names = ['navin','harsh','kiran']
mix = nums + names
mix
[23, 56, 14, 36, 45, 'navin', 'harsh', 'kiran']
nums.append(33)
nums
[23, 56, 14, 36, 45, 33]
nums.count(14)
1
nums.count(15)
0
nums.insert(1,55)
nums
[23, 55, 56, 14, 36, 45, 33]
nums.remove(56)
nums
[23, 55, 14, 36, 45, 33]
nums.pop(4)
45
nums
[23, 55, 14, 36, 33]

nums.pop()
33
>>> nums
[23, 55, 14, 36]
>>> del nums[2:4]
>>> nums
[23, 55]
>>> nums.extend([44,56,11,99])
>>> nums
[23, 55, 44, 56, 11, 99]
>>> nums[2:4] = [54,76]
>>> nums
[23, 55, 54, 76, 11, 99]
>>> nums.reverse()
>>> nums
[99, 11, 76, 54, 55, 23]
>>> nums.sort()
>>> nums
[11, 23, 54, 55, 76, 99]
>>> min(nums)
11
>>> max(nums)
99
>>> sum(nums)
318
>>> min(names)
'harsh'
>>> max(names)
'navin'
>>> sum(names)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sum(names)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> 
>>> a = [33, 76, 24, 56]
>>> b = ["navin", "kiran", "harsh"]
>>> print((a[:2] + b[1:])[-3])
76
