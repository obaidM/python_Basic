num1 = input("please enter num1")

num2 = input("please enter num2")

if num1 > num2:
    print("Num1 is bigger than num2")

if num1< num2:
    print("Num1 is less than num2 ")

if num1== num2:
    print("Num1 and num2 are equal to eachother")

out1= "num1 was {} and num2 was {}"
output= out1.format(num1,num2)
print(output)
