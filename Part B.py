import random
word = ""
letter = ""
updatedspaces = []
def intialize ():
    wordBank = ['keyboard', 'computer', 'mouse', 'application']
    word = random.choice(wordBank)
    updatedspaces = []
    spaces = "___"
    print(spaces), len(word)
    
def getLetter():
    letter = raw_input('Guess a letter ')
    global letter
    letterList = []
    global letterList  
    letterList.append(letter)
    

def checkifWon ():
    if len(letterList) == len(word): 
        print('Good job, you won!')
        
    else:
        getLetter()
            

def main ():
    intialize()
    getLetter()
    checkifWon()

main()


def checkLetter():
    global updatedSpaces
    if letter in word:
        checkifWon()
        updatedSpaces = updatedSpaces -1
        
    else:
        lives = lives -1
        getLetter()
        
        #Suraj
        
