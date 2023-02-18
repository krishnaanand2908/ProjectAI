import random
import os
import fontstyle
import pyttsx3




def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 210)
    engine.say(text)
    engine.runAndWait()


def speakFast(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty("rate", 240)
    engine.say(text)
    engine.runAndWait()


def guess_game_v5():
    os.system("CLS")
    num = random.random()
    guess = 1
    print(fontstyle.apply(
        f"You have to guess a rational number between 0 to 1\nYou will only get 9 chances!\n Enjoy :-)", "Cyan/bold"))
    speak(f"You have to guess a rational number between 0 to 1, You will only get 9 chances!, ENJOY!")

    while (guess <= 9):
        guessed_number = float(
            input(fontstyle.apply("Enter the number:\n", "Purple/bold")))

        if guessed_number == -29001:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", 'white/bold'))
            print(fontstyle.apply(
                f'The number you have to guess is {num}', 'purple/bold/underline'))

        elif guessed_number == -29002:
            guess -= 2
            print(fontstyle.apply(f"Turns remaining: {9-guess}", 'white/bold'))

        elif guessed_number == -29003:
            guessed_number = random.random()
            print(fontstyle.apply(f"Turns remaining: {9-guess}", 'white/bold'))
            print(fontstyle.apply('Rational Number is reassined!', ' red/bold'))

        elif int(guessed_number) == num:
            congo = fontstyle.apply(
                "Congratulations!\nYou have guessed the number!", "yellow/green/underline/italic")
            print(congo)
            speak("Congratulations!!!... You have guessed the number!!!...")
            print((fontstyle.apply(f"You took {guess} turns!", "red/bold")))
            speak(f"You took {str(guess)} turns!...")

            print(fontstyle.apply(
                "Thank Mr. Krishna Anand for creating me...", 'yellow/bold'))
            speak("Thank Mr. Krishna Anand for creating me.")

            guess = guess + 1
            break

        elif int(guessed_number) < num:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", "white/bold"))

            smaller = fontstyle.apply(
                "The number you have entered is smaller than the number to be guessed!", "bold/italic/blue")
            print(smaller)
            speakFast(
                "The number you have entered is smaller than the number to be guessed!")
            guess = guess + 1
            continue

        elif int(guessed_number) > num:
            print(fontstyle.apply(f"Turns remaining: {9-guess}", 'white/bold'))

            greater = fontstyle.apply(
                "The number you have entered is greater than the number to be guessed!", "bold/italic/red")
            print(greater)
            speakFast(
                "The number you have entered is greater than the number to be guessed!")
            guess = guess + 1
            continue

        else:
            exit()

    if guess > 9:
        lose = fontstyle.apply("Game Over!", "bold/italic/yellow")
        print(lose)
        speak("GAME... OVER...")
        print(fontstyle.apply(f"The number was {num}", "blue/bold/underline"))
        speak(f"The number was {str(num)}...")
        print(fontstyle.apply('You LOOSE! HAHA', 'red/bold'))
        speak('You Loose... HAHA...')


def main_game_():
    os.system('cls')
    print(fontstyle.apply("Gathering Information...", "blue/bold"))
    speak("Gathering Information...")
    print(fontstyle.apply("Opening Guess Game version 8.0", "blue/bold"))
    speak("Opening Guess Game version 8.0...")
    print(fontstyle.apply("Clearing THE SCREEN...", 'blue/bold'))
    speak("Clearing the SCREEN...")

    os.system("CLS")

    print(fontstyle.apply("HI, it's PARTH!", 'blue/bold'))
    speak("HI, It's PARTH!...")
    choice_colour = fontstyle.apply(
        "Press Enter to continue or Q to quit!", "bold/italic/green/underline")
    print(choice_colour)
    speak("Press Enter to continue or Q to quit!... ")
    choice = input()
    choice = choice.upper()
    if choice == "":
        try:
            guess_game_v5()

        except ValueError:
            print(fontstyle.apply(
                'An Error occured||Please Try Again', 'red/bold/underline'))
            speak("AN ERROR OCCURED... PLEASE TRY AGAIN...")
            speak('Press Enter to reset the game. No other choice. HAHA...')
            temp = input(fontstyle.apply(
                'Press Enter to reset the game[No Other Choice HAHA]', 'purple/bold/underline'))

    elif choice == "Q":
        bye = fontstyle.apply(
            "|---Please come again soon---|", "bold/italic/white/red_bg")
        print(bye)
        speak("Please Come Again Soon...")

    else:
        print()
