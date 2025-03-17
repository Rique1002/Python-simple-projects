grade1 = input("Enter your Finance grade:")
grade2 = input("Enter your Programming grade:")
grade3 = input("Enter your Communication grade:")


gradeList = [grade1,grade2,grade3]
gradeLen = len(gradeList)



def averageChecker():
    sum = float(grade1) +  float(grade2) + float(grade3)
    average = float(sum)/float(gradeLen)
    print("Your average is: " + str(average))
   
    
    if average > 100 or average <= 50:
        print("Invalid Grade")
    
    elif average >= 98 and average <= 100:
        print("With Highest Honors")
    
    elif average >= 95 and average <= 97:
      print("With High Honors")
    
    elif average >= 94 and average <= 94:
      print("With Honors")
    
    elif average >= 75 and average <= 89:
        print("Passed")
    
    else: 
        print("Failed")


averageChecker()

