#A) Leia 3 Nomes, e para cada nome 3 notas, calcule a média dos alunos e ao final escreva "Aprovado" para notas maiores que 5 e "Reprovado" para notas menores que 6.
para isso use quantas variáveis forem necessárias.

#EU FIZ MEU CÓDIGO NO VISUALG, SE PRETENDE TESTA-LO COPIE A PARTIR DA LINHA 7 ATE A LINHA 61.


algoritmo "Avaliação de Notas"
var
   nomes: vetor[1..3] de caractere
   notas: vetor[1..3, 1..3] de numerico
   linha, coluna: inteiro
   nome1, status: caractere
   n1, n2, n3, media: numerico
inicio
para linha de 1 ate 3 faca
          Escreval("Digite o nome do aluno: ")
          leia(nome1)
          nomes[linha] <- nome1
          
          Escreval("Digite a primeira nota do aluno: ")
          Leia(n1)
          notas[linha,1] <- n1
          
          Escreval("Digite a segunda nota do aluno: ")
          Leia(n2)
          notas[linha,2] <- n2
          
          Escreval("Digite a terceira nota do aluno: ")
          Leia(n3)
          notas[linha,3] <- n3

          media <- (n1 + n2 + n3) / 3

          se media < 6 entao
            status <- ("REPROVADO!")
          senao
            status <- ("APROVADO!")
          Fimse


Escreva("Nome: ", nome1)
Escreva(" Notas: ", n1, n2, n3)
Escreva(" Média: ", media)
Escreval(" Situação: ", status)
fimpara

escreval("===================================================================")

Escreval("Nome            |   N1  |   N2  |   N3  | Média | Situação  |")
Escreval("--------------------------------------------------------------")

para linha de 1 ate 3 faca
       Escreva(nomes[linha]:15, " | ")
       Escreva(notas[linha,1]:5:2, " | ")
       Escreva(notas[linha,2]:5:2, " | ")
       Escreva(notas[linha,3]:5:2, " | ")
       Escreva((notas[linha,1] + notas[linha,2] + notas[linha,3]) / 3:5:2, " | ")
       Escreval(status, " | ")

fimpara
fimalgoritmo
