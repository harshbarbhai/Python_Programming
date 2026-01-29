print("Enter first number: ")
No1=input()

print("Enter Second number: ")
No2=input()

print(type(No1))
print(type(No2))

#Ans=No1+No2 #in will concate not add 
Ans=int(No1)+int(No2)

print(type(No1)) #not int because type cast int only for that line
print(type(No2)) #not int because type cast int only for that line

print("Addition is: ",Ans)


