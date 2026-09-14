from P06_3498_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self._entrada = PilhaEncadeada()
        self._saida = PilhaEncadeada()
        self._sz = 0
        
    def _reorganizar(self):
        '''
        Reorganiza os elementos da fila, movendo-os da pilha de entrada para a pilha de saída.
        
        ## Complexidade:
            O(N), onde N é o número de elementos na fila. Isso ocorre porque, no pior caso, todos os elementos da pilha de entrada precisam ser movidos para a pilha de saída.

        Args:
            None
                    
        Returns:
            None
        '''
        
        while (not self._entrada.esta_vazia()):
            self._saida.push(self._entrada.pop())
        
        
    def enfileirar(self, item):
        '''
        Enfileira um item na fila.
        
        ## Complexidade
            O(1), pois a operação de empilhar na pilha de entrada é constante.
        
        Args:
            item (any): O item a ser enfileirado
            
        Returns:
            None
        '''
        
        
        self._entrada.push(item)
        self._sz += 1
    
    def desenfileirar(self):
        '''
        Desenfileira um item da fila.
        
        ## Complexidade
            O(1) amortizado. No pior caso, a operação pode ser O(N)
        
        Args:
            None
        
        Returns:
            item (any): O item desenfileirado
        '''
        
        if self._sz == 0:
            raise IndexError("A fila está vazia")
        self._sz -= 1
        
        if (not self._saida.esta_vazia()):
            return self._saida.pop()
        
        self._reorganizar()
        
        return self._saida.pop()

    
    def frente(self):
        '''
        Retorna o item que está na frente da fila, sem removê-lo.
        
        ## Complexidade
            O(1) amortizado. No pior caso, a operação pode ser O(N).

        Args:
            None

        Returns:
            item (any): O item que está na frente da fila
        '''
        
        if self._sz == 0:
            raise IndexError("A fila está vazia")
        
        if (not self._saida.esta_vazia()):
            return self._saida.topo()
        
        self._reorganizar()
        
        return self._saida.topo()
    
    def esta_vazia(self):
        '''
        Verifica se a fila está vazia.
        
        ## Complexidade
            O(1), pois a operação de verificar o tamanho da fila é constante.

        Args:
            None

        Returns:
            bool: True se a fila estiver vazia, False caso contrário
        '''
        
        return self._sz == 0
    
    def __len__(self):
        return self._sz
    
    def __repr__(self):
        if (self._sz == 0): return "| ]"
        
        ret = "| "
        
        pentrada = ""
        psaida = ""
        
        crr = self._entrada._topo
        for i in range(len(self._entrada)):
            if i:
                pentrada += " | "
            pentrada += str(crr.valor)
            crr = crr.prox
    
        crr = self._saida._topo
        for i in range(len(self._saida)):
            if i:
                psaida += " | "
            psaida += str(crr.valor)
            crr = crr.prox
        
        if (not pentrada):
            return "| " + psaida[::-1] + " ]"
        
        if (not psaida):
                return "| " + pentrada + " ]"
        return "| " + pentrada + " | " + psaida[::-1] + " ]"
