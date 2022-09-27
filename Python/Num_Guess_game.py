import random
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Game():
    number =random.randint(50,80)
    NO=number
    i=1
    print("\nguess  the number{range 50 to 80}: ")
    while(i<8):
        guess=int(input())
        if (guess == number):
            if(i==1):
                print("\t   **** WoW WONDERING ****\n")
                speak("wow WONDERING")
            elif(i==2):
                print("\t     **** Very NICE ****\n")
                speak("Very NICE")
            elif(i==3):
                print("\t    **** Beautiful ****\n")
                speak("Beautiful")
            elif(i==4):
                print("\t\t****GOOD****\n")
                speak(" Good ")
            
            print("\t\t************")
            print("\t\t  YOU WON")
            print("\t\t************")
            speak("you are won")
            break
        elif(guess>=(number+5)):
            print("you guessed too high")
            print("Guess Again:")
        elif(guess <= (number-5)):
            print("you guessed too low")
            print("Guess Again:")
        elif(guess <= (number+5) and  guess >=(number-5)):
            print("you closed to the ans.")
            print("Guess Again:")
        i=i+1
    if(i==8):
       print("\t\t_____________")
       print("\t\t You..Loss")
       print("\t\t_____________")
       speak("you loss")
       print("\n\tNO:",NO)
       
    Game()
speak("welcome to play")
print("_______PLAY______\n\n")
Game()