usernameInput = input("Username :\n")
passwordInput = input("Password\n")
if usernameInput== "admin" and passwordInput =="1234" :
    print("Welcome to My Shop.")
    Keybord1 = 50
    Ram1 = 90
    Monitor1 = 250
    print("1. keybor 50(THB)")
    Keybord2 = int(input())
    print("2. Ram 90(THB)")
    Ram2 = int(input())
    print("3. Mornitor 250(THB)")
    Monitor2 = int(input())
    print((Keybord1*Keybord2)+(Ram1*Ram2)+(Monitor1*Monitor2),"(THB)")