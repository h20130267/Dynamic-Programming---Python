def sortList(l):
    i = len(l)
    j = 0
    while i > 0:
        for j in range(i-1):
            if l[j][2] > l[j+1][2]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
        i = i-1
    return l

def weightedJobScheduling(l):
    maxProfit = [jobspec[3] for jobspec in l]
    #print(maxProfit)
    lLen = len(l)
    for i in range(1,lLen):
        for j in range(i):
            if l[i][1] >= l[j][2]:
                temp = l[i][3] + maxProfit[j]
                if temp > maxProfit[i]:
                    maxProfit[i] = temp
    return max(maxProfit)

def printJobSchedulingOrder(l):
    jobOrderRev = ""
    maxProfit = [jobspec[3] for jobspec in l]
    print(maxProfit)
    lLen = len(l)
    for i in range(1,lLen):
        for j in range(i):
            if l[i][1] >= l[j][2]:
                temp = l[i][3] + maxProfit[j]
                if temp > maxProfit[i]:
                    maxProfit[i] = temp
    maxProfitIndex = maxProfit.index(max(maxProfit))
    i = maxProfitIndex
    j = max(maxProfit)
    while(True):
        jobOrderRev += l[i][0]
        j = j-l[i][3]
        if(j == 0):
            break
        i = maxProfit.index(j)
    return jobOrderRev[::-1]
# l is list of lists with each element of l as [jobName,startTime,endTime,profit]
l = [['a',1,4,3],['b',4,6,5],['c',6,7,2],['d',5,7,8],['e',6,8,6],['f',7,10,8]]
l = sortList(l)
#now l contains list elements in sorted(increasing) order of their end times
#print(l)
print ("Weighted job Scheduling Max Profit: ",weightedJobScheduling(l))
print ("Job Scheduling Order for Max Profit: ",printJobSchedulingOrder(l))
