marks = [65, 72, 80, 55, 90]

average = sum(marks) / len(marks)

print("Average marks:", average)

if average >= 75:
    print("Good performance")
elif average >= 50:
    print("Average performance")
else:
    print("Needs improvement")