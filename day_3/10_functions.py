#functions: 

# define a function
def print_codanics():
    print("Codanics is a great company!")
    
# function call
print_codanics()

#using parameters

text="codanics is great company"
def prt_codanics(text):
    print(text)
    
prt_codanics(text)

def school_education(age):
    if age==5:
        print("you are in kindergarten")
    elif age>5:
        print("hammad should go to higher school")
    elif age<5:
        print("Hammad is still a baby")
age=int(input("please enter Hammad Age:"))
school_education(age)


# use of return statement

def future_age(age):
    new_age=age+20
    return  new_age

print(future_age(18))