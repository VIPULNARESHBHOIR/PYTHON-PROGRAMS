import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#function to speak something 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



# creating a function 
def Game():
    #making a list and taking a user input
    list1=["STONE","PAPER","SEASOR"]
    speak(list1)
    k=int(input("YOU:"))
    if (k>=3):
        exit()
    user=list1[k]
    print("USER:",user)

    #taking a computer input       
    rad=random.choice(list1)
    print("Comp:",rad)

    #declaring WINNER!
    if (user==rad):
        print("\t\t TIE")
        speak("tie")
    elif ((user=="STONE" and rad=="SEASOR") or (user=="SEASOR" and rad=="PAPER") or (user=="PAPER" and rad=="STONE") or ()):
        print("\t\t***YOU WIN***")
        speak("you won")
    else:
        print("\t\tYOU LOSS")
        speak("YOU loss")

    Game()

#importing random module
import random
print("\t\tclick: 0.STONE 1.PAPER 2.SEASOR::")
Game()