# Comparação dos Algoritmos HC, SA e GA para o problema das 8 rainhas

## Overview dos algoritmos

Hill-Climbing with Restart: algoritmo de busca local que tenta encontrar a solução ótima para um problema, ajustando iterativamente uma solução próxima à solução atual, movendo-se na direção que leva a uma melhoria no valor da função objetivo.

Simulated Annealing: técnica de otimização probabilística usada para encontrar a solução aproximadamente ótima de um problema, permitindo a aceitação ocasional de soluções piores do que a atual, com uma probabilidade que diminui ao longo do tempo. Isso ajuda a evitar ficar preso em mínimos locais e a explorar o espaço de busca de forma mais eficaz.

Genetic Algorithm: essa técnica de otimização funciona gerando uma população inicial de soluções candidatas, avaliando sua adequação por meio de uma função objetivo e, em seguida, aplicando operadores genéticos repetidamente, para evoluir as soluções ao longo de várias gerações, até que uma solução satisfatória seja encontrada ou um critério de parada seja atingido.

## O problema

O Problema das 8 rainhas consiste em encontrar uma solução para dispor 8 rainhas em um tabuleiro de Xadrez 8x8 de forma que nenhuma rainha ataque a outra.

## Parâmetros a serem considerados

Para o HC-R, fazer um restart a cada vez que alcançar o mínimo local (20 restarts no total);
Para o SA, defina a temperatura como 1000 e cada iteração deve reduzi-la um percentual entre 0.1% a 1%;
Para o GA, use uma população de 20 indivíduos com 50 gerações, e probabilidade de mutação entre 5% a 20%.


## Implementação

Os códigos foram implementados em Python, utilizando bibliotecas de geração aleatória e gráficas. Foram utilizados como base os códigos disponibilizados nos notebooks Hill Climbing para a solução do problema TSP, Simulated Annealing aplicado ao problema TSP e Genetic Algorithm para o problema das 8 rainhas que foram disponibilizados e discutidos durante as aulas de Inteligência Artificial.


## Resultados



## Comparação



## Conclusão