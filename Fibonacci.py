import math
# 1. Algoritmo Inocente/Evidente
# Se calculan los mismos numeros muchas veces llevando a una complejidad exponencial.
def nth_fibonacci_Naive(n):
    if n<=1:
        return n
    # Llamada recursiva
    return nth_fibonacci_Naive(n-1) + nth_fibonacci_Naive(n-2)

# 2. Algoritmo con memoización
# Guardamos calculos ya realizados en la tabla de memoización, evitando redundantes y la complejidad se convierte lineal
def nth_fibonacci_Memoization(n):
    M = [-math.inf for _ in range (n)]
    return nth_fibonacci_M(n,M)
def nth_fibonacci_M(n,M):
    # Si la posición n dentro de la tabla es -infinito, no se encuentra calculado el n-esimo numero.
    if M[n-1] == -math.inf:
        # Caso base, si n <= 1, guardamos en la tabla a n.
        if n<=1:
            M[n-1] = n
        # Si no se cumple el caso base se continúa la recursión
        else:
            M[n-1] = nth_fibonacci_M(n-1,M) + nth_fibonacci_M(n-2,M)
    return M[n-1]

# 3. Algoritmo Bottom-Up
def nth_fibonacci_BottomUp(n):
    M = [-math.inf for _ in range (n)]
    return nth_fibonacci_M(n,M)
def nth_fibonacci_B(n,M):
    # Para Bottom Up inicializamos casos base
    M[0] = 0
    M[1] = 1
    # Cambiamos la recursión y el caso base por ciclos
    """
    if M[n-1] == -math.inf:
        # Caso base, si n <= 1, guardamos en la tabla a n.
        if n<=1:
            M[n-1] = n
        # Si no se cumple el caso base se continúa la recursión
        else:
            M[n-1] = nth_fibonacci_M(n-1,M) + nth_fibonacci_M(n-2,M)
    """
    for i in range(2, n+1):
        M[i] = M[i-1] + M[i-2]
    return M[n]


# print(nth_fibonacci_Naive(38))
# print(nth_fibonacci_Memoization(38))
print(nth_fibonacci_BottomUp(38))

# Memoizacion
# Guardar los resultados ya computados de subproblemas.
