# ============================================================
# Dictionary Tricks
# ============================================================

def f(x):
    return {
        'a': 1,
        'b': 2
    }.get(x, 9)    # 9 will be returned default if x is not found

f('a')
# 1
f('b')
# 2
f('c')
# 9
f('fuck')
# 9

d = {2:3, 1:89, 4:5, 3:0}
dict(sorted(d.items()))

# {1: 89, 2: 3, 3: 0, 4: 5}


# ============================================================
# String Similarity
# ============================================================

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
  
>>> similar("Apple","Appel")
0.8
>>> similar("Apple","Mango")
0.0  


# ============================================================
# Args & Kwargs Basics
# ============================================================

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# First argument : Hello
# Next argument through *argv : Welcome
# Next argument through *argv : to
# Next argument through *argv : GeeksforGeeks
  
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
myFun(first='Geeks', mid='for', last='Geeks')
# first == Geeks
# mid == for
# last == Geeks

def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
# args: ('geeks', 'for', 'geeks')
# kwargs: {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)        
foo()     
# TypeError: foo() missing 1 required positional argument: 'required'
foo('hello')
# hello
foo('hello',1,2,3)
# hello
# (1, 2, 3)
foo('hello',1,2,3,key1='value',key2=999)
# hello
# (1, 2, 3)
# {'key1': 'value', 'key2': 999}

# args 其實就是 list, kwargs 其實就是 dict, 新增新資料的方式相同
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )


# ============================================================
# Args & Kwargs in Classes
# ============================================================

class car():
    def __init__(self,*args): # args receives unlimited no. of arguments as an array
        self.speed = args[0] 
        self.color = args[1]
                 
#creating objects of car class (args)        
audi=car(200,'red')
bmw=car(250,'black')
mb=car(190,'white')
    
print(audi.color)
print(bmw.speed)
# red
# 250

class car():
    def __init__(self,**kwargs): # kwargs receives unlimited no. of arguments as an array
        self.speed = kwargs['s'] 
        self.color = kwargs['c']
                 
#creating objects of car class (kwargs)
audi=car(s=200,c='red')
bmw=car(s=250,c='black')
mb=car(s=190,c='white')
    
print(audi.color)
print(bmw.speed)
# red
# 250


# ============================================================
# Unpacking with * and **
# ============================================================

def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
# 6

def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))
# 45

# merging_lists
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
# [1, 2, 3, 4, 5, 6]

# merging_dicts
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# string_to_list
a = [*"RealPython"]
print(a)
# ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
