# Define a static variable and access that through a class

class Stud:
    id = 1

print("var : ",Stud.id)

# Define a static variable and access that through a instance

obj = Stud()
print("var : ",obj.id)

# Define a static variable and change within the instance

obj.id = 2
print("var : ",obj.id)

# Define a static variable and change within the class

Stud.id = 6
print("var : ",Stud.id)
