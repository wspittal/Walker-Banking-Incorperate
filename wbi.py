from datetime import datetime; from time import sleep


users = {"Spencer Karby":"l + bozo + ratio", "Owen Reaser":"academic weapon", "Michael Tomczak":"Genius"}
admins = {"Walker Spittal":{"adminpass": "Hamilton is awesome", "masterpassword": "Avery", "authority": 8}, "Avery Lassiter":{"adminpass": "coolest person alive", "masterpassword": "Walker", "authority": 4}}
userinfo = {"Spencer Karby":{"balance":10, "deposits":[], "withdrawals":[], "transfers":[], "pin": "1234"}, "Owen Reaser":{"balance":100000, "deposits":[], "withdrawals":[], "transfers":[], "pin": "7676"}, "Michael Tomczak":{"balance":904730957, "deposits":[], "withdrawals":[], "transfers":[], "pin": "8888"}}

def homescreen():
    print("     --- Welcome to Walker Banking ---\n         -------------------\n        /     Raleigh NC    \ \n        |"+ str(datetime.now()).split(".")[0] + "|\n        \                   /\n         -------------------\n\n1. Login\n2. Exit")
    while True:
      enter = input("Please choose a service: ")
      if enter == "1" or enter.lower() == "login":
        while True:
          print("\nWhat do you want to login as:\n1. Admin\n2. User\n3. Go Back")
          answer = input("Please choose a service: ")
          if answer == "1" or answer.lower() == "admin":
            while True:  
              adminname = input("\nEnter admin username")
              adminpassword = input("Enter password: ")
              if adminname not in admins:
                print("Invalid Username, Please try again")
              elif adminpassword != admins[adminname]["adminpass"]:
                print("Invalid Password, Please try again")
              else:
                print("Welcome " + adminname)
                admin(users, userinfo, admins, adminname)
          elif answer == "2" or answer.lower == "user":
              userlogin(users)
          elif answer == "3" or answer.lower() == "go back":
              homescreen()
          else:
            print("Bad Input")
      elif enter == "2":
        exit()
      else:
        print("Bad Input")
def userlogin(users):
  while True:
    username = input("\nEnter Username")
    password = input("Enter Password")
    if username not in users:
      print("Invalid Username")
    elif password != users[username]:
      print("Wrong Password")
    else:
      print("Welcome " + username)
      break
  menu(users, userinfo, username, password)
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
  print("---- Admin Menu ----\nPlease choose a option\n1. Add User\n2. Remove User\n3.Display All Users\n4. Logout")
  while True:  
    select = input("CHOOSE")
    if select == "1":
      newusername = input("Please enter the new users username")
      newuserpassword = ("Please enter the new users passcode")
      users[newusername] = newuserpassword
      newbalance = input("Please enter the balance of this new user")
      userinfo[newusername] = {"balance": float(newbalance), "deposits": [], "withdrawls": [], "transfers": []}
      print(newusername + "was added as a user")
      admin(users,userinfo, admins, adminname)
    if select == "2":
      if admins[adminname]["authority"] >= 3:
        print("Denied, Authorization level is too low")
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
              print("Cancelling")
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
      
def admin(users, userinfo):
  print("")
              
              
homescreen()
