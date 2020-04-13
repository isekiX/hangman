

#http://tinyurl.com/jhrvs94

def hangman(word):
    wrong = 0
    stages = ["",
              "_______          ",
              "|                ",
              "|       |        ",
              "|       O        ",
              "|      /|\       ",
              "|      / \       ",
              "|                "
              ]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong < len(stages)-1:
        print("\n")
        msg="Imagine a character please.: "
        char=input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong +=1
        print(" ".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))

        if "__" not in board:
            print("You won")
            print(" ".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lost, The answer is {}.".format(word))

hangman("cat")


