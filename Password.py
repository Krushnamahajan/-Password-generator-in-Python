import random
chars = "1234567890qwertyuiopasdfghjklzxcvbnm,./!@#$%^&*()_+~"
length = int(input("Enter Length : "))
password = ""

for a in range(length):
    password +=random.choice(chars)
    print(password)
