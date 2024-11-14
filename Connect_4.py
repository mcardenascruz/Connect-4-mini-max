import random
import copy
import pygame
import math
import time

#pygame
pygame.init()

#colors
white = 255,255,255
red = 255,0,0
bg = 43, 43, 43
orange= 252, 177, 3
pink = 252, 13, 212
lightgreen = 0, 250, 112
blue = 2, 20, 186
yellow = 255, 255, 0
lightBlue= 0, 225, 255




#window setup
width, height = 1000, 700
win = pygame.display.set_mode((width, height))
win.fill(bg)




class Connect4:
    def __init__(self, player1,player2):
        self.player1  = player1
        self.player2 = player2
        self.scores=[]
        self.board_W =7
        self.board_H = 6
        self.gird =  [[(0)for x in range(self.board_W)]for y in range(self.board_H)]
        self.PLAYER_PIECE = 1
        self.AI_PIECE = 2

    #Checking postions AND wins

    #check if valid postion
    def ValidPos(self,gird,pos):
        if gird[0][pos] == 0:
            return True

    #checking differnt types of winning moves
    def checkvertical(self, gird, playerTurn):
        for col in range(self.board_W ):
            for row in range(self.board_H-3):
                if gird[row][col] == playerTurn and gird[row+1][col] == playerTurn and gird[row+2][col] == playerTurn and gird[row+3][col] == playerTurn:
                    return True

    def checkHorintal(self, gird,playerTurn):
        for c in range(self.board_W-3):
            for r in range(self.board_H):
                if gird[r][c] == playerTurn and gird[r][c+1] == playerTurn and gird[r][c+2] == playerTurn and gird[r][c+3] == playerTurn:
                    return True


    def checkDiagonal(self, gird,playerTurn):
        for c in range(self.board_W-3):
            for r in range(self.board_H-3):
                if gird[r][c] == playerTurn and gird[r+1][c+1] == playerTurn and gird[r+2][c+2] == playerTurn and gird[r+3][c+3] == playerTurn:
                    return True




    def checkDiagonal2(self, gird,playerTurn):
        # Check negatively sloped diaganols
        for c in range(self.board_W-3):
            for r in range(3, self.board_H):
                if gird[r][c] == playerTurn and gird[r-1][c+1] == playerTurn and gird[r-2][c+2] == playerTurn and gird[r-3][c+3] == playerTurn:
                    return True

    #checks if someone won
    def checkwin(self,gird,playerTurn):
        if self.checkvertical(gird,playerTurn) or self.checkHorintal(gird,playerTurn) or self.checkDiagonal(gird,playerTurn)  or self.checkDiagonal2(gird,playerTurn) == True:
            return True

    #under CONstrtuion
    #def DROP_animation(self,player, x):
    #    y = 50
    #    if player == 1:
    #        while y < 600:
    #            pygame.draw.circle(win,(yellow),(x,y),40)
    #            y = y +10
    #            time.sleep(.01)
    #            pygame.display.update()
    #
    #    else:
    #        pygame.draw.circle(win,(red),(x,50),40)
    #places a piece

    def Place_peice(self,gird,pos, playerTurn):
        if self.ValidPos(gird,pos):
            for row in range(6):
                if gird[row][pos] == 0:
                    firstopen = row
            gird[firstopen][pos] = playerTurn


        else:
            return False


    #draws the person who places next
    def drawnext_move(self,playerTurn):
        if playerTurn == 1:
            colour = red
        else:
            colour = yellow
        pygame.draw.rect(win,(colour), [855,545,110,110])
        pygame.draw.rect(win,(0, 0, 0), [860,550,100,100])
        pygame.draw.circle(win,(colour),(910,600),40)


    #draws texts
    def draw_text_nextPlayer(self):
        font = pygame.font.SysFont("comicsans", 30, bold=True)
        label = font.render("Next Turn!", 1, lightBlue)
        win.blit(label,(830,490))

    def Draw_winner(self,playerturn):
        font = pygame.font.SysFont("comicsans", 100, bold=True)
        label = font.render("Player"+str(playerturn)+"wins", 1, (0,0,0))
        win.blit(label,(200,300))

    #Get the infromation from set Username
    def GetPLayerINfo(self,player):
        with open("Data_Bases/Connect_4_count.txt", "r") as f:
            lines = f.readlines()


        NewPlayer = True
        for line in lines:
            if player in line:
                NewPlayer = False
        if NewPlayer == False:
            for line in lines:
                if player in line:
                    for count, letter in enumerate(line):
                        if letter==",":
                            player = (line[:count])
                            count = (line[count+1:])
                            self.scores.append(int(count))
                            print("wellcomeback! {} you have a total of {} wins".format(player,count))
                            stop = True
        else:
            with open("Data_Bases/Connect_4_count.txt", "a") as f:
                f.write("\n{},0".format(player))
                print("A new player finaly")
                self.scores.append(0)
    def draw(self):
        pygame.draw.rect(win,(blue), [180,100,640,550])
        for county, col in enumerate(self.gird):
            for countx, value in enumerate(col):
                if value == 0:
                    pygame.draw.circle(win,(white),(227+countx*91,153+county*91),40)
                if value == 1:
                    pygame.draw.circle(win,(yellow),(227+countx*91,153+county*91),40)
                if value == 2:
                    pygame.draw.circle(win,(red),(227+countx*91,153+county*91),40)

    #update the user score
    def update_score(self,player,score):
        with open("Data_Bases/Connect_4_count.txt", "r") as f:
            lines = f.readlines()
        for count1, line in enumerate(lines):
            if player in line:
                for count, letter in enumerate(line):
                    if letter==",":
                        lines[count1] = player+","+str(score)+"\n"
                        flie = open("Data_Bases/Connect_4_count.txt", "w")
                        flie.writelines(lines)
                        flie.close()

    #manages what happens after a win
    def winner(self,playerTurn,player):
        global pt1,pt2
        if playerTurn == 1:
            self.scores[0] += 1
            self.update_score(player,self.scores[0])
        else:
            self.scores[1] += 1
            self.update_score(player,self.scores[1])
        global board
        self.Draw_winner(playerTurn)
        pygame.display.update()
        time.sleep(5)

    #draws the scores
    def get_count(self):
        global pt1,pt2
        with open("Data_Bases/Connect_4_count.txt", "r") as f:
            lines = f.readlines()
            pt1 = self.scores[0]
            pt2 = self.scores[1]
            font = pygame.font.SysFont("comicsans", 25, bold=True)
            label = font.render(self.player1+" wins: "+str(pt1), 1, (yellow))
            label2 = font.render(self.player2+ " wins: " +str(pt2), 1, (red))
            win.blit(label2,(800,20))
            win.blit(label,(10,20))

    def Draw_Cricle(self,x,player):
        if player == 1:
            pygame.draw.circle(win,(red),(x,50),40)
        else:
            pygame.draw.circle(win,(yellow),(x,50),40)
        pygame.display.update()
    def vaild_locations(self,gird):
        vaild_locations = []
        for col in range(self.board_W):
            if self.ValidPos(gird,col):
                vaild_locations.append(col)
        return vaild_locations






