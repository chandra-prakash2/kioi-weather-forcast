import csv
import random
import math

WeatherData = open('weatherdata.csv','r')
WeatherOne = list(csv.reader(WeatherData))

thetas = [1, 2, 3, 4, 5, 6]
alpha = 0.000000001

DataNeeded = []

for i in range(1,len(WeatherOne)):
    BlankList = []
    BlankList.append(1)
    BlankList.append(float(WeatherOne[i][0]))
    BlankList.append(float(WeatherOne[i][1]))
    BlankList.append(float(WeatherOne[i][2]))
    BlankList.append(float(WeatherOne[i][4]))
    BlankList.append(float(WeatherOne[i][3]))
    DataNeeded.append(BlankList)

for iternumber in range(0,10000000):

    Dels = [0, 0, 0, 0, 0]
    CostFun = 0

    for SingleData in DataNeeded[0:151]:
        for j in range(0,5):
            Dels[j] += (2*(thetas[0]*SingleData[0] + thetas[1]*SingleData[1] + thetas[2]*SingleData[2] +
                           thetas[3]*SingleData[3] + thetas[4]*SingleData[4] - SingleData[5])*SingleData[j])

    for j in range(0,5):
        Dels[j] = Dels[j]/151

    for j in range(0,5):
        thetas[j] = thetas[j] - alpha*Dels[j]

    for SingleData in DataNeeded[0:151]:
        CostFun += (math.pow((thetas[0]*SingleData[0]+ thetas[1]*SingleData[1] + thetas[2]*SingleData[2]
                    +thetas[3]*SingleData[3] + thetas[4]*SingleData[4] - SingleData[5]),2))

    CostFun = CostFun/151

    print('The value of Cost Function in iteration number '+str(iternumber)+" is "+str(CostFun))


#testing

for SingleData in DataNeeded[151:175]:
    NewTem= (thetas[0]*SingleData[0]+ thetas[1]*SingleData[1] + thetas[2]*SingleData[2] +thetas[3]*SingleData[3] +
           thetas[4]*SingleData[4])

    Error= NewTem-SingleData[5]

    print('Predicted Tem ='+str(NewTem)+ 'Actual Tem  ' + str(SingleData[5]) +'  and Erroe '+ str(Error))

