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
    
    def comprimir_arquivo(self, arquivo_entrada, arquivo_saida, arquivo_dicionario):
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
        
        # Escrever o dicionário de Huffman em um arquivo texto
        with open(arquivo_dicionario, 'w', encoding='utf-8') as f_dict:
            for caractere, codigo in self.codigos.items():
                f_dict.write(f"{caractere}:{codigo}\n")
    
    def descomprimir_arquivo(self, arquivo_comprimido, arquivo_dicionario, arquivo_descomprimido):
        # Ler o dicionário de Huffman do arquivo
        with open(arquivo_dicionario, 'r', encoding='utf-8') as f_dict:
            self.codigos = {}
            for linha in f_dict:
                if ':' in linha:
                    caractere, codigo = linha.strip().split(':', 1)
                    self.codigos[caractere] = codigo
        
        # Reconstruir a árvore de Huffman com base no dicionário
        self.raiz = NodoHuffman()
        for caractere, codigo in self.codigos.items():
            nodo_atual = self.raiz
            for bit in codigo:
                if bit == '0':
                    if not nodo_atual.esquerda:
                        nodo_atual.esquerda = NodoHuffman()
                    nodo_atual = nodo_atual.esquerda
                else:
                    if not nodo_atual.direita:
                        nodo_atual.direita = NodoHuffman()
                    nodo_atual = nodo_atual.direita
            nodo_atual.caractere = caractere
        
        # Ler bytes do arquivo comprimido
        with open(arquivo_comprimido, 'rb') as f:
            bytes_codificados = f.read()
        
        # Converter bytes de volta para a string binária
        texto_codificado_binario = bin(int.from_bytes(bytes_codificados, 'big'))[2:]
        
        # Decodificar o texto binário usando os códigos Huffman e a árvore reconstruída
        texto_decodificado = ''
        nodo_atual = self.raiz
        for bit in texto_codificado_binario:
            if bit == '0':
                nodo_atual = nodo_atual.esquerda
            else:
                nodo_atual = nodo_atual.direita
            
            if nodo_atual.caractere:
                texto_decodificado += nodo_atual.caractere
                nodo_atual = self.raiz
        
        # Escrever o texto decodificado no arquivo de saída
        with open(arquivo_descomprimido, 'w', encoding='utf-8') as f:
            f.write(texto_decodificado)


huffman = Huffman()
    
arquivo = '1000000caracteres'
    
entrada = './Arquivos_descompactados/' + arquivo + ".txt"
pasta_compactados = './Arquivos_compactados/'
pasta_dicionario = './dicionario/'
pasta_descompactados = './Arquivos_descomprimidos/'
    
if not os.path.exists(pasta_compactados):
    os.makedirs(pasta_compactados)
if not os.path.exists(pasta_dicionario):
    os.makedirs(pasta_dicionario)
if not os.path.exists(pasta_descompactados):
    os.makedirs(pasta_descompactados)

arquivo_saida = pasta_compactados + arquivo + '.huf'
arquivo_dicionario = pasta_dicionario + arquivo + '_dicionario.txt'
arquivo_descomprimido = pasta_descompactados + arquivo + '_descomprimido.txt'
    
# Comprimir o arquivo de entrada
huffman.comprimir_arquivo(entrada, arquivo_saida, arquivo_dicionario)
print(f"Arquivo comprimido '{entrada}' para '{arquivo_saida}' e dicionário gerado em '{arquivo_dicionario}'")
    
# Descomprimir o arquivo de saída usando o dicionário gerado
huffman.descomprimir_arquivo(arquivo_saida, arquivo_dicionario, arquivo_descomprimido)
print(f"Arquivo '{arquivo_saida}' descomprimido usando '{arquivo_dicionario}' para '{arquivo_descomprimido}'")
