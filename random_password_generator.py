import random
import string

l=int(input("Enter length of password"))
print("choose character set  password for these\n 1. Digits\n 2.Letters\n 3-Special Characters\n 4.Exit")
c=""
while(True):
  choice=int(input("Select from above options"))
  if(choice==1):
    c+=string.ascii_letters
  elif(choice==2):
    c+=string.digits
  elif(choice==3):
    c+=string.punctuation
  elif(choice==4):
    break
  else:
    print("please select valid option")
password=[]
for i in range (l):
  randchar=random.choice(c)
  password.append(randchar)


print("password is "+"".join(password))