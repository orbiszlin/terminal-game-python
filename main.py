
hp = 100
xp = 0

def stats():
    print(f"### HP {hp} ### XP {xp} ###")

def welcome_screen():
    print("########################")
    print("     Vítej v RPG hře    ")
    print("########################")

    print("\nMenu:")
    print("1 - Zahájit hru")
    print("Cokoliv jiného - ukončit hru")

def tavern():
    print("-----------------------")
    print("      Jsi v krčmě      ")
    print("-----------------------")

    stats()

    print("\nMenu:")
    print("1 - Koupím si pivo")
    print("2 - Koupím si polévku")
    print("3 - Koupím si velké jídlo")

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        print("Koupil jsis báječné pivo")
    elif int(choice) == 2:
        print("Koupil jsis hnusnou polévku")
    elif int(choice) == 3:
        print("Dostal jsi před sebe půlku divočáka")

    stats()
    crossroad()

def crossroad():
    print("-----------------------")
    print("   Jsi na křizovatce   ")
    print("-----------------------")

    print("\nMenu:")
    print("1 - Tréninkové hriště")
    print("2 - Krčma")
    print("3 - Souboj")

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        print("Budeš trénovat")
    elif int(choice) == 2:
        tavern()
    elif int(choice) == 3:
        print("Budeš bojovat")
    else:
        crossroad()


def main():
    welcome_screen()

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        crossroad()
    else:
        print("Hra ukončena")


main()
