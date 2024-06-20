# Comparação dos Algoritmos HC, SA e GA para o problema das 8 rainhas

## Overview dos algoritmos

Hill-Climbing with Restart: algoritmo de busca local que tenta encontrar a solução ótima para um problema, ajustando iterativamente uma solução próxima à solução atual, movendo-se na direção que leva a uma melhoria no valor da função objetivo. É mais simples e direto, sem ajustes complexos e com uma resposta mais rápida. Pode ser suficiente em espaço de soluções pequeno. 

Simulated Annealing: técnica de otimização probabilística usada para encontrar a solução aproximadamente ótima de um problema, permitindo a aceitação ocasional de soluções piores do que a atual, com uma probabilidade que diminui ao longo do tempo. Isso ajuda a evitar ficar preso em mínimos locais (como pode acontecer no Hill-Climbing) e a explorar o espaço de busca de forma mais eficaz.

Genetic Algorithm: essa técnica de otimização funciona gerando uma população inicial de soluções candidatas, avaliando sua adequação por meio de uma função objetivo e, em seguida, aplicando operadores genéticos repetidamente, para evoluir as soluções ao longo de várias gerações, até que uma solução satisfatória seja encontrada ou um critério de parada seja atingido.

## O problema

O Problema das 8 rainhas consiste em encontrar uma solução para dispor 8 rainhas em um tabuleiro de Xadrez 8x8 de forma que nenhuma rainha ataque a outra.

## Parâmetros a serem considerados

- Para o HC-R, fazer um restart a cada vez que alcançar o mínimo local (20 restarts no total);
- Para o SA, defina a temperatura como 1000 e cada iteração deve reduzi-la um percentual entre 0.1% a 1%;
- Para o GA, use uma população de 20 indivíduos com 50 gerações, e probabilidade de mutação entre 5% a 20%.


## Implementação

Os códigos foram implementados em Python, utilizando bibliotecas de geração aleatória e gráficas. Foram utilizados como base os códigos disponibilizados nos notebooks Hill Climbing para a solução do problema TSP, Simulated Annealing aplicado ao problema TSP e Genetic Algorithm para o problema das 8 rainhas que foram disponibilizados e discutidos durante as aulas de Inteligência Artificial.


## Resultados e comparações

Um gráfico de caixa, ou box plot, é uma ferramenta visual para resumir a distribuição de um conjunto de dados. Ele exibe a mediana, quartis e possíveis valores extremos (outliers).
Para as análise, estamos considerando o tabuleiro inicial abaixo:

<div align="center">
    <img src="/img/tabuleiro_principal.png">
</div>

Abaixo é apresentado um gráfico com o intuito de comparar a distribuição dos dados entre os três algoritmos utilizados.

<div align="center">
    <img src="/img/custo_algoritmos.png">
</div>


|          Algoritmo         |  Máximo  |  Mínimo  |  Mediana |  Desvio padrão  |
| -------------------------- | -------- | -------- | -------- | --------------- |
| Hill-Climbing com Restart  |   4.000  |  0.000   |   1.566  |      0.773      |
| Simulated Annealing        |   2.000  |  0.000   |   0.866  |      0.434      |
| Genetic Algorithm          |   2.000  |  0.000   |   0.966  |      0.668      |


Observando a distribuição dos valores, o algoritmo HC-R tem uma média de 1.566, indicando que os valores estão acima de 1 em média, mas com uma dispersão significativa, sendo a maior entre os algoritmos. Com a mediana em 2, podemos concluir que pelo menos metade dos valores são 2 ou maior. Abaixo é apresentado um gráfico do custo de uma execução do HC-R e podemos observar uma grande variação nos resultados.

<div align="center">
    <img src="/img/hc.png">
</div>

Já no algoritmo SA, a média foi de 0.866, indicando valores abaixo de 1 em média, diferentemente do HC. O SA também apresenta um valor de dispersão menor entre os algoritmos. Pelos quartis, podemos perceber que a maioria dos valores é 1, mas conseguimos achar valores mínimos perfeitos (0).
Abaixo é apresentado um gráfico do custo de uma execução do SA e podemos observar, pelas oscilações da linha azul (custo atual), que o algoritmo está explorando diferentes soluções, algumas das quais são piores e outras melhores. A estabilização da linha laranja (melhor custo) depois da iteração 10, indica que o algoritmo encontrou uma solução ótima ou quase ótima. A maior mudança do algoritmo nas primeiras iterações, sugere uma eficiência em encontrar uma boa, nem sempre ótima, solução mais rapidamente.

<div align="center">
    <img src="/img/sa.png">
</div>

Observando os resultados do algoritmo GA, vimos que a média é de 0.967, que assim como o HC, indica que  os valores estão mais próximos de 1. Pelo desvio padrão, podemos ver a indicação de uma distribuição semelhante ao do algoritmo SA, porém ele apresenta uma tendência a valores maiores, assim como o HC. Teve um comportamento semelhante ao do SA nos quartis.
Considerando o comportamento dos algoritmos, o HC ter tido valores maiores nos mostra que ele ficou preso em um mínimo local, a desvantagem do algoritmo em comparação com os demais. O desvio padrão maior que os outros também indica maior variabilidade no resultado, provavelmente porque a cada iteração, ele ficou preso em mínimos locais bem diferentes. O SA teve um desvio padrão menor, o que sugere maior consistência nos resultados e na média produz resultados mais baixos.

## Conclusão

Hill-Climbing é o algoritmo com maior média e maior variabilidade dos custos, o que pode indicar que ele produz resultados mais altos, mas menos consistentes. Simulated Annealing tem a menor média e variabilidade, sugerindo resultados mais baixos e mais consistentes. Genetic Algorithm está no meio-termo, com uma média ligeiramente superior ao Simulated Annealing e variabilidade moderada, sugerindo que pode ser uma boa escolha para cenários onde se busca um balanço entre a qualidade da solução e a consistência.