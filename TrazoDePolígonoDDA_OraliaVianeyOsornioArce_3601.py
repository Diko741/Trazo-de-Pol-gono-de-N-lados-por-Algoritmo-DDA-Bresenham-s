import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image
plt.imshow(Image.open('fondo.png'))
coordenadas = []

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    xinc = 1 if dx > 0 else -1
    yinc = 1 if dy > 0 else -1
    
    if dx > dy:
        steps=dx
        xx, xy, yx, yy = xinc, 0, 0, yinc
    else:
        steps=dx
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, yinc, xinc, 0

    dx = abs(dx)
    dy = abs(dy)
    P = 2*dy - dx
    y = 0
    #Retorno de los elementos uno a uno 
    for x in range(int(dx + 1)):
        yield x1 + x*xx + y*yx, y1 + x*xy + y*yy
        if P >= 0:
            y += 1
            P -= 2*dx
        P += 2*dy

def llenarCoordenadas(num, medio, base):  
    gradosI=0
    x1, y1 = medio
    x2, y2 = base 
    for i in range(num):
        coordenadas.append([])
        print(math.degrees(gradosI))
        for j in range(2): 
            if j == 0:
                puntos = round((x1+math.cos(gradosI)*(x2 - x1)-math.sin(gradosI) * (y2 - y1)))
                coordenadas[i].append(puntos)
            else: 
                puntos = round((y1 + math.sin(gradosI) * (x2 - y1) + math.cos(gradosI)  * (y2 - y1)))
                coordenadas[i].append(puntos)
        gradosI += math.radians(360/num)

def grafica(num):
    resultado=[]
    for k in range(num):
        if k == num-1:
            puntos = list(DDA(coordenadas[k][0], coordenadas[k][1], coordenadas[0][0], coordenadas[0][1]))
            resultado+=puntos

        else:
            puntos = list(DDA(coordenadas[k][0], coordenadas[k][1], coordenadas[k+1][0], coordenadas[k+1][1]))
            resultado+=puntos
            
    for i in resultado:
        plt.gca().add_patch(Rectangle((i), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 50)
        

#Solicitar los valores
if __name__ == "__main__": 
    x2 = int(input("\033[;36m"+"Longitud="+'\033[0;m'))
    num= int(input("\033[4;35m"+"Lados="+'\033[0;m'))   
    x1 = 1
    y1 = 1
    base= (x1+x2, y1)
    origen = (x1, y1)
    llenarCoordenadas(num, origen, base)
    grafica(num)
    print(coordenadas)
    plt.show()