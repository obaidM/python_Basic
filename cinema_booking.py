films = {

    "Finding Dory": {"min_age":3, "tickets":5},
    "Tarzan": {"min_age":13,"tickets":11},
    "Crash": {"min_age":17,"tickets":3}
    }

while True:

       
       choice = input("What would you like to watch?:").strip().title()
       if choice in films:
           age = int(input("how old are you ?:"))
           if age < films[choice]["min_age"]:
              print("You are too young to watch {}".format(choice))
           else:
              if films[choice]["tickets"] >0:
                 films[choice]["tickets"]= films[choice]["tickets"] -1
                 if films[choice]["tickets"] == 0:
                    print ("We are sorry {} is sold out".format(choice))
                 else:
                    print("tickets left for {}: {}".format(choice,films[choice]["tickets"]) )                                                 
                    print("Enjoy {}".format(choice))
       else:
          print("Sorry, we don't have that film")
       
