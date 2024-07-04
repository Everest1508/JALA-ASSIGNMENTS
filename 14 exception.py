# 1. Arithmetic Exception without exception handling
# result = 10 / 0  

# 2.  try-catch block
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")

# 3. call without try block
def method_with_exception():
    raise ValueError("This is a custom exception")

# Uncomment the next line to see the exception without try block
# method_with_exception()

# 4. multiple catch blocks
try:
    value = int("abc")
except ValueError as ve:
    print(f"ValueError: {ve}")
except TypeError as te:
    print(f"TypeError: {te}")

# 5. user message
try:
    raise Exception("This is a custom exception with a message")
except Exception as e:
    print(f"Exception: {e}")

# 6. user define exception
class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom exception")
except CustomException as ce:
    print(f"CustomException: {ce}")

# 7. finally block
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")
finally:
    print("Finally block executed")

# 8. Arithmetic Exception
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")

# 9. FileNotFoundException
# Uncomment the next line to see the exception
# with open("file.txt", "r") as file:
#     content = file.read()

# 10. ClassNotFoundException
# Uncomment the next line to see the exception
# obj = MyClass()  # Assuming MyClass is not defined

# 11. IOException
# Uncomment the next line to see the exception
# with open("/dev/full", "w") as file:
#     file.write("This will raise an IOException")

# 12. NoSuchFieldException
class ExampleClass:
    field = "Example Field"

try:
    value = ExampleClass.field1
except AttributeError as ae:
    print(f"NoSuchFieldException: {ae}")
