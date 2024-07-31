import csv

# Step 2: Define a function to read grades from a CSV file
def read_grades_from_csv(file_path):
    grades = []
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            grades.append([float(grade) for grade in row[1:]])  # Assuming the first column is student name or ID
    return grades

# Step 3: Calculate the mean grade for each student
def calculate_mean_grades(grades):
    mean_grades = [round(sum(student_grades)) / len(student_grades) for student_grades in grades]
    return mean_grades

# Step 4: Award degrees based on mean grade
def award_degrees(mean_grades):
    degrees = []
    for grade in mean_grades:
        if grade >= 70:
            degrees.append('First Class')
        elif grade >= 60:
            degrees.append('Second Class Upper')
        elif grade >= 50:
            degrees.append('Second Class Lower')
        elif grade >= 40:
            degrees.append('Pass')
        else:
            degrees.append('Fail')
    return degrees

# Step 5: Main function to tie everything together
def process_student_grades(file_path):
    grades = read_grades_from_csv(file_path)
    mean_grades = calculate_mean_grades(grades)
    degrees = award_degrees(mean_grades)
    for i, degree in enumerate(degrees):
        print(f"Student {i+1}: Mean Grade = {mean_grades[i]:.1f}, Degree = {degree}")

# Assuming the CSV file is named 'student_grades.csv' and located in the same directory as this script
if __name__ == "__main__":
    process_student_grades('students.csv')
