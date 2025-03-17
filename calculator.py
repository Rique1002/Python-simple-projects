print(" Basic Calculator ")
operation = input ("Pick operation: (Addition, Subtraction, Division, Multiplication, Modulo, Exponential)")
first_number = input ("Enter your first number: ")
second_number = input ("Enter your second number: ")


def addition(first_number, second_number):
    print(first_number + second_number)

def subtraction(first_number, second_number):
    print(first_number - second_number)

def division(first_number, second_number):
    print(first_number / second_number)

def multiplication(first_number, second_number):
   print(first_number * second_number)

def modulo(first_number, second_number):
    print(first_number % second_number)

def exponential(first_number, second_number):
    print(first_number ** second_number)
    
def subscribe():
    print("Subscribe for Premium!")

if  operation == "Addition":
    addition(int(first_number), int(second_number))
elif operation == "Subtraction":
    subtraction(int(first_number), int(second_number))
elif operation == "Division":
    division(int(first_number), int(second_number))
elif operation == "Multiplication":
    multiplication(int(first_number), int(second_number))
elif operation == "Modulo":
    modulo(int(first_number), int(second_number))
elif operation == "Exponential":
    exponential(int(first_number), int(second_number))
else:
    subscribe()