#Exercise 3: Print characters present at an even index number

word = input('Enter word:')
print("Original string:", word)

size = len(word)

print("printing only even index character.")
for i in range(0, size -1, 2):
    print("index[", i, "]", word[i])
    