print("welcome to QUIZY QUIZ!")
playing=input("Do you want to start the game? ")

if playing.lower()!="yes":
    quit()

print("Great! Lets begin the fun!!!")
print("You will have 5 Questions in this game.\nYou will be rewarded 1 point for every correct answer.")
score=0

answer = input("1.Does India have a National Sport?...yes or no? ")
if answer.lower()=="no":
    print("Correct!\n Your next question.")
    score+=1
else:
    print("Opps..Incorrect\n India doesn't have a National Sport ")

answer = input("2.How many teeth does an adult human have? ")
if answer.lower()=="32":
    print("Correct!\n Your next question.")
    score+=1
else:
    print("Opps..Incorrect\n The correct answer is 32 ")

answer = input("3.What are animals that eat both meat and plants called? ").lower()
if answer=="omnivores":
    print("Correct!\n Your next question.")
    score+=1
else:
    print("Opps..Incorrect\n The correct answer is omnivores ")

answer = input("4.What is the largest internal organ in the human body? ")
if answer.lower()=="liver":
    print("Correct!\n Your next question.")
    score+=1
else:
    print("Opps..Incorrect\n The correct answer is liver ")

answer = input("5. C programs are convrted into the machine language with the help of? ")
if answer.lower()=="compilers":
    print("Correct!\n")
    score+=1
else:
    print("Opps..Incorrect\n The correct answer is compiler ")

print("You have attempted all the questions!\nYour score is " + str(score))