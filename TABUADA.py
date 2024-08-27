print("MENU")
print("ESCOLHA ENTRE AS OPÇÕES ABAIXO")
print("1 - Escolha a operação e o número (+, -, *, /)")
print("2 - Escolha somente a operação, Tabuada Completa! (+, -, *, /)")
print("3 - SAIR")
opcao = int(input("Digite aqui o número: "))

if opcao == 1:
    print("Qual operação vai querer utilizar?")
    print("Escolha entre as seguintes opções")
    print("(+, -, *, /)")
    operacao = str(input("Digite aqui: "))
    numero = int(input("Qual o número da tabuada você quer: "))

    if operacao == "+":
        for x in range(1, 11):
            print(numero, " + ", x, " = ", numero + x)
    elif operacao == "-":
        for x in range(1, 11):
            print((x + numero), " - ", numero, " = ", (x + numero) - numero)
    elif operacao == "*":
        for x in range(1, 11):
            print(numero, " * ", x, " = ", numero * x)
    elif operacao == "/":
        for x in range(1, 11):
            print((x * numero), " / ", numero, " = ", (x * numero) / numero)

if opcao == 2:
    print("Qual operação vai querer utilizar?")
    print("Escolha entre as seguintes opções")
    print("(+, -, *, /)")
    operacao = str(input("Digite aqui: "))

    if operacao == "+":
        print("Aqui está sua tabuada completa!")
        for numero in range(1, 11):
            print("==================")
            for x in range(1, 11):
                print(numero, " + ", x, " = ", numero + x)
    elif operacao == "-":
        print("Aqui está sua tabuada completa!")
        for numero in range(1, 11):
            print("==================")
            for x in range(1, 11):
                print((x + numero), " - ", numero, " = ", (x + numero) - numero)
    elif operacao == "*":
        print("Aqui está sua tabuada completa!")
        for numero in range(1, 11):
            print("==================")
            for x in range(1, 11):
                print(numero, " x ", x, " = ", numero * x)
    elif operacao == "/":
            print("Aqui está sua tabuada completa!")
            for numero in range(1, 11):
                print("==================")
                for x in range(1, 11):
                    print((x * numero), " / ", numero, " = ", (x * numero) / numero)

if opcao == 3:
    print("ENCERRANDO CÓDIGO PYTHON")
