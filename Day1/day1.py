import numpy as math
def main():
    file = open("c:/Users/david.palomero/Documents/GitHub/AdventofCode/Day1/input.txt", "r")
    line= file.readline()
    total=0
    numero=100756
    totalnumero=0
    while numero >= 9:
            numero= math.floor(numero/3)-2
            totalnumero=totalnumero+numero
    
    print(totalnumero)
    while line:
        numero=int(line)
        totalnumero=0
        #limite en nueve
        while numero >= 9:
            numero= math.floor(numero/3)-2
            totalnumero=totalnumero+numero
        total=totalnumero+total
        line= file.readline()
    print (total)
    file.close()






if __name__ == "__main__":
    main()