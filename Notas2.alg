#A) Leia 3 Nomes, e para cada nome 3 notas, calcule a média dos alunos e ao final escreva "Aprovado" para notas maiores que 5 e "Reprovado" para notas menores que 6.
para isso use quantas variáveis forem necessárias.

#EU FIZ MEU CÓDIGO NO VISUALG, SE PRETENDE TESTA-LO COPIE A PARTIR DA LINHA 7 ATE A LINHA 56.


algoritmo "Avaliação de Notas"
var
   nomes, status: vetor[1..3] de caractere
   notas: vetor[1..3, 1..3] de numerico
   linha, coluna: inteiro
   media: numerico
inicio
para linha de 1 ate 3 faca
          Escreva("Digite o nome do aluno: ")
          leia(nomes[linha])

          Escreva("Digite a primeira nota do aluno: ")
          Leia(notas[linha,1])

          Escreva("Digite a segunda nota do aluno: ")
          Leia(notas[linha,2])

          Escreva("Digite a terceira nota do aluno: ")
          Leia(notas[linha,3])

          media <- (notas[linha,1] + notas[linha,2] + notas[linha,3]) / 3

          se media < 6 entao
            status[linha] <- ("REPROVADO!")
          senao
            status[linha] <- ("APROVADO!")
          Fimse


Escreva("Nome: ",nomes[linha]," | ")
Escreva(" Notas:",notas[linha,1],notas[linha,2],notas[linha,3]," | ")
Escreva(" Média:", media:5:2," | ")
Escreval(" Situação: ", status[linha]," | ")
fimpara

escreval("===================================================================")

Escreval("Nome            |   N1  |   N2  |   N3  | Média | Situação    |")
Escreval("--------------------------------------------------------------")

para linha de 1 ate 3 faca
       Escreva(nomes[linha]:15, " | ")
       Escreva(notas[linha,1]:5:2, " | ")
       Escreva(notas[linha,2]:5:2, " | ")
       Escreva(notas[linha,3]:5:2, " | ")
       Escreva((notas[linha,1] + notas[linha,2] + notas[linha,3]) / 3:5:2, " | ")
       Escreval(status[linha]:11, " | ")

fimpara
fimalgoritmo
