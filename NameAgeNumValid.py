import sys

fname = input("Enter your  First Name:")
lname = input("Enter your Last Name:")


#if len(name) == 0:
while(len(fname) == 0):
        print("First name cant be null!!")
        fname = input("Enter your first name:")
#elif len(name) < 4 or name.isalpha() != True:
while(len(fname) < 4 or fname.isalpha() != True):
        print("Please enter a valid first name")
        fname = input("Enter your first name:")

while(len(lname) == 0):
        print("Last Name cant be null!!")
        lname = input("Enter your Last Name:")
#elif len(name) < 4 or name.isalpha() != True:
while(len(lname) < 2 or lname.isalpha() != True):
        print("Please enter a valid last name:")
        lname = input("Enter your Last Name:")

age = input("Enter your age:")
lim = 150
#if len(age) == 0:
while(len(age) == 0):
    print("Age cant be null")
    age = input("Enter your age:")
#elif((int(age) > lim) or (age.isdigit() == False)):
while((age.isdigit() == False) or (int(age) > lim)):
    print("Please enter a valid age")
    age = input("Enter your age")

cnum = input("Enter your mobile number:")
#if len(cnum) == 0:
while(len(cnum) == 0):
    print("Mobile number cant be null")
    cnum = input("Enter your mobile number")
#elif((int(len(cnum)) != 10) or (cnum.isdigit() != True)):
while((int(len(cnum)) != 10) or (cnum.isdigit() != True)):
    print("Enter a valid mobile number")
    cnum = input("Enter your mobile number")

print("*****************************")
print("Name:",fname,lname)
print("Age:",age)
print("Mobile number:",cnum)
