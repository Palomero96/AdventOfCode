import numpy as math
def main():
    file = open("c:/Users/david.palomero/Documents/GitHub/AdventofCode/Day2/input.txt", "r")
    
    numeros = file.readline().split(",")
    #Transformamos los string a numeros
    for i in  range(0, len(numeros)):
        numeros[i]=int(numeros[i])
        verb=0
        noun=0
    for verb in range(0,99):
        for noun in range(0,99): 
            numeros[0]=noun
            numeros[1]=verb
            print(numeros[0])
            print(numeros[1])
            for i in range(0, len(numeros),4):
                posicionreal=i
                #print(posicionreal)
                #print(posicionreal+1)
                #print(posicionreal+2)
                #print(posicionreal+3)  
                if numeros[posicionreal] == 1:
                    numeros[numeros[posicionreal+3]]= numeros[numeros[posicionreal+1]] + numeros[numeros[posicionreal+2]]
                if numeros[posicionreal] == 2:
                    numeros[numeros[posicionreal+3]]= numeros[numeros[posicionreal+1]] * numeros[numeros[posicionreal+2]]
                if numeros[posicionreal] == 99:          
                    break
            if numeros[0] == 19690720:
                print (100*noun +verb)
                break   
    file.close()






if __name__ == "__main__":
    main()