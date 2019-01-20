#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal
import time
import random
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import collections
style.use('fivethirtyeight')
fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
fig.set_size_inches(18.5, 10.5, forward=True)
ax1 = fig.add_subplot(1,1,1)
np.set_printoptions(threshold=sys.maxsize)
class battleShip:
    def __init__(self, n, col, row, populationCounts, mutation):
        self.n = n
        # make a Matrix nxn
        self.env = np.zeros((n, n))
        self.col = col
        self.mutationRate = mutation
        self.timeout = time.time() + 5
        self.row = row
        self.populationCounts = populationCounts
        self.population = {}
        self.all = sum(row)
        # print(self.env, col, row, sum(row))
    

    def rowColSum(self, matrix):
        # check sum column is equals to number of column
        i = 0
        colSum = []
        for num in self.col:

            colSum.append(num - sum(matrix[:, i]))
            # print(self.env[:,i])
            i += 1
        # print(self.colSum)
        # if(sum(self.colSum) == 0):
        #     print"ok";
        # check sum row is equals to number of row
        rowSum = []
        j = 0
        for num in self.row:
            # print(self.env[j,:])
            rowSum.append(num - sum(matrix[j, :]))
            j += 1
        # print(rowSum)
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
        matrix = np.zeros((self.n, self.n))
        # matrix neighbors
        matrixN = np.zeros((self.n, self.n))
        self.timeout = time.time() + 0.5
        while(i < self.all):

            if(time.time() > self.timeout):
                return matrix, False
            x = (np.random.choice(self.n, 1)-1)[0]
            y = (np.random.choice(self.n, 1)-1)[0]
            if(x == self.n-1):
                print(True)
            j = 0
            # print(self.col[z])
            # while(j < self.col[z]):
            self.checkCellNeighbors()
            self.env = matrix
            # print(x)
            # and (self.row[x] > sum(matrix[x,:])) and (self.col[y] > sum(matrix[:,y]))):
            if((matrix[x, y] != 1) and (self.row[x] != 0) and (self.col[y] != 0)):
                # print(self.cellNeighbors[x,y])
                if(self.cellNeighbors[x, y] == 1):
                    if(((matrix[x-1, y-1] == 1) and (matrixN[x-1, y-1] == 3 or matrixN[x-1, y-1] == 3)) or ((matrix[x+1, y+1] == 1) and (matrixN[x+1, y+1] == 3 or matrixN[x+1, y+1] == 0))):
                        
                        if(matrix[x-1, y-1] == 1 and matrixN[x-1, y-1] == 0):
                            matrixN[x-1, y-1] = 3
                        elif(matrix[x+1, y+1] == 1 and matrixN[x+1, y+1] == 0):
                            matrixN[x+1, y+1] = 3
                        matrix[x, y] = 1
                        matrixN[x, y] = 3
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i += 1
                    elif(((matrix[x-1, y+1] == 1) and (matrixN[x-1, y+1] == 4 or matrixN[x-1, y+1] == 0)) or ((matrix[x+1, y-1] == 1) and (matrixN[x+1, y-1] == 4 or matrixN[x+1, y-1] == 0))):
                        if(matrix[x-1, y+1] == 1 and matrixN[x-1, y+1] == 0):
                            matrixN[x-1, y+1] = 4
                        elif(matrix[x+1, y-1] == 1 and matrixN[x+1, y-1] == 0):
                            matrixN[x+1, y-1] = 4
                        matrix[x, y] = 1
                        matrixN[x, y] = 4
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i += 1
                    elif(((matrix[x-1, y] == 1) and (matrixN[x-1, y] == 2 or matrixN[x-1, y] == 0)) or ((matrix[x+1, y] == 1) and (matrixN[x+1, y] == 2 or matrixN[x+1, y] == 0))):
                        if(matrix[x-1, y] == 1 and matrixN[x-1, y] == 0):
                            matrixN[x-1, y] = 2
                        elif(matrix[x+1, y] == 1 and matrixN[x+1, y] == 0):
                            matrixN[x+1, y] = 2
                        matrix[x, y] = 1
                        matrixN[x, y] = 2
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i += 1
                    elif(((matrix[x, y-1] == 1) and (matrixN[x, y-1] == 1 or matrixN[x, y-1] == 0)) or ((matrix[x, y+1] == 1) and (matrixN[x, y+1] == 1 or matrixN[x, y+1] == 0))):
                        if(matrix[x, y-1] == 1 and matrixN[x, y-1] == 0):
                            matrixN[x, y-1] = 1
                        elif(matrix[x, y+1] == 1 and matrixN[x, y+1] == 0):
                            matrixN[x, y+1] = 1
                        matrix[x, y] = 1
                        matrixN[x, y] = 1
                        # self.makeMines(matrix, x, y, True)

                        # self.makeMines(matrix, x, y)
                        i += 1

                elif(self.cellNeighbors[x, y] == 0):
                    matrix[x, y] = 1
                    # self.makeMines(matrix, x, y)
                    i += 1
                elif(self.cellNeighbors[x, y] == 2):
                    if((x == 0 and y == 0) or (x == 0 and y == self.n-1) or (x == self.n-1 and y == self.n-1) or (x == self.n-1 and y == 0)):
                        continue
                    elif(x == 0 and y > 0):
                        if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                            matrix[x, y] = 1
                            matrixN[x, y] = 1
                            # self.makeMines(matrix, x, y, True)
                            i += 1
                    elif(x > 0 and y == 0):
                        if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):
                            matrix[x, y] = 1
                            matrixN[x, y] = 2
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                            i += 1
                    elif(x == self.n-1 and y > 0):
                        if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                            matrix[x, y] = 1
                            matrixN[x, y] = 1
                            i += 1
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                    elif(x > 0 and y == self.n-1):
                        if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrix[x+1, y] == 2)):
                            matrix[x, y] = 1
                            matrixN[x, y] = 2
                            # self.makeMines(matrix, x, y, True)
                            # self.makeMines(matrix, x, y)
                            i += 1

                    else:
                        if((matrix[x-1, y-1] + matrix[x+1, y+1] == 2) and (matrixN[x-1, y-1] == 3) and (matrixN[x+1, y+1] == 3)):

                            matrix[x, y] = 1
                            matrixN[x, y] = 3
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i += 1
                        elif((matrix[x-1, y+1] + matrix[x+1, y-1] == 2) and (matrixN[x-1, y+1] == 4) and (matrixN[x+1, y-1] == 4)):

                            matrix[x, y] = 1
                            matrixN[x, y] = 4
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i += 1
                        elif((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):

                            matrix[x, y] = 1
                            matrixN[x, y] = 2
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i += 1
                        elif((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):

                            matrix[x, y] = 1
                            matrixN[x, y] = 1
                            # self.makeMines(matrix, x, y, True)

                            # self.makeMines(matrix, x, y)
                            i += 1
                        else:
                            continue
                elif(self.cellNeighbors[x, y] > 2):
                    continue
            # sys.stdout.write('\r Waiting ')

                # j+=1
            # i+=1
        # matrix = self.removeMines(matrix)
        # print(matrix)
        # print(matrixN)
        # print(self.cellNeighbors )

        self.env = matrix
        return matrix, matrixN, True
        # print(matrix[3,3])

# 1 1 1 => 1
#
# 1
# 1
# 1 => 2
#

    def makeOne1(self):
        i = 0
        z = 0
        matrix = np.zeros((self.n, self.n))
        # matrix neighbors
        matrixN = np.zeros((self.n, self.n))
       
        self.timeout = time.time() + 1
        while(i < self.all):

            if(time.time() > self.timeout):
                matrix = np.zeros((self.n, self.n))
                # matrix neighbors
                matrixN = np.zeros((self.n, self.n))
                self.timeout = time.time() + 5
                i=0
            x = (np.random.choice(self.n, 1)-1)[0]
            y = (np.random.choice(self.n, 1)-1)[0]
            if(x == self.n-1):
                print(True)
            j = 0
            # print(self.col[z])
            # while(j < self.col[z]):
            self.checkCellNeighbors()
            self.env = matrix
            # print(x)
            if((matrix[x, y] != 1) and (self.row[x] != 0) and (self.col[y] != 0) and ((self.row[x] > sum(matrix[x, :])) or (self.col[y] > sum(matrix[:, y])))):#and (self.row[x] != 0) and (self.col[y] != 0) and (self.row[x] > sum(matrix[x, :])) and (self.col[y] > sum(matrix[:, y]))):
                # print(self.cellNeighbors[x,y])
                if(self.cellNeighbors[x, y] == 1):
                    
                    if(((matrix[x-1, y] == 1) and (matrixN[x-1, y] == 2 or matrixN[x-1, y] == 0)) or ((matrix[x+1, y] == 1) and (matrixN[x+1, y] == 2 or matrixN[x+1, y] == 0))):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):
                            if(matrix[x-1, y] == 1 and matrixN[x-1, y] == 0):
                                matrixN[x-1, y] = 2
                            
                            elif(matrix[x+1, y] == 1 and matrixN[x+1, y] == 0):
                                matrixN[x+1, y] = 2

                            matrix[x, y] = 1
                            matrixN[x, y] = 2
                            i += 1
                    elif(((matrix[x, y-1] == 1) and (matrixN[x, y-1] == 1 or matrixN[x, y-1] == 0)) or ((matrix[x, y+1] == 1) and (matrixN[x, y+1] == 1 or matrixN[x, y+1] == 0))):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if(matrix[x, y-1] == 1 and matrixN[x, y-1] == 0):
                                matrixN[x, y-1] = 1
                            elif(matrix[x, y+1] == 1 and matrixN[x, y+1] == 0):
                                matrixN[x, y+1] = 1
                            matrix[x, y] = 1
                            matrixN[x, y] = 1
                            i += 1

                elif(self.cellNeighbors[x, y] == 0):
                    matrix[x, y] = 1
                    i += 1
                elif(self.cellNeighbors[x, y] == 2):
                    if((x == 0 and y == 0) or (x == 0 and y == self.n-1) or (x == self.n-1 and y == self.n-1) or (x == self.n-1 and y == 0)):
                        continue
                    elif(x == 0 and y > 0):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                    elif(x > 0 and y == 0):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):

                            if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1
                    elif(x == self.n-1 and y > 0):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                    elif(x > 0 and y == self.n-1):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):

                            if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrix[x+1, y] == 2)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1

                    else:
                       
                        if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):
                            if(self.lessThan4Neighbors(matrix,x,y,2)):

                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1
                        elif((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                            if(self.lessThan4Neighbors(matrix,x,y,1)):

                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                        else:
                            continue
                elif(self.cellNeighbors[x, y] > 2):
                    continue
         

        # print(matrix)
       
        # self.env = matrix
        return matrix, matrixN, True
       

  


# sum all neighbors


    def checkCellNeighbors(self):
        matrix = self.env
        # print(matrix)
        self.cellNeighbors = signal.convolve2d(
            matrix, np.ones((3, 3)), mode='same')
        
        return True

    
    def makePopulation(self):
        self.population = []
        for i in range(1, self.populationCounts):
            myDic = {}
            matrix, matrixP, ok = self.makeOne1()
            if(ok == True):
                row = self.rowColSum(matrix)[0]
                col = self.rowColSum(matrix)[1]
                myDic = {"matrix": matrix, "row": row, "col": col, "rowSum": sum(
                    [abs(x) for x in row]), "colSum": sum([abs(x) for x in col]),'positions': matrixP}
                
                self.population.append(myDic)
        
        self.sortPopulation()

    def sortPopulation(self):
        self.population = sorted(
            self.population, key=lambda x: x['colSum'] + x['rowSum'])
        i = (np.random.choice(10, 1)-1)[0]
        j = (np.random.choice(5, 1)-1)[0]
        # j = (np.random.choice(len(self.population), 1)-1)[0]
        min1 = self.population[0]
        min2 = self.population[j]
        # print(self.population[0]['colSum'] + self.population[0]['rowSum'] )
        # print(min2)
        return min1, min2

   

    def lessThan4Neighbors(self, matrix, x, y, myType):
        sum = 1
        flag1 = True
        flag2 = True
        for i in range(0, self.n-1):
            
            if(myType == 1 and y+i < self.n):
                if(matrix[x,y+i] == 1 and flag1):
                    sum +=1
                else:
                    flag1 = False
                if(matrix[x,y-i] == 1 and flag2):
                    sum +=1
                else:
                    flag2 = False

                
            elif(myType == 2 and x+i < self.n ):
                if(matrix[x+i,y] == 1 and flag1):
                    sum +=1
                else:
                    flag1 = False
                if(matrix[x-i,y] == 1 and flag2):
                    sum +=1
                else:
                    flag2 = False
        if sum > 4 : 
            return False

        return True


    def fitness(self,mutation ):

        matrix1, matrix2 = self.sortPopulation()
        bestCol = matrix1['col']
        bestRow = matrix1['row']
        
        bestColSum = matrix1['colSum']
        bestRowSum = matrix1['rowSum']
        
        bestCol2 = matrix2['col']
        bestRow2 = matrix2['row']
        
        bestColSum2 = matrix2['colSum']
        bestRowSum2 = matrix2['rowSum']

        # matMin = matrix1['colSum'] + matrix1['rowSum']
        if (matrix1['colSum'] + matrix1['rowSum'] == 0):
            print(matrix1)
        # print(matrix1['colSum'] + matrix1['rowSum'])
        matrix1p = matrix1['positions']
        matrix1 = matrix1['matrix']
        matrix2 = matrix2['matrix']
       
        matrix = np.zeros((self.n, self.n))
        matrixP = np.zeros((self.n, self.n))
        for i in range(0, self.n-1):
            for j in range(0, self.n-1):
                if(matrix1[i, j] == matrix2[i, j]):#and bestRow[i] == 0 and bestCol[j] == 0 and bestRow2[i] == 0 and bestCol2[j] == 0):
                    matrix[i, j] = matrix1[i, j]
                    matrixP[i, j] = matrix1p[i, j]
                    
                elif(bestRow[i] == 0 and bestRow2[i] == 0):
                    matrix[i, j] = matrix1[i, j]
                    matrixP[i, j] = matrix1p[i, j]
                elif(bestCol[j] == 0 and bestCol2[j] == 0):
                    matrix[j, i] = matrix1[j, i]
                    matrixP[j, i] = matrix1p[j, i]
               
        for i in range(0, self.n-1):
            for j in range(0, self.n-1):
                
                if((bestRow[i] != 0 and bestRow2[i] != 0) and matrix[i, j] == 1 ):
                    matrix[i, j] = 0    
                    matrixP[i, j] = 0
                    # print("ok"
                    
                if(bestCol[j] != 0 and bestCol2[j] != 0 and matrix[i, j] == 1 ):
                    matrix[i, j] = 0
                    matrixP[i, j] = 0 
                    
                    
        
        # print(matrix)
        #crossOver
        
        # matrix, matrixP = self.crossOver(matrix, matrixP, bestCol, bestRow, bestColSum, bestRowSum)
        if(matrix.sum() < sum(self.row)):
            # print("matrix",matrix.sum())
            matrix, matrixP, ok = self.addOnes(matrix, matrixP)
            # matrix, matrixP = self.mutation(matrix, matrixP)
            matrix, matrixP = self.crossOver(matrix, matrixP)

            if(ok == True):
                row = self.rowColSum(matrix)[0]
                col = self.rowColSum(matrix)[1]
                myDic = {"matrix": matrix, "row": row, "col": col, "rowSum": sum([abs(x) for x in row]), "colSum": sum([abs(x) for x in col]),'positions': matrixP}
                matMin = sum([abs(x) for x in row]) + sum([abs(x) for x in col])
                # flag = True
                # for item in self.population:
                #     if((item['matrix']==myDic['matrix']).all()):
                #         print((item['matrix']==myDic['matrix']).all())
                #         # print(item['matrix'])
                #         # print(myDic['matrix'])
                #     # if(item['matrix'] == myDic['matrix']):
                #         flag = False
                # if flag:
                self.population.append(myDic)
                # popLen = (int)(len(self.population))
                # if(  popLen > 20):
                #     for i in range(19, (popLen-2)):
                #         del self.population[i]
                if(matMin == 0):
                    print("answer is :")
                    print(matrix)
                    print(matrixP)
                    plt.pause(100)
                if(matMin < 5):
                    print(matrix)
                    print(matrixP)
        # print(matrix)
        # return sum([abs(x) for x in row]) + sum([abs(x) for x in col])
        return matMin

    def addOnes(self, matrix, matrixP):
        i = 0
        z = 0
        matrix = matrix
        # matrix neighbors
        matrixN = matrixP
        # lessThan4
        matrixS = np.zeros((self.n, self.n))
        self.timeout = time.time() + 5
        while(matrix.sum() != self.all ):

            if(time.time() > self.timeout):
                matrix = matrix
                # matrix neighbors
                matrixN = matrixP
                self.timeout = time.time() + 5
                # lessThan4
            x = (np.random.choice(self.n, 1)-1)[0]
            y = (np.random.choice(self.n, 1)-1)[0]
            if(x == self.n-1):
                print(True)
            j = 0
            # print(matrix.sum(), self.all)
            # while(j < self.col[z]):
            self.checkCellNeighbors()
            self.env = matrix
            
            # print(x)
            if((matrix[x, y] != 1)and (self.row[x] != 0) and (self.col[y] != 0) and (self.row[x] != 0) and (self.col[y] != 0) and ((self.row[x] > sum(matrix[x, :])) or (self.col[y] > sum(matrix[:, y])))):#and (self.row[x] != 0) and (self.col[y] != 0) and (self.row[x] > sum(matrix[x, :])) and (self.col[y] > sum(matrix[:, y]))):
                # print(self.cellNeighbors[x,y])
                if(self.cellNeighbors[x, y] == 1):
                    
                    if(((matrix[x-1, y] == 1) and (matrixN[x-1, y] == 2 or matrixN[x-1, y] == 0)) or ((matrix[x+1, y] == 1) and (matrixN[x+1, y] == 2 or matrixN[x+1, y] == 0))):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):
                            if(matrix[x-1, y] == 1 and matrixN[x-1, y] == 0):
                                matrixN[x-1, y] = 2
                            
                            elif(matrix[x+1, y] == 1 and matrixN[x+1, y] == 0):
                                matrixN[x+1, y] = 2

                            matrix[x, y] = 1
                            matrixN[x, y] = 2
                            i += 1
                    elif(((matrix[x, y-1] == 1) and (matrixN[x, y-1] == 1 or matrixN[x, y-1] == 0)) or ((matrix[x, y+1] == 1) and (matrixN[x, y+1] == 1 or matrixN[x, y+1] == 0))):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if(matrix[x, y-1] == 1 and matrixN[x, y-1] == 0):
                                matrixN[x, y-1] = 1
                            elif(matrix[x, y+1] == 1 and matrixN[x, y+1] == 0):
                                matrixN[x, y+1] = 1
                            matrix[x, y] = 1
                            matrixN[x, y] = 1
                            i += 1

                elif(self.cellNeighbors[x, y] == 0):
                    matrix[x, y] = 1
                    i += 1
                elif(self.cellNeighbors[x, y] == 2):
                    if((x == 0 and y == 0) or (x == 0 and y == self.n-1) or (x == self.n-1 and y == self.n-1) or (x == self.n-1 and y == 0)):
                        continue
                    elif(x == 0 and y > 0):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                    elif(x > 0 and y == 0):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):

                            if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1
                    elif(x == self.n-1 and y > 0):
                        if(self.lessThan4Neighbors(matrix,x,y,1)):

                            if((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                    elif(x > 0 and y == self.n-1):
                        if(self.lessThan4Neighbors(matrix,x,y,2)):

                            if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrix[x+1, y] == 2)):
                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1

                    else:
                       
                        if((matrix[x-1, y] + matrix[x+1, y] == 2) and (matrixN[x-1, y] == 2) and (matrixN[x+1, y] == 2)):
                            if(self.lessThan4Neighbors(matrix,x,y,2)):

                                matrix[x, y] = 1
                                matrixN[x, y] = 2
                                i += 1
                        elif((matrix[x, y-1] + matrix[x, y+1] == 2) and (matrixN[x, y-1] == 1) and (matrixN[x, y+1] == 1)):
                            if(self.lessThan4Neighbors(matrix,x,y,1)):

                                matrix[x, y] = 1
                                matrixN[x, y] = 1
                                i += 1
                        else:
                            continue
                elif(self.cellNeighbors[x, y] > 2):
                    continue

        self.env = matrix
        return matrix, matrixN, True

    def crossOver(self, matrix, matrixP):
        # c =  (int)(matrix.sum()) + 1
        # # print("c," ,c )
        # b = (np.random.choice(100, 1)-1)[0]
       
        if random.randint(0,100) < self.mutationRate:
            matrix = np.rot90(matrix)
            matrixP = np.rot90(matrixP)
            # matrix = matrix[::-1]
            # matrixP = matrixP[::-1]
        # if(b % 5 == 3):
        #     # matrix = np.fliplr(matrix)
        #     # matrixP = np.fliplr(matrixP)
        #     matrix = matrix[::-1]
        #     matrixP = matrixP[::-1]

       
        return matrix, matrixP
   
   

