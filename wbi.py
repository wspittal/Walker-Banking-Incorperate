from datetime import datetime
from time import sleep
from random import randint
from storage import admins
from storage import stored as userinfo

def updatestorage(userinf):
  global admins
  text = "stored =  {\n"
  for i in userinf:
    text += "  \"" + userinf[i][0] + "\":[\"" + userinf[i][0] + "\", \"" + userinf[i][1] + "\", " + str(userinf[i][2]) + ", \"" + userinf[i][3] + "\", " + str(userinf[i][4]) + ", " + str(userinf[i][5]) + ", " + str(userinf[i][6]) + ", " + str(userinf[i][7]) + ", " + str(userinf[i][8]) + ", "
    if userinf[i][9]: text += "\"" + userinf[i][9] + "\"],"
    else: text += "False" + "],"
    text += "\n"
  text += "}\nadmins = [\n"
  for i in admins:
    text += "  \"" + i + "\",\n"
  text += "]"
  f = open("storage.py", "w")
  f.write(text)
  f.close()

def homescreen():
  global userinfo
  updatestorage(userinfo)
  print("    --- Welcome to WS Banking ---\n         -------------------\n        /     Raleigh NC    \ \n        |"+ str(datetime.now()).split(".")[0] + "|\n        \                   /\n         -------------------\n\n1. Login\n2. Exit")
  while True:
    enter = input("Please choose a service: ")
    if enter == "1" or enter.lower() == "login":
      while True:
        print("\nWhat do you want to login as:\n1. Admin\n2. User\n3. Go Back")
        answer = input("Please choose a service: ")
        if answer == "1" or answer.lower() == "admin":
          adminlogin(admins)
        elif answer == "2" or answer.lower == "user":
            userlogin()
        elif answer == "3" or answer.lower() == "go back":
          print("Returning to homescreen...")
          sleep(1)
          homescreen()
        else:
          print("\nBad Input\n")
    elif enter == "2" or enter.lower() == "exit":
      print("Thank you for banking with Walker Banking Incorperate, Have a Great Day")
      exit()
    else:
      print("\nBad Input\n")
      sleep(randint(5, 10) / 10)

def userlogin():
  global userinfo
  updatestorage(userinfo)
  while True:
    username = input("\nEnter Username")
    password = input("Enter Password")
    if username not in userinfo:
      print("Invalid Username or Password")
    elif password != userinfo[username][1]:
      print("Invalid Username of Password")
    else:
      print("Welcome " + username)
      menu(username)

def adminlogin(admins):
  global userinfo
  updatestorage(userinfo)
  while True:  
    adminname = input("\nEnter admin username: ")
    if adminname not in admins:
      print("Invalid Username, Please try again")
      adminlogin(admins)
    adminpassword = input("Enter password: ")
    if adminpassword != userinfo[adminname][1]:
      print("Invalid Password, Please try again")
    else:
      print("\nWelcome " + adminname)
      admin(admins, adminname)

def menu(username):
  global userinfo
  updatestorage(userinfo)
  print("Please enter the service number\n1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Change Password\n6. Logout")
  while True:
    ask = input("Please choose a service")
    if ask == "1":
      withdrawl = input("Please enter withdrawl amount")
      if float(withdrawl) <= userinfo[username][4]:
        userinfo[username][4] -= float(withdrawl)
        userinfo[username][6].append((withdrawl, str(datetime.now()).split(".")[0]))
        print("$" + str(withdrawl) + " withdrawn from your account\nnew balance: $" + str(userinfo[username][4]) + "\nReturning to main menu...")
        menu(username)
      elif float(withdrawl) > userinfo[username][4]:
        print("You don't have enough money, your current balance is: " + str(userinfo[username][4]))
      else:
        print("Bad Input")
    elif ask == "2":
      while True:  
        deposit = input("How much would you like to deposit")
        userinfo[username][4] += float(deposit)
        userinfo[username][5].append((deposit, str(datetime.now()).split(".")[0]))
        print("$" + deposit + " had been added to your account\nnew balance: " + str(userinfo[username][4]) + "\nResturning to main menu...")
        menu(username)
    elif ask == "3":
      print("If you want to abort the transfer enter abort")
      while True:
        transferdestination = input("Who would you like to transfer funds to")
        if transferdestination.lower() == "abort":
          print("Returning to main menu...")
          menu(username)
        elif transferdestination not in userinfo:
          print("That is not a user establihsed under our bank")
        elif transferdestination in userinfo:
          transferamount = input("How much would you like to transfer?")
          if float(transferamount) < 0:
            print("Please only use positive numbers")
          elif float(transferamount) <= userinfo[username][4]:
            userinfo[username][4] -= float(transferamount)
            userinfo[transferdestination][4] += float(transferamount)
            userinfo[username][7].append([transferamount, str(datetime.now()).split(".")[0]])
            userinfo[transferdestination][7].append([transferamount, str(datetime.now()).split(".")[0]])
            print("Transfering $" + transferamount + " to " + transferdestination + "...")
            sleep(2)
            print("\nTransfer Successful\nYour current balance is: $" + str(userinfo[username][4]) + "\nRetunring to main menu")
            menu(username)
          elif float(transferamount) > userinfo[username][4]:
            ("Insufficient funds")
          else:
            print("Invalid input")
    elif ask == "4":
      print("------- Walker Banking -------\n----- " + str(datetime.now()).split(".")[0]) + " -----\n-------------------------------\nUsername: "
      print("Username\n Password: " + userinfo[username][1] + "\nYour Balance: $" + str(userinfo[username][4]) + "\nUser Activities\n\n\nYour Withdrawls: \n")
      for i in userinfo[username][6]:
        print("      " + i[1] + " withdrew $" + i[0])
      print("Your Deposits:\n")
      for i in userinfo[username][5]:
        print("      " + i[1] + " deposited $" + i[0])
      print("Your Transfers:\n")
      for i in userinfo[username][7]:
        print("     $" + i[0] +" transferred at " + i[1])
      print("-------------------------------\nReturning to main menu")
      menu(username)
    elif ask == "5":
      while True:
        passwordcheck = input("For Security Reasons, Please enter your 4 digit pin")
        if passwordcheck != userinfo[username][3]:
          print("Incorrect Pin")
        elif passwordcheck == userinfo[username][3]:
          newpassword = input("Please enter new password")
          userinfo[username][1] = newpassword
          updatestorage(userinfo)
          break
    elif ask =="6":
      print("Logging Out...")
      homescreen()
    updatestorage(userinfo)

