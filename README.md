# Trabalho Prático 2 de Algoritmo e Estrutura de Dados III
Este é um trabalho prático desenvolvido para a disciplina de Algoritmos e Estruturas de Dados III. O projeto consiste em implementações de um programa capaz de compactar e descompactar textos utilizando o algoritmo de Huffman. Neste README está presente as instruções para executar cada código.

## Conteúdo

1. [Compressor de Texto](#compressor-de-texto)
2. [Observaçõoes Gerais](#observações-gerais)
3. [Autores](#autores)

## Compressor de Texto

O Compressor de Texto tem duas funções principais: Compactar e descompactar. A função compactar recebe um arquivo .txt e o converte em um arquivo .huf utilizando o algoritmo de Huffman, já a função descompactar recebe um arquivo .huf e o coverte em um .txt, fazendo o caminho reverso.

### Arquivo: `Compressor_de_Texto.py`

#### Estruturas de Dados

- **No**: Objetos dessa classe serão os nós para a árvore binária de Huffman
- **ListaNos**: Essa classe primeiramente guardará uma lista com todos os caracteres do texto lido, cada caractere vai ser atribuído a um nó e ordenados em ordem crescente de frequência. A partir dessa lista ordenada será criada a árvore binária.
- **HuffmanTree**: Essa classe é a que a armazena a árvore em si

#### Funções 

- `def navegar()`: Apenas navega pela árvore e imprime na tela os elementos em pré-ordem
- `def codifica()`: Gera o código em binário para cada nó da árvore
- `def getTextBin()`: A partir da árvore e de uma lista com o texto original, retorna uma string com o texto em binário conforme o código de cada caracter na árvore
- `def getBinLetter()`: Procura um dado caractere na árvore e retorna seu código
- `def arvToBin()`: Retorna uma string com a formação da árvore em pré-ordem
- `def decodeBin()`: A partir da árvore e do texto em binário resgata o texto original

### Como Usar

1. Compile o código.
2. Execute o programa.
3. A interface irá te dar as opções de compactar e descompactar, basta escolher a opção e selecionar o arquivo desejado.
4. O arquivo deve seguir as seguintes recomendações: Caso for compactar, use como entrada um arquivo .txt. Caso for descompactar, use como entrada um arquivo .huf e um .txt contendo a árvore gerada pela compactação.

## Observações Gerais

## Autores
- Emanuel Guimarães Santana - emanuel.guimaraes@ufvjm.edu.br
- Robson da Lomba Campos Junior - robson.campos@ufvjm.edu.br
- Samuel Couto Monteiro Assunção - monteiro.samuel@ufvjm.edu.br
- Marcela Cristina Santos Cruz - marcela.cruz@ufvjm.edu.br
