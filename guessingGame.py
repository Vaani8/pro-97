import random
number = random.randint(1,9)
chance = 0
print("GUESS A NUMBER ( BETWEEN 1 TO 9 )")
while chance < 5:
    guess = int(input("ENTER YOUR GUESS -> "))
    if(number == guess):
        print("CONGRATULATIONS ! YOU WON !")
        break
    elif(guess < number):
        print("YOUR GUESS IS TOO LOW . ENTER A NUMBER GREATER THAN " , guess)
    else:
        print("YOUR GUESS IS TOO HIGH . ENTER A NUMBER SMALLER THAN " , guess)
    chance +=1
if not chance < 5:
    print ("YOU LOSE !")