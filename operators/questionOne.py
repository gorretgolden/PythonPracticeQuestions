# Write a python program that takes in a student name, class, and section. It should also take in five subject marks of the students and find the total mark and percentage.
# Display a result in such a way that their name, class, section, and percentage are printed

student_name = input("Enter your  name:")
student_class = input("Enter your class:")
semester = input("Enter your semester:")
python = float(input("Enter your Python mark:"))
java = float(input("Enter your Java mark:"))
javasacript = float(input("Enter your Javascript mark:"))
php = float(input("Enter your Php  mark:"))
react = float(input("Enter your React mark:"))

total_mark = python + java + javasacript + php + react
percentage = (total_mark / 5)

print("\n---------Output-------------")
print("Student Name:", student_name)
print("Class:", student_class)
print("Semester:", semester)
print(f"Dear {student_name} you are in {student_class} and in {semester}, your percentage mark is {percentage} %")
