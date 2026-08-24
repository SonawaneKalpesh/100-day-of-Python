import csv

# Write CSV file
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerow(["Rahul", 21, 85])
    writer.writerow(["Priya", 22, 92])
    writer.writerow(["Amit", 20, 78])

print("CSV file created successfully!")


# Read CSV file
print("\n--- Student Data ---")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)