import heapq
import os
from tkinter import *
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog

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
    
    def comprimir_arquivo(self):
        self.codigos = {}
        arquivo_entrada = entry_arquivo_compactar.get()
        pasta_compactados = './Arquivos_compactados/'
        pasta_dicionario = './dicionario/'
            
        if not os.path.exists(pasta_compactados):
            os.makedirs(pasta_compactados)
        if not os.path.exists(pasta_dicionario):
            os.makedirs(pasta_dicionario)
        
        arquivo_saida = pasta_compactados + nome_arquivo(arquivo_entrada) + '.huf'
        arquivo_dicionario = pasta_dicionario + nome_arquivo(arquivo_entrada) + '_dicionario.txt'

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
    
    def descomprimir_arquivo(self):
        arquivo_comprimido = entry_arquivo_descompactar.get()
        arquivo_dicionario = entry_dicionario.get()
        pasta_descompactados = './Arquivos_descomprimidos/'
        
        if not os.path.exists(pasta_descompactados):
            os.makedirs(pasta_descompactados)

        arquivo_descomprimido = pasta_descompactados + nome_arquivo(arquivo_comprimido) + '_descomprimido.txt'

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

#-Botões dinâmicos
def show_frame(frame, button, other_button):
    frame.tkraise()
    button.config(relief="sunken", state="disabled", bg='#666666', fg='black', bd=0)
    other_button.config(relief="raised", state="normal", bg='#8D8D8D', fg='black', bd=0)

#-Arrastar e soltar arquivos
def on_drop(event, entry_widget):
    file_path = event.data.strip('{}')
    entry_widget.delete(0, END)
    entry_widget.insert(0, file_path)

