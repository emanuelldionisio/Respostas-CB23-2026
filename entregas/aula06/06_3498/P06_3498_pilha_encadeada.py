

class PilhaEncadeada:
    #No: (valor atual (int), prox (No))
    class _No:
        def __init__(self, valor, prox = None):
            self.valor = valor
            self.prox = prox
    
    def __init__(self):
        
        self._topo = None
        self._sz = 0
        pass

    def push(self, item):
        '''
        Empilha um item na pilha.
        
        ## Complexidade
            O(1), pois a operação de empilhar é constante.

        Args:
            item (any): O item a ser empilhado

        Returns:
            None
        '''
        
        novoNo = self._No(item, self._topo)
        self._topo = novoNo 
        self._sz += 1

    def pop(self):
        '''
        Desempilha um item da pilha.
        
        ## Complexidade
            O(1), pois a operação de desempilhar é constante.

        Args:
            None

        Returns:
            item (any): O item desempilhado
        '''
        
        if (self._sz == 0):
            raise IndexError("A pilha está vazia")
        ret = self._topo.valor
        self._topo = self._topo.prox
        self._sz -= 1
        return ret
    
    def topo(self):
        '''
        Retorna o item que está no topo da pilha, sem removê-lo.
        
        ## Complexidade
            O(1), pois a operação de acessar o topo da pilha é constante.

        Args:
            None

        Returns:
            item (any): O item que está no topo da pilha
        '''
        
        if (self._sz == 0):
            raise IndexError("A pilha está vazia")
        return self._topo.valor
    
    def __len__(self):
        '''
        Retorna o tamanho da pilha.
        
        ## Complexidade
            O(1), pois a operação de obter o tamanho da pilha é constante.

        Args:
            None

        Returns:
            int: O tamanho da pilha
        '''
        
        return self._sz
    
    def __repr__(self):
        '''
        Retorna uma representação em string da pilha.
        
        ## Complexidade
            O(n), onde n é o tamanho da pilha, pois a operação de representar a pilha em string é linear.

        Args:
            None

        Returns:
            str: A representação em string da pilha
        '''
        
        if (self._sz == 0):
            return "|]"
        
        ret = "| "; crr = self._topo
        
        for i in range(self._sz):
            if i:
                ret += " | "
            ret += str(crr.valor)
            crr = crr.prox
        return ret + " ]"
    
    def esta_vazia(self):
        
        '''
        Verifica se a pilha está vazia.

        ## Complexidade
            O(1), pois a operação de verificar se a pilha está vazia é constante.

        Args:
            None

        Returns:
            bool: True se a pilha estiver vazia, False caso contrário
        '''
        
        return self._sz == 0