def main():
    mutationRate = 3
    # col = [1,2,1,3,2,2,3,1,5,0]
    # row = [3,2,2,4,2,1,1,2,3,0]
    # populationCounts = 1000
    # bs = battleShip(10, col, row, populationCounts , mutationRate)
   
    col = [2, 4, 1, 1, 2, 4, 1, 4]
    row = [3, 1, 4, 1, 2, 3, 0, 5]
    populationCounts = 10
    bs = battleShip(8, col, row, populationCounts, mutationRate)


    
    # col = [2, 4, 17, 12, 2, 4, 25, 4, 30, 1, 4, 1, 2, 3, 0, 5, 21, 4, 10, 1, 2, 24, 11, 4, 3, 1, 23, 1, 2, 3, 0, 5,3, 1, 4, 1, 2, 3, 0, 5, 2, 34, 1, 1, 2, 4, 1, 4, 2, 4, 1, 1, 2, 4, 1, 4, 3, 1, 4, 1, 2, 3, 0, 5,]
    # row = [3, 1, 4, 1, 2, 30, 0, 5, 2, 4, 1, 25, 2, 4, 12, 4, 2, 24, 10, 17, 21, 4, 1, 23, 3, 1, 4, 11, 2, 3, 0, 5, 3, 1, 34, 1, 2, 3, 0, 5, 2, 4, 1, 1, 2, 4, 1, 4, 2, 4, 1, 1, 2, 4, 1, 4, 3, 1, 4, 1, 2, 3, 0, 5,]
    # print(sum(row))
    # print(sum(row)==sum(col))
    # populationCounts = 10
    # bs = battleShip(64, col, row, populationCounts,mutationRate)

    
    bs.makePopulation()
    # bs.fitness()
    xs = []
    ys = []
    # plt.xlim(-1, 1)
    # plt.ylim(-1, 1)

    # Don't mess with the limits!
    plt.autoscale(False)
    def fit(i):
        # print("ok2")
        
        xs.append(i)
        ys.append(bs.fitness(mutationRate))
        ax1.clear()
        ax1.plot(xs,ys)
    # print("ok1")
    anim = animation.FuncAnimation(fig, fit)
    plt.show()
    # bs.bestChoices()
    # bs.makeOne()
    # bs.chackCellNeighbors()
    # bs.isOk()
    # bs.neighbers()
if __name__ == "__main__":
    main()
