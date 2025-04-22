# Empezamos con la solución recursiva.
"""
Solo podemos, vender la vara completa, o cortarla.
Vamos a cortar y donde vamos a cortar son las unicas primeras opciones que tenemos.

Cuando decidimos cortar, acabamos con dos varas mas pequeñas, cada una con la misma configuración del problema original,
queremos maximizar cuanto podemos obtener a partir de ellas y maximizar cuanto obtendremos por ambas combinadas.

El hecho que los dos subproblemas sean iguales al problema original es la clave para la programación dinámica.


Bajo está configuración, podemos plantear
Optimal(n) = Price[i] + Optimal(n-i)
¿Como determinamos i entonces?
    Probamos todos los valores de i posibles.
    Para todo valor de i, desde 1 hasta n determinar cuánto se puede ganar vendiendo una vara de esa longitud y luego
    recursivamente cortar el restante


Una vez tenemos planteada la recursión solo debemos componer el caso base, el caso base más simple es cuando nos queda
una vara de 0 de longitud, que obtenemos cuando vendemos una vara de tamaño n primero, dejandonos con nada.
"""

import math

# 1. Algoritmo Evidente, programa recursivo
# Es importante no hacer demasiado en un inicio, peimero obtener una respuesta funcional es suficiente, simple y sin preocuparse de eficiencia aún.
# Hay 2^n-1 posibilidades
def rod_cutting_Naive(P, n):
    if n == 0:
        return 0
    else:
        q = -math.inf
        #Queremos probar todos los posibles cortes iniciales i
        for i in range(1,n+1):
            v = P[i-1] + rod_cutting_Naive(P,n-i)
            if v > q:
                q = v
        return q



def rod_cutting_Memoization(P,n):
    M = [-math.ing for _ in range ()]
    return rod_cutting_M(P,n,M)

def rod_cutting_M(P,n,M):
    if M[n] == -math.inf:
        if n == 0:
            M[n] = 0
        else:
            for i in range(1,n+1):
                v = P[i-1] + rod_cutting_Naive(P,n-i)
                if v > q:
                    q = v
            

    if true:
        print("hi")


print(rod_cutting_Naive([1,5,8,9],4))

            