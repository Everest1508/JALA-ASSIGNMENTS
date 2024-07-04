# Write a program to print your name

print("Ritesh")

# Write a program for a single line comment and multi-line comments

print("Single Line Comment")
# Single Line Comment

print("Multi-line Comment")
'''This is
Multi line Commnet'''

# Define variables for different Data Types and print on the console

var_int=34
print("Type of var_int : ",type(var_int))
var_bool=True
print("Type of var_bool : ",type(var_bool))
var_float=34.2
print("Type of var_float : ",type(var_float))
var_string="Ritesh"
print("Type of var_string : ",type(var_string))

# Define the Local and Global Variables with the same name and print both variables
# Understand the scope of the varibles

var = 'global var'
def localVar():
    var='local var'
    print(var)

print('Global var : ',var)
localVar()
print("Value of Var after Function : ",var)

# Global keyword for modify the global var

def modify():
    global var
    var = 'updated'

modify()
print("Var value : ", var)