import datetime
from time import sleep
import math

def greet():
    return "Hallo!"

def farewell():
    return "Auf Wiedersehen!"

def time():
    T = datetime.datetime.now()
    return f"Aktuell ist {T.hour}:{T.minute}"

def datum():
    D = datetime.datetime.now()
    return f"Heute ist der {D.day}.{D.month}.{D.year}"

def rechner(user):
    try:
        result = eval(user)
        return f"Das Ergebnis ist {result}"
    except Exception as ex:
        return f"Ihre rechnung hat ein fehlern: '{user}' -> {ex}" 
    

def rechnung(txt):
    zeichen = "+-*/()"
    return any(c.isdigit() for c in txt) and any(c in txt for c in zeichen)

def handle(input):
    txt = input.lower()
    
    if 'hallo' in txt or 'hi' in txt: return greet()   
    elif 'bye' in txt or 'tschüss' in txt: return farewell()    
    elif 'time' in txt or 'zeit' in txt: return time()   
    elif 'datum' in txt or 'date' in txt: return datum() 
    elif rechnung(txt): return rechner(txt)
    else: return "Entschuldigung, das habe ich nicht verstanden."

def main():
    while True:
        sleep(0.1)
        user = input('user: ')
        
        if user.lower() in ['e', 'q']:
            print("Programm beendet.")
            break 
        
        print('FOX: ' + handle(user))  
        
if __name__ == "__main__":
    main()