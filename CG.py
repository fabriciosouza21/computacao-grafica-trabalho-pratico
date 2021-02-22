

import numpy as np
import math

from typing import List, Tuple
from scipy.special import comb

 
class BezierCurve:

    def __init__(self, list_of_points: List[Tuple[float, float]]):
        self.list_of_points = list_of_points
        # Degree determines the flexibility of the curve.
        # Degree = 1 will produce a straight line.
        self.degree = len(list_of_points) - 1
        self.output_values=None
        self.x=[]
        self.y=[]
        self.to_plot_x = None
        self.to_plot_y = None
 

    def basis_function(self, t: float) -> List[float]:
        assert 0 <= t <= 1, "Time t must be between 0 and 1."
        output_values: List[float] = []
        for i in range(len(self.list_of_points)):
            # basis function for each i
            output_values.append(
                comb(self.degree, i) * ((1 - t) ** (self.degree - i)) * (t ** i)
            )
        assert round(sum(output_values), 5) == 1
        self.output_values = output_values
        return output_values
 
    def bezier_curve_function(self, t: float) -> Tuple[float, float]:
        assert 0 <= t <= 1, "Time t must be between 0 and 1."
        basis_function = self.basis_function(t)
        x = 0.0
        y = 0.0
        for i in range(len(self.list_of_points)):
            x += basis_function[i] * self.list_of_points[i][0]
            y += basis_function[i] * self.list_of_points[i][1]
        self.x=x.copy()
        self.y=y.copy()
        return (x, y)
 
    def generate_curve(self, step_size: float = 0.01):
        to_plot_x: List[float] = []  # x coordinates of points to plot
        to_plot_y: List[float] = []  # y coordinates of points to plot
        t = 0.0
        while t <= 1:
            value = self.bezier_curve_function(t)
            to_plot_x.append(value[0])
            to_plot_y.append(value[1])
            t += step_size
        x = [i[0] for i in self.list_of_points]
        y = [i[1] for i in self.list_of_points]
        self.to_plot_x=to_plot_x.copy()
        self.to_plot_y=to_plot_y.copy()

# iNICIA COM OS VALORES DE Y E X INVERSOS NA TUPLA
def points_BezierCurve(pontos):

  a=BezierCurve(pontos)  
  x=[]
  y=[]
  a.generate_curve()

  for i in range(len(a.to_plot_x)):
    x.append(math.ceil(a.to_plot_x[i]))
    y.append(math.ceil(a.to_plot_y[i]))
  coord=list(zip(y,x))
  coord=list(dict.fromkeys(coord))
  pontosx=pontos[-1][0]
  pontosy=pontos[-1][1]
  pontoxy=(pontosy,pontosx)
  coord.append(pontoxy)
  return (coord)



def midPointCircleDraw(x_centre, y_centre, r): 
    x = r 
    y = 0
    list_points=[]
  
    list_points.append((x + x_centre,y + y_centre))
     
    if (r > 0) : 
        list_points.append((-x + x_centre,-y + y_centre))
        list_points.append((y + x_centre,x + y_centre)) 
        list_points.append((-y + x_centre,-x + y_centre))
    P = 1 - r  
    while x > y: 
      
        y += 1
          
        if P <= 0:  
            P = P + 2 * y + 1
               
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        if (x < y): 
            break
           
        list_points.append((x + x_centre,y + y_centre)) 
        list_points.append((-x + x_centre,y + y_centre))  
        list_points.append((x + x_centre,-y + y_centre))   
        list_points.append((-x + x_centre,-y + y_centre))  
          
  
        if x != y: 
            list_points.append((y + x_centre,x + y_centre))
            list_points.append((-y + x_centre,x + y_centre))  
            list_points.append((y + x_centre,-x + y_centre))  
            list_points.append((-y + x_centre,-x + y_centre))
    return list_points

def exec_midPointCircleDraw(pontos):
    return midPointCircleDraw(pontos[1],pontos[2],pontos[0])

def midPointCircleDraw_entrada():
    return ["Raio","ponto"]

def points_BezierCurve_entrada():
    return ["Ponto inicial","Ponto Final","Controles"]

def chunks(lista, n=2):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]

def exec_points_BezierCurve(pontos):
    pontos = list(chunks(pontos))
    pontos = list(map(lambda x: (x[1],x[0]),pontos))
    new_pontos = [pontos[0]]
    controles = pontos[2:]
    new_pontos.extend(controles) 
    new_pontos.append(pontos[1])
    return points_BezierCurve(new_pontos)

