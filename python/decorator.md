# Decorators
## A decorator is a function that runs some other function by adding some more functionalities
**Introduction source**: https://www.programiz.com/python-programming/decorator

## example:
``` python
def func1(): #A sample function
	print("Monday")
#func2 is a decorator
def func2(func1): #It takes a function
	print("today is") #it adds a functionality
	return func1 #It returns that function
a = func2(func1)
a() #a is now decorated
```

Above can be written better as:
``` python
def func2(func1):
	print("today is")
	return func1
@func2
def func1():
	print("Monday")
func1()
```
Remember flask used decorators (@app.route())? It makes much more sense now!

