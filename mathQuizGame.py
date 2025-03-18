print("Welcome to Math Quiz Game!")
start = input("Type START: ")

def quizOne():  
    print("What is 12 multiplied by 5?") 
    i = 0

    while i < 4:
        answerOne = input("Answer: ")
        if answerOne == "60" :
            print("Nice!")
            break
        else:
            print("Try Again!")

        i = i+1
    else:
        print("You lose!")
    

while start == "START":
    quizOne()
    break
else: 
    print("Run the program again")



    


    
