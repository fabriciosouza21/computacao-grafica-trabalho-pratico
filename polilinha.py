from bresenham import bresenham 

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