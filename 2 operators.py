# Write a function for arithmatic operation

a = 34
b = 245
add = a + b
sub = b - a
div = b / a
mult = a * b
print("Addition : ",add)
print("Subtraction : ",sub)
print("Multiplication : ",mult)
print("Division : %.2f"%(div))

# Write a Method for increment and decrement operators
a = 1
while a<=10:
    print(a,end=" ")
    a += 1  # Increment by 1
print()
a = 10
while a >= 1:
    print(a,end=" ")
    a -= 1 # Decrement by 1

# Write a program to find the two numbers equal or not

a = 9
b = 5

if a == b:
    print("Both numbers are equal")
elif a != b:
    print("Both numbers are Different")

# Program for relational operators

a = 32
b = 64

print(a < b) # less than
print(a > b) # greater than
print(a == b) # equal to
print(a != b) # not equal to
print(a <= b) # less than equal to
print(a >= b) # greater than equal to

# Print the larger and smaller number

num1 = 98
num2 = 78

if num1 > num2:
    print("{0} is greater than {1}".format(num1,num2))
elif num1 < num2:
    print("{1} is greater than {0}".format(num1,num2))
else:
    print("{0} is equal to {1}".format(num1,num2))