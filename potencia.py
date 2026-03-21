while True:
    base = int(input("Base: "))
    expoente = int(input("Expoente: "))
    if base == 0:
        print("-----------------------------------calma pai-----------------------------------------")
        print("-------------------------------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------------")
        potencia = base ** expoente
        print("Potência:", base, "**", expoente, "=", potencia)
        
        