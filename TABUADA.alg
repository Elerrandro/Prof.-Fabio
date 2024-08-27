//PRÁTICA DE ALGORITMO
//1) Desenvolva um algoritmo e um programa em python. Que escreva na tela uma tabuada dinâmica com todas as seguintes operações(+,-,*,/).

algoritmo "TABUADA"
var
  numero, opcao, x: inteiro
  operacao: caractere
inicio
//MENU SIMPLES
escreval("MENU")
escreval("ESCOLHA ENTRE AS OPÇÕES ABAIXO")
escreval("1 - Qual a operação que você quer usar? (+, -, *, /). ")
escreval("2 - tabuada completa! (+, -, *, /). ")
escreval("3 - Sair ")
escreva("Digite aqui o número: ")

leia(opcao) //lê a escolha do usuario

limpatela  //VAI LIMPAR A TELA

se opcao = 1 entao //ESTRUTURA CONDICIONAL
   escreval("Qual a operação vai querer usar?")
   escreval("Escolha entre (+, -, *, /)")
   escreva("Digite aqui: ")
   leia(operacao)
   escreval("Qual o número da tabuada que você quer?")
   leia(numero)
limpatela
//AQUI COMEÇA O ALGORITMO DA TABUADA!
//SOMA
    se operacao = "+" entao
       escreval("Aqui está sua tabuada!")
       para x de 1 ate 10 passo 1 faca
            escreval(numero, " +", x, " = ", numero + x)
       fimpara
    fimse
//SUBTRAÇÃO
    se operacao = "-" entao
       escreval("Aqui está sua tabuada!")
       para x de 1 ate 10 passo 1 faca
            escreval((x + numero), " -", numero, " = ", (x + numero) - numero)
       fimpara
    fimse
//MULTIPLICAÇÃO
    se operacao = "*" entao
       escreval("Aqui está sua tabuada!")
       para x de 1 ate 10 passo 1 faca
            escreval(numero, " x", x, " = ", numero * x)
       fimpara
    fimse
//DIVISÃO
    se operacao = "/" entao
       escreval("Aqui está sua tabuada!")
       para x de 1 ate 10 passo 1 faca
            escreval((x * numero), " /", numero, " = ", (x * numero) / numero)
       fimpara
    fimse
fimse
//ESTRUTURA CONDICIONAL
se opcao = 2 entao
   escreval("Qual a operação vai querer usar?")
   escreval("Escolha entre (+, -, *, /)")
   escreva("Digite aqui: ")
   leia(operacao)
limpatela
//TABUADA COMPLETA DE SOMA
     se operacao = "+" entao
     escreval("Aqui sua Tabuada Completa!")
     escreval("===========================")
         para numero de 1 ate 10 passo 1 faca
              para x de 1 ate 10 passo 1 faca
                   escreval(numero, " +", x, " = ", numero + x)
              fimpara
              escreval("===============")//LINHA DE SEPARAÇÃO
         fimpara
     fimse
//TABUADA COMPLETA DE SUBTRAÇÃO
     se operacao = "-" entao
     escreval("Aqui sua Tabuada Completa!")
     escreval("===========================")
         para numero de 1 ate 10 passo 1 faca
              para x de 1 ate 10 passo 1 faca
                   escreval((x + numero), " -", numero, " = ", (x + numero) - numero)
              fimpara
              escreval("===============")//LINHA DE SEPARAÇÃO
         fimpara
     fimse
//TABUADA COMPLETA DE MULTIPLICAÇÃO
     se operacao = "*" entao
     escreval("Aqui sua Tabuada Completa!")
     escreval("===========================")
         para numero de 1 ate 10 passo 1 faca
              para x de 1 ate 10 passo 1 faca
                   escreval(numero, " x", x, " = ", numero * x)
              fimpara
              escreval("===============")//LINHA DE SEPARAÇÃO
         fimpara
     fimse
//TABUADA COMPLETA DE DIVISÃO
     se operacao = "/" entao
     escreval("Aqui sua Tabuada Completa!")
     escreval("===========================")
         para numero de 1 ate 10 passo 1 faca
              para x de 1 ate 10 passo 1 faca
                   escreval((x * numero), " /", numero, " = ", (x * numero) / numero)
              fimpara
              escreval("===============")//LINHA DE SEPARAÇÃO
         fimpara
     fimse
fimse

se opcao = "3" entao
   escreval("ENCERRANDO ALGORITMO!")
fimse
fimalgoritmo
