# get user email
# slice out user name
# slice out domain name
# format message
# display output message

email = input("What is your email?:")
email = email.lower().strip()

username = email[0:email.index("@"):1]

domain = email[(email.index("@")+1):]

out1= "Hello There!!, your username is: {}  and your Domain name is: {}"
output = out1.format(username,domain)

print(output)


