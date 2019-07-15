Bag = 250
coffee = 50
cake = 25
username = input("Username :")
password = input("Password :")

if username == "rachata" and password == "1234":
    print("Welcome to shopee")
    print("1.Bag = 250 THB")
    print("2.coffee = 50 THB")
    print("3.cake = 25 THB")
    userSelected = int(input("Product :"))
    if userSelected == 1:
        ea = int(input("ea:"))
        price = Bag * ea
        print("result :",price,"THB")

    elif userSelected == 2:
        ea = int(input("ea:"))
        price = coffee * ea
        print("result :",price,"THB")

    elif userSelected == 3:
        ea = int(input("ea:"))
        price = cake * ea
        print("result :", price, "THB")
    else:
        print("ERROR")
