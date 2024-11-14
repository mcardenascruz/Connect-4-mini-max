from Classes import *

win = pygame.display.set_mode((1200, 600))


# colors
white = 255,255,255
Player_Color = 227, 6, 2
bg = 43, 43, 43
orange= 252, 177, 3
blue = 103, 178, 207
pink = 252, 13, 212
lightgreen = 0, 250, 112
light_red = 255, 156, 156
gold = 255, 234, 0
gery = 163, 163, 163
light_blue = 67, 216, 230



# pygame baisc set up
pygame.init()
width, height = 1000, 700
win = pygame.display.set_mode((1000, 700))
background = pygame.image.load("Images/Backgorund.jpg")
font = pygame.font.SysFont("comicsans", 20, bold=True)

# class set up
Jokes = FunnyJokes()
label = font.render(Jokes.joke, 1, (231 , 218 , 70))


# Games
def main_slide():
    game = SlideGrid(3)
    display = Graphics(game)
    player = Blank(game)
    ref = Rules(game)
    run = True
    count = 0

    while run:

        win.fill(bg)

        display.PyDrawPuzzle()
        display.write(15, 0, 30, "Possible images:", light_blue)
        display.write(830, 0, 30, "Moves:" + str(count), light_red)
        display.draw_otherpics()
        pygame.display.update()
        y, x = player.get_pos(display.gird)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.move(y, x, 0, -1, display.gird)
                    count += 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.move(y, x, 0, 1, display.gird)
                    count += 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move(y, x, 1, 0, display.gird)
                    count += 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move(y, x, -1, 0, display.gird)
                    count += 1
                elif event.key == pygame.K_RETURN:
                    display.gird = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
                    count = 0
                elif event.key == pygame.K_SPACE:
                    player.start(display.gird)
            if event.type == pygame.QUIT:
                run = False

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

def Maze_Game():
    #pygameCap
    pygame.display.set_caption("Maze")

    #class variables
    player = PlayerAndSetup()
    player.start()
    maze = player.maze
    player.setStart()
    player.get_score()
    slover = A_star()
    slover.start(maze)
    FPS = 10
    fpsClock = pygame.time.Clock()
    run = True


    timer = 0
    Show_bestMove = False

    while run:
        timer = (timer +1)
        timerx = int(timer/10)
        pygame.display.update()
        win.fill(bg)
        player.pyDrawMaze()
        player.Score(timerx)
        if Show_bestMove == True:
            player.Best_Moves()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.pymoveL()
            player.checkwin(timerx)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.pymoveR()
            player.checkwin(timerx)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.pymoveD()
            player.checkwin(timerx)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.pymoveU()
            player.checkwin(timerx)
        if keys[pygame.K_RETURN]:
            slover.A_star(maze)
            Show_bestMove = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        fpsClock.tick(FPS)

run = True
while run:
    pygame.display.update()

    win.blit(background, (0,0))
    win.blit(label,(17,620))
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()


        if mx > 50 and mx < 400 and my >425 and my < 550:
            background = pygame.image.load("Images/Maze_Game_puzzle.png")
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_slide()
        elif mx > 50 and mx < 400 and my >150 and my < 250:
            background = pygame.image.load("Images/Maze_game_menu.png")
            if event.type == pygame.MOUSEBUTTONDOWN:
                Maze_Game()
        elif mx > 50 and mx < 400 and my >300 and my < 375:
            background = pygame.image.load("Images/Maze_Game_Menu_connect4.png")
            if event.type == pygame.MOUSEBUTTONDOWN:
                Connect4_Game()
        else:
            background = pygame.image.load("Images/Backgorund.jpg")
        if event.type == pygame.QUIT:
            run = False