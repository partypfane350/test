import datetime
from time import sleep
import json
import os
from spiele import Ratespiel, schere_stein_papier

class FOX:
    def __init__(self, data_path="daten.json"):
        self.daten = {}
        self.commands = {
            self.speichern: ['speicher', 'save'],
            self.add: ['add'],
            self.delete: ['delete', 'del', 'löschen'],
            self.show_data:  ['data', 'daten'],
            self.greet: ['hallo', 'hi', 'hey'],
            self.farewell: ['bye', 'tschüss', 'auf wiedersehen'],
            self.time: ['time', 'zeit', 'uhr'],
            self.datum: ['datum', 'date'],
            self.spiele: ['lass spielen', 'spielen']
        }
        
        if os.path.exists(data_path):
            with open(data_path, "r") as f:
                self.daten = json.load(f)
          
#  handling
    def handle(self, input):
        self.txt = input.lower()
        return self.verteilungs_command()
 
    def verteilungs_command(self):
        for cmd, keywords in self.commands.items():
            if any(self.txt.startswith(k) for k in keywords):
                return cmd()
            elif any(c.isdigit() for c in self.txt) and any(c in self.txt for c in "+-*/()"):
                return self.rechner(self.txt)
        return "Unbekannter Befehl."
          
#  Daten
    def speichern(self, data_path="daten.json"):
        rest = self.txt.split(" ", 1)[1]
        key, value, anzahl = rest.split(" ", 2)
        try:
            anzahl = int(anzahl)
        except ValueError:
            return "FEHLER! Anzahl muss eine Zahl sein." 
        
        try:
            if not key or not value:
                raise ValueError 
        except ValueError:
            return "FEHLER! Bitte im Format 'speicher <key> <value> <anzahl>' eingeben."  
        
        self.daten[key] = {"value": value, "anzahl": anzahl}
        
        with open(data_path, "w") as f:
            json.dump(self.daten, f, indent=4)
            
        return f"Gespeichert: {key} -> {value}, Anzahl: {anzahl}"   
                  
    def delete(self, data_path="daten.json"):
        key = self.txt.split(" ", 1)[1]
        try:
            if key not in self.daten:
                raise KeyError
        except KeyError:
            return f"FEHLER! Schlüssel '{key}' nicht gefunden."
        
        else:
            del self.daten[key]
            with open(data_path, "w") as f:
                json.dump(self.daten, f, indent=4)
            return f"Gelöscht: {key}"
                
    def show_data(self):
        return json.dumps(self.daten, indent=4) if self.daten else "Keine Daten gespeichert."

#  Begüßung und verabschiedung           
    def greet(self):
        return "Hallo"

    def farewell(self):
        return "Auf Wiedersehen"

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
        
    def spiele(self):
        auswahl = input("was möchtest du spielen, ssp oder guess: ")
        if auswahl == 'ssp':
            return schere_stein_papier()
        elif auswahl == 'guess':
            return Ratespiel()
        #anpassen
        

def main():
    fox = FOX()
    while True:
        sleep(0.1)
        user = input('user: ')
        
        if user.lower() in ['e', 'q']:
            print("Programm beendet.")
            break 
        
        print(f'FOX: {fox.handle(user)}')  
        
        
if __name__ == "__main__":
    main()