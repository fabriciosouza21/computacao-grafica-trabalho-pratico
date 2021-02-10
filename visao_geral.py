from bresenham import bresenham,matriz_zero
from tkinter import *

class visao_geral:
    
    def __init__(self,my_parente,matrix):
        self.matrix = matrix
        self.my_parente = my_parente
        self.labels = []
        self.grid = self.generate_labels()
        self.generate_screen()
    def generate_labels(self):
        linha = 0
        coluna = 0
        for element_linha in self.matrix:
            for element_coluna in element_linha: 
                if element_coluna:
                    pixel = Label(self.my_parente,bg="red",bd=10,relief="raised")
                else:
                    pixel = Label(self.my_parente,bg="white",bd=10,relief="raised")
                self.labels.append([pixel,(linha,coluna)])
                coluna+=1
            linha+=1
            coluna=0
    def generate_screen(self):
        for label in self.labels:
            label[0].grid(row=label[1][0], column=label[1][1])

def preencher_matriz_coodenadas(matrix,coodenadas,last_row):
    for coodenada in coodenadas:
        matrix[last_row-coodenada[0]][coodenada[1]]=1

def converter_matriz(coordenadas): 
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
    A= matriz_zero(max(new_linha)+1,max(new_coluna)+1)
    preencher_matriz_coodenadas(A,coordenadas,max(new_linha))       
    return A


root = Tk()
valores = list(bresenham(10, 2, 15,-10 ))
A = converter_matriz(valores)
myapp = visao_geral(root,A)
root.title("visão geral")
root.mainloop()