import AulasPraticas.AP_03_ordenacao as ord
import random
import time
import sys

K_REPETICOES = 50
INT_MAX = int(1e8)
sys.setrecursionlimit(10000)


def instanciaAleatoria(N:int) -> list:
    """Gera uma lista com N inteiros aleatórios.
    
        Utiliza a constante INT_MAX para gerar N inteiros no intervalo [0, INT_MAX]. Este
        será considerado como caso médio.
        
        Args:
            N (int): O tamanho da lista a ser gerada
            
        Returns:
            list: Lista com N inteiros aleatórios
    """
    instancia = [ random.randint(0, INT_MAX) for i in range(N) ]
    return instancia

def instanciaReversa(N: int) -> list:
    """Gera uma lista com N inteiros ordenados inversamente.
        
            Os inteiros começam do N e vão até o 1, logo, o retorno é algo próximo de 
            [N, N-1, N-2, ..., 3, 2, 1]. Este vai ser o pior caso para o QuickSort, pois
            o pivot vai ser o elemento extremo.
            
            Args:
                N (int): O tamanho da lista a ser gerada
                
            Returns:
                list: Lista com N inteiros ordenados inversamente
    """
    instancia = [ i for i in range(N, 0, -1) ]
    return instancia

def alternar(instancia: list, N: int, l: int, r: int):
    if (l == r): return
    if (r - l == 1):
        instancia[l], instancia[r] = instancia[r], instancia[l] 
        return
        
    mid = (l+r)//2
    lmetade = [instancia[i] for i in range(l, r+1, 2)]
    rmetade = [instancia[i] for i in range(l+1, r+1, 2)]
    
    instancia[l:mid+1] = lmetade
    instancia[mid+1:r+1] = rmetade
    
    alternar(instancia, N, l, mid)
    alternar(instancia, N, mid+1, r) 

def instanciaAlternada(N: int) -> list:
    """Gera uma lista com N inteiros ordenados aternadamente.
            
                Os inteiros começam do 1 e vão até o N. O objetivo dessa função é replicar o comportamento
                do mergeSort, mas ao contrário (pegando os inteiros de dois em dois recursimanete), gerando, 
                assim, o pior cenário para este.
                
                Args:
                    N (int): O tamanho da lista a ser gerada
                    
                Returns:
                    list: Lista com N inteiros alternadamente
    """
    instancia = [i for i in range(1, N+1)]
    alternar(instancia, N, 0, N-1)
    return instancia
    
def mediaTempo(N:int, funcaoInstancia, funcaoSort):
    soma = 0
    for i in range(K_REPETICOES):
        instancia = funcaoInstancia(N)
        inicio = time.perf_counter()
        funcaoSort(instancia)
        fim = time.perf_counter()
        soma += fim - inicio
    return soma / K_REPETICOES

if __name__ == "__main__":
    print("-" * 64)
    print(f"{'Caso Médio':^64}")
    print("-" * 64)
    
    print(f"{'Algoritmo':^16} {f"N":^16} {f"Tempo":^16}")
    print("-" * 64)
    
    for i in [50, 100, 500, 1000, 5000]:
        print(f"{'Selection Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaAleatoria, ord.selection_sort):.5f}s":^16}")
        print(f"{'Merge Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaAleatoria, ord.divide_and_conquer_sort):.5f}s":^16}")
        print(f"{'Quick Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaAleatoria, ord.quick_sort):.5f}s":^16}")
        print("-" * 64)
    
    print(f"{'Pior caso':^64}")
    print("-" * 64)
    
    print(f"{'Algoritmo':^16} {f"N":^16} {f"Tempo":^16}")
    print("-" * 64)
        
    for i in [50, 100, 500, 1000, 5000]:
        print(f"{'Selection Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaAleatoria, ord.selection_sort):.5f}s":^16}")
        print(f"{'Merge Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaAlternada, ord.divide_and_conquer_sort):.5f}s":^16}")
        print(f"{'Quick Sort':^16} {f"{i}":^16} {f"{mediaTempo(i, instanciaReversa, ord.quick_sort):.5f}s":^16}")
        print("-" * 64)

    