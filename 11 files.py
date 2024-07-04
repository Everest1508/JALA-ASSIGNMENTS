import os

# Read text
file_path = "sample.txt"
b_file_path = "binary_file.bin"


with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Write text

text_to_write = "Hello, this is a sample text."

with open(file_path, "w") as file:
    file.write(text_to_write)

# Read a file stream
with open(b_file_path, "rb") as file:
    byte_data = file.read()
    print(byte_data)


# random access
with open(b_file_path, "rb") as file:
    byte_data = file.read(1024)
    print(byte_data)

# seek()
index_to_seek = 1024

with open(b_file_path, "rb") as file:
    file.seek(index_to_seek)
    byte_data = file.read(1024) 
    print(byte_data)

# Check access

if os.access(file_path, os.R_OK):print("Read access granted.")
else:print("Read access denied.")

if os.access(file_path, os.W_OK):print("Write access granted.")
else:print("Write access denied.")