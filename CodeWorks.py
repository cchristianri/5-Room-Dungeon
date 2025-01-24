from idlelib.pyshell import restart_line
from math import trunc

print("=== THE FIVE ROOM DUNGEON ===")
import random
import time

System = True
charCreation = False
classes = False
room1 = False
redbook = False
lever = False
fist = random.randint(1, 12)
knife = random.randint(1, 15)
sword = random.randint(1, 25)
axe = random.randint(1, 30)
fistI = ("your weapon is your fists, you may roll up to a d12")
knifeI = ("your weapon is a knife, you may roll up to a d15")
swordI = ("your weapon is a sword, you may roll up to a d25")
axeI = ("your weapon is an axe, you may roll up to a d30")
weapon = knife
weaponI = knifeI
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
charisma = 0
wisdom = 0
health = 0
speed = 0
boost = 0
damage = random.randint(1, 8) + 2 + strength



def attack():
    global weapon
    weapon += strength


def boosting():
    global strength, dexterity, constitution, intelligence, charisma, wisdom, boost

    statsPlus = input("Choose to boost [S]rength [D]exterity [C]onstitution [I]ntelligence [W]isdom [C]harisma : ")

    if statsPlus == "S" or statsPlus == "s":
        strength += 1
        boost -= 1
        checkstats()

    elif statsPlus == "D" or statsPlus == "d":
        dexterity += 1
        boost -= 1
        checkstats()

    elif statsPlus == "C" or statsPlus == "c":
        constitution += 1
        boost -= 1
        checkstats()

    elif statsPlus == "I" or statsPlus == "i":
        intelligence += 1
        boost -= 1
        checkstats()

    elif statsPlus == "W" or statsPlus == "w":
        wisdom += 1
        boost -= 1
        checkstats()

    elif statsPlus == "C" or statsPlus == "c":
        charisma += 1
        boost -= 1
        checkstats()

    if boost != 0:
        boosting()


def checkstats():
    print(f'''                  Your strength is {strength}
                                your dexterity is {dexterity}
                                your constitution is {constitution}
                                your intelligence is {intelligence}
                                your charisma is {charisma}
                                your wisdom is {wisdom}
                                your health is {health}
                                your speed is {speed}
                                your boost is {boost}''')


wraithArmor = 12
wraithHealths = 6
wraithminiOnce = False


def wraithattacking():
    global health
    w = random.randint(1, 5)
    if w == 2:
        print("wraith did 2 damage to your health")
        health -= 2
    if w == 4:
        print("wraith did 4 damage to your health")
        health -= 4
    else:
        print("the wraiths attacked you but missed")


def wraithmini():
    global wraithArmor, damage, wraithHealths, weapon, weaponI, wraithminiOnce, redbook

    if not wraithminiOnce:
        talktowraiths = random.randint(1, 20)

        if talktowraiths == 15:
            wraithencounterquestion()


        elif talktowraiths == 7:
            print("Go to the book shelf and pull the red book")
            time.sleep(3)
            redbook = True
            wraithminiOnce = True

        elif talktowraiths != 7 or talktowraiths != 13:
            print("No Response")
            wraithagain = input("Would you like to ask the wraiths again? Y/N? ")
            if wraithagain == "Y" or wraithagain == "y":
                wraithmini()
            elif wraithagain == "N" or wraithagain == "n":
                wraithminiOnce = True

        else:
            print("I dont understand")
            wraithmini()

    if wraithminiOnce:
        print("you have already completed the wraith encounter")
        time.sleep(3)


