Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={3,7.8,"java",6+9j,True,False}
type(a)
<class 'set'>
print(a)
{False, True, (6+9j), 3, 7.8, 'java'}
#add
a={4,7,9,10,20}
a.add(50)
a
{50, 4, 20, 7, 9, 10}
#issubset()
a={2,3,4,5,6,7,8}
b={8,9,10,11,12}
a.issubset(b)
False
a={1,2,3,4,5,6,7}
b={4,5,6,7}
b.issubset(a)
True
a.issubset(b)
False
#superset()
a={1,2,3,4,5,6,7}
b={4,5,6,7}
a.issuperset(b)
True
a={1,3,4,5,6}
b={5,6}
b.issuperset(a)
False
a.issuperset(b)
True
#union()
a={4,5,6,7,8,9,10,11}
b={5,6,7,8,9,10,11,12}
a.union(b)
{4, 5, 6, 7, 8, 9, 10, 11, 12}
>>> #intersection()
>>> a=8,9,10,11,12,13,14}
SyntaxError: unmatched '}'
>>> a={8,9,10,11,12,13,14}
>>> b={2,3,4,5,6,7,8,9,10}
>>> a.intersection(b)
{8, 9, 10}
>>> #difference()
>>> a={2,4,6,8,10,12,14}
>>> b={10,12,14,16,18}
>>> a.difference(b)
{8, 2, 4, 6}
>>> b.difference(a)
{16, 18}
>>> #update()
>>> a={1,3,5,7,9,11,13}
>>> b={5,6,7,8,9,10,11}
>>> a.update(b)
>>> a
{1, 3, 5, 6, 7, 8, 9, 10, 11, 13}
>>> b
{5, 6, 7, 8, 9, 10, 11}
>>> b.update(a)
>>> b
{1, 3, 5, 6, 7, 8, 9, 10, 11, 13}
>>> b
{1, 3, 5, 6, 7, 8, 9, 10, 11, 13}
>>> #symmetric difference
>>> a={4,5,6,7,8,9,10}
>>> b={1,2,3,4,5,6,7,8}
>>> a.symmetric_difference(b)
{1, 2, 3, 9, 10}
>>> b.symmetric_difference(a)
{1, 2, 3, 9, 10}
>>> #difference update
>>> a={2,4,6,8,10,12,14}
>>> b={1,2,3,5,7,8,10,12}
>>> a.difference_update(b)
>>> a
{4, 6, 14}
>>> a
{4, 6, 14}
>>> b.difference_update(a)
>>> b
{1, 2, 3, 5, 7, 8, 10, 12}
