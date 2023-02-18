import os
import fontstyle as fnt
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import random
import json
import requests
import time
import PyPDF2
import random_poem
import GuessGameV8_
import overloadgame
import rps
import superCalcy

class AI:
    day = int(datetime.datetime.now().day)  # defines day
    month = int(datetime.datetime.now().month)  # defines month
    year = int(datetime.datetime.now().year)  # defines year
    date = f'{month}-{day}-{year}'
    class NotASequenceError(Exception):
        "Raised when the given argument is not of a sequence"

    class FileAlreadyExistsError(Exception):
        "Raised when the file already exists"
        
    def __init__(self, aiName, aiCreater, aiFullForm) -> None:
        self.ainame = aiName
        self.aicreater = aiCreater
        self.aifullform = aiFullForm

    @classmethod
    def fromStr(cls, nameCommaOwnerCommaFullForm):
        """The function fromStr is a class method of class AI which will work as a constructor. To use this method you have to give it an argument in the form of a string separated by a comma "," and a space " ". The word on the left side of the comma "," and a space " " is the name of AI and the word on the right side of the comma "," and a space " " is the name of the creater of the AI. The last value of this string must be the full form of the ai. At the end this method returns the names and stored them in the variables ainame, aicreater and aifullform resptively.

        Args:
            nameCommaOwner (string):
                This argument must be separated by a comma and a space for successfull results without any errors. For example, let the ai's name be Jarvis, its creater's name be Stark and its full form  be 'Just A Rather Very Intellegent System'. In this case we should write "Jarvis, Stark, "Just A Rather Very Intellegent System".

        Returns:
            variables self.ainame and self.aicreater: Name of the AI, name of its creater and the ai's full form respetively.
        """
        ainame, aicreater, aifullform = nameCommaOwnerCommaFullForm.split(",")
        return cls(ainame, aicreater, aifullform)

    @staticmethod
    def speak(audio):
        '''
        This function will speak or rather pronounce the argument which you will give it.
        '''
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 198)
        engine.setProperty('voice', voices[0].id)

        engine.say(audio)
        engine.runAndWait()
    
    @staticmethod   
    def speakFast(audio):
        '''
        This function will speak or rather pronounce the argument which you will give it. It it different from the speak funtion because this one speaks faster than the original speak funtnio.
        '''
        quickEngine = pyttsx3.init('sapi5')
        quickVoices = quickEngine.getProperty('voices')
        quickEngine.setProperty('rate', 230)
        quickEngine.setProperty('voice', quickVoices[0].id)

        quickEngine.say(audio)
        quickEngine.runAndWait()

    @staticmethod
    def takeCommand():
        """This functions gets input from the user in by his/her voice

        Returns:
            string: The return value, query, contains whatever the user has said when the program was taking input from him/her in the form of a string.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(fnt.apply('Listening...', 'blue/bold'))
            r.pause_threshold = 1
            r.energy_threshold = 400
            audio = r.listen(source)
            try:
                print(fnt.apply('Recognizing...', 'blue/bold'))
                query = r.recognize_google(audio, language='en-in')
                print(fnt.apply(f'User said: {query}', 'blue/bold'))
            except:
                print(fnt.apply(f'Can\'t Recognize! Say that again please!', 'blue/bold'))
                return (fnt.apply('An error occured...', 'red/bold'))
        return query
    
    def wishMe(self):
        day = int(datetime.datetime.now().day)  # defines day
        month = int(datetime.datetime.now().month)  # defines month
        year = int(datetime.datetime.now().year)  # defines year
        
        global date
        date = f'{month}-{day}-{year}'

        hour = int(datetime.datetime.now().hour)
        
        print(fnt.apply('What\'s your name user?', 'blue/bold'))
        AI.speak('What\'s your name user?...'); 
        self.name = AI.takeCommand()
        
        self.special_names = {"krishna anand":"Madhav", "shivraj anand":"Uncle Shiv", "vandana kumari":"Grand Ma"}
        
        if self.name.lower() in self.special_names.keys():
            self.name = self.special_names.get(self.name)
            print(fnt.apply("Special user detected!"))
            AI.speak("Special user detected...")
            
        if (hour >= 0 and hour < 12) or hour == 12:
            print(fnt.apply(f'Good Morning {self.name}', 'green/bold/underline'))
            AI.speak(f'Good Morning {self.name}')
        elif (hour > 12 and hour < 18):
            print(fnt.apply(f'Good Afternoon {self.name}', 'green/bold/underline'))
            AI.speak(f'Good Afternoon {self.name}')
        else:
            print(fnt.apply(f'Good Evening {self.name}', 'green/bold/underline'))
            AI.speak(f'Good Evening {self.name}')
        if day == 1 and month == 1:
            print(fnt.apply(f"Happy New Year {self.name}", 'purple/bold/underline'))
            
        print(fnt.apply('How may I help you?', 'blue/bold'))
        AI.speak('How may I help you?')
    
    def introduction(self):
        print(
            fnt.apply(f"Hi, it's {self.ainame}!", "cyan/bold")
        )
        AI.speak(f"Hi, it's {self.ainame}!")
        print(
            fnt.apply(f"{self.ainame} stands for {self.aifullform}.", "cyan/bold")
        )
        AI.speak(f"{self.ainame} stands for {self.aifullform}.")
        print(
            fnt.apply(f"I am an artificial intelligence developed by {self.aicreater}", "cyan/bold")
        )
        AI.speak(f"I am an artificial intelligence developed by {self.aicreater}")

    def changeName(self):
        print(fnt.apply('Forgotting name...', 'blue/bold'))
        AI.speak('Forgotting name...')
        print(fnt.apply('Tell me your name, user...', 'blue/bold'))
        AI.speak('Tell me your name, user...')    
        self.name = AI.takeCommand()
        
        if not self.name or self.name.isspace(): # if the name is repeating or if the name is empty
            print(fnt.apply('Invalid name. Please try again.', 'red/bold'))
            AI.speak('Invalid name. Please try again.')
            AI.changeName(self) # re-running the function
        else:
            if self.name in self.special_names.keys():
                self.name = self.special_names.get(self.name)
                print(fnt.apply('Name changed succesfully', 'green/bold'))
                AI.speak('Name changed succesfully')
                print(fnt.apply(f'Hi {self.name}', 'blue/bold'))
                AI.speak(f'Hi {self.name}')
    
    @staticmethod    
    def wikisearch(query):
        WIKI_SEARCH_OPTIONS = {"wikipedia":2, "essay":10}
        for key in WIKI_SEARCH_OPTIONS.keys():
            if key in query:
                query = query.replace(key)
                results = wikipedia.summary(query, sentences=WIKI_SEARCH_OPTIONS.get(key))
                break
        print(fnt.apply(results, "blue/bold"))
        AI.speak(results) if WIKI_SEARCH_OPTIONS.get(key) > 3 else AI.speakFast(results)
    
    @staticmethod   
    def webOpen(query):
        websites = {
            'youtube': 'www.youtube.com',
            'google': 'www.google.com',
            'replit': 'https://replit.com/~',
            'web code': 'https://replit.com/~',
            'stack overflow': 'stackoverflow.com',
            'whatsapp web': 'web.whatsapp.com',
            'chatGPT': 'chat.openai.com'
        }
        for website, url in websites.items():
            if f"open {website}" in query:
                print(fnt.apply(f"Opening {website}...", "green/bold"))
                AI.speak(f"Opening {website}")
                webbrowser.open_new(url)
    
    @staticmethod
    def webSearch():
        base_url = "https://www.google.com/search?q="
        print(fnt.apply("What should I search?", "blue/bold"))
        AI.speak("What should I search?")
        content = AI.takeCommand()
        webbrowser.open_new(base_url+content)
       
    @staticmethod 
    def playMusic(songsPath):
        songs = os.listdir(songsPath)
        index = random.randint(0, len(songs))
        os.startfile(songsPath, songs[index])
        
    @staticmethod
    def openFile(filePath):
        os.startfile(filePath)
    
    @staticmethod
    def getTime():
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        second = int(datetime.datetime.now().second)
        print(fnt.apply(f"The time is {hour}:{minute}:{second}"))
        AI.speak(f"The time is {hour} hours {minute} minutes and {second} seconds")
        if hour <= 12:
            if minute > 1:
                print(fnt.apply(f"It's {hour}:{minute} P.M."))
                AI.speak(f"It's {hour}:{minute} P.M.")
            else:
                print(fnt.apply(f"It's {hour}:{minute} A.M."))
                AI.speak(f"It's {hour}:{minute} A.M.")
        else:
            print(fnt.apply(f"It's {hour}:{minute} P.M."))
            AI.speak(f"It's {hour}:{minute} P.M.")
            
    def gameing(self):
        gamelist = ["GuessTheNumber", "RockPaperScissors"]
        print(fnt.apply("What game do you want to play?", "blue/bold"))
        AI.speak("What game do you want to play?")
        i = 1
        for game in gamelist:
            print(fnt.apply(f"{i} for {game}", "yellow/bold"))
            i=i+1
        gameChoice = int(input("--> "))
        os.system('cls')
        print(fnt.apply('Let\'s play a game!', 'blue/bold'))
        AI.speak('Let\'s play a game...')
        match gameChoice:
            case 1:
                print(fnt.apply('Choose your difficulty level.'))
                AI.speak('Choose your difficulty level.')
                print(fnt.apply(
                    'Enter 1 for easy mode, 2 for medium mode, 3 for hard mode, 4 for the impossible mode and 5 for the OVERLOAD difficulty!', 'cyan/bold'))
                AI.speak(
                    ('Enter 1 for easy mode 2 for medium mode 3 for hard mode 4 for the impossible mode and 5 for OVERLOAD difficulty!!!'))
                mode = int((input(fnt.apply('--->   ', 'blue/bold'))))
                match mode:
                    case 1:
                        print(fnt.apply('Downloading easy difficulty...', 'green/bold'))
                        AI.speak('Downloading easy difficulty...')
                        GuessGameV8_.main(100)
                    case 2:
                        print(fnt.apply('Downloading medium difficulty...', 'yellow/bold'))
                        AI.speak('Downloading medium difficulty...')
                        GuessGameV8_.main(250)
                    case 3:
                        print(fnt.apply('Downloading hard difficulty...', 'red/bold'))
                        AI.speak('Downloading hard difficulty...')
                        GuessGameV8_.main(500)
                    case 4:
                        print(fnt.apply(
                            'System Overloadd!\nDownloading Overload difficulty...', 'black/bold'))
                        AI.speak('System Overload! Downloading Overload difficulty...')
                        overloadgame.main_game_()
                    case _:
                        print(fnt.apply('Can you please stop bothering me?', 'red/bold'))
                        AI.speak('Can you please stop bothering me?')
                        print(fnt.apply('<(-_-)>/', 'red/bold'))
            case 2:
                rps.RPS()
            
    def openCalc(self):
        print(fnt.apply('Opening manual calculator...', 'blue/bold'))
        AI.speak('Opening manual calculator...')
        superCalcy.main_calcy()
        
    def repeat(self, query):
        print(fnt.apply(f'{query}', 'blue/bold'))
        query = query.replace('repeat', '')
        AI.speak(f'You said: {query}')
        
    @classmethod
    def shutdown(self):

        print(fnt.apply('Shutting down PARTH program...', 'red/bold'))
        AI.speak('Shutting down PARTH program...')
        print(fnt.apply(f'Bye {self.name}', 'blue/bold'))
        AI.speak(f'Bye {self.name}')
        print(fnt.apply('Deactivated', 'red/bold'))
        exit()
        
    @staticmethod
    def pdfMerge(pdfs):
        if (type(pdfs) == list) or (type(pdfs) == tuple) or (type(pdfs) == set):
            raise AI.NotASequenceError("AI.pdfMerge takes 1 argument pdfs which must be a sequence(list, tuple or set)")
        for pdf in pdfs:
             print(fnt.apply(f"{pdf}\n", "cyan/bold"))
        merger = PyPDF2.PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write("MergedFile.pdf")
        merger.close()
        print(fnt.apply("Operation Successfully Completed", "green/bold"))
    
    @staticmethod
    def mkfile(fileName, fileExtention, folderPath):
        file = fileName + "." + fileExtention
        folder = os.listdir(folderPath)
        if file in folder:
            raise AI.FileAlreadyExistsError(f"A file named '{file}' at '{folderPath}' already exists!")
        with open(f"{fileName}.{fileExtention}", "a") as f:
            f.write("This file is created by AI.mkfile function\n")
            
    @staticmethod
    def log_poem():
        poem = random_poem.get_poem(count=0.1)
        with open("AI_PoetryLog.txt", "a") as poetryLog:
            poetryLog.write(poem)
            poetryLog.write("\n_______________________________________________________")
            
        return poem
    
    @staticmethod
    def newsTimesOfIndia():
        url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d19f29ffa9a849dc819d5277b02f31ef"
        try:
            response = requests.get(url)
        except:
            AI.speak("Please check your internet connection")
            
        news = requests.get(url).text
        headlines = json.loads(news)
        articles = headlines['articles']
        i=1
        print(fnt.apply("Today's news headlines are as follows: ", "blue/bold"))
        for headline in articles:
            print(fnt.apply(headline['title'], "cyan/underline"))
            AI.speak(headline['title'])
            time.sleep(1)
            i+=1
        print(fnt.apply("Thankyou, have a nice day ahed! :) ", "blue/bold"))
        
    
if __name__ == '__main__':
    os.system("cls")
    poem = AI.log_poem()
    print(poem)
    AI.speakFast(poem)