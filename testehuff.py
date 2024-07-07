import heapq
import os

class NodoHuffman:
    def __init__(self, caractere=None, frequencia=0):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None
    
    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

class Huffman:
    def __init__(self):
        self.raiz = None
        self.codigos = {}
    
    def construir_arvore(self, frequencias):
        fila_prioridade = []
        for caractere, freq in frequencias.items():
            heapq.heappush(fila_prioridade, NodoHuffman(caractere, freq))
        
        while len(fila_prioridade) > 1:
            esquerda = heapq.heappop(fila_prioridade)
            direita = heapq.heappop(fila_prioridade)
            novo_nodo = NodoHuffman(frequencia=esquerda.frequencia + direita.frequencia)
            novo_nodo.esquerda = esquerda
            novo_nodo.direita = direita
            heapq.heappush(fila_prioridade, novo_nodo)
        
        self.raiz = heapq.heappop(fila_prioridade)
    
    def gerar_codigos(self, nodo, codigo_atual=''):
        if nodo:
            if nodo.caractere:
                self.codigos[nodo.caractere] = codigo_atual
            self.gerar_codigos(nodo.esquerda, codigo_atual + '0')
            self.gerar_codigos(nodo.direita, codigo_atual + '1')
    
    def codificar(self, texto):
        codigo = ''
        for caractere in texto:
            codigo += self.codigos[caractere]
        return codigo
    
    def comprimir_arquivo(self, arquivo_entrada, arquivo_saida):
        # Contagem de frequências dos caracteres no arquivo de entrada
        frequencias = {}
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            texto = f.read()
            for caractere in texto:
                if caractere in frequencias:
                    frequencias[caractere] += 1
                else:
                    frequencias[caractere] = 1
        
        # Construir a árvore de Huffman com base nas frequências
        self.construir_arvore(frequencias)
        
        # Gerar os códigos Huffman para cada caractere
        self.gerar_codigos(self.raiz)
        
        # Codificar o texto original usando os códigos Huffman
        texto_codificado = self.codificar(texto)
        
        # Escrever o texto codificado em binário no arquivo de saída
        with open(arquivo_saida, 'wb') as f:
            # Convertendo a string binária para bytes
            bytes_codificados = int(texto_codificado, 2).to_bytes((len(texto_codificado) + 7) // 8, 'big')
            f.write(bytes_codificados)


huffman = Huffman()
arquivo_entrada = 'entrada.txt'
arquivo_saida = 'saida.huf'
huffman.comprimir_arquivo(arquivo_entrada, arquivo_saida)
