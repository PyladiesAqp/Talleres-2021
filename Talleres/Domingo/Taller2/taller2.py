# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:58:01 2021

@author: Naomi Ceder
"""
#03.2.1 Numbers

>>> x = 5 + 2 - 3 * 2    
>>> x
---
>>> 5 / 2
---            #1
>>> 5 // 2
---               #2
>>> 5 % 2
---
>>> 2 ** 8
---
>>> 1000000001 ** 3
---    #3

>>> x = 4.3 ** 2.4
>>> x
---
>>> 3.5e30 * 2.77e45   
---
>>> 1000000001.0 ** 3 
---

>>> (3+2j) ** (2+3j)
---
>>> x = (3+2j) * (4+9j)
>>> x
---
>>> x.real 
---
>>> x.imag 
---

>>> round(3.49)       
---
>>> import math
>>> math.ceil(3.49)  
---

>>> x = False
>>> x
----
>>> not x
---
>>> y = True * 2    
>>> y
---


#03.2.2 Lists

>>> x = ["first", "second", "third", "fourth"]
>>> x[0]                    
---              
>>> x[2]                   
---
>>> x[-1]               
---                 
>>> x[-2]               
---               
>>> x[1:-1]             
---          
>>> x[0:3]                    
---  #3
>>> x[-2:-1]                  
---                    
>>> x[:3]                     
---  #4
>>> x[-2:]                    
---           

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[1] = "two"
>>> x[8:9] = []
>>> x
----
>>> x[5:7] = [6.0, 6.5, 7.0]          
>>> x
---
>>> x[5:] 
---

>>> x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(x)
---
>>> [-1, 0] + x                     
---
>>> x.reverse()                     
>>> x
---
#03.2.3. Tuples

>>> x = [1, 2, 3, 4]
>>> tuple(x)
---


>>> x = (1, 2, 3, 4)
>>> list(x)
---

#03.2.4. Strings

>>> x = "live and     let \t   \tlive"
>>> x.split()
---
>>> x.replace("    let \t   \tlive", "enjoy life")
---



>>> e = 2.718
>>> x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
>>> print("The constant e is:", e, "and the list x is:", x)  
---
>>> print("the value of %s is: %.2f" % ("e", e))   
---

#03.2.5 Dictionaries

>>> x = {1: "one", 2: "two"}
>>> x["first"] = "one"     #A
>>> x[("Delorme", "Ryan", 1995)] = (1, 2, 3)   
>>> list(x.keys())
---
>>> x[1]
---
>>> x.get(1, "not available")
---
>>> x.get(4, "not available")         
---

#03.2.6 Sets

>>> x = set([1, 2, 3, 1, 3, 5])
>>> x
---  
>>> 1 in x                    
---
>>> 4 in x               
---
>>>





