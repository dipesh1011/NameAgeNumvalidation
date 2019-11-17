num = input("Enter the number to calculate multiplication table:")
while(num.isdigit() == False):
    print("Enter a integer number:")
    num = input("Enter the number to calculate multiplication table:")
print("***************************")
print("Multiplication table of",num,"is:")
for i in range(1, 11):
    res = int(num) * i
    print(num,"*",i,"=",res)