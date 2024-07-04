students = {
    "101": "Arjun",
    "102": "Priya",
    "103": "Rahul",
    "104": "Ananya",
    "105": "Kiran"
}

students["106"] = "Vidya"
students["103"] = "Updated Rahul"

print("Student with ID 104:", students["104"])

classes = {
    "ClassA": {"101": "Arjun", "102": "Priya"},
    "ClassB": {"201": "Rahul", "202": "Ananya"},
    "ClassC": {"301": "Kiran", "302": "Vidya"}
}

for class_name, class_students in classes.items():
    print(f"\nClass: {class_name}")
    for student_id, student_name in class_students.items():
        print(f"Student ID: {student_id}, Name: {student_name}")

print("\nKeys in students:", list(students.keys()))

if "102" in students:
    del students["102"]
    print("Value with ID 102 deleted.")
else:
    print("Value with ID 102 not found.")

print("\nUpdated students:", students)
