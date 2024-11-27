x=10  #int
y=10.2 #float
z="hello"  #string

#implicit type conversion
x=x*y
print(type(x)) #output: <class 'float'>

x=5
y=6.5
x=x+y
print(type(x))  

#explicit type conversion
age=input("what is your age?")
print(type(age)) #output: <class 'str'>
age=int(age) 
print(type(age)) #output: <class 'int'>