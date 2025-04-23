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

print(LCS_Naive(['A','B','C','B','D','A','B'], ['B','D','C','A','B','A']))
#print(LCS_Naive(['B','A'], ['B','A','C']))