class AiConnect4(Connect4):


    def point_system(self,window, playerTurn):

        score = 0
        opp_piece = self.PLAYER_PIECE
        if playerTurn == self.PLAYER_PIECE:
            opp_piece = self.AI_PIECE

        if window.count(playerTurn) == 3 and window.count(0) == 1:
            score += 10000
        elif window.count(playerTurn) == 2 and window.count(0) == 2:
            score += 100
        elif window.count(playerTurn) == 1 and window.count(0) == 3:
            score += 10


        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score += -100000

        elif window.count(opp_piece) == 2 and window.count(0) == 2:
            score += -1000
        elif window.count(opp_piece) == 1 and window.count(0) == 3:
            score += -10

        return score





    def easy(self,pos, playerTurn):
        self.Place_peice(self.gird,pos,playerTurn)


    def score_position(self,gird, playerTurn):
        score=0

        #score center collum
        #center_array = []
        #for i in range(self.board_H):
        #    center_array.append(gird[i][3])
        #center_count = center_array.count(playerTurn)
        #score += center_count*3


        #checks how many peice are in the window of 4
        for row in range(self.board_H):
            row_array = gird[row]
            for col in range(self.board_W-3):
                window = row_array[col:col+4]
                score += AiConnect4.point_system(self,window,playerTurn)

        #score vertical
        for col in range(self.board_W):

            #makes list in the vertical
            col_array = []
            for row in range(self.board_H):
                col_array.append(gird[row][col])

            for row in range(self.board_H-3):
                window = col_array[row:row+4]

                score += AiConnect4.point_system(self,window,playerTurn)


        #check +dia
        for row in range(self.board_H-3):
            for col in range(self.board_W-3):

                window= [gird[row+i][col+i]for i in range(4)]

                score += AiConnect4.point_system(self,window,playerTurn)
        #check -dia
        for row in range(self.board_H-3):
            for col in range(self.board_W-3):
                window= [gird[row+3-i][col+i]for i in range(4)]
                score += AiConnect4.point_system(self,window,playerTurn)
        return score

    def is_terminal_node(self,gird):
        return self.checkwin(gird,self.AI_PIECE) or self.checkwin(gird,self.PLAYER_PIECE) or len(self.vaild_locations(gird))==0

    def minimax(self,gird,depth, alpha, beta, maximixingPlayer):

        Valid_locations = self.vaild_locations(gird)
        is_terminal = AiConnect4.is_terminal_node(self,gird)
        if depth ==0 or is_terminal:
            if is_terminal:
                if self.checkwin(gird,self.AI_PIECE):

                    return (None, 10000000)#

                elif self.checkwin(gird,self.PLAYER_PIECE):
                    return (None, -10000000)#sing worng

                else: # game is over
                    return (None,0)
            else:
                return (None,(AiConnect4.score_position(self,gird, self.AI_PIECE)))
        if maximixingPlayer:
            value = -float('inf')
            column = random.choice(Valid_locations)
            for col in Valid_locations:
                temp_board = copy.deepcopy(gird)
                self.Place_peice(temp_board,col, self.AI_PIECE)
                new_score = AiConnect4.minimax(self,temp_board,depth-1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                #alpha = max(alpha, value)
                #if alpha >= beta:
                #    break
            return column, value

        else:
            column = random.choice(Valid_locations)
            value = float('inf')
            for col in Valid_locations:
                temp_board = copy.deepcopy(gird)
                self.Place_peice(temp_board,col, self.PLAYER_PIECE)
                new_score = AiConnect4.minimax(self,temp_board,depth-1,alpha, beta, True)[1]
                if new_score < value:
                    value = new_score
                    column = col
                #beta = min(beta, value)
                #if alpha >= beta:
                #    break
            return column, value



def Connect4_Game():
    player2 = input("enter your username!: ")
    player1  = input("enter your username!: ")

    Connect = Connect4(player1,player2)
    #RANDOM VARIABLES
    board_H = 6
    board_W = 7
    run=True
    playerTurn = 2



    mx = 0
    FPS = 144
    fpsClock = pygame.time.Clock()


    def refresh():
        win.fill(bg)
        Connect.draw()
        Connect.drawnext_move(playerTurn)
        Connect.draw_text_nextPlayer()
        Connect.get_count()
        Connect.Draw_Cricle(mx,playerTurn)
        pygame.display.update()





    Connect.GetPLayerINfo(Connect.player1)
    Connect.GetPLayerINfo(Connect.player2)


    while run:

        #drawing pygame
        Connect.drawnext_move(playerTurn)
        refresh()



        for event in pygame.event.get():
            #gets mouse cords
            mx , my = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:

                #converts mouse cords to gird value
                x = math.floor(mx/91)-2

                #checks if postions is vaild
                if x >-1 and x < 7 and Connect.ValidPos(Connect.gird,x) == True:

                    #changes player turn (ai=1 player  = 2)
                    playerTurn = playerTurn%2 +1

                    #checks if ai is in play
                    if Connect.player1 == "AI easy" and playerTurn==1:

                        Best_move,minimax_score = (AiConnect4.minimax(Connect,Connect.gird,3,-float("inf"), float("inf"),True))
                        AiConnect4.easy(Connect,Best_move,playerTurn)


                    #else human
                    else:
                        Connect.Place_peice(Connect.gird,x, playerTurn)

                    #checks if win
                    if Connect.checkwin(Connect.gird,playerTurn) == True:
                        Connect.draw()
                        if playerTurn == 1: # player

                            Connect.winner(playerTurn,Connect.player1)
                        else:
                            Connect.winner(playerTurn,Connect.player2)
                        Connect.gird = [[(0)for x in range(board_W)]for y in range(board_H)]


            if event.type == pygame.QUIT:
                run = False
        fpsClock.tick(FPS)

Connect4_Game()