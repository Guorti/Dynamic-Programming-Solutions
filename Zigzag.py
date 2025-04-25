def Zig_Naive(S):
    n = len (S)
    i = n-1
    return Zig_Naive_Aux(S,n,i,False)

def Zig_Naive_Aux(S, n, i, F):
    if n == 0 or i == 0:
        return 0
    if S[i-1] - S[n-1] > 0 and F == False:
        return Zig_Naive_Aux(S, n-1, i-1, True) + 1

    if S[i-1] - S[n-1] < 0 and F == True:
        return Zig_Naive_Aux(S, n-1, i-1, False) + 1
    
    if S[i-1] - S[n-1] > 0 and F == True:
        return Zig_Naive_Aux(S, n, i-1, F)
    else:
        return Zig_Naive_Aux(S, n-1, i-1, F)


print(Zig_Naive([5,2,9,4,7,1]))