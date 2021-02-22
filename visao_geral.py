from bresenham import bresenham, bresenham_entrada, exec_bresenham,matriz_zero
from tkinter import *
from CG import *
from preenchimento_recursivo import *
from polilinha import exec_polilinha, polilinha_entrada, polilinha_pontos
from cohen_suth import cohenSutherlandClip, exec_line_clip, line_clip, line_clip_entrada
from trasacao import escala_entrada, exec_escala, exec_rotacao, exec_trasacao, rotacao, rotacao_entrada,translacao,escala,translacao_entrada


class visao_geral:
    
    def __init__(self,my_parente,matrix,algoritimo,entrada,preenchimento=False):
        self.matrix = matrix
        self.my_parente = my_parente
        self.labels = []
        self.grid = self.generate_labels()
        self.entradas = []
        self.executa = algoritimo
        self.generate_screen()
        self.generate_imput(entrada)
        self.preenchimento = preenchimento
    def generate_labels(self):
        linha = 0
        coluna = 0
        for element_linha in self.matrix:
            for element_coluna in element_linha: 
                if element_coluna:
                    if element_coluna == 1:
                        pixel = Label(self.my_parente,bg="red",bd=7,relief="raised")
                    else:
                        pixel = Label(self.my_parente,bg="blue",bd=7,relief="raised")
                else:
                    if coluna == 0:
                            if linha!=20:
                                pixel = Label(self.my_parente,text=f"{19-linha}",bg="white",bd=5,relief="raised")
                            else:
                                pixel = Label(self.my_parente,bg="white",bd=7,relief="raised")
                    elif linha == 20:
                        pixel = Label(self.my_parente,text=f"{coluna-1}",bg="white",bd=5,relief="raised")
                    else:
                        pixel = Label(self.my_parente,bg="white",bd=7,relief="raised")
                self.labels.append([pixel,(linha,coluna)])
                coluna+=1
            linha+=1
            coluna=0
    def generate_screen(self):
        for label in self.labels:
            label[0].grid(row=label[1][0], column=label[1][1])
    
    def generate_imput(self,entradas):
        linha = len(self.matrix)
        for entrada in entradas:
            descricao = Label(self.my_parente,text=f"{entrada}")
            descricao.grid(row=len(self.matrix)-linha,column=len(self.matrix[0]))
            linha -= 1
            ed = Entry(self.my_parente)
            ed.grid(row=len(self.matrix)-linha, column=len(self.matrix[0]))
            linha -= 1
            self.entradas.append(ed)
        bt = Button(self.my_parente,text="Confirmar",command=self.bt_click)
        bt.grid(row=len(self.matrix)-linha, column=len(self.matrix[0]))

    def bt_click(self):
        pontos = []
        for ponto in self.entradas:
            num= ponto.get()
            tratamento_ponto = num.split(",")
            new_ponto = list((map(lambda x: int(x) ,tratamento_ponto)))
            pontos.extend((new_ponto))
        pontos = self.executa(pontos)
        if self.preenchimento:
            self.matrix = converter_matriz(pontos[0])
            print(21- pontos[1][0])
            preenchimento_recursivo(self.matrix,20-pontos[1][0],pontos[1][1])
        else:
            self.matrix = converter_matriz(pontos)
        self.grid = self.generate_labels()
        self.generate_screen()
               

def preencher_matriz_coodenadas(matrix,coodenadas,last_row):
    for coodenada in coodenadas:
        matrix[last_row-coodenada[0]][coodenada[1]]=1

def converter_matriz(coordenadas): 
    linha,coluna=zip(*coordenadas)
    minimo_coluna = (min(coluna))
    minimo_linha = (min(linha))
    new_coluna = list(map(lambda x: x + 1,coluna))
    new_linha = linha#list(map(lambda x: x + 1,linha))
    if minimo_coluna < 0 :
        equalizado = -minimo_coluna
        new_coluna = list(map(lambda x: x + equalizado,coluna))
    if minimo_linha < 0:
        equalizado = -minimo_linha
        new_linha = list(map(lambda x: x + equalizado,linha))
    coordenadas = list(zip(new_linha,new_coluna))
    A= matriz_zero(21,40)
    preencher_matriz_coodenadas(A,coordenadas,19)       
    return A


root = Tk()
A = matriz_zero(21,40)
#valores = points_BezierCurve([(0,0),(20,7),(40,0)])
#valores = polilinha_pontos([(-1,-4),(3,2),(7,-4),(3,-11)])
#valores = line_clip(7, 9, 11, 4)
#A = converter_matriz(valores)
#preenchimento_recursivo(A,4,3)

myapp = visao_geral(root,A,exec_polilinha,polilinha_entrada())
root.title("visão geral")
root.mainloop()
#0,0,0,10,5,4        
# 2,5