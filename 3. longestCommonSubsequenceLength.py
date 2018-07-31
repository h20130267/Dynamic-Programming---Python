def lengthLCS(str1,str2):
    if len(str1)==0 or len(str2)==0:
        return 0
    else:
        rli = ['0'] + list(str1)
        cli = ['0'] + list(str2)
        li =[[] for i in range(len(rli))]
        for r,rchar in enumerate(rli):
            for c,cchar in enumerate(cli):
                if r == 0 or c == 0:
                    li[r].append(0)
                else:
                    if rchar == cchar:
                        li[r].append(li[r-1][c-1] + 1)
                    else:
                        li[r].append(max(li[r-1][c],li[r][c-1]))
        return li[len(str1)][len(str2)]

def printLengthLCS(str1,str2):
    if len(str1)==0 or len(str2)==0:
        print("No Longest Common Subsequence Possible !!!")
    else:
        rli = ['0'] + list(str1)
        cli = ['0'] + list(str2)
        L =[[] for i in range(len(rli))]
        for r,rchar in enumerate(rli):
            for c,cchar in enumerate(cli):
                if r == 0 or c == 0:
                    L[r].append(0)
                else:
                    if rchar == cchar:
                        L[r].append(L[r-1][c-1] + 1)
                    else:
                        L[r].append(max(L[r-1][c],L[r][c-1]))

        length = L[len(str1)][len(str2)]
        #print(length)
        i = m = len(str1)
        j = n = len(str2)
        lcsRev=""
        while i>=0 and j>=0:
            if rli[i] == cli[j]:
                #print(rli[i])
                lcsRev+=rli[i]
                i = i-1
                j = j-1
            else:
                if L[i-1][j] > L[i][j-1]:
                    i = i-1
                    j = j
                else:
                    i = i
                    j = j-1
        lcs = lcsRev[::-1]
        if lcs[0] == '0':
            return lcs[1:]
        else:
            return lcs


#str1 = input("Enter String 1: ")
#str2 = input("Enter String 2: ")
str1 = "XMJYAUZ"
str2 = "MZJAWXU"
#str1 = "BANANA"
#str2 = "ATANA"
print("Length of Longest Common Subsequence b/w given two Strings is: ",lengthLCS(str1,str2))
print("Longest common Subsequence b/w given two strings is: ",printLengthLCS(str1,str2))
