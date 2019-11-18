usernameInput = input("Username :\n")
passwordInput = input("Password\n")
def login():
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def Menu():
    print("--------------------------------")
    print("Welcom to BNK48 SHOP.")
    print("1. PHOTOSET JABAJA ")
    print("2. PHOTOSET REBORN ")
    print("3. PHOTOSET KIMIWA MELODY ")
    print("4. PHOTOSET SHONICHI ")
    print("5. HANDSHAKE EVENT ")
    print("--------------------------------")
    return Menu
def Selected():
    vat = 7
    print(">>> Please Select PRODUCT<<<<<")
    Num = int(input())
    print(">>> HOW MANY PIECES<<<<<")
    Num2 = int(input())
    print("--------------------------------")
    if Num == 1:
        print("YOU SHOULD 1.PHOTOSET JABAJA")
        Num3 = (350 * Num2) + (350 * vat) / 100
        print(Num3)
    elif Num == 2:
        print("YOU SHOULD 2.PHOTOSET REBORN ")
        Num3 = (350 * Num2) + (350 * vat) / 100
        print(Num3)
    elif Num == 3:
        print("YOU SHOULD 3.PHOTOSET KIMIWA MELODY")
        Num3 = (350 * Num2) + (350 * vat) / 100
        print(Num3)
    elif Num == 4:
        print("YOU SHOULD 4.PHOTOSET SHONICHI")
        Num3 = (350 * Num2) + (350 * vat) / 100
        print(Num3)
    elif Num == 5:
        print("YOU SHOULD 5.HANDSHAKE EVENT ")
        Num3 = (350 * Num2) + (350 * vat) / 100
        print(Num3)
    return Selected()

print(Menu())
print(Selected())