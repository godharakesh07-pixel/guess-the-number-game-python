import random
secret_number=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Enter number:"))
    attempts+=1
    #if attempts>=5:
           # print("you entered maximum 5 times !try again")
            #break
    if guess>secret_number:
        print("To heigh!")
    elif guess<secret_number:
        print("to low")
    else:
        #guess==secret_number
        print("congratulations")
        print("you guessed the number in ",attempts,"attempts")
        
        break
