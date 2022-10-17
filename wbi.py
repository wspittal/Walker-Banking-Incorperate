from datetime import datetime; from time import sleep


users = {"Spencer Karby":"l + bozo + ratio", "Owen Reaser":"academic weapon", "Michael Tomczak":"Genius", "Parker Dillon": "69420"}
use = ["Spencer Karby", "Owen Reaser", "Michael Tomczak", "Parker Dillon"]
admins = {"Walker Spittal":{"adminpass": "Hamilton is awesome", "masterpassword": "Avery", "clearance": 8}, "Avery Lassiter":{"adminpass": "coolest person alive", "masterpassword": "Walker", "clearance": 4}}
userinfo = {"Spencer Karby":{"balance":10, "deposits":[], "withdrawals":[], "transfers":[], "pin": "1234"}, "Owen Reaser":{"balance":100000, "deposits":[], "withdrawals":[], "transfers":[], "pin": "7676"}, "Michael Tomczak":{"balance":904730957, "deposits":[], "withdrawals":[], "transfers":[], "pin": "8888"}, "Parker Dillon":{"balance":9820939709827390, "deposits":[], "withdrawals":[], "transfers":[], "pin": "1234"}}

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
              userlogin(users)
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
      print("Invalid Username")
    elif int(password) != users[username]:
      print("Wrong Password")
    else:
      print("Welcome " + username)
      menu(users, userinfo, username, password)

def adminlogin(admins):
  while True:  
    adminname = input("\nEnter admin username: ")
    if adminname not in admins:
      print("Invalid Username, Please try again")
      adminlogin(admins)
    adminpassword = input("Enter password: ")
    if adminpassword != admins[adminname]["adminpass"]:
      print("Invalid Password, Please try again")
    else:
      print("\nWelcome " + adminname)
      admin(users, userinfo, admins, adminname)

def menu(users, userinfo, username, password):
  print("1. Please enter the service number\n1. Withdraw Money\n2. Deposit Money\n3. Transfer Money\n4. My Account Information\n5. Change Password\n6. bLogout")
  while True:
    ask = input("Please choose a service")
    if ask == "1":
      withdrawl = input("Please enter withdrawl amount")
      if float(withdrawl) <= userinfo[username]["balance"]:
        userinfo[username]["balance"] -= float(withdrawl)
        userinfo[username]["withdrawals"].append((withdrawl, str(datetime.now()).split(".")[0]))
        print(str(withdrawl) + "$ withdrawn from your account\nnew balance: $" + str(userinfo[username]["balance"]) + "\nReturning to main menu...")
        menu(users, userinfo, username, password)
      elif float(withdrawl) > userinfo[username]["balance"]:
        print("You don't have enough money, your current balance is: " + str(userinfo[username]["balance"]))
      else:
        print("Bad Input")
    elif ask == "2":
      while True:  
        deposit = input("How much would you like to deposit")
        userinfo[username]["balance"] += float(deposit)
        userinfo[username]["deposits"].append((deposit, str(datetime.now()).split(".")[0]))
        print(deposit + "$ had been added to your account\nnew balance: " + userinfo[username]["balance"] + "\nResturning to main menu...")
        menu(users, userinfo, username, password)
    elif ask == "3":
      print("If you want to abort the transfer enter abort")
      while True:
        transferdestination = input("Who would you like to transfer funds to")
        if transferdestination.lower() == "abort":
          print("Returning to main menu...")
          menu(users, userinfo, username, password)
        elif transferdestination not in users:
          print("That is not a user establihsed under our bank")
        elif transferdestination in users:
          transferamount = input("How much would you like to transfer?")
          if float(transferamount) < 0:
            print("Please only use positive numbers")
          elif float(transferamount) <= userinfo[username]["balance"]:
            userinfo[username]["balance"] -= float(transferamount)
            userinfo[transferdestination]["balance"] += float(transferamount)
            userinfo[username]["transfers"].append((transferamount, str(datetime.now()).split(".")[0]))
            userinfo[transferdestination]["transfers"].append((transferamount, str(datetime.now()).split(".")[0]))
            print("Transfering " + transferamount + "$ to " + transferdestination + "...")
            sleep(2)
            print("\nTransfer Successful\nYour current balance is: " + str(userinfo[username]["balance"]) + "$\nRetunring to main menu")
            menu(users, userinfo, username, password)
          elif float(transferamount) > userinfo[username]["balance"]:
            ("Insufficient funds")
          else:
            print("Invalid input")
    elif ask == "4":
      print("------- Walker Banking -------\n----- " + str(datetime.now()).split(".")[0]) + " -----\n-------------------------------\nUsername: "
      print("Username\n Password: " + password + "\nYour Balance: " + str(userinfo[username]["balance"]) + "$\nUser Activities\n\n\nYour Withdrawls: \n")
      for i in userinfo[username]["withdrawls"]:
        print("      " + i[1] + " " + i[0])
      print("Your Deposits:\n")
      for i in userinfo[username]["Deposits"]:
        print("      "+ i[1] + " " + i[0])
      print("\n\nYour Transfers:\n")
      for i in userinfo[username]["Transfers"]:
        print("     "+i[2]+" Transferred to "+i[1]+" "+i[0])
      print("-------------------------------\nReturning to main menu")
      menu(users, userinfo, username, password)
    elif ask == "5":
      while True:
        passwordcheck = input("For Security Reasons, Please enter your 4 digit pin")
        if passwordcheck != userinfo[username]["pin"]:
          print("Incorrect Pin")
        elif passwordcheck == userinfo[username]["pin"]:
          newpassword = input("Please enter new password")
          userinfo[username]["password"].replace(newpassword)
    elif ask =="6":
      print("Logging Out...")
      homescreen()

