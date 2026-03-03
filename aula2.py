import random
x = 1
while(x == 1) :
    resp1 = input("Cual dado: ")
    if resp1 == "1d6":
        resp = input("Roll dice? y/n: ")
        if resp == "y":
            num = random.randint(1, 6)
            print(num)
        elif resp == "n":
            print("tabom..")
            x += 1
    
    elif resp1 == "1d4":
        resp = input("Roll dice? y/n: ")
        if resp == "y":
            num = random.randint(1, 4)
            print(num)
        elif resp == "n":
            print("tabom..")
            
    
    elif resp1 == "1d10":
        resp = input("Roll dice? y/n: ")
        if resp == "y":
            num = random.randint(1, 10)
            print(num)
        elif resp == "n":
            print("tabom..")
            

    elif resp1 == "1d20":
        resp = input("Roll dice? y/n: ")
        if resp == "y":
            num = random.randint(1, 20)
            print(num)
        elif resp == "n":
            print("tabom..")

