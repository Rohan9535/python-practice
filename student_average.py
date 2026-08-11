name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = float(input("Enter mark: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Student:", name)
print("Average marks:", average)