def wraithencounterquestion():
    global wraithArmor, damage, wraithHealths, weapon, weaponI, wraithminiOnce

    print("\033[31m YOU HAVE ANGERED THE WATER WRAITHS AND TWO OF THEM HAVE EMERGED FROM THE WATER\033[0m")
    wraithEncounter = input("[F]ight the wraiths, offer your [W]eapon as a gift: ")

    if wraithEncounter == "W" or wraithEncounter == "w" and weapon != fist:
        print("Wraiths have accepted your offering")
        weapon = fist
        weaponI = fistI
        time.sleep(2)

        wraithagain = input("Would you like to ask the wraiths again? Y/N? ")
        if wraithagain == "Y" or wraithagain == "y":
            wraithmini()
        elif wraithagain == "N" or wraithagain == "n":
            print()

    elif wraithEncounter == "F" or wraithEncounter == "f":
        wraithfightminiarmor()

    else:
        print("I do not understand")
        wraithencounterquestion()


def wraithfightminiarmor():
    global wraithArmor, damage, wraithHealths, weapon, weaponI
    print("THE WRAITHS HAVE ARMOR ON YOU MUST BREAK IT BEFORE YOU CAN SLAY THEM! (12 armor health).")
    print(weaponI)
    time.sleep(5)
    wraithArmor -= weapon
    print(f"YOU DID d{weapon} ARMOR DAMAGE")
    if wraithArmor <= 0:
        wraithfightminidamage()
    if wraithArmor > 0:
        wraithattacking()
        wraithfightminiarmor()


def wraithfightminidamage():
    global wraithArmor, damage, wraithHealths, weapon, weaponI, wraithminiOnce, redbook

    print("YOU HAVE BROKE THEIR ARMOR NOW YOU MUST DELIVER THE FINAL BLOW. (6 health)")
    time.sleep(5)

    wraithHealths -= damage
    print(f"YOU DID {damage} DAMAGE")
    if wraithHealths <= 0:
        print("YOU SLAYED BOTH WRAITHS")
        print('One wraith talks in a very low tone. "R..Red... ')
        print("the wraith took it's final breath before he could finish his sentence.")
        time.sleep(3)
        redbook == True
        wraithminiOnce = True

    if wraithHealths > 0:
        time.sleep(3)
        wraithattacking()
        wraithfightminidamage()

eelArmor = 20
eelHealths = 10

def eelattacking():
    global health
    w = random.randint(1, 10)
    if w == 5:
        print("eel did 2 damage to your health")
        health -= 5
    if w == 7:
        print("eel did 4 damage to your health")
        health -= 7
    else:
        print("the eel attacked you but missed")




def eelfightminiarmor():
    global eelArmor, damage, eelHealths, weapon, weaponI, lever
    if lever == False:
        print("As soon as you pull the lever a trap door open. ROARRRR, you look back and see a 9ft long eel comes down")
        print("You are forced to fight the eel")
        time.sleep(3)
        print("THE EEL HAS ARMOR ON YOU MUST BREAK IT BEFORE YOU CAN SLAY THEM! (20 armor health).")
        print(weaponI)
        time.sleep(5)
        eelArmor -= weapon
        print(f"YOU DID d{weapon} ARMOR DAMAGE")
        if eelArmor <= 0:
            eelfightminidamage()
        if eelArmor > 0:
            eelattacking()
            eelfightminiarmor()

            if lever == True:
                print("lever had already been pulled")
                time.sleep(3)

def eelfightminidamage():
    global eelArmor, damage, eelHealths, weapon, weaponI, lever

    print("YOU HAVE BROKE IT'S ARMOR NOW YOU MUST DELIVER THE FINAL BLOW. (10 health)")
    time.sleep(5)

    eelHealths -= damage
    print(f"YOU DID {damage} DAMAGE")
    if eelHealths <= 0:
        print("THE EEL HAS BEEN SLAYED")
        lever = True
        time.sleep(3)

    if eelHealths > 0:
         time.sleep(3)
         eelattacking()
         eelfightminidamage()


