# if name1.lower() == ("walker" or "walker spittal") or ("avery" or "avery lassiter") and name2.lower() == ("walker" or "walker spittal") or ("avery" or "avery lassiter") and name1.lower() != name2.lower():
# don't think I don't see this (Ima show to Avery at lunch lol)
from datetime import datetime
from time import sleep

admins = ["Walker Spittal", "Avery Lassiter", "Owen Reaser"]
userinfo = {
 #"username"        :[Name,              password/adminpass,     admin, pin,    bal,    [d],[w],[t],cl,mstrpass"]}
  "Spencer Karby"   :["Spencer Karby",   "l + bozo + ratio",     False, "1234", 10,     [], [], [], 1, False],
  "Owen Reaser"     :["Owen Reaser",     "academic weapon",      True,  "7676", 100000, [], [], [], 8, "bestatcoding"],
  "Micheal Tomkzak" :["Micheal Tomkzak", "Genius",               False, "8888", 904957, [], [], [], 1, False],
  "Parker Dillon"   :["Parker Dillon",   "69420",                False, "1234", 982739, [], [], [], 1, False],
  "Walker Spittal"  :["Walker Spittal",  "Hamilton is awesome",  True,  "7727", 1,      [], [], [], 8, "Avery"],
  "Avery Lassiter"  :["Avery Lassiter",  "coolest person alive", True,  "0911", 1,      [], [], [], 4, "Walker"]
}

def homescreen():
    print("     --- Welcome to WS Banking ---\n         -------------------\n        /     Raleigh NC    \ \n        |"+ str(datetime.now()).split(".")[0] + "|\n        \                   /\n         -------------------\n\n1. Login\n2. Exit")
    while True:
      enter = input("Please choose a service: ")
      if enter == "1" or enter.lower() == "login":
        while True:
          print("\nWhat do you want to login as:\n1. Admin\n2. User\n3. Go Back")
          answer = input("Please choose a service: ")
          if answer == "1" or answer.lower() == "admin":
            adminlogin(admins)
          elif answer == "2" or answer.lower == "user":
              userlogin(userinfo)
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
        sleep(.75)

def userlogin(users):
  while True:
    username = input("\nEnter Username")
    password = input("Enter Password")
    if username not in users:
      print("Invalid Username or Password")
    elif password != users[username][1]:
      print("Invalid Username of Password")
    else:
      print("Welcome " + username)
      menu(users, username)

def adminlogin(admins):
  global userinfo
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

def menu(users, username):
  print("Please enter the service number\n1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Change Password\n6. Logout")
  while True:
    ask = input("Please choose a service")
    if ask == "1":
      withdrawl = input("Please enter withdrawl amount")
      if float(withdrawl) <= users[username][4]:
        users[username][4] -= float(withdrawl)
        users[username][6].append((withdrawl, str(datetime.now()).split(".")[0]))
        print("$" + str(withdrawl) + " withdrawn from your account\nnew balance: $" + str(users[username][4]) + "\nReturning to main menu...")
        menu(users, username)
      elif float(withdrawl) > users[username][4]:
        print("You don't have enough money, your current balance is: " + str(users[username][4]))
      else:
        print("Bad Input")
    elif ask == "2":
      while True:  
        deposit = input("How much would you like to deposit")
        users[username][4] += float(deposit)
        users[username][5].append((deposit, str(datetime.now()).split(".")[0]))
        print("$" + deposit + " had been added to your account\nnew balance: " + str(users[username][4]) + "\nResturning to main menu...")
        menu(users, username)
    elif ask == "3":
      print("If you want to abort the transfer enter abort")
      while True:
        transferdestination = input("Who would you like to transfer funds to")
        if transferdestination.lower() == "abort":
          print("Returning to main menu...")
          menu(users, username)
        elif transferdestination not in users:
          print("That is not a user establihsed under our bank")
        elif transferdestination in users:
          transferamount = input("How much would you like to transfer?")
          if float(transferamount) < 0:
            print("Please only use positive numbers")
          elif float(transferamount) <= users[username][4]:
            users[username][4] -= float(transferamount)
            users[transferdestination][4] += float(transferamount)
            users[username][7].append([transferamount, str(datetime.now()).split(".")[0]])
            users[transferdestination][7].append([transferamount, str(datetime.now()).split(".")[0]])
            print("Transfering $" + transferamount + " to " + transferdestination + "...")
            sleep(2)
            print("\nTransfer Successful\nYour current balance is: $" + str(users[username][4]) + "\nRetunring to main menu")
            menu(users, username)
          elif float(transferamount) > users[username][4]:
            ("Insufficient funds")
          else:
            print("Invalid input")
    elif ask == "4":
      print("------- Walker Banking -------\n----- " + str(datetime.now()).split(".")[0]) + " -----\n-------------------------------\nUsername: "
      print("Username\n Password: " + users[username][1] + "\nYour Balance: $" + str(users[username][4]) + "\nUser Activities\n\n\nYour Withdrawls: \n")
      for i in users[username][6]:
        print("      " + i[1] + " withdrew $" + i[0])
      print("Your Deposits:\n")
      for i in users[username][5]:
        print("      " + i[1] + " deposited $" + i[0])
      print("Your Transfers:\n")
      for i in users[username][7]:
        print("     $" + i[0] +" transferred at " + i[1])
      print("-------------------------------\nReturning to main menu")
      menu(users, username)
    elif ask == "5":
      while True:
        passwordcheck = input("For Security Reasons, Please enter your 4 digit pin")
        if passwordcheck != users[username][3]:
          print("Incorrect Pin")
        elif passwordcheck == users[username][3]:
          newpassword = input("Please enter new password")
          users[username][1] = newpassword
          break
    elif ask =="6":
      print("Logging Out...")
      homescreen()

