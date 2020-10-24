from random import randint

#Liste der möglichen Optionen
t = ["Stein", "Papier", "Schere"]

#generiere eine zufällige Zahl
computer = t[randint(0,2)]

#Spieler wird auf False gesetzt
player = False

while player == False:
#Spieler wird auf True gesetzt
    player = input("Schere, Stein, Papier? ")
    if player == computer:
        print("unentschieden - beide das gleiche")
    elif player == "Stein":
        if computer == "Papier":
            print("Du verlierst!", computer, "bedeckt", player)
        else:
            print("Du gewinnst", player, "zerschlägt", computer)
    elif player == "Papier":
        if computer == "Schere":
            print("Du verlierst!", computer, "schneidet", player)
        else:
            print("Du gewinnst", player, "bedeckt", computer)
    elif player == "Schere":
        if computer == "Stein":
            print("Du verlierst!", computer, "zerschlägt", player)
        else:
            print("Du gewinnst", player, "schneidet", computer)
    else:
        print("Falsche Eingabe - Bitte auf die schreibweise achten")
    #Der Spieler wird wieder auf FALSE gesetzt, damit der Loop weiter geht
    player = False
    computer = t[randint(0,2)]
