
def bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def matriz_zero(linha,colunas):
    matrix = []
    linhas = []
    for linha in range(linha):
        for coluna in range(colunas):
            linhas.append(0)
        matrix.append(linhas)
        linhas = []
    return matrix
def preencher_matriz_coodenadas(matrix,coodenadas,last_row):
    for coodenada in coodenadas:
        matrix[last_row-coodenada[0]][coodenada[1]]=1
def exec_bresenham(pontos):
    return list(bresenham(pontos[0],pontos[1],pontos[2],pontos[3]))
def bresenham_entrada():
    return ["pontos"]