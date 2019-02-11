j=0
f=0
n=0
x=0
ck=0
wk = 0
jk = 0
#These are different values for the various while statments in my game.
def complete(j): #This function makes sure that you can't play the same level twice.
    print("Congratulations You have Completed the Level!")
    nomore2.append(j)
    """I decided to make this a function because It I use this multiple time in my code and repeating would be annoying.
    Also It is a simple parameter function that makes my code look less cludered."""
def Ascii(o):
    print(" _       __               __   _____                      __ ")
    time.sleep(o)
    print("| |     / /___  _________/ /  / ___/___  ____ ___________/ /_")
    time.sleep(o)
    print("| | /| / / __ \/ ___/ __  /   \__ \/ _ \/ __ `/ ___/ ___/ __ |")
    time.sleep(o)
    print("| |/ |/ / /_/ / /  / /_/ /   ___/ /  __/ /_/ / /  / /__/ / / /")
    time.sleep(o)
    print("|__/|__/\____/_/   \__,_/   /____/\___/\__,_/_/   \___/_/ /_/ ")
    time.sleep(o)
"""This is the function for my Ascii art. I chose o as my parameter so I can change my time.sleep time by inputing it
in my parameter spot when calling the function."""

import time
#This is the import for time as I use the time.sleep() function multiple time to create a cool delay effect.
import random
#This is the import for random as I use the random.randint() function to randomize the order of my word search lines.
wordlisteasy = ["chris","fox","batman","git","game","rob"]
wordlistmed = ["fire","llik","math","gwood","boring","go","open","ten","word","myg","ekab"]
"""#This is used to check if the word variable are text file and in this list."""
wordlisthard = ["eikooc","nohtyp","buhtig","clock","canada","drib","swim","glass","brick","mrahcyp","retaw","think","screen","list","tes"]
"""These three lists are used to check if the word inputed are the same as in the text file."""
countereasy = []#Is used later to makes sure you can't repeat a word in the easy level
countermed = []#Is used later to make sure you can't repeat a word in the medium level.
counterhard = []#Is used later to make sure you can't repeat a word in the hard level.
"""These lists are used so you can't guess the same word twice.
Also it is used to see if you guessed all the word in the list. I did this so there is no way to cheat the game and you
can't get to the required len number to end the level without guessing all the word."""
counterhardr=[] #This has the same use as the counter lists above but for the reverse words.
randomprotect = []
randomprotect3 = []
randomprotect1 = []
"""The randomprotect lists are used so that the randomized lines don't repeat the same line over again."""
whilelist1 = []
whilelist2 =[]
whilelist3 = []
"""The whilelists are used so after all the lines are printed
the grid stops printing"""
countermedr = []#this is the counter for words being guessed twice but for the reverse words.
nomore2 = []#Is used so you can't play the same level twice.

Ascii(0.2)
"""Above is the function for the Ascii title. I used this because it is a cool way to open my word search game. 
I used time.sleep to create a cool loading effect. My function is used to allow me to use it later in my code without
 having to print it all out again."""
