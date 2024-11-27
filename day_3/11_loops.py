# types of loop
# 1. for loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
    
text = "Hello, World!"

for char in text:
    print(char)
    
       # using range function
for i in range(5):  # This will iterate from 0 to 4
    print(f"Iteration {i}")

squares = [x ** 2 for x in range(10)]
print(squares)


student_grades = {
    'Alice': 90,
    'Bob': 85,
    'Charlie': 92
}

#Looping Through a Dictionary
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
# 2. while 
count = 1

while count <= 5:
    print(count)
    count += 1  # Increment the count
user_input = ""

while user_input.lower() != "exit":
    user_input = input("Type 'exit' to quit: ")
    print(f"You typed: {user_input}")
    
running = True

while running:
    user_input = input("Type 'stop' to end the loop: ")
    if user_input.lower() == 'stop':
        running = False  # Set the flag to False to stop the loop
    else:
        print(f"You typed: {user_input}")
# 3. nested loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Print a new line after each row





# 4. break and continue statement
# 5. pass statement