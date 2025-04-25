import math
import pprint


# 1. Algoritmo Inocente
# No nos preocupamos por optimización, solo queremos una respuesta funcional
# Complejidad 2^n
def LCS_Naive_Aux(X,x_n,Y,y_n):
    # Si la longitud de X o Y es cero
    if x_n == 0 or y_n == 0:
        return 0
    # -1 para acceder al numero de esa longitud
    if X[x_n-1] == Y[y_n-1]:
        return LCS_Naive_Aux(X,x_n-1,Y,y_n-1) + 1
    else:
        u = LCS_Naive_Aux(X,x_n-1,Y,y_n)
        l = LCS_Naive_Aux(X,x_n,Y,y_n-1)
        return max(u, l)

def LCS_Naive(X,Y):
    a = len (Y)
    return LCS_Naive_Aux(X, len (X), Y, len (Y))

# 2. Algoritmo con memoización.
# Añadimos tabulación de resultados
"""
Cuando el algoritmo inocente lleva a cabo la recursión, este hace cálculos del LCS redundantes, ejemplo, cuando el arbol izquierdo busca el LCS
entre X[i][j], y luego el arbol derecho nuevamente encuentra la necesidad de buscar el mismo LCS de X[i][j], este cálculo es redundante y pudo 
evitarse tabulando, lo que se llama un -----Overlapping Problem-----

Complejidad O(m*n)

ATENCIÓN: Esto no es Dynamic Programming, DP utiliza Bottom-up, cuando utilizamos recursión seguimos haciendo Top Down
Sin embargo la tabla si se llenará desde Top a Down
"""
def LCS_Memo_Aux(X,x_n,Y,y_n, M):
    # Si la longitud de X o Y es cero
    if M[x_n][y_n] < 0:
        if x_n == 0 or y_n == 0:
            M[x_n][y_n] = 0
            pprint.pprint(M)
        # -1 para acceder al numero de esa longitud
        else:
            if X[x_n-1] == Y[y_n-1]:
                return LCS_Memo_Aux(X,x_n-1,Y,y_n-1,M) + 1
            else:
                u = LCS_Memo_Aux(X,x_n-1,Y,y_n,M)
                l = LCS_Memo_Aux(X,x_n,Y,y_n-1,M)
                M[x_n][y_n] = max(u, l)
                pprint.pprint(M)
    return M[x_n][y_n]

def LCS_Memo(X,Y):
    # Y Columnas, X Filas
    M = [[-math.inf for _ in range(len (Y)+1)] for _ in range(len (X)+1)]
    pprint.pprint(M)
    return LCS_Memo_Aux(X, len (X), Y, len (Y), M)


# 3. Bottom-Up
def LCS_Memo_Bottom_Up(X,Y):
    # Y Columnas, X Filas
    x_n = len (X)
    y_n = len (Y)
    # Primero se crean columnas, luego filas
    M = [[0 for _ in range(len (X)+1)] for _ in range(len (Y)+1)]
    pprint.pprint(M)
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    for i in range (1, y_n + 1):
        for j in range (1, x_n + 1):
                if X[j-1] == Y[i-1]:
                    M[i][j] = M[i-1][j-1] + 1 
                else:
                    u = M[i-1][j]
                    l = M[i][j-1]
                    M[i][j] = max(u, l)
                    pprint.pprint(M)
                    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    return M[y_n][x_n]

# 4. Bottom Up con BackTracking
def LCS_Memo_Bottom_Up_BackTracking(X,Y):
    # Y Columnas, X Filas
    x_n = len (X)
    y_n = len (Y)
    # Primero se crean columnas, luego filas
    M = [[0 for _ in range(len (X)+1)] for _ in range(len (Y)+1)]
    pprint.pprint(M)
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    for i in range (1, y_n + 1):
        for j in range (1, x_n + 1):
                if X[j-1] == Y[i-1]:
                    M[i][j] = M[i-1][j-1] + 1 
                else:
                    u = M[i-1][j]
                    l = M[i][j-1]
                    M[i][j] = max(u, l)
                    pprint.pprint(M)
                    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    return M[y_n][x_n]




#print(LCS_Naive(['A','B','C','B','D','A','B'], ['B','D','C','A','B','A']))
#print(LCS_Naive(['B','A'], ['B','A','C']))

#print(LCS_Memo(['A','B','C','B','D','A','B'], ['B','D','C','A','B','A']))

print(LCS_Memo_Bottom_Up(['A','B','C','B','D','A','B'], ['B','D','C','A','B','A']))
#print(LCS_Memo_Bottom_Up(['B','A'], ['B','A','C']))