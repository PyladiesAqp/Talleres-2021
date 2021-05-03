# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:32:14 2021

@author: Naomi Ceder
"""

03.2.1 Numbers

>>> x = 5 + 2 - 3 * 2    
>>> x
1
>>> 5 / 2
2.5               #1
>>> 5 // 2
2                  #2
>>> 5 % 2
1
>>> 2 ** 8
256
>>> 1000000001 ** 3
1000000003000000003000000001    #3

>>> x = 4.3 ** 2.4
>>> x
33.13784737771648
>>> 3.5e30 * 2.77e45   
9.695e+75
>>> 1000000001.0 ** 3 
1.000000003e+27

>>> (3+2j) ** (2+3j)
(0.6817665190890336-2.1207457766159625j)
>>> x = (3+2j) * (4+9j)
>>> x                               #1
(-6+35j)
>>> x.real 
-6.0
>>> x.imag 
35.0

>>> round(3.49)       #1
3
>>> import math
>>> math.ceil(3.49)  #2
4

>>> x = False
>>> x
False
>>> not x
True
>>> y = True * 2    #1
>>> y
2

03.2.2 Lists

>>> x = ["first", "second", "third", "fourth"]
>>> x[0]                   #1 
'first'                    #1
>>> x[2]                   #1
'third'
>>> x[-1]               #2 
'fourth'                #2 
>>> x[-2]               #2
'third'                 #2
>>> x[1:-1]             #2
['second', 'third']           #3
>>> x[0:3]                    #3 
['first', 'second', 'third']  #3
>>> x[-2:-1]                  #3
['third']                     #3
>>> x[:3]                     #3
['first', 'second', 'third']  #4
>>> x[-2:]                    #4
['third', 'fourth']           #4

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[1] = "two"
>>> x[8:9] = []
>>> x
[1, 'two', 3, 4, 5, 6, 7, 8]
>>> x[5:7] = [6.0, 6.5, 7.0]          #1
>>> x
[1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]
>>> x[5:] 
[6.0, 6.5, 7.0, 8]

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(x)
9
>>> [-1, 0] + x                     #1
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.reverse()                    #2 
>>> x
[9, 8, 7, 6, 5, 4, 3, 2, 1]

03.2.3. Tuples

>>> x = [1, 2, 3, 4]
>>> tuple(x)
(1, 2, 3, 4)


>>> x = (1, 2, 3, 4)
>>> list(x)
[1, 2, 3, 4]

03.2.4. Strings

>>> x = "live and     let \t   \tlive"
>>> x.split()
['live', 'and', 'let', 'live']
>>> x.replace("    let \t   \tlive", "enjoy life")
'live and enjoy life'
>>> import re                         #1
>>> regexpr = re.compile(r"[\t ]+")
>>> regexpr.sub(" ", x)
'live and let live'


>>> e = 2.718
>>> x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
>>> print("The constant e is:", e, "and the list x is:", x)   #1
The constant e is: 2.718 and the list x is: [1, 'two', 3, 4.0,
['a', 'b'], (5, 6)]
>>> print("the value of %s is: %.2f" % ("e", e))    #2
the value of e is: 2.72

03.2.5 Dictionaries

>>> x = {1: "one", 2: "two"}
>>> x["first"] = "one"     #A
>>> x[("Delorme", "Ryan", 1995)] = (1, 2, 3)   #1
>>> list(x.keys())
['first', 2, 1, ('Delorme', 'Ryan', 1995)]
>>> x[1]
'one'
>>> x.get(1, "not available")
'one'
>>> x.get(4, "not available")         #2
'not available'

03.2.6 Sets

>>> x = set([1, 2, 3, 1, 3, 5])   #1
>>> x
{1, 2, 3, 5}    #2
>>> 1 in x                 #3      
True
>>> 4 in x               #3 
False
>>>

