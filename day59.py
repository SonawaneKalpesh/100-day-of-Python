students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}

max_key = max(students, key=students.get)

print("Key with maximum value:", max_key)
print("Maximum value:", students[max_key])