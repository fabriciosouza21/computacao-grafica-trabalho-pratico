def preenchimento_recursivo(Matriz,x,y):
    ponto_atual=[x,y]
    if (Matriz[x][y]!= 1 and Matriz[x][y] != 2 ):
        Matriz[x][y]=2
        if (x+1 < len(Matriz) and y+1 < len( Matriz[x]) ):
            preenchimento_recursivo(Matriz,x+1,y)
            preenchimento_recursivo(Matriz,x-1,y)
            preenchimento_recursivo(Matriz,x,y+1)
            preenchimento_recursivo(Matriz,x,y-1)


