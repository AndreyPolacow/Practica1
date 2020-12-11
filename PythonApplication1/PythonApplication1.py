groupmates = [
  {
    "name": "Максим",
    "surname": "Петров",
    "exams": ["Философия","ИС","АиГ"],
    "marks": [4, 3, 5]
  },
  {
    "name": "Алексей",
    "surname": "Попов",
    "exams": ["Философия","ИС","АиГ"],
    "marks": [3, 2, 3, 3, 3]
  },
  {
    "name": "Михаил",
    "surname": "Табала",
    "exams": ["КТП","ЭЭиС","Психология"],
    "marks": [3, 5, 4, 3, 5]
  },
  {
    "name": "Тимур",
    "surname": "Ахламов",
    "exams": ["Философия","ИС","АиГ"],
    "marks": [5, 5, 5, 4, 5]
  },
  {
    "name": "Егор",
    "surname": "Гирамович",
    "exams": ["Философия","ИС","АиГ"],
    "marks": [5, 5, 5, 5, 5]
  }
]

def count_mark(students,mark):
    print ("name".ljust(15), "surname".ljust(8), u"exams".ljust(8), u"marks".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(8), str(student["exams"]).ljust(8), str(student["marks"]).ljust(20))

need = int(input('Average score :'))

count_mark(groupmates,need)