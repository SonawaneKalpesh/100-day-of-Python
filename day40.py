text = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(text)):
    if i < len(text) - 1 and text[i] == text[i + 1]:
        count += 1
    else:
        compressed += text[i] + str(count)
        count = 1

print("Compressed string:", compressed)