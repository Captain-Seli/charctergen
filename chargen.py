import random
#Random table of defining physical feature based on race
#Age
#Table of posessions tied to profession

def displayRaceOptions():
    print("Select a Race")
    print()
    print("1: Azonian")
    print("2: Akomaseri")
    print("3: Carcharian")
    print("4: Elf")
    print("5: Kyranian")
    print("6: Imperial")
    print("7: Sinai")

def age():
    race = input()
    # age = 0
    if race == "1":
        raceName = "Azonian"
        age = randint(18,121)

    if race == "2":
        raceName = "Akomaseri"
        age = randint(18,121)
        
    if race == "3":
        raceName = "Carcharian"
        age = randint(18,121)

    if race == "4":
        raceName = "Elf"
        age = randint(18,501)
        
    if race == "6":
        raceName = "Imperial"
        age = randint(18,121)
        
    if race == "5":
        raceName = "Kyranian"
        age = randint(18,121)
        
    if race == "7":
        raceName = "Sinai"
        age = randint(18,501)
    print("AGE: " + str(age))
    return age


def charName():
    race = input("Enter Number: ")
    print()
    if race != "1" and race != "2" and race != "3" and race != "4" and race != "5" and race != "6" and race != "7":
        print("Invalid race.")
    if race == "1":
        nameFile = open("Azon Names.txt")
        raceName = "Azonian"
        randomName = random.randint(1,170)
        name = nameFile.readlines()
        print("NAME: " + name[randomName])
        print ("RACE: Human")
        print("CULTURE: Azonian")
        
    
    if race == "2":
        nameFile = open("Akomaseri Names.txt")
        raceName = "Akomaseri"
        randomName = random.randint(1,41)
        name = nameFile.readlines()
        print ("NAME: " + name[randomName])
        print ("RACE: Human")
        print("CULTURE: Akomaseri")
        

    if race == "3":
        nameFile = open("Carcharian Names.txt")
        raceName = "Carcharian"
        randomName = random.randint(1,150)
        name = nameFile.readlines()
        print ("NAME: " + name[randomName])
        print ("RACE: Carcharian")
        

    if race == "4":
        nameFile = open("Elf Names.txt")
        raceName = "Elf"
        randomName = random.randint(1,173)
        name = nameFile.readlines()
        print ("NAME: " + name[randomName])
        print ("RACE: Elf")
        

    if race == "6":
        nameFile = open("Imperial Names.txt")
        raceName = "Imperial"
        randomName = random.randint(1,181)
        name = nameFile.readlines()
        print ("NAME: " + name[randomName])
        print ("RACE: Human")
        print("CULTURE: Imperial (Venian)")
        

    if race == "5":
        nameFile = open("Kyranian Names.txt")
        raceName = "Kyranian"
        randomName = random.randint(1,161)
        name = nameFile.readlines()
        print ("NAME: " + name[randomName])
        print ("RACE: Human")
        print("CULTURE: Kyranian")
        

    if race == "7":
        nameFile = open("Sinai Names.txt")
        raceName = "Sinai"
        randomName = random.randint(1,151)
        name = nameFile.readlines()
        print ("NAME:" + name[randomName])
        print ("RACE: Sinai")
    return raceName 

def profPick():
    professionFile = open("Professions.txt")
    randomProfession = random.randint(1,123)
    profession = professionFile.readlines()
    print("PROFESSION: " + profession[randomProfession])
    return profession[randomProfession]

def traitPick():
    traitFile = open("Traits.txt")
    randomTrait = random.randint(1,106)
    trait = traitFile.readlines()
    print("TRAIT: " + trait[randomTrait])
    return trait[randomTrait]

def flawPick():
    flawFile = open("Flaws.txt")
    randomFlaw = random.randint(1,79)
    flaw = flawFile.readlines()
    print("FLAW: " + flaw[randomFlaw])
    return flaw[randomFlaw]

def loop():

    more = input("Press 1 to make a new character." + "\n" + "Press 2 to exit" + "\n" + "Choice: ")
    if more == "1":
        displayRaceOptions()
        charName()
        profPick()
        traitPick()
        flawPick()
        # age()
        loop()
    else:
        print("Done Generating Characters")

def charList(): #Not currently working
    charList = open("Characters.txt", "a")
    charList.write(charName() + "\t" + profPick() + "\t" + traitPick() + "\t" + flawPick() + "\n")
    charList.close()
    
def main():
    loop()
main()