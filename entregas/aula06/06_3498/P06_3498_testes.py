import unittest
from P06_3498__fila_encadeada import FilaEncadeada
from P06_3498_pilha_encadeada import PilhaEncadeada

class TestPilhaEncadeada(unittest.TestCase):
    
    def test_LIFO(self):
        
        pilha = PilhaEncadeada()
        
        with self.assertRaises(IndexError):
            pilha.topo()
                
        with self.assertRaises(IndexError):
            pilha.pop()
        
        pilha.push(1)
        self.assertEqual(pilha.topo(), 1)
        
        pilha.push(1)
        self.assertEqual(pilha.topo(), 1)
        
        pilha.push(3.14)
        self.assertEqual(pilha.topo(), 3.14)
        
        self.assertEqual(pilha.pop(), 3.14)
        self.assertEqual(pilha.topo(), 1)
        
        pilha.push(None)
        self.assertEqual(pilha.topo(), None)
        
        self.assertEqual(pilha.pop(), None)
        self.assertEqual(pilha.topo(), 1)
        
        self.assertEqual(pilha.pop(), 1)
        self.assertEqual(pilha.topo(), 1)
        
        self.assertEqual(pilha.pop(), 1)
        
        self.assertTrue(pilha.esta_vazia())
        
        with self.assertRaises(IndexError):
            pilha.topo()
        
        with self.assertRaises(IndexError):
            pilha.pop()
        
        
    def test_len(self):
        pilha = PilhaEncadeada()
        
        self.assertEqual(len(pilha), 0)
        
        pilha.push(1)
        self.assertEqual(len(pilha), 1)
        
        pilha.push(2)
        self.assertEqual(len(pilha), 2)
        
        pilha.pop()
        self.assertEqual(len(pilha), 1)
        
        pilha.push(3)
        self.assertEqual(len(pilha), 2)
        
        pilha.pop()
        self.assertEqual(len(pilha), 1)
        
        pilha.pop()
        self.assertEqual(len(pilha), 0)
        
class TestFilaEncadeada(unittest.TestCase):
    def test_FIFO(self):
        
        fila = FilaEncadeada()
        
        with self.assertRaises(IndexError):
            fila.frente()
        with self.assertRaises(IndexError):
            fila.desenfileirar()
        
        fila.enfileirar(1)
        self.assertEqual(fila.frente(), 1)
        
        fila.enfileirar(2)
        self.assertEqual(fila.frente(), 1)
        
        fila.desenfileirar()
        self.assertEqual(fila.frente(), 2)
        
        fila.enfileirar(3.14)
        self.assertEqual(fila.frente(), 2)
        
        fila.desenfileirar()
        self.assertEqual(fila.frente(), 3.14)
        
        fila.enfileirar(None)
        self.assertEqual(fila.frente(), 3.14)
        
        fila.desenfileirar()
        self.assertEqual(fila.frente(), None)
        
        fila.desenfileirar()
        self.assertTrue(fila.esta_vazia())
        
        with self.assertRaises(IndexError):
            fila.frente()
        with self.assertRaises(IndexError):
            fila.desenfileirar()
        
        fila.enfileirar("hey, listen!")        
        self.assertEqual(fila.frente(), "hey, listen!")
        
        fila.enfileirar("link!!!")
        self.assertEqual(fila.frente(), "hey, listen!")
        
        fila.desenfileirar()
        self.assertEqual(fila.frente(), "link!!!")
        
        fila.desenfileirar()
        self.assertTrue(fila.esta_vazia())
    
        with self.assertRaises(IndexError):
            fila.frente()
            
        with self.assertRaises(IndexError):
            fila.desenfileirar()
                
    def test_len(self):
        fila = FilaEncadeada()
        
        self.assertEqual(len(fila), 0)
        
        fila.enfileirar(1)
        self.assertEqual(len(fila), 1)
        
        fila.enfileirar(2)
        self.assertEqual(len(fila), 2)
        
        fila.desenfileirar()
        self.assertEqual(len(fila), 1)
        
        fila.enfileirar(3)
        self.assertEqual(len(fila), 2)
        
        fila.desenfileirar()
        self.assertEqual(len(fila), 1)
        
        fila.desenfileirar()
        self.assertEqual(len(fila), 0)
        
        fila.enfileirar(4)
        self.assertEqual(len(fila), 1)
        
        fila.desenfileirar()
        self.assertEqual(len(fila), 0)
    
        
if __name__ == "__main__":
    unittest.main()
    