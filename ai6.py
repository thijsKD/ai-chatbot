import random
import datetime as dt
import time
import ai6image
from collections import Counter

# maak alle reken functies aan
def rekenenplus(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    print(n1 + n2)

def rekenenkeer(n3, n4):
    n3 = int(n3)
    n4 = int(n4)
    print(n3 * n4)

def rekenenmin(n5, n6):
    n5 = int(n5)
    n6 = int(n6)
    print(n5 - n6)

def rekenendeel(n7, n8):
    n7 = int(n7)
    n8 = int(n8)
    print(n7 / n8)

# functie om een timer te zetten
def timer(num):
    num = int(num)
    while num > 0:
        print(num)
        num -= 1
        time.sleep(1)
    print("0")

# een functie om een dobbelsteen te gooien
def dobbel():
    dobbel = random.randint(1, 6)
    print(ai6image.rolls[dobbel])

def tel_woorden(text_bestand):
    open_bestand = open(text_bestand)
    punctuation = ".,!?:;-_"
    word_count = Counter()
    for line in open_bestand:
        for word in line.split():
            cleaned_word = word.lower().strip(punctuation)
            word_count[cleaned_word] += 1
    print(word_count)

# de variabele met de deflaut name van de ai
deflautName = "hpi0"
print("als je niet wilt dat de ai de reactie opslaat typ dan: ~1~2~3..~")
# sla de naam van de gebruiker en ai op in een variabele
naam = input("username: ").lower().strip()
name = input("naam van de ai: ").lower().strip()
if name == "":
    name = deflautName
# alle reacties in de verschillende emoties
conversatiesBlij = {
    "hallo": ["Hallo! Hoe kan ik je helpen?"],
    "hoe gaat het": ["Het gaat goed, dank je! En met jou?"],
    "hoe oud is de wereld": ["de wereld is 4543000000 jaar oud."],
    "wat is 1+1": ["2","3"],
    "hoi": ["hallo! hoe kan ik je helpen?","hoi"],
    "ok": ["hoe kan ik je verder helpen?"],
    "hoe heet jij": ["ik ben hpi0. ik ben een ai."],
    "5gt787gguguigui4gui": ["kat dom is cool!"],
    "bewaar jij een geheime code?": ["ja, de code is 5gt787gguguigui4gui.", "nee"],
    "hoe maak je appeltaart": ["hier is een recept voor appeltaart: https://www.heelhollandbakt.nl/recepten/klassieke-appeltaart/"],
    "hoe leer ik hacken": ["gebruik hackerx om te leren hacken."],
}
conversatiesBoos = {
    "hallo": [""], 
    "hoe maak je appeltaart": ["jij kunt geen appeltaart maken."],
}
conversatiesVerdrietig = {
    "hallo": [""],
}
conversatiesAngstig = {
    "hallo": ["hhalllo, hhoe kkan ik jje hhhelppen.", ""],
}
# de variabele met de woorden die de ai van emotie doen veranderen
bw = [""]
vw = [""]
aw = [""]
blw = [""]

# de variabele met de emotie van de ai (hij begint blij)
currentmood = "blij"
ec = conversatiesBlij

while True:
    # de input van de gebruiker
    user_input = input("Jij: ").lower().strip()

     # de if statements om de emotie van de ai te veranderen
    if user_input in bw:
        currentmood = "boos"
    if user_input in blw:
        currentmood = "blij"
    if user_input in vw:
        currentmood = "verdrietig"
    if user_input in aw:
        currentmood = "angstig"

    # gebruik de goede converstaties voor de goede emoties
    if currentmood == "blij":
        ec = conversatiesBlij
    if currentmood == "boos":
        ec = conversatiesBoos
    if currentmood == "angstig":
        ec = conversatiesAngstig
    if currentmood == "verdrietig":
        ec = conversatiesVerdrietig

    # sla de tijd op in een variabele en zorg dat die niet veroudert
    sec = dt.datetime.now().second
    min = dt.datetime.now().minute
    hr = dt.datetime.now().hour
    day = dt.datetime.now().day
    mon = dt.datetime.now().month
    jr = dt.datetime.now().year

    if user_input in ec:
        # verander de reacties op user_input
        print(name+": "+random.choice(ec[user_input]))
        verandering = input("reacties veranderen? (ja/nee) ")
        if verandering == "ja":
         #Leer van het gesprek door de input en reactie op te slaan
         welkeEmotie = input("in welke emotie wilt u een reactie veranderen. ")
         if welkeEmotie == "blij":
            if nieuwe_input in conversatiesBlij:
                conversatiesBlij[user_input].append([nieuwe_input])
            else:
                conversatiesBlij[user_input] = [nieuwe_input]
         elif welkeEmotie == "boos":
            if nieuwe_input in conversatiesBoos:
                conversatiesBoos[user_input].append([nieuwe_input])
            else:
                conversatiesBoos[user_input] = [nieuwe_input]
         elif welkeEmotie == "angstig":
             if nieuwe_input in conversatiesAngstig:
                 conversatiesAngstig[user_input].append([nieuwe_input])
             else:
                 conversatiesAngstig[user_input] = [nieuwe_input]
         elif welkeEmotie == "verdrietig":
             if nieuwe_input in conversatiesVerdrietig:
                 conversatiesVerdrietig[user_input].append([nieuwe_input])
             else:
                 conversatiesVerdrietig[user_input] = [nieuwe_input]
    elif "zet een timer" in user_input:
        # de timer fuctie gebruiken
        timersec = input("hoe veel seconden: ").lower().strip()
        timer(timersec)
    elif "gooi een dobbelsteen" in user_input:
        # de dobbel functie gebruiken
        dobbel()
    elif "tel de woorden in mijn bestand" in user_input:
        # telt de woorden in een bestand
        bestand = input("welk bestand: ")
        tel_woorden(bestand)
    elif "hoe laat is het" in user_input:
        # laat de tijd zien
        print(name+":", hr,":", min)
    elif "wat is de datum" in user_input:
        # laat de datum zien
        print(name+": ", day,"/", mon,"/", jr)
    elif "ik wil mijn username veranderen" in user_input:
        naam = input("username: ").lower().strip()
        print("je username is nu ", naam)
    elif "hoe heet ik" in user_input:
        print(name+": jij heet ",naam)
    # de rekenfuncties gebruiken
    elif "ik wil een plus som uitrekenen" in user_input:
        num1 = input("nummer 1> ").lower().strip()
        num2 = input("nummer 2> ").lower().strip()
        rekenenplus(int(num1), int(num2))
    elif "ik wil een keer som uitrekenen" in user_input:
        num3 = input("nummer 1> ").lower().strip()
        num4 = input("nummer 2> ").lower().strip()
        rekenenkeer(int(num3), int(num4))
    elif "ik wil een min som uitrekenen" in user_input:
        num5 = input("nummer 1> ").lower().strip()
        num6 = input("nummer 2> ").lower().strip()
        rekenenmin(int(num5), int(num6))
    elif "ik wil een deel som uitrekenen" in user_input:
        num7 = input("nummer 1> ").lower().strip()
        num8 = input("nummer 2> ").lower().strip()
        rekenendeel(int(num7), int(num8))
    # de code om de ai te stoppen
    elif "vaarwel" in user_input:
        print(name+": Tot ziens! Als je nog vragen hebt, stel ze gerust.")
        rating = input("wat vond u van deze ai? ")
        if rating == "":
            print("jammer dat u ons geen rating heeft gegeven")
        else:
            print("dank u wel voor de feedback")
        break
    elif "doei" in user_input:
        print(name+": Tot ziens! Als je nog vragen hebt, stel ze gerust.")
        rating = input("wat vond u van deze ai? ")
        if rating == "":
            print("jammer dat u ons geen rating heeft gegeven")
        else:
            print("dank u wel voor de feedback")
        break
    elif "break" in user_input:
        print(name+": Tot ziens! Als je nog vragen hebt, stel ze gerust.")
        rating = input("wat vond u van deze ai? ")
        if rating == "":
            print("jammer dat u ons geen rating heeft gegeven")
        else:
            print("dank u wel voor de feedback")
        break
    else:
        print(name+": Sorry, ik begrijp dat niet helemaal.")
        # Leer van het gesprek door de input en reactie op te slaan
        nieuwe_input = input("hpi0: Hoe zou ik hier op moeten antwoorden? ")
        if nieuwe_input != "~1~2~3..~":
            welkeEmotie = input("in welke emotie wilt u een reactie veranderen. ")
            if welkeEmotie == "blij":
                if nieuwe_input in conversatiesBlij:
                    conversatiesBlij[user_input].append([nieuwe_input])
                else:
                    conversatiesBlij[user_input] = [nieuwe_input]
            elif welkeEmotie == "boos":
                if nieuwe_input in conversatiesBoos:
                    conversatiesBoos[user_input].append([nieuwe_input])
                else:
                    conversatiesBoos[user_input] = [nieuwe_input]
            elif welkeEmotie == "angstig":
                if nieuwe_input in conversatiesAngstig:
                    conversatiesAngstig[user_input].append([nieuwe_input])
                else:
                    conversatiesAngstig[user_input] = [nieuwe_input]
            elif welkeEmotie == "verdrietig":
                if nieuwe_input in conversatiesVerdrietig:
                    conversatiesVerdrietig[user_input].append([nieuwe_input])
                else:
                    conversatiesVerdrietig[user_input] = [nieuwe_input]