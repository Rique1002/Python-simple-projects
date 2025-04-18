class Student:
    def __init__(self, name, course, year,section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print("  Name   : "+ self.name)
        print("  Course : "+ self.course)
        print("  Year   : "+ self.year)
        print("  Section: " + self.section)



listOfStudents = []

while True:
      print("\n")
      sName = input("Enter student's name:  ")
      sCourse = input("Enter course:  ")
      sYear = input("Enter year:  ")
      sSection = input("Enter section:  ")
      sOne = Student(sName,sCourse,sYear,sSection)
      listOfStudents.append(sOne)
      print(" ")
      createStudent = input("Would you like to enter new Student? (yes/no): ")
      print(" ")
      if createStudent == 'Yes' or  createStudent=='yes': pass
      else: 
           print("Thank you for visiting. Here are the registered student/s: ")
           break
      

i = 1
for student in listOfStudents:
    print(" ")
    print("Student " + str(i))
    print("\n")
    student.introduce()
    i += 1