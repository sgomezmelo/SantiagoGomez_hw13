import numpy as np
import random

def sort_doors():
    lista1 = ['goat', 'goat', 'car']
    random.shuffle(lista1)
    return lista1

def choose_door():
    r = np.random.choice([0,1,2])
    return r

def reveal_door(lista, choice):
    primera_cabra = False
    i = 0
    lista_mod = lista[:]
    while(primera_cabra == False):
        if(lista[i] == 'goat' and i != choice):
            primera_cabra = True
            lista_mod[i] = 'GOAT_MONTY'
        i += 1
    return lista_mod

def finish_game(lista,choice,change):
    if(change == False):
        return lista[choice]
    else:
        for i in range(len(lista)):
            if( i != choice and lista[i] != 'GOAT_MONTY'):
                return lista[i]
        
n = 100

lista_true = []
lista_false = []

for i in range(n):
    p = sort_doors()
    c = choose_door()
    p = reveal_door(p,c)
    lista_true.append(finish_game(p,c,True))
    lista_false.append(finish_game(p,c,False))

n_true = 0
n_false = 0

for i in range(n):
    if(lista_true[i] == 'car'):
        n_true += 1
    if(lista_false[i] == 'car'):
        n_false += 1

print('La probabilidad de ganar si el jugador decide cambiar despues de 100 intentos')
print(float(n_true)/n)

print('La probabilidad de ganar si el jugador no decide cambiar despues de 100 intentos')
print(float(n_false)/n)
    
