import random
x = 1
while (x == 1):
    perguntaDado = input("qual dado? ")
    quant = int(perguntaDado.split("d")[0])
    dado = int(perguntaDado.split("d")[1])
    # print(dado)
    giro = 1
    total = 0
    while (giro <= quant):
        if dado == 4:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 6:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 8:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 10:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 12:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 16:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 20:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        elif dado == 100:
            num = random.randint(1, dado)
            print(giro, "dado:", num)
            giro += 1
        else:
            print("tem não parça")
        
        total += num
    print("total:" , total)