while f == 0:
    intro = input("What Level Do You Want to Play (1 = easy, 2 = medium, 3 = hard)")
    if intro == "1" and "1" not in nomore2:#The not in statment makes sure that if you have "1" in the list the if statement won't activate.
        file = open("easy.txt","r")
        liness1 = file.readlines()
        while ck == 0:
            randomthing1 = random.randint(0,6)
            if randomthing1 not in randomprotect1:#This makes sure that after all the lines are printed it won't keep going"
                print(liness1[randomthing1].replace(" ", "").replace("", " ").strip())#Makes even spacing between letters..
                randomprotect1.append(randomthing1)#ads the random randint into list so it can't get chosen again.
                whilelist1.append("hi")#adds a phrase to whilelist1 to be used in the next line.
                if len(whilelist1) == 7:#Makes sure if you have 7 "hi" phrases the while statment ends.
                    break
        """The while statement is ended so that when the grid is completely printed you will be able
                    to guess the worst in the list and actualy play the game."""
        print("welcome to the first level, There are 5 words")
        while j == 0:
            time.sleep(0.3)
            word = input("\nWhat Word Do you Wanna Guess ").lower()#makes sure your input is made lowercase for the variable.
            text_file1 = open("easy.txt","r") #reads the text file.
            lines1 = text_file1.readlines()#This reads the lines in text_file1 variable.
            for line1 in lines1:
                if word in line1 and word in wordlisteasy and word not in countereasy:#Checks if guessed word is in list. and not in countereasy list.
                    print("congratultions you have gotten a word.")
                    countereasy.append(word)#adds input to counter list so you can't guess again.
                    print(str(countereasy))#Shows the player what words they have guessed correctly.
            if len(countereasy) == 5:#makes sure once you guess all the words the level ends and are able to play new level.
                complete("1")#This activates the complete() function with the parameter j being "1"
                break


    elif intro == "2" and "2" not in nomore2:#Makes sure that you can't repeat level once you have beaten it.
        file2 = open("medium.txt","r")
        liness2 = file2.readlines()
        while wk == 0:
            randomthing = random.randint(0, 8)#Same code as before but for a different level and therefor more lines.
            if randomthing not in randomprotect:
                print(liness2[randomthing].replace(" ", "").replace("", " ").strip())#the.strip removes whitespace from the print statement
                randomprotect.append(randomthing)
                whilelist2.append("hi")
                if len(whilelist2) == 9:
                    break
            """This is repeated code from the first level but updated for the new perameters of the medium grid"""

        print("welcome to the second level, There are 10 words")
        while n == 0:
            time.sleep(0.3)
            word2 = input("\nWhat Word Do you Wanna Guess ").lower()#the /n creates a perfect space when being printed.
            #I did the /n for viewer appeal. The \n had nothing to do with efficiency.
            text_file2 = open("medium.txt", "r")
            lines2 = text_file2.readlines()#reads every line of the text file.
            for line2 in lines2:
                if word2 in line2 and word2 in wordlistmed and word2 not in countermed or word2[::-1] in wordlistmed and word2[::-1] not in countermedr:
                    print("congratultions you have gotten a word.")
                    countermed.append(word2)
                    countermedr.append(word2[::-1])# The ::-1 reverses the word inputed by user.
                    print(str(countermed))
            """The ::-1 is used in if statment so that the user can guess words that are reversed in the grid."""
            if len(countermed) == 10:#This line of code activates the if statement if their are ten words in the list.
                complete("2")#This activates the complete() function with the parameter j being "2"
                break#this breaks the while loop it is currently in. This basically brings you back to the menu.


    elif intro == "3" and "3" not in nomore2:
        file3 = open("hard.txt","r")# make reverse and verticle words
        liness3 = file3.readlines()
        while jk == 0:
            randomthing3 = random.randint(0,11)#repeated code but with diffent amount of random randints for the different amount of lines.
            if randomthing3 not in randomprotect3:
                print(liness3[randomthing3].replace(" ", "").replace("", " ").strip())
                randomprotect3.append(randomthing3)
                whilelist3.append("hi")
                if len(whilelist3) == 12:
                    break
        print("Welcome to the Third and Final Level, There are 15 words")
        while x == 0:
            time.sleep(0.3)
            word3 = input("\nWhat Word Do you Wanna Guess ").lower()#Space at end of dialouge make input more visualy appealing.
            text_file3 = open("hard.txt", "r")
            lines3 = text_file3.readlines()#reads the lines of the text file.
            for line3 in lines3:
                if word3 in line3 and word3 in wordlisthard and word3 not in counterhard or word3[::-1] in wordlisthard and word3 not in counterhard:
                    print("congratultions you have gotten a word.")
                    counterhard.append(word3)
                    counterhardr.append(word3[::-1])#the ::-1 reverses word3.
                    print(str(counterhard))
            if len(counterhard) == 15:#activates the if statements if there are 15 words in the counterhard list.
                complete("3")#This activates the complete() function with the parameter j being "3"
                break
    if len(nomore2) == 3:#activates the if statements if the nomore2 list has 3 words in it.
        time.sleep(0.5)
        exit("Congratulations You Having Finished All the Levels.")

        """This peice of code is activated once you have completed all the levels. The exit statment
        is here so once you are done you get a congratulations message and 
        then the game ends as they are no more levels."""