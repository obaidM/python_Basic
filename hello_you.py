# ask user for name
# ask user their age
# ask user for city
# ask user what they enjoy
 # create output text
 # we will learn input and output

name = input("what is your name?:")
age = input("what is your age?:")
city = input ("what is your city?:")
enjoy = input ("what do you enjoy?:")

out1= "Hello {}, you are {}years old , you live in {} and you enjoy {}"

output= out1.format(name, age,city,enjoy)
print(output)
