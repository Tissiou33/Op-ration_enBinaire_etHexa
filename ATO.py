# travaillons sur du binaire et de l'hexa
import sys

def enter_entier():
    #cette fonction vérifie le type du nombre entré
    while True:
        try:
            nombre = int(input("Entrer un nombre : "))
            return (nombre)
        except ValueError:
            print("Entrz un entier")

def conversion_binaire(n):
    #conversion des nombre decimaux en binaire
    print("")
    binaire = []
    valeur = ''
    if n == 0:
        valeur = 00
        return valeur
    elif n == 1:
        valeur ='01'
        return valeur
    else:
        while(n!=0):
            r= n%2
            binaire.append(r)
            n //=2
    i=-1
    while(i> -len(binaire)-1):
        valeur += str(binaire[i])
        i-=1
    return valeur

def conv_h(n):
    #Retourne le reste (modulo) des nombre hexadécimaux
    print("")
    possibilite = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    val = possibilite[n]
    return val

def conversion_hexa(n):
    #convertit les décimaux en hexadécimaux
    print('Conversion en Hexadécimal')
    hexadecimal = []
    val = ''
    i = -1
    nombre = n
    while (n!=0):
        r = n%16
        reste = conv_h(r)
        hexadecimal.append(reste)
        n //=16
    #return hexadecimal
    
    if nombre<16:
        hexadecimal.append(0)
    
    while(i> -len(hexadecimal)-1):
        val += str(hexadecimal[i])
        i-=1   
    return val 
    
def hexadecimal():
    nombre = enter_entier()
    n = conversion_hexa(nombre)
    print("0x_" + n)

def binaire():
    
    nombre = enter_entier()
    n=conversion_binaire(nombre)
    print("0b_" + n)

def bin_dec(n):
    i = 1
    conv = str(n)
    b = len(conv)
    valeur = 0
    for element  in conv:
        expo = 2**(b-i)
        valeur += int(element) * expo
        i += 1
    return valeur

nombre = enter_entier()
deci = bin_dec(nombre)
print(deci)
