with open("data.txt", "r") as file:
    lines = file.readlines()

longest_line = max(lines, key=len)

print("Longest line:")
print(longest_line.strip())

print("Length:", len(longest_line.strip()))