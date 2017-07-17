import random

health = 50
#dfc stands for difficuilty level

dfc = 3

potion_health= random.randint(25,50)


health = (health + potion_health) / dfc

print (health)
