import string
import random

lowercase,uppercase=list(string.ascii_lowercase),list(string.ascii_uppercase)
digits,symbols=list(string.digits),list(string.punctuation)

while True:
    try:
        userpassword_length=int(input("Enter your password length : "))
        if userpassword_length<8:
            print("Please enter your password length must be 8")
        else:
            break
    except:
        print("Dear User, please enter the digits ")


combined_lists = list(zip(lowercase,uppercase,digits,symbols))
random.shuffle(combined_lists)
lowercase,uppercase,digits,symbols=zip(*combined_lists)

alpha,number = round(userpassword_length * (30/100)),round(userpassword_length * (20/100))

password=[]
for i in range(alpha):
    password.extend([lowercase[i],uppercase[i]])
for j in range(number):
    password.extend([digits[j],symbols[j]])

random.shuffle(password)

password="".join(password)
print(f"Your password is : {password}")


