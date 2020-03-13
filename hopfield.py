import os


def calcWeight(savedsample):
    N = len(savedsample[0])
    P = len(savedsample)
    mat = [0]*N
    returnMat = []
    for i in range(N):
        m = mat[:]
        returnMat.append(m)
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            sum = 0
            for u in range(P):
                sum += savedsample[u][i] * savedsample[u][j]
            returnMat[i][j] = sum/float(N)
    return returnMat


def calcXi(inMat , weighMat):
    returnMat = inMat
    choose = []
    for i in range(len(inMat)/5):
        #随机改变N/5个神经元的值，该参数可调，也可同时改变所有神经元的值
        choose.append(random.randint(0,len(inMat)-1))
    for i in choose:
        sum = 0
        for j in range(len(inMat)):
            sum += weighMat[i][j] * inMat[j]
        if sum>=0:
            returnMat[i] = 1
        else: returnMat[i] = -1
    return returnMat

 sample =  [[1,-1,-1,-1,1,
           1,1,-1,-1,1,
           1,-1,1,-1,1,
           1,-1,-1,1,1,
           1,-1,-1,-1,1],
          [1,1,1,1,1,
           1,-1,-1,-1,-1,
           1,1,1,1,1,
           1,-1,-1,-1,-1,
           1,1,1,1,1],
          [1,1,1,1,-1,
           1,-1,-1,-1,1,
           1,1,1,1,-1,
           1,-1,-1,1,-1,
           1,-1,-1,-1,1],
          [-1,1,1,1,-1,
           1,-1,-1,-1,1,
           1,-1,-1,-1,1,
           1,-1,-1,-1,1,
           -1,1,1,1,-1]]
def addnoise(mytest_data,n):
    for x in range(n):
        for y in range(n):
            if random.randint(0, 10) > 7:
                mytest_data[x * n + y] = -mytest_data[x * n + y]
    return mytest_data


def regularout(data,N):
    for j in range(N):
        ch = ""
        for i in range(N):
            ch += " " if data[j*N+i] == -1 else "X"
        print ch

if __name__ == '__main__':
	print "sfjafaklsfjalf"
	regularout(sample[1],5)
	test = addnoise(sample[1],5)
	regularout(test,5)
	for i in range(2000):
    	test = calcXi(test,weightMat
	regularout(test,5)