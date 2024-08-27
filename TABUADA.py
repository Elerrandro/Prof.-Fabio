import os
#FUNÇÃO PARA LIMPAR TELA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


print("MENU")
print("ESCOLHA ENTRE AS OPÇÕES ABAIXO")
print("1 - Escolha a operação e o número (+, -, *, /)")
print("2 - Escolha somente a operação, Tabuada Completa! (+, -, *, /)")
print("3 - SAIR")
opcao = int(input("Digite aqui o número: "))

limpar_tela() #VAI LIMPAR A TELA ANTES DE CONTINUAR

if opcao == 1:
    print("Qual operação vai querer utilizar?")
    print("Escolha entre as seguintes opções")
    print("(+, -, *, /)")
    operacao = str(input("Digite aqui: "))
    numero = int(input("Qual o número da tabuada você quer: "))
