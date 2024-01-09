#Import des librairies
import time
import random

#Définition des variables
Player = []
Dice = 100
PlayerTurn = -1 #Est -1 car 1 est ajouté en début de boucle while. Si on ajoute 1 à la fin alors le joueur change en sortant de la boucle et en annonçant le perdant.
RollDelay = 2
FakeThrow = 9
DelayDivider = 0

#Définit le temps des faux lancés, nécessaire à l'effet de roulement du dé (FakeDice).
for j in range(1, FakeThrow+1) :
    DelayDivider += j
DelayFraction = 3/DelayDivider

#Définition du nombre de joueurs.
NumbPlayer = input("Nombre de joueurs :")

#Demande un nom par joueur.
for i in range(int(NumbPlayer)) :
    P = input("Nom d'un joueur :")
    Player.append(P)
    
#Mélange l'ordre des joueur et l'annonce.
random.shuffle(Player)
print("L'ordre est : " + ' / '.join(map(str, Player)))    
time.sleep(0.5)

#Déroulement des lancés concecutifs, jusqu'à un résultat de 1.
while Dice > 1:
    PlayerTurn += 1
    if PlayerTurn == len(Player):
        PlayerTurn = 0

    time.sleep(0.5)
    for k in range(1, FakeThrow+1) :
        Delay = k*DelayFraction
        FakeDice = random.randint(1, Dice+1)
        while FakeDice > Dice :
            FakeDice = random.randint(1, Dice+1)
        if len(Player[PlayerTurn]) <= 4:
            print(Player[PlayerTurn] +": \t\t" + str(FakeDice), flush=True, end="\r")
        else:
            print(Player[PlayerTurn] +": \t" + str(FakeDice), flush=True, end="\r")
        time.sleep(Delay)
        
    Dice = random.randint(1, Dice+1)
    if len(Player[PlayerTurn]) <= 4:
        print(Player[PlayerTurn] +": \t\t" + str(Dice) + " !")
    else:
        print(Player[PlayerTurn] +": \t" + str(Dice) + " !")
    time.sleep(1.5)

#Annonce du perdant.
print(Player[PlayerTurn] + " est le grand perdant !")
time.sleep(3.5)
