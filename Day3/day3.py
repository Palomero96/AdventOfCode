def main():
    file = open("c:/Users/david.palomero/Documents/GitHub/AdventofCode/Day3/input.txt", "r")
    cable1= file.readline()

    cable2= file.readline()
    cable1=[dir.strip() for dir in cable1.split(",")]
    cable2=[dir.strip() for dir in cable2.split(",")]
    puntos1=obtenerpuntos(cable1)
    puntos2=obtenerpuntos(cable2)
    cruces=intersection(puntos1,puntos2)

   
    distancias=manhatan(cruces)
    
    print ("Solucion parte 1 "+ str(min(distancias)))
    pasos= obtenerPasos(puntos1, puntos2, cruces )
    print( "Solucion Parte 2 "+ str(min(pasos)))

def obtenerPasos (puntos1:list, puntos2:list, cruces:list):
    listPasos=[]
    for cruce in cruces:
        pasos=0
        for i in puntos1:
            if i==cruce:
                pasos=pasos+1
                break
            else:
                pasos=pasos+1
        for i in puntos2:
            if i==cruce:
                pasos=pasos+1
                break
            else:
                pasos=pasos+1
        listPasos.append(pasos)
    return listPasos

def manhatan(cruces: list):
    distancias=[]
    for punto in cruces:
        distancias.append(abs(punto[0])+ abs(punto[1]))
    return distancias
     
def obtenerpuntos(cable: list):
    puntos=[]
    x, y =0, 0
    for i in cable:
        direccion = i[0]
        distancia = int(i[1:])
        for d in range(0, distancia):
            if direccion== "R":
                x = x + 1
            if direccion =="L":
                x= x - 1
            if direccion == "U":
                y=y+1
            if direccion =="D":
                y=y-1
            puntos.append((x,y))
    return puntos

def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))

if __name__ == "__main__":
    main()