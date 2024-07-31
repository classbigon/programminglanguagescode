import csv

#This open the csv file and read the contents of the file
with open('students.csv', 'r') as file:
    grades = []
    csv_reader = csv.reader(file)
    next(csv_reader) # jumps over the header file
    for row in csv_reader:
      grades.append([float(grade) for grade in row[1:]]) 

#This calculates the mean grades of each student
mean_grades = [round(sum(grade)/12) for grade in grades]
print(mean_grades[1:])

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
    return(degrees)


students_grades = grades
student_mean_grades = mean_grades
degrees = award_degrees(mean_grades)
for i, degree in enumerate(degrees):
        print(f"Student {i+1}: Mean Grade = {mean_grades[i]:.2f}, Degree = {degree}")
     


















    
# with open('overall.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Name', 'student_mean_grade', 'Student_degree'])
#     for student_mean_grade in enumerate(student_mean_grades):
#           csv_writer.writerow([f'Student {i+1}', student_mean_grade, degree])