while System:
    background = True
    while background:
        print('''        \033[92m You wake up one morning in your cozy cottage and start getting ready for the day.
         As you move around, you notice that your roommate isn’t home. 
         You find a note he left, saying "went to town to buy some groceries".
          Hours pass, and as darkness begins to settle in, worry starts to creep in. 
          You decide to leave and search for him. On your way to town, 
          you come across a cave that sends shivers down your spine. 
          Eerie noises echo from inside, and when you look down, 
          you see your friend’s knife lying on the ground near the cave's entrance. \033[0m''')
        background = False
        time.sleep(5)
        charCreation = True

    while charCreation:
        char = input("\033[94m Would you like to be an [E]lf [H]uman [D]warf? : ")

        if char == "E" or char == "e":
            confirm = input("Press Y to confirm otherwise choose again : ")
            if confirm == "Y" or confirm == "y":
                strength += -1
                dexterity += 1
                constitution += 0
                intelligence += 1
                charisma += 0
                wisdom += 0
                health += 6
                speed += 30
                boost += 1
                checkstats()

                charCreation = False
                classes = True
        elif char == "H" or char == "h":
            confirm = input("Press Y to confirm otherwise choose again : ")
            if confirm == "Y" or confirm == "y":
                strength += 0
                dexterity += 0
                constitution += 0
                intelligence += 0
                charisma += 0
                wisdom += 0
                health += 8
                speed += 25
                boost += 2
                checkstats()

                charCreation = False
                classes = True
        elif char == "D" or char == "d":
            confirm = input("Press Y to confirm otherwise choose again : ")
            if confirm == "Y" or confirm == "y":
                strength += 1
                dexterity += 0
                constitution += 1
                intelligence += 0
                charisma += -1
                wisdom += 0
                health += 10
                speed += 20
                boost += 1
                checkstats()

                charCreation = False
                classes = True
        else:
            print("\033[91m I did not understand try again.")

        while classes:
            myclass = input("Now you must pick your background [W]arrior [S]cientist [G]ymnast : ")

            if myclass == "W" or myclass == "w":
                strength += 1
                charisma += 1
                boost += 1
                classes = False
                checkstats()
                boosting()
                room1 = True

            elif myclass == "S" or myclass == "s":
                intelligence += 1
                wisdom += 1
                boost += 1
                classes = False
                checkstats()
                boosting()
                room1 = True

            elif myclass == "G" or myclass == "g":
                dexterity += 1
                constitution += 1
                boost += 1
                classes = False
                checkstats()
                boosting()
                room1 = True

        while room1:
            print('''            \033[31m You step into a dark humid room that seems to echo with quiet sounds of dripping water.
            The chamber is flooded ankle deep with a gentle current rippling through murky water.
            Along the walls you can see the fungi glowing faintly, casting an eerie blue-green light across the room.
            Stone pillars rise from the water, covered in moss and slimy vines, supporting a crumbling ceiling.
            At the far end of the chamber, you see a raised stone platform with a rusty iron door.
            The water appears deeper around the platform, and you see something shimmer beneath the surface–
            a hint of movement or perhaps an object buried in the slit below.
            Faint whispers fill the air, giving an unsettling sense of secrets hidden below. \033[0m''')

            lookAroundRoom1 = input("You can [L]ook around the room, [W]alk towards the platform : ")

            if lookAroundRoom1 == "L" or lookAroundRoom1 == "l":

                print("You look around the room and notice theirs a table against a wall and across from  the table there is a bookshelf")

                investigateR1 = input("Investigate the [T]able, investigate the [B]ookshelf, [I]gnore all")

                if investigateR1 == "T" or investigateR1 == "t":
                    print("You walk to the table and look around it, you look under the table and notice there is a lever. : ")
                    exR1 = input("[P]ull the lever or [I]gnore it. : ")
                    if exR1 == "P" or "p":
                        eelfightminiarmor()




            if lookAroundRoom1 == "W" or lookAroundRoom1 == "w":

                print("As you walk towards the platform you notice that their is a deep pit around it filled with water, voices can be heard coming from the water.")

                w1 = input("[T]alk to the voices, [J]ump onto the platform, [L]eap into the pit : ")

                if w1 == "t" or w1 == "T":
                    wraithmini()
