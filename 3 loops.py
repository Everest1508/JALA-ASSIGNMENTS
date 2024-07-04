# Write a program to print "Bright IT Career" ten times using for loop

for _ in range(10):
    print("Bright IT Career")

# Write a program to print 1 to 20 numbers using the while loop

num = 1
while num <= 20:
    print(num, end=" ")
    num += 1
print()

# Program to equal operator and not equal operators

a = 43
b = 42

print(a == b)
print(a != b)

# Write a program to print the odd and even numbers

print("Even numbers : ",end="")
for i in range(1,31):
    if i % 2 == 0:
        print(i , end=" ")
print()
print("Odd numbers : ",end="")
for i in range(1,31):
    if i % 2 == 0:
        print(i , end=" ")
print()
# Write a program to print largest number among three

a,b,c = 23,53,22

if a > b and a > c:
    print("{0} is greatest number".format(a))
elif b > a and b > c:
    print("{0} is greatest number".format(b))
else:
    print("{0} is greatest number".format(c))

# Write a program to print even numbers between 10 to 20 using while

a = 10

while a <=20:
    if a % 2 == 0:
        print(a,end=" ")
    a+=10
print()

# Write a program to print 1 to 10 using the do-while loop
a = 1
while True:
    if a > 10:
        break
    else:
        print(a,end=" ")
        a += 1
print()

# Write a program to find armstrong numbers or not

num = 371
cal = 0
pow = len(str(num))
for i in str(num):
    cal += int(i)**pow
if str(cal) == str(num):
    print("{0} is Armstrong number".format(num))
else:
    print("{0} is not Armstrong number".format(num))

# Write a program to find prime or not.
n = 7
flag = True
if n <= 1:
    flag = False
else:
    for i in range(2, n):
            if n % i == 0:
                flag = False
                break

print("{0} is prime number".format(n)) if flag == True else print(
    "{0} is not prime number".format(n))

# Write a program to palindrome or not.

string = 'string'
if string == string[::-1]:
    print("{0} is palindrome string".format(string))
else:
    print("{0} is not palindrome string".format(string))

# Program to check whether number is odd or even using switch

num = 75

if num % 2 == 0:
    print("Number is Even")
elif num % 2 != 0:
    print("Number is Odd")

# Print gender (Male/Female) program according to given M/F using switch

gender = 'M'

if gender == 'M':
    print("MALE")
elif gender == 'F':
    print("FEMALE")
