from filecmp import cmp
import random
from collections import Counter
import os
import pprint 
import ast
import time
def read():
    palabra = " "
    data= []
    with open("data.txt" , "r" , encoding="utf-8") as f:
        for line in f:
            data.append(line)
        palabra = random.choice(data)
        palabra = palabra.strip("\n")
    return palabra 
def run():
    palabra = read()
    contador = 0
    word = list(palabra)
    adivinanza= []
    for i in word:
        contador += 1
        adivinanza.append("_ ")
    
    finish = 0
    vidas = 6
    int(vidas)
    while finish == 0:
        os.system("cls")
        print("----------------------------------")
        print("Adivine la palabra: ")
        print(" ")
        for i in range(len(adivinanza)):
            adivinanza2="".join(adivinanza)
        print(adivinanza2)
        str(adivinanza)
        print(" ")
        print("Le quedan:" ,vidas ,"vidas")
        print("----------------------------------")
        letra = input( "ingrese una letra: ")
        error = 0
        for i in range(0, contador):
            if letra == word[i]:
                adivinanza[i] = letra
            else:
                error +=1                      
            if word == adivinanza:
                finish = 1
            else: 
                finish = 0
        
        if error == contador:
            if vidas > 0:
                print("Letra incorrecta, por favor vuelta a intentarlo! ") 
                vidas -= 1
                time.sleep(1)
        else: 
            pass
        if vidas == 0:
            os.system("cls")
            print("PERDISTE! Agotaste las vidas") 
            finish = 1
            time.sleep(1)
        else:
            pass
    if vidas > 0:
        os.system("cls")
        print("Adivinaste!")
        for i in range(len(adivinanza)):
            adivinanza2="".join(adivinanza)
        print("La palabra era: " , adivinanza2)
        
    print("Gracias por haber jugado! ")
    
if __name__ == "__main__":
    run()