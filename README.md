# Trabalho Prático 2 de Algoritmo e Estrutura de Dados III
Este é um trabalho prático desenvolvido para a disciplina de Algoritmos e Estruturas de Dados III. O projeto consiste em implementações de um programa capaz de compactar e descompactar textos utilizando o algoritmo de Huffman. Neste README estão presentes as instruções para executar o código.

## Conteúdo

1. [Compressor de Texto](#compressor-de-texto)
2. [Observações Gerais](#observações-gerais)
3. [Autores](#autores)

## Compressor de Texto

O Compressor de Texto tem duas funções principais: Compactar e descompactar. A função compactar recebe um arquivo .txt e o converte em um arquivo .huf utilizando o algoritmo de Huffman, já a função descompactar recebe um arquivo .huf e o coverte em um .txt, fazendo o caminho reverso.

### Arquivo: `Compressor_de_Texto.py`

#### Estruturas de Dados
- **NodoHuffman**: Objetos dessa classe serão os nós para a árvore binária de Huffman
- **Huffman**: Essa classe é a responsável por todo funcionamento do algoritmo, desde gerar a árvore até realizar a compressão

#### Funcionalidades
- Compressão de Arquivo: Comprime um arquivo de texto utilizando o algoritmo de Huffman.
- Descompressão de Arquivo: Descomprime um arquivo binário utilizando um dicionário de Huffman gerado durante a compressão.
- Geração de Dicionário: Gera um dicionário de Huffman contendo os códigos utilizados para a compressão.
  
### Como Usar

1. Instale as bibliotecas necessárias caso ainda não as tenha (tkinter, tkinterdnd2 e as demais sugeridas pelo terminal do linux).
2. Compile o código.
3. Execute o programa.
4. A interface irá te dar as opções de compactar e descompactar, basta escolher a opção e selecionar o arquivo desejado.
5. O arquivo deve seguir as seguintes recomendações: Caso for compactar, use como entrada um arquivo .txt. Caso for descompactar, use como entrada um arquivo .huf e um .txt contendo os códigos das letras gerados pela compactação (Dicionário).

## Observações Gerais
- É importante que o arquivo de entrada não contenha caracteres especiais. Ele precisa seguir o modelo dos arquivos de entrada enviados como exemplo.
- O arquivo de entrada também não pode conter quebras de linhas e/ou espaços.
- Certifique-se de que o compressor esteja no mesmo diretório da pasta "img" pois nela contém imagens necessárias para a execução da interface.
- As imagens não serão carregadas, nem a interface funcionará caso as bibliotecas necessárias não estejam instaladas corretamente.


## Autores
- Emanuel Guimarães Santana - emanuel.guimaraes@ufvjm.edu.br
- Robson da Lomba Campos Junior - robson.campos@ufvjm.edu.br
- Evelen Pinheiro de Oliveira - evelen.pinheiro@ufvjm.edu.br
- Marcos Eduardo da Silva Braga - marcos.braga@ufvjm.edu.br
- Samuel Couto Monteiro Assunção - monteiro.samuel@ufvjm.edu.br
- Marcela Cristina Santos Cruz - marcela.cruz@ufvjm.edu.br
