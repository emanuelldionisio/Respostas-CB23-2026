import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS iterativo.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    
    def dfs(x_inicial, y_inicial):
            """Abre passagens iterativamente a partir da sala (x_inicial, y_inicial)."""
            random.shuffle(directions)
            
            # Há duas pilhas: uma para continuar a busca e outra para o caminho atual. A pilha de caminho é esvaziada quando não há mais vizinhos a visitar, e então a busca continua na pilha de continuar.
            pilhaContinuar = [(x_inicial, y_inicial, directions.copy())]; pilhaCaminho = []
    
            while (len(pilhaContinuar) or len(pilhaCaminho)):
                
                
                pilhaAtual = pilhaCaminho if len(pilhaCaminho) else pilhaContinuar
                
                x, y, ordem = pilhaAtual.pop()
                
                maze[2 * x + 1][2 * y + 1] = room
                
                # Ordem aleatória garante labirintos distintos a cada execução
                item = random.choice(ordem); ordem.remove(item)
                
                dx, dy = item
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    # Derruba a parede entre (x,y) e (nx,ny)
                    maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                    pilhaCaminho.append((nx, ny, directions.copy()))
                
                if (len(ordem)):
                    pilhaContinuar.append((x, y, ordem))
              
    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * n))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def find_path(maze, inicio = (1, 1), room=0, wall=1, cheese='.', path = '-'):
    
    if (maze[1][1] == cheese):
        return

    maze[1][1] = path
    
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(atual, pai):
        
        for l, r in direcoes:
            prox = (atual[0] + l, atual[1] + r)
            
            if prox[0] >= len(maze) or prox[0] < 0: continue
            if prox[1] >= len(maze[0]) or prox[1] < 0: continue
            
            if (prox == pai): continue
            
            if (maze[prox[0]][prox[1]] == wall): continue
            
            if (maze[prox[0]][prox[1]] == cheese):
                return True
                        
            maze[prox[0]][prox[1]] = path
            if dfs(prox, atual):
                return True
            maze[prox[0]][prox[1]] = room
        
        return False
        
    dfs((1,1), (1,1))    
    

# Example usage:
if __name__ == '__main__':
    m, n = 20, 20  # Grid size
    #random.seed(10110)
    maze = generate_maze(m, n, " ", "#", "x")
    #print_maze(maze)
    
    find_path(maze, (1,1), " ", "#", "x", ".")
    print_maze(maze)