menuList = []
Price = []


def bill():
    total = 0
    print("---Calculator---")
    for number in range(len(menuList)):
        print(menuList[number], Price[number])
        total += int(Price[number])
    print(total)


while True:
    menuName = input("Menu:")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price:"))
        menuList.append(menuName)
        Price.append(menuPrice)

bill()
