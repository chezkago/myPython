#Python basic calculator 
class Operations:
    def addition(self, num1, num2):
        print(f"{num1} + {num2} = {num1+num2}")
        print("#########")
    def substraction(self, num1, num2):
        print(f"{num1} - {num2} = {num1-num2}")
        print("#########")
    def multiplication(self, num1, num2):
        print(f"{num1} * {num2} = {num1*num2}")
        print("#########")
    def division(self, num1, num2):
        print(f"{num1} / {num2} = {num1/num2:.2f}")
        print("#########")

if __name__ == "__main__":
    print("Welcome to Calculator.py!")
    
    correct_operation = True
    while(correct_operation == True): #Loop until proper operation chosen
        input_operation = input("Choose an operation(+,-,*,/, stop): ")
        operation = input_operation.lower()
        if operation == "+":
            print("---------")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter first number: "))
            print("---------")
            myadd = Operations()
            myadd.addition(num1, num2)
        elif operation == "-":
            print("---------")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter first number: "))
            print("---------")
            mysub = Operations()
            mysub.substraction(num1, num2)
        elif operation == "*":
            print("---------")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter first number: "))
            print("---------")
            mymul = Operations()
            mymul.multiplication(num1, num2)
        elif operation == "/":
            print("---------")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter first number: "))
            print("---------")
            mymul = Operations()
            mymul.division(num1, num2)
        elif operation == "stop":
            print("Calculator Shutting Down, Bye Bye!")
            print("#########")
            correct_operation = False
        else:
            print("Invalid Input, Try again")