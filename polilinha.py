from bresenham import bresenham 

def chunks(lista, n=2):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]

class polilinha:
    def __init__(self,pontos):
        self.pontos = pontos
        self.polilinhas = []
        self.generate_edges()
        
    def generate_edges(self):
        origem = self.pontos[0]
        destino = self.pontos[1]
        ponto = 2
        while ponto <= len(self.pontos):
            coordenadas= list(bresenham(origem[0],origem[1],destino[0],destino[1]))
            self.polilinhas.extend(coordenadas)
            origem = destino
            if ponto < len(self.pontos):
                destino = self.pontos[ponto]
            ponto += 1
        self.polilinhas.extend(list(bresenham(origem[0],origem[1],self.pontos[0][0],self.pontos[0][1])))

def polilinha_pontos(pontos):
    pontos = pontos
    restas = polilinha(pontos)
    return restas.polilinhas 

def exec_polilinha(pontos):
    pontos = list(chunks(pontos))
    return polilinha_pontos(pontos)

def polilinha_entrada():
    return ["vertices"]