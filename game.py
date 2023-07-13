from mine_sweeper_module import minesweeperboard

class game():
    def __init__(self):
        self.board = minesweeperboard()


    def startfunc(self):
        question_difficulty_boolean = False
        while question_difficulty_boolean == False:
            question_difficulty = input("What difficulty would you like?(easy, medium, hard)\n")
            if question_difficulty == "easy" or question_difficulty == "medium" or question_difficulty == "hard":
                question_difficulty_boolean = True
            else:
                print("Invalid difficulty")
        result = self.board.setStuff(question_difficulty)
        if(result==False):
            print("Invalid difficulty option")
        self.questionfunc()
        return question_difficulty
       

    def emptyboardfunc(self, tilelisttempty):
        count = 1
        if self.board.getSize() == 8:
            print("     A  B  C  D  E  F  G  H")
        elif self.board.getSize() == 12:
            print("     A  B  C  D  E  F  G  H  I  J  K  L")
        elif self.board.getSize() == 16:
            print("     A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P")
        for i in range(self.board.getTotalTiles()):
            p = i+1
            if(p % self.board.boardsize) == 1:
                if count < 10:
                    print("",count, " ", end="")
                elif count >= 10:
                    print(count, " ", end="")
         
            print("["+ str(self.board.getTileListEmpty()[i]) +"]", end="")
            if(p % self.board.getSize()) == 0:
                print("")
                count+= 1

    def questionfunc(self):

        self.emptyboardfunc(self.board.getTileListEmpty())
        answer1answer = False
        answer2answer = False
        answer3answer = False

        while answer2answer == False:
            answer2 = input("What X value (letters lowercase)") 
            if self.board.getSize() == 8:
                answer2list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
            elif self.board.getSize() == 12:
                answer2list = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k' :11, 'l': 12,}
            elif self.board.getSize() == 16:
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
                if answer1 < self.board.getSize():
                    answer1 = answer1 * self.board.getSize()
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
        if self.board.getHasMines() == False:
            self.board.minelaying(location)
            self.board.setHasMines(True)
        if answerthree == "f":
           self.board.setFlag(location)

        elif answerthree == "n":
            result = self.board.selectTile(location)
            if(result == False):
                print("you lose")
                quit()
        else:
            print("invalid option")
        self.board.wincondition()
        #count +=1
        winn = self.board.wincondition()
        if winn == True:
            print("You win congrats")
            quit()

        self.questionfunc()
