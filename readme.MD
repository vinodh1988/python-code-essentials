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


## global and local variables

By default any variable declared within a function acts as local variable
even though same variable available outside the function

Yet python facilitates developer to refer to the global version of the variable
by using a key word called global

## *args and **kwargs

1. use * if you are not sure about no of arguments, while passing parameters
we can send as many values as we want . the parameters are collected as a tuple

2. similarly if you want to pass keyword arguments and collect it as dictionary
in the function definition use **

## Callback functions

 A function which is passed as parameter to another function is called as callback function

 it is called so because it meant to be called back the function that is being called
 currently

 # Closures

 In most functional languages , defining a function within a function is possible

 and the inner function always can access variable which are in the context of outer function

 and those variables are accessible in the inner function even after outer function
 finished execution

 and outer function cannot access variables which are part of inner function


 ### nonlocal keyword

 withing in the innerfunction if you do not want to create a variable in local scope
 if you want to create in outer function scope use nonlocal keyword

 ### map, reduce and filter

 #### Map 
   
   * processing each list item individually
   *  for each item processed we return a result
   *  for a map operation no of inputs = no of outputs
   *  that is if n items is process the result would also be n items

#### Filter
  
   * process each item individually
   * for each item processed we need to return a result[ only true or false]
   * for a filter no of inputs >= no of outputs
   * filter will remove the processed individual elements which returned false 

#### reduce

   * Process each item individually but we always take result of last iteration
   * input for callback will have two parameter two-> current element one-> Previous iteration result
   * for n inputs there will only one final output

### Modules in python

In python context, a module in nothing collection of python files
in python files, we will have variables, functions, classes
we can import these variables, functions and classes in other modules
So Module is a logical context to group functions, variables and classes