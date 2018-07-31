#Number of ways of Partitioning an Integer into sum of positive integers
# Eg: P[n=3]=>No of ways of Partitioning an Integer 3 using positive integers {0,1,2,3}
# Solved using Dynamic Programming

def integerPartition(intNum):
    li = [[] for i in range(intNum+1)]
    for r in range(intNum+1):
        for c in range(intNum+1):
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

    return li[intNum][intNum]



while(True):
    print()
    print ("Enter Number 1 for Integer Partitions count")
    print ("Enter Number 2 to Exit this program")
    print()
    option = int(input("Choose your option: "))
    if option == 1:
        intNum = int(input("Enter the Positive Integer: "))
        if intNum >= 0:
            print("we can partition {} into {} ways".format(intNum,integerPartition(intNum)))
        else:
            print("Pls Choose a Valid Number !!!")
    elif option == 2:
        quit()
    else:
        print("Choose a valid option !!!")
