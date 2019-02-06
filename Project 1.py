j=0
f=0
n=0
x=0
wordlisteasy = ["chris","fox","batman","git","game"]
wordlistmed = ["fire","kill","math","gwood","boring","go","open","ten","word","gym","bake"]
wordlisthard = ["eikooc","nohtyp","buhtig","clock","canada","drib","swim","glass","brick","mrahcyp","retaw","think","screen","list","tes"]
countereasy = []
countermed = []
counterhard = []
counterhardr=[]
while f == 0:
    intro = input("What Level Do You Want to Play (1 = easy, 2 = medium, 3 = hard)")
    if intro == "1":
        file = open("easy.txt","r")
        for x in range(1,7):
            print(file.readline().replace(" ", "").replace("", " ").strip())
        print("welcome to the first level, There are 5 words")
        while j == 0:
            word = input("What Word Do you Wanna Guess").lower()
            text_file1 = open("easy.txt","r")
            lines1 = text_file1.readlines()
            for line1 in lines1:
                if word in line1 and word in wordlisteasy and word not in countereasy:
                    print("congratultions you have gotten a word.")
                    countereasy.append(word)
                    print(str(countereasy))
            if len(countereasy) == 5:
                print("You have completed this level Congrats!!")
                break


    elif intro == "2":
        file2 = open("medium.txt","r")
        for b in range(1,9):
            print(file2.readline().replace(" ", "").replace("", " ").strip())
        print("welcome to the second level, There are 10 words")
        while n == 0:
            word2 = input("What Word Do you Wanna Guess").lower()
            text_file2 = open("medium.txt", "r")
            lines2 = text_file2.readlines()
            for line2 in lines2:
                if word2 in line2 and word2 in wordlistmed and word2 not in countermed:
                    print("congratultions you have gotten a word.")
                    countermed.append(word2)
                    print(str(countermed))
            if len(countereasy) == 10:
                print("You have completed this level Congrats!!")
                break
    elif intro == "3":
        file3 = open("hard.txt","r")# make reverse and verticle words
        for s in range(1, 12):
            print(file3.readline().replace(" ", "").replace("", " ").strip())
        print("Welcome to the Third and Final Level, There are 15 words")
        while x == 0:
            word3 = input("What Word Do you Wanna Guess").lower()
            text_file3 = open("hard.txt", "r")
            lines3 = text_file3.readlines()
            for line3 in lines3:
                if word3 in line3 and word3 in wordlisthard or word3[::-1] in wordlisthard and word3 not in counterhard:
                    print("congratultions you have gotten a word.")
                    counterhard.append(word3)
                    counterhardr.append(word3[::-1])
                    print(str(counterhard))
            if len(counterhard) == 15:
                print("You have completed this level Congrats!!")
                break
