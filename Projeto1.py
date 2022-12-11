class vertice:
    def __init__(self, pais):
        self.lista = []
        self.pais = pais

    def print_lista(self):
        print(self.pais, ":", self.lista)

    def adiciona_adjacencia(self, valor):
        self.lista.append(valor)    


def prepara_grafo():
    f = open("cliques_copas.txt", "r") # Apos abrir o codigo pula 4 linhas de comentario e espaco em branco
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    Grafo = []
    for linha in f:
        nome = linha.split(":") # Separa o nome do pais do restante da lista
        node = vertice(nome[0].strip()) # Retira os espacos em branco antes e depois do nome do pais
        for vizinho in nome[1].split(","): # Para cada vizinho na lista do pais
            node.adiciona_adjacencia(vizinho.strip(",; \n")) # Adiciona esse vizinho na lista, limpando os caracteres
        Grafo.append(node) # Adiciona o vertice ao grafo
    f.close()

    return Grafo

def Bron_kerbosch(conjuntoR, conjuntoP, conjuntoX):# o P recebe todos os objetos vertice, cada um com um nome e uma lista de strings
    if not conjuntoP and not conjuntoX:
        nomes = []
        for membros in conjuntoR:# Se printar o R vai sair um monte de objetos, entao preciso buscar os nomes
            nomes.append(membros.pais)
        if len(nomes) >= 3:
            print("Clique: ", nomes)
    for node in conjuntoP:# Cada no em P eh um objeto da classe vertice
###################################################### Tratando R        
        copiaR = conjuntoR.copy()
        copiaR.append(node)# Preciso fazer o append antes de enviar como parametro porque o metodo append nao retorna nada, entao se passar R.append() ele chega como None.
        
###################################################### Tratando P
        copiaP = [] # Cada no em P eh um objeto da classe vertice, mas a interseccao com a lista de 'node' deve ser tratada porque sao strings
        #Preciso colocar em copiaP todos os elementos em P cujo elemento.pais esta na lista de 'node'
        for elemento in conjuntoP: # iterando vertices (objetos)
            if elemento.pais in node.lista:
                copiaP.append(elemento)
######################################################
        copiaX = []
        for elemento in conjuntoX:# Mesmo tratamento do conjunto P fazendo interseccao com a lista de node
            if elemento.pais in node.lista:
                copiaX.append(elemento)

        Bron_kerbosch(copiaR, copiaP, copiaX)
        conjuntoP.remove(node)
        conjuntoX.append(node)

def calcula_coeficiente(Grafo):
    coeficiente_aglomeracao = 0
    for node in Grafo: # Brasil (lista)
        possiveis_triangulos = (len(node.lista)*(len(node.lista) - 1))/2
        triangulos_reais = 0
        for vizinho in node.lista: # Italia (string)
            for busca in Grafo: # Busca no grafo a lista da Italia
                if(busca.pais == vizinho): # Quando acha
                    for sub_vizinho in busca.lista: # Busca nessa lista
                        if (sub_vizinho != node.pais) and (sub_vizinho in node.lista): # Verifica se o vertice não eh o original e se ele esta conectado ao original
                            triangulos_reais += 1
        if possiveis_triangulos != 0: # Evita divisao por 0 quando nao ha a possibilidade de triangulo
            coeficiente_aglomeracao += triangulos_reais/possiveis_triangulos
    return coeficiente_aglomeracao/len(Grafo)


if __name__ == '__main__':
    Grafo = prepara_grafo()
    for node in Grafo:
        node.print_lista()
    print("Coeficiente de aglomeracao: " + str(calcula_coeficiente(Grafo)))
    Bron_kerbosch([],Grafo,[])

