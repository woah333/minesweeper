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
        elif string == "medium":
            self.boardsize = 12
            self.amountmines = 20
            self.totaltiles = 144
            self.tilelistempty = [" "]* 144
        elif string == "hard": 
            self.boardsize = 16
            self.amountmines = 40
            self.totaltiles = 256
            self.tilelistempty = [" "]* 256
        else:
            print("Invalid difficulty option")
    
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
        # count = 1
        # if self.boardsize == 8:
        #     print("     A  B  C  D  E  F  G  H")
        # elif self.boardsize == 12:
        #     print("     A  B  C  D  E  F  G  H  I  J  K  L")
        # elif self.boardsize == 16:
        #     print("     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
        # for i in range(self.totaltiles):
        #     p = i+1
        #     if(p % self.boardsize) == 1:
        #         if count < 10:
        #             print("",count, " ", end="")
        #         elif count >= 10:
        #             print(count, " ", end="")
         
        #     print("[" + str(self.tilelist[i]) + "]", end="")
        #     if(p % self.boardsize) == 0:
        #         print("")
        #         count+= 1


    def isRight(self, i):
        return i % self.boardsize == self.boardsize-1
    
    def isLeft(self, i):
        return i % self.boardsize == 0
        
            
    def emptyboardfunc(self, tilelisttempty):
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
         
            print("["+ str(self.getTileListEmpty()[i]) +"]", end="")
            if(p % self.boardsize) == 0:
                print("")
                count+= 1

    
    def startfunc(self):
        question_difficulty_boolean = False
        while question_difficulty_boolean == False:
            question_difficulty = input("What difficulty would you like?(easy, medium, hard)\n")
            if question_difficulty == "easy" or question_difficulty == "medium" or question_difficulty == "hard":
                question_difficulty_boolean = True
            else:
                print("Invalid difficulty")
        return question_difficulty
    
    def questionfunc(self):

        self.emptyboardfunc(self.getTileListEmpty())
        answer1answer = False
        answer2answer = False
        answer3answer = False

        while answer2answer == False:
            answer2 = input("What X value (letters lowercase)") 
            if self.getSize() == 8:
                answer2list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
            elif self.getSize() == 12:
                answer2list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k' :11, 'l': 12,}
            elif self.getSize() == 16:
                answer2list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k' :11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16}
            if answer2 in answer2list:
                answerof2 = answer2list[answer2]
                answer2answer = True
            else:
                print("Invalid Y value")

        while answer1answer == False:
            answer1 = input("What Y value (numbers)")
            if answer1.isnumeric()==True:
                answer1 = int(answer1)-1
                if answer1 < self.getSize():
                    answer1 = answer1 * self.getSize()
                    answer1answer = True
                else:
                    print("Invalid Y value")
            else:
                print("Invalid Y Value")

        while answer3answer == False:
            answer3 = input("Flag or no flag (f/n)")
            if answer3 == "f" or answer3 == "n":
                answer3answer = True
            else:
                print("invalid choice")
        locate = answer1 + answerof2 - 1
        self.changingtheboard(locate, answer3)


    def changingtheboard(self, location, answerthree): 
        if self.hasmines == False:
            self.minelaying(location)
            self.hasmines = True
        if answerthree == "f":
            if self.tilelist[location]=="X" and self.tilelistempty[location]==" ":
                self.tilelistempty[location]="F"
            elif self.tilelist[location]=="O" and self.tilelistempty[location]==" ":
                self.tilelistempty[location]="F"
            elif self.tilelist[location]=="X" and self.tilelistempty[location]=="F":
                self.tilelistempty[location]=" "
            elif self.tilelist[location]=="O" and self.tilelistempty[location]=="F":
                self.tilelistempty[location]=" "
        elif answerthree == "n":
            if self.tilelist[location]=="X":
                self.tilelistempty[location]="X"
                print("you lose")
                quit()
            elif self.tilelist[location]!="X":
                if self.tilelist[location]==0:
                    self.tilelistempty[location]="_"
                    self.checkaround8(location)
                else:
                    self.tilelistempty[location] = self.tilelist[location]
        else:
            print("invalid option")
        #count +=1
        winlist = []
        for i in range(len(self.tilelist)):
            if self.tilelistempty[i] == "F" and self.tilelist[i] == "X":
                winlist.append(i)
        print("Flags placed:", len(winlist))
        if len(winlist)>= self.amountmines:
            print("You win congrats")
            quit()
        self.questionfunc()
       


