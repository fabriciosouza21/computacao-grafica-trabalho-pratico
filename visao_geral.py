from tkinter import Label


from tkinter import *
from tkinter import ttk

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
                    pixel = Label(self.my_parente,bg="red",bd=4)
                    print("vermelhor")
                else:
                    pixel = Label(self.my_parente,bg="white",bd=4)
                    print("azul")
                self.labels.append([pixel,(linha,coluna)])
                coluna+=1
            linha+=1
            coluna=0
    def generate_screen(self):
        for label in self.labels:
            label[0].grid(row=label[1][0], column=label[1][1])

    
                
      

A = [[1,0,0,0,0,0,0],
     [0,1,0,0,0,0,0],
     [0,0,1,0,0,0,0],
     [0,0,0,1,0,0,0],
     [0,0,0,0,1,0,0],
     [0,0,0,0,0,1,0],
     [0,0,0,0,0,0,1]]   
root = Tk()
myapp = visao_geral(root,A)
root.title("visão geral")
root.mainloop()