def calculadora_IMC():
    print("Cálculo de IMC")
    
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite o sua altura em metros: "))
    
    IMC = peso / (altura ** 2)
    
    print(f"O seu IMC é: {IMC:.2f}")
    
    if (IMC < 17):
        print("Muito abaixo do peso")
    elif (IMC >= 17 and IMC < 18.5):
        print("Abaixo do peso")
    elif (IMC >= 18.5 and IMC < 25):
        print("Peso ideal")
    elif (IMC >= 25 and IMC < 30):
        print("Sobrepeso")
    elif (IMC >= 30 and IMC < 35):
        print("Obesidade")
    elif (IMC >= 35 and IMC < 40):
        print("Obesidade severa")
    else:
        print("Obesidade morbida")

    continuar = input("Deseja continuar na calculadora [S/N]? ").strip().upper()
    if continuar != "S":
        print("====="*10)
        menu()
    else:
        print("====="*10)
        calculadora_IMC()
               
              
def calculadora():
    print("CALCULADORA")

    n1 = int(input("Digite um número: "))
    operacao = input("Digite uma operação (+, -, *, /): ")
    n2 = int(input("Digite um número: "))

    if (operacao == "+"):
        resultado = n1 + n2
    elif (operacao == "-"):
        resultado = n1 - n2
    elif (operacao == "*"):
        resultado = n1 * n2
    elif (operacao == "/"):
        if n2 != 0:
            resultado = n1 / n2
        else:
            print("Erro: Divisão por zero não é permitida.")
            return
            
    print(f"O resultado é: {resultado}")

    continuar = input("Deseja continuar na calculadora [S/N]? ").strip().upper()
    if continuar != "S":
        print("====="*10)
        menu()
    else:
        print("====="*10)
        calculadora()       
        
def calculadora_idade():
    print("Cálculo de Idade")

    ano = int(input("Digite o ano do seu nascimento: "))
    idade = 2024 - ano

    print(f"A sua idade é: {idade}")
    continuar = input("Deseja continuar na calculadora [S/N]? ").strip().upper()
    if continuar != "S":
        print("====="*10)
        menu()
    else:
        print("====="*10)
        calculadora_idade()

def menu():
    opcao = input("""
        MENU
    
    (1) - Calculadora
    (2) - Calculadora IMC
    (3) - Calculadora IDADE
    (4) - SAIR
    """)
    if (opcao == "1"):
        print("====="*10)
        calculadora()
    elif (opcao == "2"):
        print("====="*10)
        calculadora_IMC()
    elif (opcao == "3"):
        print("====="*10)
        calculadora_idade()
    elif(opcao == "4"):
        print("====="*10)
        login()
    
def login():
    while True:
        print("LOGIN DA CONTA")
        login = input("Digite seu nome de usuario: ")
        senha = input("Digite a senha: ")
    
        if (login == "XPTO" and senha == "12345678"):
            print("ACESSO PERMITIDO")
            print("====="*10)
            menu()
            
        else:
            print("ACESSO NEGADO")
            print("====="*10)
        
login()
