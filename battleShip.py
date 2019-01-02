    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from scipy import signal

class battleShip:
    def __init__(self, n, col, row):
        self.n = n
        #make a Matrix nxn
        self.env = np.zeros((n,n))
        self.col = col
        self.row = row
        self.all = sum(row)
        # print(self.env, col, row, sum(row))
    #Make a random matrix that have 1 that sums of them equels to sum of ships


    #
    # Helper functions
    # These are used as support, but aren't direct GA-specific functions.
    #
    def isOk(self):
        #check sum column is equals to number of column
        # i = 0
        # self.colSum = []
        # for num in self.col:
           
        #     self.colSum.append(num - sum(self.env[:,i]))
        #     # print(self.env[:,i])
        #     i+=1
        # print(self.colSum)
        # if(sum(self.colSum) == 0):
        #     print"ok";
        #check sum row is equals to number of row
        self.rowSum = []
        j = 0
        for num in self.row:
            # print(self.env[j,:])
            self.rowSum.append(num - sum(self.env[j,:]))
            j+=1
        print(self.rowSum)
        if(sum([abs(x) for x in self.rowSum]) == 0):
            # print("row", num, sum(self.env[j,:]))
            return True
        
        return False 


    def makeOne(self):
        i = 0
        z = 0
        matrix = np.zeros((self.n,self.n))
        while(i < self.all):
            x= np.random.randint(0,(self.n)-1)
            y= np.random.randint(0,(self.n)-1)
            j = 0
            # print(self.col[z])
            # while(j < self.col[z]):
            self.checkCellNeighbors()
            self.env = matrix
            if((matrix[x,y] != 1) (matrix[x,y] != -1) ):#and (self.row[x] != 0) and (self.col[y] != 0)):
                if(self.cellNeighbors[x,y] == 1):
                    matrix[x,y] = 1
                    i+=1
                elif(self.cellNeighbors[x,y]==0):
                    matrix[x,y] = 1
                    i+=1
                elif(self.cellNeighbors[x,y]==2):
                    if((x == 0 and y == 0) or (x == 0 and y == self.n-1) or (x == self.n-1 and y == self.n-1) or (x == self.n-1 and y == 0)):
                        continue
                    elif(x == 0 and y > 0):
                        if(matrix[x,y-1] + matrix[x,y+1]==2):
                            matrix[x,y] = 1
                            i+=1    
                    elif(x > 0 and y == 0):
                        if(matrix[x-1,y] + matrix[x+1,y] == 2): 
                            matrix[x,y] = 1
                            i+=1
                    elif(x == self.n-1 and y > 0):
                        if(matrix[x,y-1] + matrix[x,y+1]==2):
                            matrix[x,y] = 1
                            i+=1    
                    elif(x > 0 and y == self.n-1):
                        if(matrix[x-1,y] + matrix[x+1,y] == 2): 
                            matrix[x,y] = 1
                            i+=1
                    
                    else:
                        if((matrix[x-1,y-1] + matrix[x+1,y+1] == 2) or (matrix[x-1,y+1] + matrix[x+1,y-1] == 2) or (matrix[x-1,y] + matrix[x+1,y] == 2) or (matrix[x,y-1] + matrix[x,y+1] == 2)):
                            
                            matrix[x,y] = 1
                            i+=1
                elif(self.cellNeighbors[x,y] > 2):
                    continue
                    
                    
                # j+=1
            # i+=1
        print(matrix)
        print(self.cellNeighbors)
        self.env = matrix
        # print(matrix[3,3])

    def checkCellNeighbors(self):
        matrix = self.env
        # print(matrix)
        self.cellNeighbors = signal.convolve2d(matrix, np.ones((3,3)), mode='same')
        # print(self.cellNeighbors)
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
        
row = [2,4,1,1,2,4,1,4]
col = [3,1,4,1,2,3,0,5]
bs = battleShip(8, col, row)
bs.makeOne()
# bs.chackCellNeighbors()
# bs.isOk()
# bs.neighbers()