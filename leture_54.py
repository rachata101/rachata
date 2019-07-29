def login():
    userName = input("username:")
    passWord = input("password:")
    if userName == "admin" and passWord == "1234":
        return showmenu()
    else:
        print("Wrong Username Or Password")
        return login()


def showmenu():
    print("----Shopee----")
    print("1.Vat Calculator")
    print("2.Price calculator")
    return menuSelect()


def menuSelect():
    userselected = int(input(">>"))
    if userselected == 1:
        return vatCalcultor(int(input("totalprice:")))
    elif userselected == 2:
        return priceCalculator()
    else:
        return showmenu()


def vatCalcultor(totalprice):
    vat = 7 / 100
    result = totalprice + (totalprice * vat)
    return print(result)


def priceCalculator():
    price1 = int(input("product price1:"))
    price2 = int(input("product price2:"))
    return vatCalcultor(price1 + price2)


login()