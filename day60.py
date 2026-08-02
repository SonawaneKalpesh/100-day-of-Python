student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

inverted = {}

for key, value in student_marks.items():
    inverted[value] = key

print("Original Dictionary:")
print(student_marks)

print("\nInverted Dictionary:")
print(inverted)