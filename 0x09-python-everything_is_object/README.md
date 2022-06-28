#alx higher level programming
## 0x09. Python - Everything is object


# Background context
Everything is an object. Python works differently with different types of objects. Example: Modifying a variable: 

>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>

Here b remains as the initial value of a , even thought a has changed.

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>

l is a list, it is assigned to m (making it a list). A change in either, is reflected on both. This concept is known as aliasing, l and m refer to the same object (the list).

This projects shows different ways python deals with objects.

# Tasks

# 0-answer.txt
Write the name of the function in the file, without ().

# 1-answer.txt
Write the name of the function in the file, without ().

# 2-answer.txt
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

# 3-answer.txt
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

# 4-answer.txt
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

# 5-answer.txt
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

# 6-answer.txt
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

#7-answer.txt
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

# 8-answer.txt
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

# 9-answer.txt
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

# 10-answer.txt
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