def admin(dhfdsoiwdc, adminname):
  global userinfo, admins
  updatestorage(userinfo)
  userinfo = userinfo
  print("\n---- Admin Menu ----\nPlease choose a option\n1. Add User\n2. Remove User\n3. Display all Users\n4. Logout")
  while True:
    select = input("Please choose a service")
    if select == "1" or select.lower() == "add user":
      newusername = input("Please enter the new users username")
      newuserpassword = input("Please enter the new users passcode")
      newuserpin = input("Please enter this person's pin")
      newuseradmin = not not input("If this person is an admin, type something before pressing enter. ")
      if newuseradmin:
        newusermstrpass = input("Enter this user's master password")
        newuserclearance = int(input("Enter this person's clearance"))
      else:
        newusermstrpass = False
        newuserclearance = 1
      newbalance = input("Please enter the balance of this new user")
      userinfo[newusername] = [newusername, newuserpassword, newuseradmin, newuserpin, newbalance, [], [], [], newuserclearance, newusermstrpass]
      if newuseradmin:
        admins.append(newusername)
      print(newusername + " has been added as a user")
      admin(admins, adminname)
    elif select == "2":
      while True:
        if userinfo[adminname][8] <= 3:
          print("Denied, Authorization level is too low")
          break
        admincheck = input("Please enter master password to continue")
        if admincheck != userinfo[adminname][9]:
          print("Incorrect master password")
        else:
          removal = input("Who would you like to remove?")
          if removal not in userinfo:
            print("Not a user established under Walker Banking")
          else:
            print("WARNING, IRREVERSIBLE CHANGE, ENTER 1 TO CANCEL")
            confirmation = input("Enter 2 to confirm changes")
            if confirmation == "1":
              print("Cancelling...")
              sleep(.5)
              admin(admins, adminname)
            elif confirmation == "2":
              print("removing....")
              sleep(2)
              print("User removed")
              userinfo.pop(removal)
              admin(admins, adminname)
            else:
              print("Invalid Input")
    elif select == "3" or select.lower() == "display all users":
      c = 1
      for i in userinfo:
        print("\n" + str(c) + ". "+ i + " has a balance of $" + str(userinfo[i][4]))
        c +=1
      while True:  
        moreinfo = input("\nWould you like more info? Enter 1 for more info, else enter 2")
        if moreinfo == "1" or moreinfo.lower() == "more info":
          infouser = input("\nPlease enter the name of the account")
          if infouser not in userinfo:
            print("Invalid Input")
          else:
            print("Username\n Password: " + str(userinfo[infouser][1]) + "\nBalance: $" + str(userinfo[infouser][4]) + "\nUser Activities:\n\nWithdrawls: \n")
            for i in userinfo[infouser][6]:
              print("      " + i[1] + " " + i[0])
            print("Deposits:\n")
            for i in userinfo[infouser][5]:
              print("      "+ i[1] + " " + i[0])
            print("Transfers:\n")
            for i in userinfo[infouser][7]:
              print("     "+i[2]+" Transfer "+i[1]+" "+i[0])
        elif moreinfo == "2" or moreinfo.lower() == "close":
          admin(admins, adminname)
    elif select == "4" or select.lower() == "logout":
      print("Logging out...")
      sleep(1.5)
      homescreen()
    else:
      print("Bad input")
    updatestorage(userinfo)

homescreen()
