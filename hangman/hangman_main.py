import random as r

mode_mesg = ("Please choose category for the game\n1. Countries\n2. School")
file_list = ["countries.txt", "education.txt"]
global curr_word_list

# class player
class Player:
    def __init__(self, score, life):
        self.score = score
        self.life = life

    def setScore(self, x):
        self.score = x
    
    def setLife(self, x):
        self.life = x
    
    def getScore(self):
        return self.score
    
    def getLife(self):
        return self.life

# class word list
class Word:
    def __init__(self, word, hint, point):
        self.word = word
        self.hint = hint
        self.point = point

    def setWord(self, x):
        self.word = x

    def setHint(self, x):
        self.hint = x

    def getWord(self):
        return self.word

    def getHint(self):
        return self.hint

class Word_list:
    def __init__(self):
        self.word_list=[]

    def add(self,word):
        self.word_list.append(word)

    def seeWordlist(self):
        return self.word_list

def random():
    random_num = r.randint(0,9)
    return random_num

def game(curr_word_list, player1):
    random_num_list = []
    temp_word = []
    wrong_guess = ""
    previous_word = ""
    attempt = 8
    
    temp = ""
    check = 0
    bonus = 0
    game_over = 0

    ##1 round = 5 questions
    for question_num in range (5):
        if (game_over == 1):
            print("game_over == 1")
            break
        
        num = random()
        while (1):
            if (num not in random_num_list):
                random_num_list.append(num)
                break
            else:
                num = random()
        
        curr_word = curr_word_list[random_num_list[question_num]].getWord()
        curr_hint = curr_word_list[random_num_list[question_num]].getHint()
        
        for i in curr_word:
            if (i == " "):
                temp_word += " "
            else:
                temp_word += "_"
        
        print("\nQuestion" + str(question_num+1) + "\nHint: " + curr_hint + ", Live: " + str(player1.getLife()) + "\n")
        
        while(1):
            ##print word out in "_ _ _" format
            for i in temp_word:
                print(i, end=" ")
                
            print("\tScore " + str(player1.getScore()) + ", Attempt left " +str(attempt) + ", wrong guessed: " + wrong_guess)
            wrong_guess = ""
            
            ##accept answer input
            choice = input(">>> ")
            while(1):
                ##bonus
                if (choice.isalpha() and choice.lower() == curr_word.lower() and len(choice)!=1):
                    bonus = 1
                    break
                ##single character
                elif (choice.isalpha() and len(choice)==1 and previous_word != choice):
                    previous_word = choice
                    break
                ##wrong input
                else:
                    print("Enter non-repeat single character")
                    choice = input(">>> ")
                    
            if (bonus == 1):
                ##guess whole word correct
                player1.setScore(player1.getScore()+200)
                print()
                for i in curr_word:
                    print(i, end=" ")
                print("\tScore: " + str(player1.getScore()) + ", Attempt left: ", str(attempt))
                attempt = 8
                temp_word.clear()
                bonus = 0
                previous_word = ""
                break
            else:
                ##didn't guess the whole word correct
                for i in range (len(curr_word)):
                    if (curr_word[i].lower() == choice.lower()):
                        check = 1
                        if (curr_word[i].islower()):
                            ##non-capital character
                            temp_word[i] = curr_word[i]
                        else:
                            ##capital character
                            temp_word[i] = curr_word[i]
                
                if (check == 0):
                    wrong_guess = choice
                    attempt -= 1
                else:
                    player1.setScore(player1.getScore()+10)
                check = 0

                ##no more attemp, lose one life
                if (attempt == 0):
                    attempt = 8
                    temp_word.clear()
                    player1.setLife(player1.getLife()-1)
                    wrong_guess = ""
                    break

                if (player1.getLife()<1):
                    game_over = 1
                    break
                    
                ##check whether the word is complete?
                for i in temp_word:
                    temp += i

                if (temp == curr_word):
                    print("Well done!!!")
                    attempt = 8
                    temp_word.clear()
                    player1.setScore(player1.getScore()+20)
                    wrong_guess = ""
                    break
                else:
                    temp = ""
                    
def openfile(file_order):
    infile = open(file_list[file_order],"r")
    words = infile.readlines()
    infile.close()

    return words

def main():
    print("Welcome to Hangman!!!")
    print(mode_mesg)

    choice = str(input(">>> "))
    while(1):
        if (choice.isdigit() == 1 and (choice == "1" or choice == "2")):
            choice = int(choice)
            break
        else:
            print("Enter only number (between 1 - 2)")
            choice = str(input(">>> "))

    choice -= 1
    
    # open file, get the words and put it into program
    words = openfile(choice)

    print("before", words)
    # add word into class
    new_word_list = Word_list()
    for i in range(len(words)):
        word, hint =  words[i].split(",")
        hint = hint.replace("\n", "")
        new_word_list.add(Word(word, hint, 100))

    print("after", words)

    curr_word_list = new_word_list.seeWordlist()

    player1 = Player(0, 3)
    
    ##start the game
    game(curr_word_list, player1)

    ##show result
    print("Total score:",player1.getScore(),"\tLife:",player1.getLife())

main()
