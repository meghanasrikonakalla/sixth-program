Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[4,5.6,"Meghana",5+9j,True,False]
print(a)
[4, 5.6, 'Meghana', (5+9j), True, False]
type(a)
<class 'list'>
c=[60]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("html")
a
['python', 'java', 'c', 'c++', 'html']
a.append("css","js")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.append("css","js")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["css","js")]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a.append(["css","js"])
a
['python', 'java', 'c', 'c++', 'html', ['css', 'js']]
#extend
a=["apple","banana","grapes"]
a.extend(["mango","kiwi"])
a
['apple', 'banana', 'grapes', 'mango', 'kiwi']
#insert
a.insert(1,"berry")
a
['apple', 'berry', 'banana', 'grapes', 'mango', 'kiwi']
#index
a.index("grapes")
3
a.index("mango")
4
#sort
a=["black","white","red"]
a.sort()
a
['black', 'red', 'white']
b=["hyd","bng","vja"]
b.sort()
b
['bng', 'hyd', 'vja']
c=[7,89,8,5,2,0,9]
c.sort()
c
[0, 2, 5, 7, 8, 9, 89]
#reverse
a=["c","ds","ml","ai"]
a.reverse()
a
['ai', 'ml', 'ds', 'c']
a=[100,40,65,33]
a.reverse()
a
[33, 65, 40, 100]
#pop
a=["html","css","js","bs"]
a.pop()
'bs'
a
['html', 'css', 'js']
>>> a.pop("js")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a.pop("js")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(2)
'js'
>>> a
['html', 'css']
>>> #remove
>>> a.remove("css")
>>> a
['html']
>>> #clear
>>> a=["code","course","codegnan"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b
[]
>>> b.append("meghana")
>>> b
['meghana']
>>> #copy
>>> a=["hi","hello","how"]
>>> a.copy()
['hi', 'hello', 'how']
>>> b=a.copy()
>>> b
['hi', 'hello', 'how']
>>> #length
>>> c="hello"
>>> len(c)
5
>>> d=["hello"]
>>> len(d)
1
>>> a=["hi","are","you"]
>>> len(a)
3
>>> #count
>>> a.count("how")
0
>>> a.count("are")
1
