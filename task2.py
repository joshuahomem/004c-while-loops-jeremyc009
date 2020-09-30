#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
uName=(input("Enter a username: ").strip()
pWord=(input("Enter a password: ").strip()
while uName!="admin" or pWord!= "12345":
    print("Access denied")
    uName=(input("Enter a username: ").strip()
    pWord=(input("Enter a password: ").strip()
    if uName=="admin" and pWord=="12345":
        print("Access granted")