#-Abrir o explorador de arquivos
def abrir_ficheiro(entry_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_widget.delete(0, END)
        entry_widget.insert(0, file_path)

#-Nome sem o caminho
def nome_arquivo(caminho_completo):
    return os.path.splitext(os.path.basename(caminho_completo))[0]

huffman = Huffman()

# ------------------------------------------------------------------------------
#GUI
menu_iniciar = TkinterDnD.Tk()

menu_iniciar.title("Compressor de Arquivos")
menu_iniciar['bg'] = "#151515"
photo = PhotoImage(file="img\\disquete.png")
menu_iniciar.iconphoto(False, photo)

#Dimensões
largura = 600
altura = 600
largura_screen = menu_iniciar.winfo_screenwidth()
altura_screen = menu_iniciar.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
menu_iniciar.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
menu_iniciar.resizable(False, False)

# ------------------------------------------------------------------------------
#Widgets
#HEAD
frame_head = Frame(menu_iniciar, bg="#979797")
frame_box = Frame(frame_head, bg="#151515")
titulo = Label(frame_head, text = "NOSSO ARQUIVO É TÃO COMPACTO\nQUE CABERIA EM UM DISQUETE!", bg="#979797", fg="#151515",font="Courier 10 bold", justify= LEFT)
subtitulo = Label(frame_head, text = "Se soubessemos usar um disquete.", bg="#979797", fg="#151515", font="Courier 8 bold", justify=LEFT)

#FOOTER
frame_footer = Frame(menu_iniciar, bg="#8D8D8D")
#BOTÕES DO FOOTER, COMPACTAR E DESCOMPACTAR
frame_opcoes = Frame(frame_footer)
bt_compactar = Button(frame_opcoes, text="COMPACTAR", font="Courier 10 bold", fg="#151515", disabledforeground="#FFFFFF", command=lambda: show_frame(filho1_compactar, bt_compactar, bt_descompactar))
bt_descompactar = Button(frame_opcoes, text="DESCOMPACTAR", font="Courier 10 bold", fg="#151515", disabledforeground="#FFFFFF", command=lambda: show_frame(filho2_descompactar, bt_descompactar, bt_compactar))

#IMAGEM DOS BOTÕES PASTAS
image_path = "img\\icon.png"
bt_image = PhotoImage(file=image_path)

frame_pai = Frame(frame_footer, bg="#666666")
#SESSÃO COMPACTAR
filho1_compactar = Frame(frame_pai, bg="#666666")
titulo_compactar = Label(filho1_compactar, text="Procure ou arraste seu\narquivo para a compactação", bg="#666666", fg="#FFFFFF",font="Courier 13 bold", justify= LEFT)
entry_arquivo_compactar = Entry(filho1_compactar, text="", font="Courier 8 bold")
bt_arquivo_buscar_compactar = Button(filho1_compactar, image=bt_image, bd=0, command=lambda:abrir_ficheiro(entry_arquivo_compactar))
bt_arquivo_compactar = Button(filho1_compactar, text="Compactar", bd=0, bg="#151515", fg="#FFFFFF", command=lambda: huffman.comprimir_arquivo())

#SESSÃO DESCOMPACTAR
filho2_descompactar = Frame(frame_pai, bg="#666666")
titulo_descompactar = Label(filho2_descompactar, text="Procure ou arraste seu\narquivo para a descompactação", bg="#666666", fg="#FFFFFF",font="Courier 13 bold", justify= LEFT)
titulo_arquivo_huf = Label(filho2_descompactar, text="Arquivo .huf:", font="Courier 8 bold", fg="black", bg="#666666")
entry_arquivo_descompactar = Entry(filho2_descompactar, text="", font="Courier 8 bold")
bt_arquivo_buscar_descompactar = Button(filho2_descompactar, image=bt_image, bd=0, command=lambda:abrir_ficheiro(entry_arquivo_descompactar))
bt_arquivo_descompactar = Button(filho2_descompactar, text="Descompactar", bd=0, bg="#151515", fg="#FFFFFF", command=lambda:huffman.descomprimir_arquivo())
titulo_dicionario = Label(filho2_descompactar,text="Dicionário:", font="Courier 8 bold", fg="black", bg="#666666")
entry_dicionario = Entry(filho2_descompactar, text="", font="Courier 8 bold")
bt_arquivo_buscar_dicionario = Button(filho2_descompactar, image=bt_image, bd=0, command=lambda:abrir_ficheiro(entry_dicionario))

# ------------------------------------------------------------------------------
#Layout
#HEAD
frame_head.place(relx=0.5, rely=0, anchor="n", width=450, height= 150)
frame_box.place(relx=0.8, rely=0.5, anchor="center", width=70, height=100)
titulo.place(relx=0.1, rely=0.40, anchor="w")
subtitulo.place(relx=0.1, rely=0.60, anchor="w")

#FOOTER
frame_footer.place(relx=0.5, rely=1, anchor="s", width=500, height=350)
#BOTÕES DO FOOTER, COMPACTAR E DESCOMPACTAR
frame_opcoes.configure(width=500, height=50)
frame_opcoes.grid_propagate(False)
frame_opcoes.pack()
bt_compactar.place(x=0, width=250, height=50)
bt_descompactar.place(x=250, width=250, height=50)

frame_pai.pack(fill="both", expand=True)

for frame in (filho1_compactar, filho2_descompactar):
    frame.place(width=500, height=300)

#SESSÃO COMPACTAR
titulo_compactar.pack(padx=86, pady=70, anchor="w")
entry_arquivo_compactar.place(rely=0.45, relx=0.175, width=250, height=30)
entry_arquivo_compactar.drop_target_register(DND_FILES)
entry_arquivo_compactar.dnd_bind('<<Drop>>', lambda event: on_drop(event, entry_arquivo_compactar))
bt_arquivo_buscar_compactar.place(rely=0.45, relx=0.65, width=30, height=30)
bt_arquivo_compactar.place(rely=0.45, relx=0.74, width=75, height=30)

#SESSÃO DESCOMPACTAR
titulo_descompactar.pack(padx=86, pady=70, anchor="w")
#ARQUIVO HUF
titulo_arquivo_huf.place(rely=0.39, relx=0.175)
entry_arquivo_descompactar.place(rely=0.46, relx=0.175, width=150, height=30)
entry_arquivo_descompactar.drop_target_register(DND_FILES)
entry_arquivo_descompactar.dnd_bind('<<Drop>>', lambda event: on_drop(event, entry_arquivo_descompactar))
bt_arquivo_buscar_descompactar.place(rely=0.46, relx=0.42, width=30, height=30)
#DICIONÁRIO
titulo_dicionario.place(rely=0.39, relx=0.5)
entry_dicionario.place(rely=0.46, relx=0.5, width=150, height=30)
entry_dicionario.drop_target_register(DND_FILES)
entry_dicionario.dnd_bind('<<Drop>>', lambda event: on_drop(event, entry_dicionario))
bt_arquivo_descompactar.place(rely=0.6, relx=0.175, width=312, height=30)
bt_arquivo_buscar_dicionario.place(rely=0.46, relx=0.74, width=30, height=30)

show_frame(filho1_compactar, bt_compactar, bt_descompactar)
menu_iniciar.mainloop()