# Python is a multi paradigm programming language

## python is popular functional way of coding

### Python is interpreted

Scripting/Interpreted usually will not data type specification

Same applies to python

## Python literals

String Literals = 'Raj' 'Rahul' "Rahul" <br/>
Boolean Literals = True False <br/>
Integer Literals = 234 35634 <br/>
Float Literals = 34.365 34356.3444 <br/>

## Arithmetic Operators

+, - , *, / , % , ** , //

## Relational Operators

>,<,>=,<=,!=,==

## Logical Operators
and, or  , not

## Bitwise operators

&,|,^,>>, << and ~

**Note:** No increment/Decrement operatore in python

## Python decision making and selection statements

if, elif and else keywords are used to make decision making in python <br/>

there is no switch statement supported 

**indentation plays a crucial role in decision making statements**

## Collections
#### lists

1. list is  mutable 
2. it is linear collection of elements
3. random access is possible 
4. it is ordered
5. enclosed with []

#### tuples

1. tuple is immutable
2. enclosed within ()
3. except for the immutability behavior is same as list

### set

1. it is unordered
2. set Cannot have duplicates
3. Set is mutable

### dictionary

1. Key value pairs collection
2. Keys are Unique


### in and not in operator

Used to check whether an element exists in list, tuple or set

### range function

has three form
1. range(upper)
2. range(lower,upper)
3. range(lower,upper,step)

### for loop
```
 for x in range(limit):
    #statements

```

```
lista=[1,2,3]

for x in lista:
   print(x)
```

### While loop

while condition:
    #statements

### pass keyword
 
 under an if or while statement if you dont have any statements to execute you can 
 use pass keyword

 ## Functions in python

 function syntax

 ```
   def funname(parameters):
        #statements
```

1. not mandatory to return a value
2. not mandatory to have parameters
3. by default if a function has no return statement we get None as the return value
4. Functions can be called with keyword parameters so that called no need to bother
   about positions
5. Functions can have default parameters
6. Functions cannot be overloaded
7. A variable can hold reference for a function
