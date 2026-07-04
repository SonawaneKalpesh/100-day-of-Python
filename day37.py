word1 = input("Enter first word: ").lower().replace(" ", "")
word2 = input("Enter second word: ").lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")