# Different ways creating a string.

str1 = 'new'
print(str1)

str2 = "new"
print(str2)

str3 = '''World'''
print(str3)

str4 = """It's Multi-line
String"""
print(str4)

# Concatenating two strings using + operator
str5 = str1 + str3
print("Concatenated two different strings : ",str5)

# Finding the length of the string.
print("length of the string:",len(str1))

# Searching in strings using index()
str3 = 'python'
str1 = 'on'
str2 = 'py'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))

# Matching a String Against a Regular Expression With matches().
import re
Substr = 'Pain'
str6 = 'Pain once said- I Want You To Feel Pain, To Think About Pain, To Accept Pain, To Know Pain.'
print(re.match(Substr,str6))
print()

# Comparing strings.
str8 = 'Sasuke uchiha'
str1 = 'Naruto uzumaki'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()

# startsWith(), endsWith().
string = 'Kakashi Hatake'
print(string.startswith("Kakashi"))
print(string.endswith("take"))
print()

# Trimming strings with strip().
str7 = 'Hello World hi'
print(str7.strip("hi"))
print()

# Replacing characters in strings with replace()
string = 'Hi World'
print(string.replace("Hi","Hello"))
print()

# Splitting strings with split()
str9 = 'hi-hello-bye'
print(str9.split("-"))
print()

# Converting integer objects to Strings.
numb = 10
numb1 = str(numb)
print(numb1)
print(type(numb1))

print()
# Converting to uppercase and lowercase.
string = 'hello'
string1 = 'WORLD'
print(string.upper())
print(string1.lower())