def map_grade_to_students(student_data,grade_data):
    student_dict = {student["id"]: student for student in student_data }

    for student in student_dict.values():
        student["grades"] = []


    for grade in grade_data:
        student_id = grade.get("student_id") 
        if student_id in student_dict:
            student_dict[student_id]["grades"].append({
                "subject": grade["subject"],
                "marks": grade["marks"]
            })   

    return list(student_dict.values())




student_data = [
    {'id': 'STU001', 'name': 'Alice', 'class': '10A'},
    {'id': 'STU002', 'name': 'Bob', 'class': '10B'},
    {'id': 'STU003', 'name': 'Charlie', 'class': '10A'},
    {'id': 'STU004', 'name': 'David', 'class': '10C'}
]
grades_data = [
    {'student_id': 'STU001', 'subject': 'Math', 'marks': 85},
    {'student_id': 'STU002', 'subject': 'Science', 'marks': 90},
    {'student_id': 'STU001', 'subject': 'English', 'marks': 88},
    {'student_id': 'STU004', 'subject': 'Math', 'marks': 92}
]

result = map_grade_to_students(student_data, grades_data)
for i in result:
    print(i)