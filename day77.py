text = input("Enter something to save: ")

with open("data.txt", "w") as file:
    file.write(text)

print("Data saved successfully!")