# Check whether a string is a palindrome.
word = "racecar"
if word == word[::-1]:
    print(f"'{word}' is a palindrome!")
else:
    print("Not a palindrome!")
    
# Check whether two strings are anagrams.
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Str1 and str2 are anagrams")
else:
    print("Not anagrams")
    
# Count the frequency of each character.
text = "Python"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1
print(frequency)

# Find the longest word in a sentence.
sentence = "Python is an amazing programming language"
words = sentence.split()
longest_word = words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)

# Find the shortest word.
sentence = "Python is an amazing programming language"
words = sentence.split()
shortest_word = words[0]
for word in words:
    if len(word)<len(shortest_word):
        shortest_word = word
print("The Shortest word is:", shortest_word)

# Remove duplicate characters.
text = "hello world"
result = ""
for char in text:
    if char not in result:
        result = result + char
print("Without duplicates:", result)

# Reverse the order of words.
sentence = "Python is very fun"
words = sentence.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)
print(result)

# Count the number of words.
sentence = "Python is an amazing programming language"
words = sentence.split()
word_count = len(words)
print("Number of words:", word_count)

# Find the first non-repeating character.
text = "swiss"
for char in text:
    if text.count(char) == 1:
        print("The first non-repeating character is:", char)
        break
    
# Replace every vowel with *.
word = "shahiddinshaik"
vowels = "aeiouAEIOU"
for char in vowels:
    word = word.replace(char, "*")
print(word)