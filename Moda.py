import math
import pprint


def Mode (S):
    return Mode_Aux (S, len (S), len (S))

def Mode_Aux (S, n, i):
    if n == 0 or i == 0:
        return 0
    if S[n-1] == S[i-1]:
        return Mode_Aux(S, n, i-1) + 1
    else:
        return max(Mode_Aux(S, n, i-1), Mode_Aux(S, n-1, i-1))
    
# 2. Memoización

def Mode_Memoization (S):
    n = len (S)
    M = [-math.inf for _ in range (n)]
    return Mode_Memo_Aux (S, n, n, M)

def Mode_Memo_Aux (S, n, i, M):
    if n == 0 or i == 0:
        M[n-1] = 0
    else:
        if S[n-1] == S[i-1]:
            M[n-1] = Mode_Memo_Aux(S, n, i-1, M) + 1
        else:
            M[n-1] = max(Mode_Memo_Aux(S, n, i-1, M), Mode_Memo_Aux(S, n-1, i-1, M))
    return M[n-1]


# 3. Bottom Up

def Mode_Memoization_BottomUp (S):
    n = len (S)
    M = [[0 for _ in range(n+1)] for _ in range(n+1)]
    pprint.pprint(M)
    for j in range (1, n+1):
        for k in range (1, n+1):
            if S[j-1] == S[k-1]:
                M[j][k] = M[j-1][k] + 1
                pprint.pprint(M)
            else:
                M[j][k] = max(M[j-1][k-1], M[j-1][k])
                pprint.pprint(M)
    return M[j][k]






#print (Mode_Memoization([1, 2, 2, 3, 4, 2, 5, 6, 2, 7, 2]))
#print (Mode_Memoization([1, 2, 3, 1]))
#print (Mode_Memoization_BottomUp([1, 2, 2, 3, 4, 2, 5, 6, 2, 7, 2]))
print (Mode_Memoization_BottomUp([1, 2, 3, 1]))


