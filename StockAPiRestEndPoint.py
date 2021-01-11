import numpy as np

#tickSymbol, Company Name, Current Price,Closing price



def Findstats(DataSet, SearchKey):
    for i in range(1,len(DataSet[0])):
        if(DataSet[i][0] == SearchKey):
            return(DataSet[i])

def ReturnHighestPrice(DataSet):
    company_Name = ""
    highestPrice = -1
    for i in range(1,len(DataSet)):#Starting at 1 due to the first line of data is attribute names
        if(DataSet[i][2] > highestPrice):
            highestPrice = DataSet[i][2]
            company_Name = DataSet[i][1]
    return [company_name, highestPrice]



if __name__ == '__main__':

    f = open("StockData.csv", "r")
    fL = f.readline()#first line
    totalMatrix = []
    while(not fL == ""):
        splitedString = np.array(fL.split(','))
        splitedString[len(splitedString)-1] = (splitedString[len(splitedString)-1])[0: len(splitedString[len(splitedString)-1])-1]
        totalMatrix.append(splitedString)
        fL = f.readline()
    #print(totalMatrix)
    print(Findstats(DataSet = totalMatrix, SearchKey = "ACB"))
    print(ReturnHighestPrice(totalMatrix))
