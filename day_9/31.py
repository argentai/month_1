user = ("1234")

valid = False

while not valid:

   #for i in range (3):  

        user = input("Hello, welcome! Please enter a four digit passcode to open the safe: ")
        user = user.upper()          

        if user == ("1234") :
            print("You have cracked the code, well done")
            valid = True
            break

        if user != ("1234") :
            print ("that is incorrect, please try again")
            valid = False



        elif len(user) > 4:
            print ("That is incorrect, please try again")
            valid = False

        elif len(user) < 4:
            print ("That is incorrect, please try again")
            valid = False
        else:
            print ("You have been locked out!! Alarm!!!!!!")
