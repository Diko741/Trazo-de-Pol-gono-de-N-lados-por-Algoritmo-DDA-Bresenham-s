import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image
plt.imshow(Image.open('fondo.png'))
coordenadas = []


def bresenham(x1, y1, x2, y2):
    
    dx = x2 - x1
    dy = y2 - y1

    xinc = 1 if dx > 0 else -1
    yinc = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xinc, 0, 0, yinc
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, yinc, xinc, 0

    P = 2*dy - dx
    y = 0
    #Retorno de los elementos uno a uno 
    for x in range(dx + 1):
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
            puntos = list(bresenham(coordenadas[k][0], coordenadas[k][1], coordenadas[0][0], coordenadas[0][1]))
            resultado+=puntos

        else:
            puntos = list(bresenham(coordenadas[k][0], coordenadas[k][1], coordenadas[k+1][0], coordenadas[k+1][1]))
            resultado+=puntos
            
    for i in resultado:
        plt.gca().add_patch(Rectangle((i), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 20)
        

#Solicitar los valores
if __name__ == "__main__": 
    x2 = int(input("\033[;36m"+"Ingrese la Longitud="+'\033[0;m'))
    num= int(input("\033[4;35m"+"numero de lados="+'\033[0;m'))   
    x1 = 1
    y1 = 1
    x2=x2-1
    base= (x1+x2, y1)
    origen = (x1, y1)
    llenarCoordenadas(num, origen, base)
    grafica(num)
    print(coordenadas)
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('*** BRESEMHAMS ***')
    plt.show()