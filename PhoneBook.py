contacts = {
    "number":4,
    "students":
    [
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"Test Testovsky", "email":"test@example.com"},
        {"name":"John Doe", "email":"sarah@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])