#import random
#from mine_sweeper_module import minesweeperboard

#class mineboard():
#    def __init__(self):
#        hi=0
    
#    def minelaying(self):
#        for i in range(0, minesweeperboard.getAmountMines()):
#            var = random.randint(0, minesweeperboard.getTotalTiles())
#            print(var)



 # # top left
        # if i-self.getSize()-1 >= 0:
        #     temp=i-self.getSize()-1
        #     if isinstance(self.tilelist[temp], int) and self.isLeft(i)==False:
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # top center
        # if i-self.getSize() >= 0:
        #     temp=i-self.getSize()
        #     if isinstance(self.tilelist[temp], int):
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # top right
        # if i-self.getSize()+1 >= 0:
        #     temp = i-self.getSize()+1
        #     if isinstance(self.tilelist[temp], int) and not self.isRight(i):
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # left
        # if i-1 > 0:
        #     temp = i-1
        #     if isinstance(self.tilelist[temp], int) and self.isLeft(i)==False:
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # right
        # if i+1 < self.totaltiles:
        #     temp = i+1
        #     if isinstance(self.tilelist[temp], int) and self.isRight(i)==False:
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # botom left
        # if i+self.getSize()-1 < self.totaltiles:
        #     temp = i+self.getSize()-1
        #     if isinstance(self.tilelist[temp], int) and self.isLeft(i)==False:
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # botom
        # if i+self.getSize() < self.totaltiles:
        #     temp = i+self.getSize()
        #     if isinstance(self.tilelist[temp], int):
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]
        # # bottom right
        # if i+self.getSize()+1 < self.totaltiles:
        #     temp=i+self.getSize()+1
        #     if isinstance(self.tilelist[temp], int) and self.isRight(i)==False:
        #         if self.tilelist[temp]==0:
        #             self.tilelistempty[temp]="_"
        #             self.tilelist[temp]="_"
        #             self.checkaround8(temp)
        #         else:
        #             self.tilelistempty[temp]=self.tilelist[temp]

  #    minecount = 0
            #    if i-self.getSize()-1 >= 0:
            ##        if self.tilelist[i-self.getSize()-1]=="X":
             #           minecount+= 1
             #   if i-self.getSize() >= 0:
             #       if self.tilelist[i-self.getSize()]=="X":
             #           minecount+= 1
             #   if i-self.getSize()+1 >= 0:
             #       if self.tilelist[i-self.getSize()+1]=="X":
             #           minecount+= 1
             #   if i-1 > 0:
             #       if self.tilelist[i-1]=="X":
             #           minecount+= 1
             #   if i+1 < self.totaltiles:
             #       if self.tilelist[i+1]=="X":
             ###           minecount+= 1
               # if i+self.getSize()-1 < self.totaltiles:
               #     if self.tilelist[i+self.getSize()-1]=="X":
               #         minecount+= 1
               ## if i+self.getSize() < self.totaltiles:
             #       if self.tilelist[i+self.getSize()]=="X":
             #           minecount+= 1
             #   if i+self.getSize()+1 < self.totaltiles:
             #       if self.tilelist[i+self.getSize()+1]=="X":
             #           minecount+= 1
             #   self.tilelist[i]+=minecount

#for i in range(0, self.boardsize):
            #if count < 10:
            #    print("",count, " ", end="")
            #elif count >= 10:
            #    print(count, " ", end="")
            #for i2 in range(0, self.boardsize):
            #    print("[ ]", end="")
            #if i2 >= boardsize-1:
            #print("")
            #count += 1
       # print(minelist)

 #  print(tilelist)
      #  print(len(tilelist))

        #def board(self):
    #    count = 1
    #    if self.boardsize == 8:
    #        print("     A  B  C  D  E  F  G  H")
    #    elif self.boardsize == 12:
    #        print("     A  B  C  D  E  F  G  H  I  J  K  L")
    #    elif self.boardsize == 16:
    #        print("     A  B  C  D  E  F  G  H  I
    #   J  K  L  M  N  O  P")
        #for i in range(0, self.boardsize):
            #if count < 10:
            #    print("",count, " ", end="")
            #elif count >= 10:
            #    print(count, " ", end="")
            #for i2 in range(0, self.boardsize):
            #    print("[ ]", end="")
            #if i2 >= boardsize-1:
            #print("")
            #count += 1

    #    for i in range(self.totaltiles+1):
    #        if count < 10:
    #            print("",count, " ", end="")
    #        elif count >= 10:
    #            print(count, " ", end="")
    #        if(i % self.boardsize) == 0:
    #            print("")
    #            count+= 1
    #        print("[",self.minelaying[i],"]", end="")

 #minecount = 0
                #if self.tilelist[location-self.getSize()-1]=="X":
                #    if location-self.getSize()-1 >= 0:
                #        minecount+= 1
                #if self.tilelist[location-self.getSize()]=="X":
                #    if location-self.getSize() >= 0:
                #        minecount+= 1
                #if self.tilelist[location-self.getSize()+1]=="X":
                #    if location-self.getSize()+1 >= 0:
                #        minecount+= 1
                #if self.tilelist[location-1]=="X":
                #    if location-1 >= 0:
                #        minecount+= 1
                #if location+1 < self.totaltiles:
                #    if self.tilelist[location+1]=="X":
                #        minecount+= 1
                #if location+self.getSize()-1 < self.totaltiles:
                #    if self.tilelist[location+self.getSize()-1]=="X":
                #        minecount+= 1
                #if location+self.getSize() < self.totaltiles:
                #    if self.tilelist[location+self.getSize()]=="X":
                #        minecount+= 1
                #if location+self.getSize()+1 < self.totaltiles:
                #    if self.tilelist[location+self.getSize()+1]=="X":
                #        minecount+= 1
                #if minecount == 0:
                #    self.tilelistempty[location]="_"
                #else:
                #    self.tilelistempty[location]=str(minecount)

#if self.boardsize == 8:
            # if answer1 == "1":
            #     answer1 = 0
            #     answer1answer = True
            # elif answer1 == "2":
            #     answer1 = self.getSize()
            #     answer1answer = True
            # elif answer1 == "3":
            #     answer1 = self.getSize()*2
            #     answer1answer = True
            # elif answer1 == "4":
            #     answer1 = self.getSize()*3
            #     answer1answer = True
            # elif answer1 == "5":
            #     answer1 = self.getSize()*4
            #     answer1answer = True
            # elif answer1 == "6":
            #     answer1 = self.getSize()*5
            #     answer1answer = True
            # elif answer1 == "7":
            #     answer1 = self.getSize()*6
            #     answer1answer = True
            # elif answer1 == "8":
            #     answer1 = self.getSize()*7
            #     answer1answer = True
            # elif answer1 == "9":
            #     answer1 = self.getSize()*8
            #     answer1answer = True
            # elif answer1 == "10":
            #     answer1 = self.getSize()*9
            #     answer1answer = True
            # elif answer1 == "11":
            #     answer1 = self.getSize()*10
            #     answer1answer = True
            # elif answer1 == "12":
            #     answer1 = self.getSize()*11
            #     answer1answer = True
            # elif answer1 == "13":
            #     answer1 = self.getSize()*12
            #     answer1answer = True
            # elif answer1 == "14":
            #     answer1 = self.getSize()*13
            #     answer1answer = True
            # elif answer1 == "15":
            #     answer1 = self.getSize()*14
            #     answer1answer = True
            # elif answer1 == "16":
            #     answer1 = self.getSize()*15
            #     answer1answer = True
            # else:
            #     print("invalid Y value")