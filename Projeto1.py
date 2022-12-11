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

def Bron_kerbosch(Grafo):
    conjuntoR = []
    conjuntoP = []
    conjuntoX = []

def calcula_coeficiente(Grafo):
    coeficiente_aglomeracao = 0
    for node in Grafo: # Brasil (lista)
        possiveis_triangulos = (len(node.lista)*(len(node.lista) - 1))/2
        print(node.pais)
        print("possiveis: " + str(possiveis_triangulos))
        triangulos_reais = 0
        for vizinho in node.lista: # Italia (string)
            for busca in Grafo: # Busca no grafo a lista da Italia
                if(busca.pais == vizinho): # Quando acha
                    for sub_vizinho in busca.lista:
                        if (sub_vizinho != node.pais) and (sub_vizinho in node.lista):
                            triangulos_reais += 1
        print("reais: " + str(triangulos_reais))
        if possiveis_triangulos != 0:
            coeficiente_aglomeracao += triangulos_reais/possiveis_triangulos
    return coeficiente_aglomeracao/len(Grafo)


if __name__ == '__main__':
    Grafo = prepara_grafo()
    for node in Grafo:
        node.print_lista()
    print(calcula_coeficiente(Grafo))

