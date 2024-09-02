Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [ ]
li.index(1,2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    li.index(1,2)
ValueError: 1 is not in list
li.inset(1,2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    li.inset(1,2)
AttributeError: 'list' object has no attribute 'inset'. Did you mean: 'insert'?
li.insert(1,2)
li
[2]
li.index(2)
0
a = {}
type (a)
<class 'dict'>
a = [1]
a[1] = 2
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[1] = 2
IndexError: list assignment index out of range
a = {  }
a[1] = 2
>>> a
{1: 2}
>>> a [1] =3
>>> a
{1: 3}
>>> a [3] = 4
>>> a[4] = 5
>>> a[5] =7
>>> a
{1: 3, 3: 4, 4: 5, 5: 7}
>>> 
>>> a.values()
dict_values([3, 4, 5, 7])
>>> a.get()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
>>> a.keys()
dict_keys([1, 3, 4, 5])
>>> a.items()
dict_items([(1, 3), (3, 4), (4, 5), (5, 7)])
>>> a.update[(6,8)]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.update[(6,8)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> a.update([(6,8)])
>>> a
{1: 3, 3: 4, 4: 5, 5: 7, 6: 8}
>>> a.get(3)
4
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop(6)
8
>>> a
{1: 3, 3: 4, 4: 5, 5: 7}
>>> a.popitem()
(5, 7)