def admin(users, userinfo, admins, adminname):
  print("\n---- Admin Menu ----\nPlease choose a option\n1. Add User\n2. Remove User\n3. Display all Users\n4. Logout")
  while True:  
    select = input("Please choose a service")
    if select == "1" or select.lower() == "add user":
      newusername = input("Please enter the new users username")
      newuserpassword = input("Please enter the new users passcode")
      users[newusername] = newuserpassword
      newbalance = input("Please enter the balance of this new user")
      userinfo[newusername] = {"balance": float(newbalance), "deposits": [], "withdrawls": [], "transfers": []}
      print(newusername + " has been added as a user")
      admin(users,userinfo, admins, adminname)
    elif select == "2":
      while True:
        if admins[adminname]["clearance"] <= 3:
          print("Denied, Authorization level is too low")
          break
        admincheck = input("Please enter masterpassword to continue")
        if admincheck != admins[adminname]["masterpassword"]:
          print("Incorrect masterpassword")
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
              admin(users, userinfo, admins, adminname)
            elif confirmation == "2":
              print("removing....")
              sleep(2)
              print("User removed")
              users.pop(removal)
              userinfo.pop(removal)
              admin(users, userinfo, admins, adminname)
            else:
              print("Invalid Input")
    elif select == "3" or select.lower() == "display all users":
      c = 1
      for i in users:
        print("\n" + str(c) + ". "+ i + " " + users[i])
        c +=1
      while True:  
        moreinfo = input("\nWould you like more info? Enter 1 for more info, else enter 2")
        if moreinfo == "1" or moreinfo.lower() == "more info":
          infouser = input("\nPlease enter the name of the account")
          if infouser not in users:
            print("Invalid Input")
          else:
            print("Username\n Password: " + str(users[infouser]) + "\Balance: " + str(userinfo[infouser]["balance"]) + "$\nUser Activities\n\n\nWithdrawls: \n")
            for i in userinfo[infouser]["withdrawals"]:
              print("      " + i[1] + " " + i[0])
            print("Deposits:\n")
            for i in userinfo[infouser]["deposits"]:
              print("      "+ i[1] + " " + i[0])
            print("Transfers:\n")
            for i in userinfo[infouser]["transfers"]:
              print("     "+i[2]+" Transfer "+i[1]+" "+i[0])
        elif moreinfo == "2" or moreinfo.lower() == "close":
          admin(users, userinfo, admins, adminname)
    elif select == "4" or select.lower() == "logout":
      print("Logging out...")
      sleep(1.5)
      homescreen()
    else:
      print("Bad input")

homescreen()
