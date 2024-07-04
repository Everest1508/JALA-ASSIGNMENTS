# Write a function to add integer values of an array

from copy import copy

from cv2 import sort


int_arr = [76,98,56,99,45,34,32,56]

# Write a function to calculate the average value of an array of integers

sum = 0

for i in int_arr:
    sum += i

avg = sum/len(int_arr)

print("Average : ",avg)

# Write a program to find the index of an array element

num = 45

print("Index of 45 is ",int_arr.index(45))

# Write a function to test if array contains a specific value

print("45 is present") if i in int_arr else print("45 is not present") 

# Write a function to remove a specific element from array

int_arr.remove(num)
print(int_arr)

# Write a function to copy an array to another array

copy_arr = int_arr.copy()
print(copy_arr)

#  Write a function to insert an element at a specific position in the array

index = int(input("Enter a index : "))
element = int(input("Enter a element : "))

int_arr.insert(index, element)
print(int_arr)

# Write a function to find the minimum and maximum value of an array

greatest = int_arr[0]
lowest = int_arr[0]

for i in int_arr:
    if greatest <= i:
        greatest = i
    if lowest >= i:
        lowest = i

print('Greatest number : ',greatest)
print('Lowest number : ',lowest)

# Write a function to reverse an array of integer values

int_arr.reverse()
print("Reverse Array", int_arr)

# Write a function to find the dublicate values of an array

dub_arr=[]

for i in range(len(int_arr)):
    for j in range(i+1,len(int_arr)):
        if int_arr[i] == int_arr[j]:
            dub_arr.append(int_arr[j])

print("Dublicate values : ",dub_arr)

# Write a function to find the comman values in an array

com_arr=set()
int_arr2 = [23,54,60,45,35,56,64]
for i in int_arr:
    for j in int_arr2:
        if i == j:
            com_arr.add(i)

print("Comman values : ",com_arr)

# Write a method to remove duplicate elements from an array

arr_mod = set(int_arr)

print("Array after removing dublicate values : ", list(arr_mod))

# Write a method to find the second largest number in an array

int_arr.sort()

print("Second largest value : ",int_arr[-2])

# Write a method to find number of even number and odd numbers in an array

even_no = 0
odd_no = 0

for i in int_arr:
    if i % 2 == 0:
        even_no += 1
    else:
        odd_no += 1

print("Even numbers : ",even_no)
print("Odd numbers : ",odd_no)

# Write a function to get the difference of largest and smallest value

print("Difference of largest and smallest value : ",int_arr[-1] - int_arr[0])