def admin(admins, adminname):
  global userinfo
  users = userinfo
  print("\n---- Admin Menu ----\nPlease choose a option\n1. Add User\n2. Remove User\n3. Display all Users\n4. Logout")
  while True:
    select = input("Please choose a service")
    if select == "1" or select.lower() == "add user":
      newusername = input("Please enter the new users username")
      newuserpassword = input("Please enter the new users passcode")
      newuserpin = input("Please enter this person's pin")
      newuseradmin = not not input("If this person is an admin, type something before pressing enter. ")
      if newuseradmin:
        newusermsrtpass = input("Enter this user's master password")
        newuserclearance = int(input("Enter this person's clearance"))
      else:
        newusermstrpass = False
        newuserclearance = 1
      newbalance = input("Please enter the balance of this new user")
      users[newusername] = [newusername, newuserpassword, newuseradmin, newuserpin, newbalance, [], [], [], newuserclearance, newusermstrpass]
      print(newusername + " has been added as a user")
      admin(admins, adminname)
    elif select == "2":
      while True:
        if users[adminname][8] <= 3:
          print("Denied, Authorization level is too low")
          break
        admincheck = input("Please enter master password to continue")
        if admincheck != userinfo[adminname][9]:
          print("Incorrect master password")
        else:
          removal = input("Who would you like to remove?")
          if removal not in users:
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
              users.pop(removal)
              admin(admins, adminname)
            else:
              print("Invalid Input")
    elif select == "3" or select.lower() == "display all users":
      c = 1
      for i in users:
        print("\n" + str(c) + ". "+ i + " has a balance of $" + str(users[i][4]))
        c +=1
      while True:  
        moreinfo = input("\nWould you like more info? Enter 1 for more info, else enter 2")
        if moreinfo == "1" or moreinfo.lower() == "more info":
          infouser = input("\nPlease enter the name of the account")
          if infouser not in users:
            print("Invalid Input")
          else:
            print("Username\n Password: " + str(users[infouser][1]) + "\nBalance: $" + str(users[infouser][4]) + "\nUser Activities:\n\nWithdrawls: \n")
            for i in users[infouser][6]:
              print("      " + i[1] + " " + i[0])
            print("Deposits:\n")
            for i in users[infouser][5]:
              print("      "+ i[1] + " " + i[0])
            print("Transfers:\n")
            for i in users[infouser][7]:
              print("     "+i[2]+" Transfer "+i[1]+" "+i[0])
        elif moreinfo == "2" or moreinfo.lower() == "close":
          admin(admins, adminname)
    elif select == "4" or select.lower() == "logout":
      print("Logging out...")
      sleep(1.5)
      homescreen()
    else:
      print("Bad input")

homescreen()
