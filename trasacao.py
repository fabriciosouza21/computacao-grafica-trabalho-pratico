import math
from bresenham import bresenham 
from polilinha import polilinha_pontos, chunks
class trasacao:
    
    def __init__(self,vertices):
        self.vertices = vertices

    def rotacao(self,pivo,angulo_graus):
        angulo_radianos = self.converte_para_radianos(angulo_graus)
        coordenadas = []
        coordenadas.append(pivo)
        for vertice in self.vertices:
            if vertice != pivo :
                x_linha = vertice[0]*math.cos(angulo_radianos)-vertice[1]*math.sin(angulo_radianos)
                y_linha = vertice[0]*math.sin(angulo_radianos)+vertice[1]*math.cos(angulo_radianos)
                print(x_linha,y_linha)
                x_linha = round(x_linha)
                y_linha = round(y_linha)
                coordenadas.append((x_linha,y_linha))
        return coordenadas

    def translacao(self,t_linha,t_coluna):
        self.converte_para_positivo()
        coordenadas = self.vertices
        linha,coluna=zip(*coordenadas)
        new_coluna = coluna
        new_linha = linha
        equalizado = t_coluna
        new_coluna = list(map(lambda x: x + equalizado,coluna))
        equalizado = t_linha
        new_linha = list(map(lambda x: x + equalizado,linha))
        coordenadas = list(zip(new_linha,new_coluna))
        return coordenadas
    def converte_para_radianos(self,angulo):
        angulo = angulo
        radians = angulo / 180.0 * math.pi
        return radians

    def converte_para_positivo(self):
        coordenadas = self.vertices
        linha,coluna=zip(*coordenadas)
        minimo_coluna = (min(coluna))
        minimo_linha = (min(linha))
        new_coluna = coluna
        new_linha = linha
        if minimo_coluna < 0 :
            equalizado = -minimo_coluna
            new_coluna = list(map(lambda x: x + equalizado,coluna))
        if minimo_linha < 0:
            equalizado = -minimo_linha
            new_linha = list(map(lambda x: x + equalizado,linha))
        coordenadas = list(zip(new_linha,new_coluna))
        self.vertices = coordenadas

    def escala(self,pivo,fator_x,fator_y):
        coordenadas = []
        coordenadas.append(pivo)
        for vertice in self.vertices:
            if vertice != pivo :
                x_linha = vertice[0]*fator_x
                y_linha = vertice[1]*fator_y
                x_linha = round(x_linha)
                y_linha = round(y_linha)
                coordenadas.append((x_linha,y_linha))
        return coordenadas

def rotacao(pontos,angulo=0,pivo=(0,0)):
    vertices = trasacao(pontos)
    new_vertices = vertices.rotacao(pivo,angulo)
    return polilinha_pontos(new_vertices)

def translacao(pontos,t_linha,t_coluna):
    poligono = trasacao(pontos)
    new_vertices = poligono.translacao(t_linha,t_coluna)
    return polilinha_pontos(new_vertices)

def escala(pontos,pivo,fator_x,fator_y):
    poligono = trasacao(pontos)
    return polilinha_pontos(poligono.escala(pivo,fator_x,fator_y))

def exec_rotacao(pontos):
    angulo = pontos[-1]
    pontos = pontos[:-1] 
    pontos = list(chunks(pontos))
    pivo = pontos[-1]
    vertices = pontos [:-1]
    print(vertices,angulo,pivo)
    return rotacao(vertices,angulo=angulo,pivo=pivo)
def exec_trasacao(pontos):
    t_x = pontos[-2]
    t_y = pontos[-1]
    vertices = list(chunks(pontos[:-2]))
    print("------>",t_y,t_x,vertices)
    return translacao(vertices,t_linha=t_x,t_coluna=t_y)
def exec_escala(pontos):
    fator_x = pontos[-2]
    fator_y = pontos[-1]
    pontos = list(chunks(pontos[:-2]))
    vertices = pontos[:-1]
    pivo = pontos[-1]
    print (vertices,pivo,fator_x,fator_y)
    return escala(vertices,pivo,fator_x,fator_y)

def rotacao_entrada():
    return ["vertices","pivo","angulo"]
def translacao_entrada():
    return ["vertices","deslocamento"]
def escala_entrada():
    return ["vertices","ponto fixo","fator x","fator y"]
