paragraph = input("Enter a paragraph: ").lower()

words = paragraph.split()

unique_words = set(words)

print("\nUnique words:")
print(unique_words)

print("Total unique words:", len(unique_words))