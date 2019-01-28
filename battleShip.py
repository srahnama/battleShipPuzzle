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
from matplotlib.widgets import Button
style.use('fivethirtyeight')
fig = plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
fig.set_size_inches(18.5, 10.5, forward=True)
ax1 = fig.add_subplot(1,1,1)
# fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
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


    def lessThan4Neighbors(self, matrix, x, y, myType):
        sum = 1
        flag1 = True
        flag2 = True
        for i in range(0, self.n):
            
            if(myType == 2 ):
                if(y+i < self.n):
                    if(matrix[x,y+i] == 1 and flag1):
                        sum +=1
                    else:
                        flag1 = False
                if(y-i >= 0):
                
                    if(matrix[x,y-i] == 1 and flag2):
                        sum +=1
                    else:
                        flag2 = False

                
            elif(myType == 1  ):
                if( x+i < self.n):
                    if(matrix[x+i,y] == 1 and flag1):
                        sum +=1
                    else:
                        flag1 = False
                if( x-i >= 0):                
                    if(matrix[x-i,y] == 1 and flag2):
                        sum +=1
                    else:
                        flag2 = False
        if sum > 4 : 
            return False

        return True
    
    def addOne(self):
        
        matrix = np.zeros((self.n, self.n))
        matrixP = np.zeros((self.n, self.n))
        self.timeout = time.time() + 5
        while(matrix.sum() != self.all ):

            if(time.time() > self.timeout):
                matrix = np.zeros((self.n, self.n))
                matrixP = np.zeros((self.n, self.n))
                self.timeout = time.time() + 5
                # lessThan4
            x = (np.random.choice(self.n, 1)-1)[0]
            y = (np.random.choice(self.n, 1)-1)[0]
            self.env = matrix
            self.checkCellNeighbors()
            if((matrix[x, y] != 1)and (self.row[x] != 0) and (self.col[y] != 0)  and ((self.row[x] > sum(matrix[x, :])) or (self.col[y] > sum(matrix[:, y])))):
                
                if(self.cellNeighbors[x, y] == 0):
                    # print("no")
                    matrix[x,y] = 1
                    matrixP[x,y] = -1
                elif(self.cellNeighbors[x, y] == 1):
                    if((matrix[x+1,y+1] == 1) or (matrix[x-1,y-1] == 1) or (matrix[x+1,y-1] == 1) or (matrix[x-1,y+1] == 1)):
                        continue
                    elif(matrix[x+1,y] == 1):
                        if(matrixP[x+1,y] == 1):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        if(matrixP[x+1,y] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x+1,y] = 1
                    elif(matrix[x-1,y] == 1):
                        if(matrixP[x-1,y] == 1):
                            if(self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        if(matrixP[x-1,y] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x-1,y] = 1
                    elif(matrix[x,y+1] == 1):
                        if(matrixP[x,y+1] == 2):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        if(matrixP[x,y+1] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y+1] = 2
                    elif(matrix[x,y-1] == 1):
                        if(matrixP[x,y-1] == 2):
                            if(self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        if(matrixP[x,y-1] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y-1] = 2
                elif(self.cellNeighbors[x, y] == 2):
                    if((matrix[x+1,y+1] == 1) or (matrix[x-1,y-1] == 1) or (matrix[x-1,y+1] == 1) or (matrix[x+1,y-1] == 1)):
                        continue
                    elif((matrix[x+1,y] == 1) and (matrix[x-1,y] == 1)):
                        if(matrixP[x+1,y] == 1 and matrixP[x-1,y] == 1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        elif(matrixP[x+1,y] == -1 and matrixP[x-1,y] == 1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                                matrixP[x+1,y] = 1
                        elif(matrixP[x+1,y] == 1 and matrixP[x-1,y] == -1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                                matrixP[x-1,y] = 1
                        elif(matrixP[x+1,y] == -1 and matrixP[x-1,y] == -1 ):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x+1,y] = 1
                            matrixP[x-1,y] = 1
                    elif((matrix[x,y+1] == 1) and (matrix[x,y-1] == 1)):
                        if(matrixP[x,y+1] == 2 and matrixP[x,y-1] == 2 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        elif(matrixP[x,y+1] == -1 and matrixP[x,y-1] == 2 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                                matrixP[x,y+1] = 2
                        elif(matrixP[x,y+1] == 2 and matrixP[x,y-1] == -1 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                                matrixP[x,y-1] = 2
                        elif(matrixP[x,y+1] == -1 and matrixP[x,y-1] == -1 ):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y+1] = 2
                            matrixP[x,y-1] = 2
                else:
                    continue
        return matrix, matrixP, True


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
            matrix, matrixP, ok = self.addOne()
            if(ok == True):
                row = self.rowColSum(matrix)[0]
                col = self.rowColSum(matrix)[1]
                myDic = {"matrix": matrix, "row": row, "col": col, "rowSum": sum(
                    [abs(x) for x in row]), "colSum": sum([abs(x) for x in col]),'positions': matrixP}
                
                self.population.append(myDic)
        
        print(self.population)
        self.sortPopulation()

    def sortPopulation(self):
        self.population = sorted(
            self.population, key=lambda x: x['colSum'] + x['rowSum'])
        # i = (np.random.choice(10, 1)-1)[0]
        # j = (np.random.choice(5, 1)-1)[0]
        j = (np.random.choice(len(self.population), 1)-1)[0]
        min1 = self.population[0]
        min2 = self.population[j]
        # print(self.population[0]['colSum'] + self.population[0]['rowSum'] )
        # print(min2)
        return min1, min2

   

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
        matrix2p = matrix2['positions']
        matrix1 = matrix1['matrix']
        matrix2 = matrix2['matrix']
        
        
        
        matrix = np.zeros((self.n, self.n))
        matrixP = np.zeros((self.n, self.n))

        if(sum([abs(x) for x in bestRow[:(int)(len(matrix)/2)]]) > sum([abs(x) for x in bestRow2[:(int)(len(matrix)/2)]])):
            matrix = matrix1
            matrixP = matrix1p        
            matrix[(int)(len(matrix)/2),:] = np.zeros((len(matrix)))
            matrixP[(int)(len(matrix)/2),:] = np.zeros((len(matrix)))
            matrix[(int)((len(matrix)/2)+1):,:] = matrix2[((int)(len(matrix2)/2)+1):][:]
            matrixP[(int)((len(matrix)/2)+1):,:] = matrix2p[((int)(len(matrix2)/2)+1):][:]
        else:
            matrix = matrix2
            matrixP = matrix2p
            matrix[(int)(len(matrix)/2),:] = np.zeros((len(matrix)))
            matrixP[(int)(len(matrix)/2),:] = np.zeros((len(matrix)))
            matrix[(int)((len(matrix)/2)+1):,:] = matrix1[((int)(len(matrix2)/2)+1):][:]
            matrixP[(int)((len(matrix)/2)+1):,:] = matrix1p[((int)(len(matrix2)/2)+1):][:]

        matrix, matrixP = self.crossOver(matrix, matrixP)
     
            

            # if(ok == True):
        row = self.rowColSum(matrix)[0]
        col = self.rowColSum(matrix)[1]
        myDic = {"matrix": matrix, "row": row, "col": col, "rowSum": sum([abs(x) for x in row]), "colSum": sum([abs(x) for x in col]),'positions': matrixP}
        matMin = sum([abs(x) for x in row]) + sum([abs(x) for x in col])
        
        self.population.append(myDic)
        self.sortPopulation()
        if(len(self.population) > 2*self.populationCounts):
            self.population = self.population[:self.n-1]
        
        if(matMin == 0):
            print("answer is :")
            print(matrix)
            print(matrixP)
            plt.pause(100)
        if(matMin < 5):
            print(matrix)
            print(matrixP)
       
        return matMin

    def addOnes(self, matrix1, matrixP1):
       
        matrix = matrix1
        # matrix neighbors
        matrixP = matrixP1
        self.timeout = time.time() + 5
        
        while(matrix.sum() != self.all ):

            if(time.time() > self.timeout):
                matrix = matrix1
                # matrix neighbors
                matrixP = matrixP1
                self.timeout = time.time() + 5
                # lessThan4
            x = (np.random.choice(self.n, 1)-1)[0]
            y = (np.random.choice(self.n, 1)-1)[0]
            # print(x,y)
            # print(matrix)
            self.env = matrix
            self.checkCellNeighbors()
            if((matrix[x, y] != 1) and (self.row[x] != 0) and (self.col[y] != 0)):#  and ((self.row[x] > sum(matrix[x, :])) or (self.col[y] > sum(matrix[:, y])))):
                
                if(self.cellNeighbors[x, y] == 0):
                    matrix[x,y] = 1
                    matrixP[x,y] = -1
                elif(self.cellNeighbors[x, y] == 1):
                    if((matrix[x+1,y+1] == 1) or (matrix[x-1,y-1] == 1) or (matrix[x+1,y-1] == 1) or (matrix[x-1,y+1] == 1)):
                        continue
                    elif(matrix[x+1,y] == 1):
                        if(matrixP[x+1,y] == 1):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        if(matrixP[x+1,y] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x+1,y] = 1
                    elif(matrix[x-1,y] == 1):
                        if(matrixP[x-1,y] == 1):
                            if(self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        if(matrixP[x-1,y] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x-1,y] = 1
                    elif(matrix[x,y+1] == 1):
                        if(matrixP[x,y+1] == 2):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        if(matrixP[x,y+1] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y+1] = 2
                    elif(matrix[x,y-1] == 1):
                        if(matrixP[x,y-1] == 2):
                            if(self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        if(matrixP[x,y-1] == -1):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y-1] = 2
                elif(self.cellNeighbors[x, y] == 2):
                    if((matrix[x+1,y+1] == 1) or (matrix[x-1,y-1] == 1) or (matrix[x-1,y+1] == 1) or (matrix[x+1,y-1] == 1)):
                        continue
                    elif((matrix[x+1,y] == 1) and (matrix[x-1,y] == 1)):
                        if(matrixP[x+1,y] == 1 and matrixP[x-1,y] == 1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                        elif(matrixP[x+1,y] == -1 and matrixP[x-1,y] == 1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                                matrixP[x+1,y] = 1
                        elif(matrixP[x+1,y] == 1 and matrixP[x-1,y] == -1 ):
                            if(self.lessThan4Neighbors(matrix,x+1,y,1) and self.lessThan4Neighbors(matrix,x-1,y,1)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 1
                                matrixP[x-1,y] = 1
                        elif(matrixP[x+1,y] == -1 and matrixP[x-1,y] == -1 ):
                            matrix[x,y] = 1
                            matrixP[x,y] = 1
                            matrixP[x+1,y] = 1
                            matrixP[x-1,y] = 1
                    elif((matrix[x,y+1] == 1) and (matrix[x,y-1] == 1)):
                        if(matrixP[x,y+1] == 2 and matrixP[x,y-1] == 2 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                        elif(matrixP[x,y+1] == -1 and matrixP[x,y-1] == 2 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                                matrixP[x,y+1] = 2
                        elif(matrixP[x,y+1] == 2 and matrixP[x,y-1] == -1 ):
                            if(self.lessThan4Neighbors(matrix,x,y+1,2) and self.lessThan4Neighbors(matrix,x,y-1,2)):
                                matrix[x,y] = 1
                                matrixP[x,y] = 2
                                matrixP[x,y-1] = 2
                        elif(matrixP[x,y+1] == -1 and matrixP[x,y-1] == -1 ):
                            matrix[x,y] = 1
                            matrixP[x,y] = 2
                            matrixP[x,y+1] = 2
                            matrixP[x,y-1] = 2
                else:
                    continue
        return matrix, matrixP, True



    def crossOver(self, matrix, matrixP):
        # c =  (int)(matrix.sum()) + 1
        # # print("c," ,c )
        # b = (np.random.choice(100, 1)-1)[0]
        if(matrix.sum()<self.all):
             matrix, matrixP, ok = self.addOnes(matrix, matrixP)
        else:
            while(matrix.sum()>self.all-self.row[(int)(len(matrix)/2)]):
                x = (np.random.choice(self.n, 1)-1)[0]
                y = (np.random.choice(self.n, 1)-1)[0]
                if(matrix[x,y] == 1):
                    matrix[x,y] = 0
                    matrixP[x,y] = 0
        matrix, matrixP, ok = self.addOnes(matrix, matrixP)
        # if(matrix[(int)(len(matrix)/2),:].sum()>0):
        #     print(matrix)
        # if random.randint(0,100) < self.mutationRate:
        #     for i in range(0, self.n-1):
        #         for j in range(0, self.n-1):
        #             if(matrix[i, j] == 1):
        #                 matrix[i, j] = 0
        #                 matrixP[i, j] = 0
        #                 break
        #     # matrix = np.rot90(matrix)
        #     # matrixP = np.rot90(matrixP)
        #     # matrix = matrix[::-1]
        #     # matrixP = matrixP[::-1]
        # # if(b % 5 == 3):
        #     matrix = np.fliplr(matrix)
        #     matrixP = np.fliplr(matrixP)
        # #     matrix = matrix[::-1]
        # #     matrixP = matrixP[::-1]

        # print(matrix.sum())
        return matrix, matrixP

   
   

# from tkinter import *

def main(n=0,row=[],col=[],populationCounts=0):
    # a=np.array([[0., 0., 0., 1., 0., 0., 1., 0.],
    #    [0., 1., 0., 0., 0., 0., 0., 0.],
    #    [0., 0., 0., 0., 1., 1., 1., 1.],
    #    [0., 1., 1., 0., 0., 0., 0., 0.],
    #    [0., 0., 0., 0., 0., 1., 0., 0.],
    #    [1., 1., 1., 1., 0., 1., 0., 1.],
    #    [0., 0., 0., 0., 0., 0., 0., 0.],
    #    [1., 0., 0., 1., 0., 0., 1., 0.]])
    
    # b=np.array([[0., 1., 0., 1., 0., 0., 0., 0.],
    #    [0., 1., 0., 0., 0., 1., 1., 0.],
    #    [0., 0., 0., 1., 0., 0., 0., 0.],
    #    [0., 1., 0., 0., 0., 0., 0., 1.],
    #    [0., 0., 0., 0., 1., 0., 0., 1.],
    #    [1., 1., 1., 0., 1., 0., 0., 1.],
    #    [0., 0., 0., 0., 0., 0., 0., 0.],
    #    [1., 0., 0., 0., 1., 1., 0., 1.]])
    # c = b   
    # c[(int)(len(c)/2),:] = np.zeros((8))
    # c[(int)(len(c)/2+1):,:] = a[(int)(len(c)/2+1):][:]

    # print(c)
    # print(c.sum())
    
    # for i in range(5,10):
    #     for j in range(5,10):
    #         c[]

    # print(np.concatenate(a,b))
    # # master=Tk()
    # master.geometry("400x400")
    # frame1=Frame(master, width=10, height=10, background="Blue")
    # for i in range(0,10):
    #     for j in range(0, 10):
    #         if j == 2 or j == 4:
    #             frame1.grid(row=i, column=j)

    
    mutationRate = 3
    if(n==0):

        
        # col = [1,2,1,3,2,2,3,1,5,0]
        # row = [3,2,2,4,2,1,1,2,3,0]
        # populationCounts = 1000
        # bs = battleShip(10, col, row, populationCounts , mutationRate)
    
        col = [2, 4, 1, 1, 2, 4, 1, 4]
        row = [3, 1, 4, 1, 2, 3, 0, 5]
        populationCounts = 50
        bs = battleShip(8, col, row, populationCounts, mutationRate)


        
        # col = [2, 4, 17, 12, 2, 4, 25, 4, 30, 1, 4, 1, 2, 3, 0, 5, 21, 4, 10, 1, 2, 24, 11, 4, 3, 1, 23, 1, 2, 3, 0, 5,3, 1, 4, 1, 2, 3, 0, 5, 2, 34, 1, 1, 2, 4, 1, 4, 2, 4, 1, 1, 2, 4, 1, 4, 3, 1, 4, 1, 2, 3, 0, 5,]
        # row = [3, 1, 4, 1, 2, 30, 0, 5, 2, 4, 1, 25, 2, 4, 12, 4, 2, 24, 10, 17, 21, 4, 1, 23, 3, 1, 4, 11, 2, 3, 0, 5, 3, 1, 34, 1, 2, 3, 0, 5, 2, 4, 1, 1, 2, 4, 1, 4, 2, 4, 1, 1, 2, 4, 1, 4, 3, 1, 4, 1, 2, 3, 0, 5,]
        # print(sum(row))
        # print(sum(row)==sum(col))
        # populationCounts = 100
        # bs = battleShip(64, col, row, populationCounts,mutationRate)
    else:
        bs = battleShip(n, col, row, populationCounts, mutationRate)
    
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

    def pause( e):
        anim.event_source.stop()

        print("answer is :")
        print('matrix: ')
        print(bs.population[0]['matrix'])
        print('row: ')
        print(bs.population[0]['row'])
        print('rowSum: ')
        print(bs.population[0]['rowSum'])
        print('col: ')
        print(bs.population[0]['col'])
        print('colSum: ')
        print(bs.population[0]['colSum'])
        # print(matrixP)
    def unpause(e ):
        anim.event_source.start()

        print("answer is :")
        print(bs.population[0]['matrix'])
        # print(matrixP)
    anim = animation.FuncAnimation(fig, fit)
    axpause = plt.axes([0.7, 0.05, 0.1, 0.075])
    axstart = plt.axes([0.81, 0.05, 0.1, 0.075])
    bPause = Button(axpause, 'pause')
    bPause.on_clicked(pause)
    bstart = Button(axstart, 'start')
    bstart.on_clicked(unpause)
    plt.show()
    # master.mainloop()
    # bs.bestChoices()
    # bs.makeOne()
    # bs.chackCellNeighbors()
    # bs.isOk()
    # bs.neighbers()
if __name__ == "__main__":
    main()
