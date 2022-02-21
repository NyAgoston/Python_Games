
import random
from re import S
print("Version 1.0")
#Variables, lists
betuk = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #megadott elem ellenorzese
outergamerun = True #Switch for the outer game loop
gamerun = True #Switch for the inner game loop
lepes = 1 #Represents the game turns
sajat_szavak = ["alma","elem","katasztrofa","vulkan","bettes"] #user guesses these words
#definitions
def kezdes():
    print(" ______","\n"," |  ","|","\n"," |","\n"," |","\n"," |","\n","_|_")
def egy():
    print(" ______","\n"," |  ","|","\n"," |","  O","\n"," |","\n"," |","\n","_|_")   
def ketto():
    print(" ______","\n"," |  ","|","\n"," |","  O_","\n"," |","\n"," |","\n","_|_")
def harom():
    print(" ______","\n"," |  ","|","\n"," |"," _O_","\n"," |","\n"," |","\n","_|_")    
def negy():
    print(" ______","\n"," |  ","|","\n"," |"," _O_","\n"," |   |","\n"," |","\n","_|_")   
def ot():
    print(" ______","\n"," |  ","|","\n"," |"," _O_","\n"," |   |","\n"," |   /","\n","_|_")   
def hat():
    print(" ______","\n"," |  ","|","\n"," |"," _O_","\n"," |   |","\n"," |  / \\","\n","_|_")
#Game starts here
print("Üdvözöllek a játékban! :)")
while(outergamerun): #outer game loop
    bekert = int(input("A játék megkezdéséhez nyomj 1-est, kilépéshez 2-est a játékszabályokhoz 3-ast: "))
    if bekert == 1:
        megoldas = sajat_szavak[random.randint(0,4)] #random gives a word from the set
        eredmeny = [] #stores the users guesses
        hibak = 0 #counts the mistakes if its 7 the game ends
        for i in range(len(megoldas)):
            eredmeny.append("*")
        #print(megoldas) # enable if you'd like to see the word at the begining
        print(eredmeny)
        while(gamerun): #inner game loop
            print("Adja meg a(z) ",lepes,". tippet: ",sep="")
            beker = input()
            if beker not in betuk or beker in eredmeny: #check if users guess is correct
                print("Nem megfelelő karakter")
                continue
            else:
                for i,v in enumerate(megoldas):
                    if beker == v:
                        eredmeny[i] = v
        
                print(eredmeny) #prints the guesses
                lepes += 1 #increment the turn number
                if beker not in megoldas:
                    print("Nincs benne")
                    hibak += 1
                print("Hibák száma = ",hibak) # prints the number of mistakes
                if hibak == 0:
                    kezdes()
                elif hibak == 1:
                    egy()
                elif hibak == 2:
                    ketto()
                elif hibak == 3:
                    harom()
                elif hibak == 4:
                    negy()
                elif hibak == 5:
                    ot()
                elif hibak == 6:
                    hat()
                    
            segedszo = ''.join(eredmeny) # converts the list to a string
            if segedszo == megoldas:#ends the game session if the user guessd the word
                print("Gratulálok nyertél öcskösöm! ;)")
                gamerun = False  
            if hibak == 7:
                print("Vesztettél haver! ;)")
                gamerun = False   
    elif bekert == 2:
        outergamerun = False # end the whole game
        print("Viszlát")
    elif bekert == 3:
        print("A játékosnak 7 élete van, kizárólag az angol abc betűit adhatja meg tippként, előre beállított szavak: alma, elem, vulkan, katasztrofa, benjamin")
    else:
        print("Ez nem 1,2 vagy 3-as ne szorakozz velem!")    
        
