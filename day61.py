data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

unique = {}
seen = set()

for key, value in data.items():
    if value not in seen:
        unique[key] = value
        seen.add(value)

print("Original Dictionary:")
print(data)

print("\nDictionary after removing duplicate values:")
print(unique)