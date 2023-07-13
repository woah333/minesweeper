import random
import math

class minesweeperboard():
    def __init__(self, boardsize=0, amountmines=0, totaltiles=0, tilelist=[], tilelistempty=[], hasmines=False):
        self.boardsize = boardsize
        self.amountmines = amountmines
        self.totaltiles = totaltiles
        self.tilelist = tilelist
        self.tilelistempty = tilelistempty
        self.hasmines = hasmines

    def setStuff(self, string):
        if string == "easy":
            self.boardsize = 8
            self.amountmines = 10
            self.totaltiles = 64
            self.tilelistempty = [" "]* 64
            return True
        elif string == "medium":
            self.boardsize = 12
            self.amountmines = 20
            self.totaltiles = 144
            self.tilelistempty = [" "]* 144
            return True
        elif string == "hard": 
            self.boardsize = 16
            self.amountmines = 40
            self.totaltiles = 256
            self.tilelistempty = [" "]* 256
            return True
        else:
            return False
            
    
    def setTileList(self, listt):
        self.tilelist = listt

    def getSize(self):
        return self.boardsize

    def getAmountMines(self):
        return self.amountmines

    def getTotalTiles(self):
        return self.totaltiles
    
    def getTileList(self):
        return self.tilelist    
    
    def getTileListEmpty(self):
        return self.tilelistempty
    
    def getHasMines(self):
        return self.hasmines
    
    def setHasMines(self, mines):
        self.hasmines = mines
    
    def addaround8(self, i):
            # top left
            if i-self.getSize()-1 >= 0:
                if isinstance(self.tilelist[i-self.getSize()-1], int) and self.isLeft(i)==False:
                    self.tilelist[i-self.getSize()-1]+=1
            # top center
            if i-self.getSize() >= 0:
                if isinstance(self.tilelist[i-self.getSize()], int):
                    self.tilelist[i-self.getSize()]+=1
            # top right
            if i-self.getSize()+1 >= 0:
                if isinstance(self.tilelist[i-self.getSize()+1], int) and not self.isRight(i):
                    self.tilelist[i-self.getSize()+1]+=1
            # left
            if i-1 > 0:
                if isinstance(self.tilelist[i-1], int) and self.isLeft(i)==False:
                    self.tilelist[i-1]+=1
            # right
            if i+1 < self.totaltiles:
                if isinstance(self.tilelist[i+1], int) and self.isRight(i)==False:
                    self.tilelist[i+1]+=1
            # botom left
            if i+self.getSize()-1 < self.totaltiles:
                if isinstance(self.tilelist[i+self.getSize()-1], int) and self.isLeft(i)==False:
                    self.tilelist[i+self.getSize()-1]+=1
            # botom
            if i+self.getSize() < self.totaltiles:
                if isinstance(self.tilelist[i+self.getSize()], int):
                    self.tilelist[i+self.getSize()]+=1
            # bottom right
            if i+self.getSize()+1 < self.totaltiles:
                if isinstance(self.tilelist[i+self.getSize()+1], int) and self.isRight(i)==False:
                    self.tilelist[i+self.getSize()+1]+=1

    def getaround8(self, i):
        around8list = []
        around8list.append((i, ""))
        around8list.append((i-self.getSize()-1, "left"))
        around8list.append((i-self.getSize(), ""))
        around8list.append((i-self.getSize()+1, "right"))
        around8list.append((i-1, "left"))
        around8list.append((i+1, "right"))
        around8list.append((i+self.getSize()-1, "left"))
        around8list.append((i+self.getSize(), ""))
        around8list.append((i+self.getSize()+1, "right"))
        return around8list
        
    def checkaround8(self, i):
        around8list = self.getaround8(i)
        for iii in around8list:
            (i2,lr) = iii
            if i2 >= 0 and i2 < self.totaltiles:
                if isinstance(self.tilelist[i2], int) and ((lr=="left" and self.isLeft(i)==False) or (lr=="right" and self.isRight(i)==False) or lr == ""):
                    if self.tilelist[i2]==0:
                        self.tilelistempty[i2]="_"
                        self.tilelist[i2]="_"
                        self.checkaround8(i2)
                    else:
                        self.tilelistempty[i2]=self.tilelist[i2]
        return around8list

    def minelaying(self, location):
        minelist = set()
        around8listtt = self.getaround8(location)
        while len(minelist) < self.getAmountMines():
            var = random.randint(1, self.getTotalTiles())
            around8ListDict = dict(around8listtt)
            if var not in around8ListDict:
                minelist.add(var)
        #print(minelist)
        self.tilelist = []
        for i in range(0, self.getTotalTiles()): 
            if i in minelist:
                self.tilelist.append("X")
            else:
                self.tilelist.append(0)
        for i in range(0, self.getTotalTiles()):
                if self.tilelist[i]=="X":
                    self.addaround8(i)
    
        self.setTileList(self.tilelist)
        count = 1
        if self.boardsize == 8:
            print("     A  B  C  D  E  F  G  H")
        elif self.boardsize == 12:
            print("     A  B  C  D  E  F  G  H  I  J  K  L")
        elif self.boardsize == 16:
            print("     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
        for i in range(self.totaltiles):
            p = i+1
            if(p % self.boardsize) == 1:
                if count < 10:
                    print("",count, " ", end="")
                elif count >= 10:
                    print(count, " ", end="")
         
            print("[" + str(self.tilelist[i]) + "]", end="")
            if(p % self.boardsize) == 0:
                print("")
                count+= 1


    def isRight(self, i):
        return i % self.boardsize == self.boardsize-1
    
    def isLeft(self, i):
        return i % self.boardsize == 0
    

    def setFlag(self, location):
        if self.getTileList()[location]=="X" and self.getTileListEmpty()[location]==" ":
            self.getTileListEmpty()[location]="F"
        elif str(self.getTileList()[location]).isnumeric()==True and self.getTileListEmpty()[location]==" ":
            self.getTileListEmpty()[location]="F"
        elif self.getTileList()[location]=="X" and self.getTileListEmpty()[location]=="F":
            self.getTileListEmpty()[location]=" "
        elif str(self.getTileList()[location]).isnumeric()==True and self.getTileListEmpty()[location]=="F":
            self.getTileListEmpty()[location]=" "

    def selectTile(self, location): # return true if still good, return false if lost
        if self.getTileList()[location]=="X":
            return False
        elif self.getTileList()[location]!="X":
            if self.getTileList()[location]==0:
                self.getTileListEmpty()[location]="_"
                self.checkaround8(location)
            else:
                self.getTileListEmpty()[location] = self.getTileList()[location]
            return True
        
    def wincondition(self):
        winlist = []
        for i in range(len(self.getTileList())):
            if self.getTileListEmpty()[i] == "F" and self.getTileList()[i] == "X":
                winlist.append(i)
        #print("Flags placed:", len(winlist))
        if len(winlist)>= self.getAmountMines():
            return True
        else:
            return False
        
        

