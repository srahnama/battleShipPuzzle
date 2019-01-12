#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import time
import random
class battleShip:
    def __init__(self, n, col, row, populationCounts):
        self.n = n
        #make a Matrix nxn
        self.env = np.zeros((n,n))
        self.col = col
        self.timeout = time.time() + 5
        self.row = row
        self.populationCounts = populationCounts
        self.population = {}
        self.all = sum(row)
        # print(self.env, col, row, sum(row))
    #Make a random matrix that have 1 that sums of them equels to sum of ships


    #
    # Helper functions
    # These are used as support, but aren't direct GA-specific functions.
    #
    def rowColSum(self, matrix):
        #check sum column is equals to number of column
        i = 0
        colSum = []
        for num in self.col:

            colSum.append(num - sum(matrix[:,i]))
            # print(self.env[:,i])
            i+=1
        # print(self.colSum)
        # if(sum(self.colSum) == 0):
        #     print"ok";
        #check sum row is equals to number of row
        rowSum = []
        j = 0
        for num in self.row:
            # print(self.env[j,:])
            rowSum.append(num - sum(matrix[j,:]))
            j+=1
        print(rowSum)
        # if(sum([abs(x) for x in rowSum]) == 0):
        #     # print("row", num, sum(self.env[j,:]))
        #     return True

        return rowSum, colSum


