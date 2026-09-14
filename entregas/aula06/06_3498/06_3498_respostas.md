# Análise de complexidade

O PilhaEncadeada._reorganizar tem uma complexidade no pior caso de O(N), pois, caso a pilha de saida esteja vazia, torna-se necessário passar por todos os N elementos da pilha de entrada e inserí-los na pilha da saída.

Mas, isso não ocorre em toda execução. Em específico, cada elemento é processado no máximo 3 vezes: uma vez ao ser inserido na pilha de entrada, outra vez ao ser inserido na pilha de saída e, pela última vez, ao ser retirado da pilha de saída. 

Por isso, a complexidade de desenfileirar pode ser amortizada em O(3) = O(1).

