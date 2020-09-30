##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
count=0
uName=input("Enter a username: ").strip
pWord=input("Enter a password: ").strip
while uName!="admin" or pWord!="12345":
    print("Access denied")
    count=count+1
    uName=input("Enter a username: ").strip
    pWord=input("Enter a password: ").strip
    if count>1:
        break
if uName=="admin" and pWord=="12345":
    print("Access granted")
