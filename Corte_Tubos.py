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

# 2. Algoritmo con Memoización

def rod_cutting_Memoization(P,n):
    """
    Tenemos que añadir un espacio más a nuestra tabla, si la creamos de tamaño n estamos olvidando la posibilidad de guardar el tamaño 0
    Cuando la creamos de tamaño n, estamos considerando que las unicas posibilidades son dividir toda la varilla en su longitud total, pero
    ahora en este paso de memoización almacenamos el caso base.

    Ejemplo: Vara de tamaño n [1,2,3,4,5] 5 elementos
             Vara de tamaño n, añadiendo el espacio para vara inexistente (n+1) [0,1,2,3,4,5] 6 elementos con el cero
    """
    M = [-math.inf for _ in range (n+1)]
    return rod_cutting_M(P,n,M)

def rod_cutting_M(P,n,M):
    # Si no se tiene datos respecto a esta configuración, se hace el proceso normal
    if M[n] < 0:
        if n == 0:
            M[n] = 0
        else:
            q = -math.inf
            for i in range(1,n+1):
                v = P[i-1] + rod_cutting_M(P,n-i,M)
                if v > q:
                    q = v
            M[n] = q
    return M[n]

# 3. Algoritmo BottomUp
# Pensar ¿En que orden se llena la tabla?

def rod_cutting_BottomUp(P,n):
    # Inicializamos casos base, removemos casos base y reemplazamos recursión por iteraciones
    M = [-math.inf for _ in range (n+1)]
    print(M)
    M[0] = 0
    print(M)
    for i in range(1,n+1):
        for j in range(1,i+1):
            v = P[j-1]+M[i-j]
            if M[i] < v:
                M[i] = v
                print(M)
    return M[n]

# 4. Algoritmo Bottom Up con backtracking
# Utilizamos backtracking para saber donde hicimos los cortes necesarios para llegar a la mayor ganancia
#Esto resulta en un tiempo cuadrático O(n^2), O(n) espacio
def rod_cutting_BU_Backtracking(P,n):
    M = [-math.inf for _ in range (n+1)]
    S = [None] * (n+1)
    M[0] = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            v = P[j-1]+M[i-j]
            if M[i] < v:
                # Donde determinamos el mejor valor v, también asignamos la posición del corte que resulto en ello.
                M[i] = v
                S[i] = j
    m = n
    T = []
    while m > 0:
        T.append(S[m])
        m = m - S[m]
    return M[n], T


#print(rod_cutting_Naive([1,5,8,9],4))
#print(rod_cutting_Memoization([1,5,8,9],4))
#print(rod_cutting_BottomUp([1,5,8,9],4))
print(rod_cutting_BU_Backtracking([2,5,9,10,12,13,15,16],8))

            