# 1 1 1 => 1
# 
# 1
# 1
# 1 => 2
#
# 1
#   1
#     1 => 3
#
#       1
#     1
#   1 => 4
    def makeOne(self):
        i = 0
        z = 0
        matrix = np.zeros((self.n,self.n))
        # matrix neighbors
        matrixN = np.zeros((self.n,self.n))
        self.timeout = time.time() + 0.5
        while(i < self.all):
            
            if(time.time() > self.timeout):
                return matrix, False
            x= np.random.choice(self.n,1)-1 
            y= np.random.choice(self.n,1)-1
            if(x==self.n-1):
                print(True)
            j = 0
            # print(self.col[z])
            # while(j < self.col[z]):
            self.checkCellNeighbors()
            self.env = matrix
            if((matrix[x,y] != 1)): # and (matrix[x,y] != -1)  ):#and (self.row[x] != 0) and (self.col[y] != 0)):
                # print(self.cellNeighbors[x,y])
                if(self.cellNeighbors[x,y] == 1):
                    if(((matrix[x-1,y-1] == 1) and (matrixN[x-1,y-1] == 3 or matrixN[x-1,y-1] == 3)) or ((matrix[x+1,y+1] == 1) and (matrixN[x+1,y+1] == 3 or matrixN[x+1,y+1] == 0))):
                        if(matrix[x-1,y-1] == 1 and matrixN[x-1,y-1] == 0):
                            matrixN[x-1,y-1] = 3    
                        elif(matrix[x+1,y+1] == 1 and matrixN[x+1,y+1] == 0):
                            matrixN[x+1,y+1]  = 3
                        matrix[x,y] = 1
                        matrixN[x,y] = 3
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i+=1
                    elif(((matrix[x-1,y+1] == 1 ) and (matrixN[x-1,y+1] == 4 or matrixN[x-1,y+1] == 0)) or ((matrix[x+1,y-1] == 1) and (matrixN[x+1,y-1] == 4 or matrixN[x+1,y-1] == 0))):
                        if(matrix[x-1,y+1] == 1 and matrixN[x-1,y+1] == 0):
                            matrixN[x-1,y+1] = 4    
                        elif(matrix[x+1,y-1] == 1 and matrixN[x+1,y-1] == 0):
                            matrixN[x+1,y-1]  = 4
                        matrix[x,y] = 1
                        matrixN[x,y] = 4
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i+=1
                    elif(((matrix[x-1,y] == 1) and (matrixN[x-1,y] == 2 or matrixN[x-1,y] == 0)) or ((matrix[x+1,y] == 1) and (matrixN[x+1,y] == 2 or matrixN[x+1,y] == 0))):
                        if(matrix[x-1,y] == 1 and matrixN[x-1,y] == 0):
                            matrixN[x-1,y] = 2    
                        elif(matrix[x+1,y] == 1 and matrixN[x+1,y] == 0):
                            matrixN[x+1,y] = 2
                        matrix[x,y] = 1
                        matrixN[x,y] = 2
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i+=1
                    elif(((matrix[x,y-1] == 1) and (matrixN[x,y-1] == 1 or matrixN[x,y-1] == 0)) or ((matrix[x,y+1] == 1) and (matrixN[x,y+1] == 1 or matrixN[x,y+1] == 0))):
                        if(matrix[x,y-1] == 1 and matrixN[x,y-1] == 0):
                            matrixN[x,y-1] = 1   
                        elif(matrix[x,y+1] == 1 and matrixN[x,y+1] == 0):
                            matrixN[x,y+1] = 1
                        matrix[x,y] = 1
                        matrixN[x,y] = 1
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i+=1
                    
                elif(self.cellNeighbors[x,y]==0):
                    matrix[x,y] = 1
                    # self.makeMines(matrix, x, y)
                    i+=1
                elif(self.cellNeighbors[x,y] == 2):
                    if((x == 0 and y == 0) or (x == 0 and y == self.n-1) or (x == self.n-1 and y == self.n-1) or (x == self.n-1 and y == 0)):
                        continue
                    elif(x == 0 and y > 0):
                        if((matrix[x,y-1] + matrix[x,y+1] == 2) and (matrixN[x,y-1] == 1) and (matrixN[x,y+1] == 1)):
                            matrix[x,y] = 1
                            matrixN[x,y] = 1
                            # self.makeMines(matrix, x, y, True)
                            i+=1
                    elif(x > 0 and y == 0):
                        if((matrix[x-1,y] + matrix[x+1,y] == 2) and (matrixN[x-1,y] == 2) and (matrixN[x+1,y] == 2)):
                            matrix[x,y] = 1
                            matrixN[x,y] = 2
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                            i+=1
                    elif(x == self.n-1 and y > 0):
                        if((matrix[x,y-1] + matrix[x,y+1] == 2) and (matrixN[x,y-1] == 1) and (matrixN[x,y+1] == 1)):
                            matrix[x,y] = 1
                            matrixN[x,y] = 1
                            i+=1
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                    elif(x > 0 and y == self.n-1):
                        if((matrix[x-1,y] + matrix[x+1,y] == 2) and (matrixN[x-1,y] == 2) and (matrix[x+1,y] == 2)):
                            matrix[x,y] = 1
                            matrixN[x,y] = 2
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                            i+=1

                    else:
                        if((matrix[x-1,y-1] + matrix[x+1,y+1] == 2) and (matrixN[x-1,y-1] == 3) and (matrixN[x+1,y+1] == 3)):

                            matrix[x,y] = 1
                            matrixN[x,y] = 3
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i+=1
                        elif((matrix[x-1,y+1] + matrix[x+1,y-1] == 2) and (matrixN[x-1,y+1] == 4) and (matrixN[x+1,y-1] == 4)):

                            matrix[x,y] = 1
                            matrixN[x,y] = 4
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i+=1
                        elif((matrix[x-1,y] + matrix[x+1,y] == 2) and (matrixN[x-1,y] == 2) and (matrixN[x+1,y] == 2)):

                            matrix[x,y] = 1
                            matrixN[x,y] = 2
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i+=1
                        elif((matrix[x,y-1] + matrix[x,y+1] == 2) and (matrixN[x,y-1] == 1) and (matrixN[x,y+1] == 1)):

                            matrix[x,y] = 1
                            matrixN[x,y] = 1
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i+=1
                        else:
                            continue
                elif(self.cellNeighbors[x,y] > 2):
                    continue


                # j+=1
            # i+=1
        # matrix = self.removeMines(matrix)
        # print(matrix)
        # print(matrixN)
        # print(self.cellNeighbors )
        
        self.env = matrix
        return matrix, True
        # print(matrix[3,3])

