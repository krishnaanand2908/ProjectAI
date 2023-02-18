from AiClass import AI
import os
import time
import fontstyle as fnt

parth = AI("PARTH", "Mr. Krishna Anand", "Personal Artificial Rocking and Trustworthy Helper")
def main():
    parth.wishMe()
    while True:
        query = parth.takeCommand().lower()
        if "essay" in query or "wikipedia" in query:
            parth.wikisearch(query)
            
        elif "open" in query:
            try:
                parth.webOpen(query)
            except:
                pass
            
        elif "play music" in query:
            parth.playMusic("PARTH_music")
            
        elif "search google" in query:
            parth.webSearch(query)
            
        elif 'who am i' in query or 'who i am' in query:
            print(fnt.apply(f"You are my {parth.name}"))
        
        elif "maya" in query:
            print(fnt.apply(
                f'M.A.Y.A. is like my elder sister. I used to call her didi.', 'yellow/bold/underline'))
            parth.speak('MAYA is like my elder sister. I used to call her DI,DI...') 
            
        elif "clear" and "screen" in query:
            os.system('cls')
            print(fnt.apply('"Successfully cleared the screen"', 'green/bold'))
            parth.speak('Successfully cleared the screen')
            time.sleep(2)
            os.system("cls")
            
        elif 'introduce yourself' in query:
            parth.introduction()
            
        elif 'open calculator' in query:
            print(fnt.apply('Opening manual calculator...', 'blue/bold'))
            parth.speak('Opening manual calculator...')
            parth.openCalc()
            
        elif 'change' in query.lower() and 'name' in query:
            parth.changeName()
            
        elif "the time" in query:
            parth.getTime()
        
        elif "the date" in query or "date" in query:
            print(fnt.apply(parth.date, "blue/bold"))
            parth.speak(parth.date)
        
        elif "shutdown" in query or "bye" in query:
            parth.shutdown()
            
        elif "pause" in query:
            print(fnt.apply(f"Paussed {parth.ainame}", "red/bold"))
            input(fnt.apply("Press 'Enter' to resume: ", "red/bold"))
            print(fnt.apply(f"\"Resummed\"", "green/bold"))
            
        else:
            praise_words = ['good', 'well done', 'very good',
                        'best', 'nice', 'amazing', 'excellent']
            not_good_words = ['worst', 'bad', 'worse',
                          'shut up', 'get lost', 'very bad', 'not good']
            for x in praise_words:
                if x in query:
                    print(fnt.apply(f'Thank You {parth.name}\n:)', 'yellow/bold/'))
                    parth.speak(f'Thank You {parth.name}\n:)')
                    break
            

            for y in not_good_words:
                if y in query: 
                    print(
                        fnt.apply(f'I am really sorry {parth.name}\n:(', 'black/bold/'))
                    parth.speak(f'I am really sorry {parth.name}\n:(')
                    break

            if (x in query) or (y in query):
                pass
            elif 'give' in query:
                query = query.replace('give', '')
                print(fnt.apply(f'You give{query}', 'purple/bold'))
                parth.speak(f'You give {query}')
            # if (x not in praise_words) or (y not in not_good_words):
            else:
                print(fnt.apply('Command not recognized!', 'red/bold'))
                parth.speak('Command not recognized!')
main()