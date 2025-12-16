import random
from time import sleep
 
def Ratespiel():
    geheimzahl=random.randint(1, 100)
    versuche = 1
    max_versuche = 11
    print('Willkommen zum spiel:\nGuess the number!\n')
    print('Spiel ablauf: Rate eine Zahl zwischen 1 und 100\nmax versuche: 10\nViel Glück\n')

    while True:
        try:
            geratene_zahl = int(input(f'{versuche} versuch: '))
            versuche += 1
            
            if geratene_zahl < geheimzahl:
                print('ist höher\n')
                
            elif geratene_zahl > geheimzahl:
                print('ist niedriger\n')
                
            else:
                print(f'richtig! {geheimzahl} war die zahl.\nAnzahl versuche: {versuche}\n')
                sleep(0.5)
                break
            
            if versuche == max_versuche:
                print('Du hast verloren\nvielleicht ein anderstmal\n')
                sleep(0.5)
                break
            
        except ValueError:
            print("buchstaben sind keine zahlen XD")
            
    return "Wie kann ich dir weiter helfen ?"

def schere_stein_papier():       
    runden = 1
    spieler_win = 0
    Fox_win = 0
    Max_win = 3
    
    print("Willkommen bei Schere, Stein, Papier!")
    print("Max runden 3\n")
    
    while True:
        Figuren = ["Schere", "Stein", "Papier"]
        Fox_wahl = random.choice(Figuren) 
        
        print(f"{runden} Runde")
        spieler_wahl = input("ich: ").strip().capitalize() 
        runden += 1

        if spieler_wahl not in Figuren:
            print("Ungültige Eingabe. Bitte wähle Schere, Stein oder Papier.\n")
            sleep(0.5)
            runden -= 1
            
        else:
            print(f"Fox: {Fox_wahl}")

        if spieler_wahl == Fox_wahl:
            print("glück!")     
              
        elif(spieler_wahl == "Schere" and Fox_wahl == "Papier") or \
            (spieler_wahl == "Stein" and Fox_wahl == "Schere") or \
            (spieler_wahl == "Papier" and Fox_wahl == "Stein"):  
            spieler_win += 1    
            print("...\n")
            sleep(0.5)
            
        elif(spieler_wahl == "Schere" and Fox_wahl == "Stein") or \
            (spieler_wahl == "Stein" and Fox_wahl == "Papier") or \
            (spieler_wahl == "Papier" and Fox_wahl == "Schere"):
            Fox_win += 1
            print("bin besser\n")
            sleep(0.5)
            
        if spieler_win == Max_win:
            print("du hast gewonnen\n")
            sleep(0.5)
            break
        
        if Fox_win == Max_win:
            print("du hast verloren")
            sleep(0.5)
            break

    return "Wie kann ich dir weiter helfen ?"
                      