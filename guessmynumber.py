import random

while True:
        try:
            randomNumber = random.randint(0,6)
            userInput = input("Keep a one number : ")
            predictNumber =int(userInput)
            if 0 <= predictNumber <= 6:
                if(predictNumber>randomNumber):
                    print("Predicted value is greater than the random number.")
                elif(randomNumber>predictNumber):
                    print("Predicted value is smaller than the random number.")
                else:
                    print("Your predict : " , predictNumber , "= Random number : " ,randomNumber)
                    break
            else:
                print("Your value is outside the valid range.")
            
        except ValueError:
            print("Please enter a valid integer.")


    
