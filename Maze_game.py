import random
import pygame
pygame.init()

class CreateMaze:

    def __init__(self):
        self.maze = []
        self.count = 0




        def surroundingCells(rand_wall):
            s_cells = 0
            if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
                s_cells += 1
            if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
                s_cells += 1
            if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
                s_cells +=1
            if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                s_cells += 1

            return s_cells

        # Init variables
        wall = 'w'
        cell = 'c'
        unvisited = 'u'

        global width, height

        width, height = input("Enter the width and the height (70 : 55 MAX): ").split(" ")

        width = int(width)
        height = int(height)

        if width >70:
            width =70

        if height > 55:
            height = 55





        # Denote all cells as unvisited
        for i in range(0, height):
            line = []
            for j in range(0, width):
                line.append(unvisited)
            self.maze.append(line)

        # Randomize starting point and set it a cell
        starting_height = int(random.random()*height)

        starting_width = int(random.random()*width)

        if (starting_height == 0):
            starting_height += 1
        if (starting_height == height-1):
            starting_height -= 1
        if (starting_width == 0):
            starting_width += 1
        if (starting_width == width-1):
            starting_width -= 1

        #Mark it as cell and add surrounding walls to the list
        self.maze[starting_height][starting_width] = cell
        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        # Denote walls in maze
        self.maze[starting_height-1][starting_width] = 'w'
        self.maze[starting_height][starting_width - 1] = 'w'
        self.maze[starting_height][starting_width + 1] = 'w'
        self.maze[starting_height + 1][starting_width] = 'w'

        while (walls):
            # Pick a random wall
            rand_wall = walls[int(random.random()*len(walls))-1]

            # Check if it is a left wall
            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'u' and self.maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                    # Find the number of surrounding cells
                    s_cells = surroundingCells(rand_wall)

                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])


                        # Bottom cell
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])


                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check if it is an upper wall
            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'u' and self.maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        # Upper cell
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Leftmost cell
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])

                        # Rightmost cell
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Check the bottom wall
            if (rand_wall[0] != height-1):
                if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'u' and self.maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                            if ([rand_wall[0], rand_wall[1]-1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]-1])
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)


                    continue

            # Check the right wall
            if (rand_wall[1] != width-1):
                if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'u' and self.maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                    s_cells = surroundingCells(rand_wall)
                    if (s_cells < 2):
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'

                        # Mark the new walls
                        if (rand_wall[1] != width-1):
                            if (self.maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                            if ([rand_wall[0], rand_wall[1]+1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1]+1])
                        if (rand_wall[0] != height-1):
                            if (self.maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]+1, rand_wall[1]])
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                            if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Delete wall
                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            # Delete the wall from the list anyway
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)




        # Mark the remaining unvisited cells as walls
        for i in range(0, height):
            for j in range(0, width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = 'w'

        # Set entrance and exit
        for i in range(0, width):
            if (self.maze[1][i] == 'c'):
                self.maze[0][i] = 'c'
                break

        for i in range(width-1, 0, -1):
            if (self.maze[height-2][i] == 'c'):
                self.maze[height-1][i] = 'c'
                break

        def Add_solutions(Number_of_walls,x_start,x_end,y_start,y_end):
            while Number_of_walls > 0:
                random_number_x = random.randint(x_start,x_end)
                random_number_y = random.randint(y_start,y_end)
                try:
                    if self.maze[random_number_y][random_number_x] == "w" and Number_of_walls > 0 \
                            and self.maze[random_number_y][random_number_x+1] == "c" and self.maze[random_number_y+1][random_number_x] != "c" \
                            and self.maze[random_number_y-1][random_number_x] != "c" \
                            or self.maze[random_number_y][random_number_x] == "w" and Number_of_walls > 0 \
                            and self.maze[random_number_y+1][random_number_x] == "c"  and self.maze[random_number_y+1][random_number_x+1] != "c" \
                            and self.maze[random_number_y+1][random_number_x-1] != "c":
                        self.maze[random_number_y][random_number_x] = "c"
                        Number_of_walls += -1


                except:
                    pass

        Number_of_walls = int(width*height/154)
        Add_solutions(Number_of_walls,1,width-2,1,height-2)

        Number_of_walls = int(width*height/770)
        Add_solutions(Number_of_walls,width-15,width-2,height-15,height-2)
        Add_solutions(Number_of_walls,1,15,1,15)


class PlayerAndSetup(CreateMaze):

    def start(self):
        for i in range(10):
            if self.maze[-1][-2-i] == "c":
                self.maze[-1][-2-i] = "x"
                break



    def pymoveR(self):
        if self.maze[self.x][self.y+1]!="w":
            self.maze[self.x][self.y]="u"
            self.y +=1
            self.maze[self.x][self.y]="p"
            self.count = self.count +1

    def pymoveL(self):
        if self.maze[self.x][self.y-1]!="w":
            self.maze[self.x][self.y]="u"
            self.y -=1
            self.maze[self.x][self.y]="p"
            self.count = self.count +1

    def pymoveD(self):
        if self.maze[ self.x+1][ self.y]=="c" or self.maze[self.x+1][self.y]== "u":
            self.maze[ self.x][ self.y]="u"
            self.x +=1
            self.maze[self.x][self.y]="p"
            self.count = self.count +1

    def pymoveU(self):
        if self.maze[ self.x-1][self.y]!="w":
            self.maze[self.x][self.y]="u"
            self.x -=1
            self.maze[self.x][self.y]="p"
            self.count = self.count +1


    def checkwin(self,timerx):
        try:
            if self.maze[self.x][self.y+1] == "x" or self.maze[self.x+1][self.y] == "x":
                font = pygame.font.SysFont("comicsans", 100, bold=True)
                label = font.render("YOU WIN!", 1, Player_Color)
                win.blit(label,(390,290))

                if self.count < int(self.score) and width==70 and height == 55 and timerx < int(self.TimerHighscore):
                    self.updatescore_both(timerx)
                elif self.count < int(self.score) and width==70 and height == 55:
                    self.updatescore_moves()
                elif timerx < int(self.TimerHighscore) and width==70 and height == 55:
                    self.updatescore_timer(timerx)
        except:
            pass

    def updatescore_both(self, timerx):
        with open("Data_Bases/Maze_Highscore.txt", "w") as f:
            f.write(str(self.count) + '\n')
            f.write(str(timerx))

    def updatescore_moves(self):
        with open("Data_Bases/Maze_Highscore.txt", "w") as f:
            f.write(str(self.count) + '\n')
            f.write(str(self.TimerHighscore))


    def updatescore_timer(self, timerx):
        with open("Data_Bases/Maze_Highscore.txt", "w") as f:
            f.write(self.scorestr + '\n')
            f.write(str(timerx))


    def pyDrawMaze(self):
        for y, row in enumerate(self.maze):
            for x, collum in enumerate(row):
                if collum == "p":
                    pygame.draw.rect(win, (Player_Color), [x*10+200,y*10+20,x*10+260,y*10+80])
                if collum == "c":
                    pygame.draw.rect(win, (gery), [x*10+200,y*10+20,x*10+260,y*10+80])
                if collum == "u":
                    pygame.draw.rect(win, (light_blue), [x*10+200,y*10+20,x*10+260,y*10+80])
                if collum == "w":
                    pygame.draw.rect(win, (bg), [x*10+200,y*10+20,x*10+260,y*10+80])
                if collum == "x":
                    pygame.draw.rect(win, (gold), [x*10+200,y*10+20,x*10+260,y*10+80])
                if collum == "path":
                    pygame.draw.rect(win, (light_red), [x*10+200,y*10+20,x*10+260,y*10+80])
                else:
                    pass

    def get_score(self):
        with open("Data_Bases/Maze_Highscore.txt", "r") as f:
            lines = f.readlines()
            self.score = lines[0].strip()
        with open("Data_Bases/Maze_Highscore.txt", "r") as f:
            lines = f.readlines()
            self.TimerHighscore = lines[1].strip()

        self.scorestr = str(self.score)

    def Score(self,timerx):
        #moves
        font = pygame.font.SysFont("comicsans", 30, bold=True)
        label = font.render("moves: "+ str(self.count), 1, orange)
        win.blit(label,(10,20))

        #Lowest moves
        font = pygame.font.SysFont("comicsans", 30, bold=True)
        label = font.render("highscore: "+ self.scorestr, 1, (blue))
        win.blit(label,(925,20))


        #timer
        font = pygame.font.SysFont("comicsans", 30, bold=True)
        label = font.render("time: "+ str(timerx), 1, (pink))
        win.blit(label,(10,80))

        #Fastest time
        font = pygame.font.SysFont("comicsans", 30, bold=True)
        label = font.render("fastest time: "+ str(self.TimerHighscore), 1, (lightgreen))
        win.blit(label,(925,80))

        #A_star
        font = pygame.font.SysFont("comicsans", 25, bold=True)
        label = font.render("Press Enter to Slove!", 1, (light_red))
        win.blit(label,(925,440))

    def setStart(self):
        break1 = False
        for i, row in enumerate(self.maze):
            for j, collum in enumerate(row):
                if collum == "c":
                    self.maze[i][j]="p"
                    self.x,self.y = i,j
                    break1 = True
                    break
            if break1 == True:
                break
    def Best_Moves(self):
        font = pygame.font.SysFont("comicsans", 20, bold=True)
        label = font.render("A_star Score:"+str(self.maze[0][0])+" moves", 1, (blue))
        win.blit(label,(920,465))


#class variables
class Node:
    """
        A node class for A* Pathfinding
        parent is parent of the current Node
        position is current position of the Node in the maze
        g is cost from start to current Node
        h is heuristic based estimated cost for current Node to end Node
        f is total cost of present node i.e. :  f = g + h
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
class A_star(Node):
    def start(self,maze):
        for county, row in enumerate(maze):
            for countx, value  in enumerate(row):
                if value == "p":
                    x1, y1 = countx,county
                    self.start= y1, x1

        for county, row in enumerate(maze):
            for countx, value  in enumerate(row):
                if value == "x":
                    x2, y2 = countx,county
                    self.goal = y2, x2
    def Heuristic(self,p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(int(x1) - int(x2)) + abs(int(y1) - int(y2))

    def Find_neighbours(self, current_node, maze):
        no_rows, no_columns = height, width
        moves = [[-1, 0],  # go up
                 [0, -1],  # go left
                 [1, 0],  # go down
                 [0, 1]]  # go right
        children = []

        for new_position in moves:

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range (check if within maze boundary)
            if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                    node_position[1] < 0):
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == "w":
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)
        return children
    def send_path(self,current_node, maze):
        path = []
        # here we create the initialized result maze with -1 in every position
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        # Return reversed path as we need to show from start to end path
        path = path[::-1]
        # we update the path of start to end found by A-star search with every step incremented by
        self.Best_moves=0
        for i in range(len(path)):
            maze[path[i][0]][path[i][1]] = "path"
            maze[0][0] = i


    def A_star(self, maze):


        # Create start and end node with initiazed values for g, h and f
        start_node = Node(None, self.start)
        start_node.g = 0
        goal_node = Node(None, self.goal)
        goal_node.g = goal_node.h = goal_node.f = 0
        start_node.h = self.Heuristic(start_node.position, goal_node.position)
        start_node.f =start_node.h

        # In    itialize both yet_to_visit and visited list
        # in this list we will put all node that are yet_to_visit for exploration.
        # From here we will find the lowest cost node to expand next
        unvisisted_list = []
        # in this list we will put all node those already explored so that we don't explore it again
        visited_list = []

        # Add the start node
        unvisisted_list.append(start_node)

        # Adding a stop condition. This is to avoid any infinite loop and stop
        # execution after some reasonable number of steps
        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 40

        # what squares do we search . serarch movement is left-right-top-bottom
        # (4 movements) from every positon

        # Loop until you find the end

        while len(unvisisted_list) > 0:

            # Every time any node is referred from yet_to_visit list, counter of limit operation incremented
            outer_iterations += 1

            # Get the current node
            current_node = unvisisted_list[0]
            current_index = 0
            for index, item in enumerate(unvisisted_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # if we hit this point return the path such as it may be no solution or
            # computation cost is too high
            if outer_iterations > max_iterations:
                print("giving up on pathfinding too many iterations")
                return self.send_path(current_node, maze)

            # Pop current node out off yet_to_visit list, add to visited list
            unvisisted_list.pop(current_index)
            visited_list.append(current_node)

            # test if goal is reached or not, if yes then return the path
            if current_node == goal_node:
                return self.send_path(current_node, maze)

            # Generate children from all adjacent squares
            neighbours = self.Find_neighbours(current_node, maze)
            # Loop through children
            for node in neighbours:

                # Child is on the visited list (search entire visited list)
                if len([visited_node for visited_node in visited_list if visited_node == node]) > 0:
                    continue

                # Create the f, g, and h values
                node.g = current_node.g
                ## Heuristic costs calculated here, this is using eucledian distance
                node.h = self.Heuristic(node.position, goal_node.position)


                node.f = node.g + node.h

                # Child is already in the yet_to_visit list and g cost is already lower
                if len([i for i in unvisisted_list if node == i and node.g > i.g]) > 0:
                    continue

                # Add the child to the yet_to_visit list
                unvisisted_list.append(node)


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

#pygame baisc set up
win = pygame.display.set_mode((1200, 600))

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
Maze_Game()

