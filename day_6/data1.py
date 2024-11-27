import random
import faker
import pandas as pd

# Initialize the Faker library to generate random names
fake = faker.Faker()

# Function to generate random student data
def generate_student_data(num_students=1000):
    student_data = []
    for _ in range(num_students):
        name = fake.name()  # Random name
        age = random.randint(15, 18)  # Random age between 15 and 18
        height = random.randint(150, 190)  # Random height in cm between 150 and 190
        weight = random.randint(45, 90)  # Random weight in kg between 45 and 90
        
        student_data.append([name, age, height, weight])
    
    # Create a DataFrame for easy viewing or export to CSV
    df = pd.DataFrame(student_data, columns=["Name", "Age", "Height (cm)", "Weight (kg)"])
    return df

# Generate the data
students_df = generate_student_data(1000)

# Print the first 10 records (for preview)
print(students_df.head(10))

# Optionally, you can save the DataFrame to a CSV file
students_df.to_csv('students_data.csv', index=False)
