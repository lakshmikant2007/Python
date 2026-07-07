#string is a data type that stores a sequence of character.


# user se input lena
text = input("Enter a string: ")

# print original string
print("Original string:", text)

# length of string
print("Length:", len(text))

# uppercase
print("Uppercase:", text.upper())

# lowercase
print("Lowercase:", text.lower())

# reverse string
print("Reversed:", text[::-1])

# check substring
sub = input("Enter substring to check: ")
if sub in text:
    print("Substring found")
else:
    print("Substring not found")
