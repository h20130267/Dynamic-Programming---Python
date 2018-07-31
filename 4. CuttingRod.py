p = [0]

def cuttingRod(rodLen):
    memMat = [[] for i in range(rodLen)]
    for r in range(rodLen):
        for c in range(rodLen + 1):
            if r == 0 or c == 0:
                memMat[r].append(0)
            else:
                if r > c:
                    memMat[r].append(memMat[r-1][c])
                else:
                    memMat[r].append(max(memMat[r-1][c],p[r]+memMat[r][c-r]))
    return memMat[rodLen-1][rodLen]

def printPieces(rodLen):
    L = [[] for i in range(rodLen)]
    for r in range(rodLen):
        for c in range(rodLen + 1):
            if r == 0 or c == 0:
                L[r].append(0)
            else:
                if r > c:
                    L[r].append(L[r-1][c])
                else:
                    L[r].append(max(L[r-1][c],p[r]+L[r][c-r]))
    #return L[rodLen-1][rodLen]
    i = rodLen - 1
    j = rodLen
    res = []
    while i>=0 and j>=0:
        if L[i][j] == L[i-1][j]:
            i = i-1
            j = j
        else:
            res.append(i)
            j = j-i
            i = i
    return res
    
rodLen = int(input("Enter the Rod Length: "))
for i in range(1,rodLen):
    print("Enter Profit for piece of length ",i,": ",end="")
    p.append(int(input("")))
print("Max Profit: ",cuttingRod(rodLen))
print("length of pieces to make max profit: ",printPieces(rodLen))
