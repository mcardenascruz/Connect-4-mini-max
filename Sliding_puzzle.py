import random
import pygame
import time

pygame.init()
win = pygame.display.set_mode((1000, 600))

# colors
white = 255, 255, 255
Player_Color = 227, 6, 2
bg = 43, 43, 43
orange = 252, 177, 3
blue = 103, 178, 207
pink = 252, 13, 212
lightgreen = 0, 250, 112
light_red = 255, 156, 156
gold = 255, 234, 0
gery = 163, 163, 163
light_blue = 67, 216, 230


class SlideGrid:
    def __init__(self, size):
        self.size = size

        gird = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.gird = gird
        self.font = pygame.font.SysFont("comicsans", 40, bold=True)
        ninjapig28 = pygame.image.load("Images/Ninjapig.jpg")
        ninjapig28 = pygame.transform.scale(ninjapig28, (465, 465))
        nasa = pygame.image.load("Images/nasa.jpg")
        nasa = pygame.transform.scale(nasa, (465, 465))
        chess = pygame.image.load("Images/chess.png")
        chess = pygame.transform.scale(chess, (465, 465))
        self.photolist = [ninjapig28, nasa, chess]
        self.pic = random.choice(self.photolist)


class Blank(SlideGrid):
    def get_pos(self, gird):
        for county, row in enumerate(gird):
            for countx, value in enumerate(row):
                if value == 0:
                    return county, countx

    def move(self, y, x, mx, my, gird):
        try:

            if x + mx > -1 and y + my > -1:
                moving_value = gird[y + my][x + mx]
                gird[y + my][x + mx] = 0
                gird[y][x] = moving_value
        except:
            pass

    def show_gird(self, gird):
        for row in gird:
            print(row)

    def start(self, gird):
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(1000):
            y, x = Blank.get_pos(self, gird)
            current_move = random.choice(moves)

            Blank.move(self, y, x, current_move[0], current_move[1], gird)


class Graphics(SlideGrid):
    def PyDrawPuzzle(self):
        sqaure_size = 166
        for y, row in enumerate(self.gird):
            for x, collum in enumerate(row):
                if collum == 1:
                    # pygame.draw.rect(win, (light_red), [330+sqaure_size*x,20+sqaure_size*y,155,155])
                    image = self.pic.subsurface(0, 0, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 1)
                if collum == 2:
                    image = self.pic.subsurface(155, 0, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 2)
                if collum == 3:
                    image = self.pic.subsurface(310, 0, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 3)
                if collum == 4:
                    image = self.pic.subsurface(0, 155, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 4)
                if collum == 5:
                    image = self.pic.subsurface(155, 155, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 5)
                if collum == 6:
                    image = self.pic.subsurface(310, 155, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 6)
                if collum == 7:
                    image = self.pic.subsurface(0, 310, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 7)
                if collum == 8:
                    image = self.pic.subsurface(155, 310, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    Graphics.write_number(self, 330 + sqaure_size * x, 20 + sqaure_size * y, 8)
                if collum == 0:
                    image = self.pic.subsurface(310, 310, 155, 155)
                    win.blit(image, (330 + sqaure_size * x, 20 + sqaure_size * y))
                    pygame.draw.rect(win, (bg), [330 + sqaure_size * x, 20 + sqaure_size * y, 155, 155])

    def write_number(self, x, y, num):
        label = self.font.render(str(num), 1, (0, 0, 0))
        win.blit(label, (x + 15, y))

    def write(self, x, y, size, text, color):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, (color))
        win.blit(label, (x, y))

    def draw_otherpics(self):
        photo1 = pygame.transform.scale(self.photolist[0], (150, 150))
        win.blit(photo1, (45, 50))
        photo2 = pygame.transform.scale(self.photolist[1], (150, 150))
        win.blit(photo2, (45, 220))
        photo3 = pygame.transform.scale(self.photolist[2], (150, 150))
        win.blit(photo3, (45, 390))


class Rules(SlideGrid):
    def check_win(self):
        if self.gird == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print("winner")


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


main_slide()
