from ListaNos import ListaNos
from HuffmanTree import HuffmanTree

##############################################
def openFile(file_name):	# pega o texto incial	
		try:
			file = open(file_name, "r")
			text = file.read()
			file.close()
		except IOError:
			print ("Erro ao abrir o arquivo")
		return text

def creatFile(file_name, text):		# escreve um arquivo com o texto em binário
	try:
		file = open(file_name, 'w')
		file.write(text)
		file.close()
	except IOError:
		raise print("Erro ao criar o arquivo")


##############################################

########## Main ##############

lista = list(openFile("texto.txt"))
ht = HuffmanTree()
listaNos = ListaNos(lista)
listaNos.criaArv()
ht.codifica(listaNos.raiz[0])
#ht.navegar(listaNos.raiz[0])

creatFile("saida.huf", ht.getTextBin(listaNos.raiz[0],listaNos.texto))

creatFile("dicionario.txt", ht.arvToBin(listaNos.raiz[0]))

print("Texto Codificado: " , ht.getTextBin(listaNos.raiz[0],listaNos.texto))

print("Texto Decodificado: " , ht.decodeBin(listaNos.raiz[0],ht.getTextBin(listaNos.raiz[0],listaNos.texto)))
