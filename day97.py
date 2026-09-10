import json

json_data = '''
{
    "name": "Rahul",
    "age": 21,
    "city": "Nashik",
    "skills": ["Python", "HTML", "SQL"]
}
'''

# Parse JSON string into Python dictionary
data = json.loads(json_data)

print("===== JSON DATA =====")
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])

print("\nSkills:")
for skill in data["skills"]:
    print("-", skill)

# Modify data
data["age"] = 22
data["skills"].append("JavaScript")

print("\n===== UPDATED DATA =====")
print(json.dumps(data, indent=4))