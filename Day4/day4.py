def main():
    solucionUno = part1()
    print (solucionUno)
    solucionDos = part2()
    print (solucionDos)
def part1():
    #108457-562041
    soluciones=0
    for i in range(108457,562041):
        cifras = [int(d) for d in str(i)]
        contador=0
        doble=0
        
        for i in range(0, len(cifras)-1):
            if i!=5:
                if (cifras[i]>cifras[i+1]):
                    break
                else:
                    if cifras[i] == cifras[i+1]:
                        doble= doble+1
                    contador=contador+1

        if contador == 5 and doble>=1:
            soluciones= soluciones+1
    return soluciones       

def part2():
    soluciones=0
    for i in range(108457,562041):
        cifras = [int(d) for d in str(i)]
        contador=0
        doble=0
        repetidos=[]
        for i in range(0, len(cifras)-1):
            if i!=5:
                if (cifras[i]>cifras[i+1]):
                    break
                else:
                    if cifras[i] == cifras[i+1]:
                        doble= doble+1
                    contador=contador+1
        correcto= comprobardigitos(cifras)
        if contador == 5 and doble>=1 and correcto:
            soluciones= soluciones+1
    return soluciones

def comprobardigitos(cifras):
    for i in cifras:
        cantidad=0
        for r in cifras:
            if i==r:
                cantidad=cantidad+1
        if cantidad==2:
            return True
    return False

if __name__ == "__main__":
    main()
