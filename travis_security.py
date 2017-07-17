known_users=["Alice","Bob","Claire","Dan","Emma","Fred","George","Harry"]

print(known_users)
print(len(known_users))

while True:
    print("WELCOME TO TRAVIS SECURITY SYSTEM")
    name = input("what is your name?:").strip().capitalize()

    if name in known_users:
       print("Hello {}".format(name))
       remove= input("Would you like to be remove from the system (y/n)").lower()
       if remove == "y":
           known_users.remove(name)
           print(known_users)
       elif remove == "n":
           print("no problem {}".format(name))
       
    else:
       print("Hmm, I don't think I have met you yet {}".format(name))
       add_me = input("Would you like to be added to the system (y/n)").strip().lower()
       if add_me == "y":
          known_users.append(name)
          print(known_users)
       elif add_me == "n":
            print("No worries {}".format(name))
