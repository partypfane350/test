import datetime
from time import sleep
import json
import os

daten = {} 

if os.path.exists("daten.json"):
    with open("daten.json", "r") as f:
        daten = json.load(f)
        
class FOX:
    def __init__(self):
        pass
    
    #  Daten speichern und löchen
    def speichern(self, txt):
        if txt.startswith("speicher "):
            try:
                rest = txt[len("speicher "):]
                key, value, anzahl = rest.split(" ", 2)
                try:
                    self._anzahl = int(anzahl)
                except ValueError:
                    return "Fehler: Anzahl muss eine Zahl sein."
                    
                daten[key] = {"value": value, "anzahl": anzahl}

                with open("daten.json", "w") as f:
                    json.dump(daten, f, indent=4)
                    return f"Gespeichert: {key} -> {value}, Anzahl: {anzahl}"
            except ValueError:
                return "Fehler: Bitte im Format 'speicher <key> <value> <anzahl>' eingeben."
                    
            return "Kein Speicherbefehl."
        elif txt.startswith('delete '):
            key = txt[len('delete '):]
            if key in daten:
                del daten[key]
                with open("daten.json", "w") as f:
                    json.dump(daten, f, indent=4)
                return f"Gelöscht: {key}"
            else:
                return f"Fehler: Schlüssel '{key}' nicht gefunden."
        
        elif txt.startswith('data'):
            return json.dumps(daten, indent=4) if daten else "Keine Daten gespeichert."

        
    #  Begüßung und verabschiedung           
    def greet(self):
        return "Hallo!"

    def farewell(self):
        return "Auf Wiedersehen!"


    #  Zeit und Datum
    def time(self):
        T = datetime.datetime.now()
        return f"Aktuell ist {T.hour}:{T.minute}" 


    def datum(self):
        D = datetime.datetime.now()
        return f"Heute ist der {D.day}.{D.month}.{D.year}"

                
    #  Rechner
    def rechner(self, user):
        try:
            result = eval(user)
            return f"Das Ergebnis ist {result}"
        except Exception as ex:
            return f"Ihre rechnung hat ein fehlern: '{user}' -> {ex}" 
        
    def rechnung(self, txt):
        zeichen = "+-*/()"
        return any(c.isdigit() for c in txt) and any(c in txt for c in zeichen)


#  Handlungen
def handle(input):
    txt = input.lower()   
    fox = FOX()  
    if txt.startswith('hallo') or txt.startswith('hi'): return fox.greet()
    elif txt.startswith('bye') or txt.startswith('tschüss'): return fox.farewell()    
    elif txt.startswith('time') or txt.startswith('zeit'): return fox.time()   
    elif txt.startswith('datum') or txt.startswith('date'): return fox.datum() 
    elif fox.rechnung(txt): return fox.rechner(txt)
    elif txt.startswith('speicher ') or txt.startswith('delete '):return fox.speichern(txt)
    elif txt.startswith('data'): return fox.speichern(txt)
    else: return "Entschuldigung, das habe ich nicht verstanden."


def main():
    while True:
        sleep(0.1)
        user = input('user: ')
        
        if user.lower() in ['e', 'q']:
            print("Programm beendet.")
            break 
        
        print(f'FOX: {handle(user)}')  
        
if __name__ == "__main__":
    main()