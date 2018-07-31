# This problem is similar to integer partitioning problem
# ex: Total Amount= 5 using {0,1,2,3} denomiantions in how many ways ??

#tA --> Total amount,#maxDen -->{0,1,2,.....,maxDen}
def coinChange(tA,maxDen):
    li = [[] for i in range(maxDen+1)]
    for r in range(maxDen+1):
        for c in range(tA+1):
            if r == 0:
                if c == 0:
                    li[r].append(1)
                else:
                    li[r].append(0)
            else:
                if r > c:
                    li[r].append(li[r-1][c])
                else:
                    li[r].append(li[r-1][c]+li[r][c-r])

    return li[maxDen][tA]



while(True):
    print()
    print ("Enter Number 1 for Coin Change count")
    print ("Enter Number 2 to Exit this program")
    print()
    option = int(input("Choose your option: "))
    if option == 1:
        tA = int(input("Enter the total Amount: "))
        maxDen = int(input("Enter the maximum denomination(non negative): "))
        if tA >= 0 and maxDen >= 0:
            print("Total amount {} can be obtained {} ways using max denomination {}".format(tA,coinChange(tA,maxDen),maxDen))
        else:
            print("Pls give valid inputs !!!")
    elif option == 2:
        quit()
    else:
        print("Choose a valid option !!!")