# sum all neighbors
    def checkCellNeighbors(self):
        matrix = self.env
        # print(matrix)
        self.cellNeighbors = signal.convolve2d(matrix, np.ones((3,3)), mode='same')
        # print("cellneighbors", self.cellNeighbors)
        # a = signal.convolve2d(matrix, np.ones((2,1)), mode='same')
        # print(a)
        # c = np.roll(matrix,1,0)
        # print(c)
        # d = signal.convolve2d(c, np.ones((2,1)), mode='same')
        # print(d)
        # e = np.roll(matrix,1,1)
        # print(e)
        # f = signal.convolve2d(e, np.ones((2,1)), mode='same')
        # print(f)


                # print(np.ones((2,1)))
        # self.cellNeighbors > 2
        # print(self.cellNeighbors == 2)
        # print(self.cellNeighbors == 3)
        return True

    def neighbers(self):
        matrix = self.env
        self.dic= { "row":self.rowSum, "matrix" : matrix}
        z = 0
        temp = []
        # print(matrix)
        while(not self.isOk()):
            # matrix[:,[self.rowSum.index(min(i for i in self.rowSum)), self.rowSum.index(max(i for i in self.rowSum))]] = matrix[:,[self.rowSum.index(max(i for i in self.rowSum)), self.rowSum.index(min(i for i in self.rowSum))]]
            # print("a",matrix)
            # matrix[:,[self.colSum.index(min(i for i in self.colSum)), self.colSum.index(max(i for i in self.colSum))]] = matrix[:,[self.colSum.index(max(i for i in self.colSum)), self.colSum.index(min(i for i in self.colSum))]]
            # if(sum([abs(x) for x in self.colSum]) != 0):
            #     for i in range(0, self.n):
            #        if(self.colSum[i] > 0 ):

            #     if(self.colSum[self.rowSum.index(min(i for i in self.rowSum if i != 0))] > 0):
            #         z = 0
            #         while(z < self.colSum[self.rowSum.index(min(i for i in self.rowSum if i != 0))]):
            #             ma

            j=0
            while(j< self.n):
                if(self.rowSum[j] > sum(matrix[j,:]) ):
                    j+=1
                    continue
                else:
                    print( [ self.row.index(x) for x in self.row if( x < self.row[j]) ])
                j+=1
            # if(sum([abs(x) for x in self.rowSum]) <  sum([abs(x) for x in self.dic["row"]]) ):
            #         self.env = matrix
            #         self.dic["row"] = self.rowSum;

            #         self.dic["matrix"] = self.env;
            #         print(self.dic)

            z+=1
            if(z==10):
                break
        print(self.dic)

    def makePopulation(self):
        self.population = []
        for i in range(1, self.populationCounts):
            myDic = {}
            matrix, ok = self.makeOne()
            if(ok == True   ):
                row = self.rowColSum(matrix)[0]
                col = self.rowColSum(matrix)[1]
                myDic= { "matrix": matrix, "row":row, "col": col , "rowSum": sum([ abs(x) for x in row]), "colSum": sum([ abs(x) for x in col])   }

                self.population.append(myDic)
        # print(self.population)
        print(min(self.population, key=lambda x:x['colSum'] + x['rowSum']))
        # print(min(self.population, key=lambda x:x['rowSum']))
        # print(min(self.population[item]['colSum'] + self.population[item]['colSum'] for item in self.population))
        # print(min(self.population[item]['rowSum'] for item in self.population))
        # print(self.population[min(self.population, key=self.population.get)])
         
    def fitness(self):
        print("fitness")
    def crossOver(self):
        print("crossOver")
def main():

    col = [2,4,1,1,2,4,1,4]
    row = [3,1,4,1,2,3,0,5]
    populationCounts = 100000
    bs = battleShip(8, col, row, populationCounts)
    bs.makePopulation()
    # bs.makeOne()
    # bs.chackCellNeighbors()
    # bs.isOk()
    # bs.neighbers()
if __name__ == "__main__":
    main()
