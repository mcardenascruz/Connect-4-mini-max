# Connect-4-mini-max
The most relevant algorithms used in the Connect-4 game are described in this section. Part of it is based in an excellent tutorial from Keith Galli.
For the Connect-4 game the algorithms deserving major attention are:
Algorithm to check the win in Connect 4.
AI algorithm (Minimax with alpha-beta pruning and heuristics) to allow to play against the computer in Connect-4.
Algorithm for the update of the leader board of the 3 top winners.

Connect-4 game is a two players game on a board of 7 vertical columns and 6 horizontal rows. In the game, each player makes their moves by inserting coloured discs (a different colour per player). Once left into the top of each column, the disc drops into the lowest unoccupied cell in that column.  Only one disc can be dropped in each turn. The player able to connect 4 coloured discs horizontally, vertically or diagonally wins the game. Table 11 shows the pseudocode of the algorithm used to check and recognize the win in the Connect-4 game.
As explained in the Analysis (see section: 1.6.3 Game playing algorithms), minimax algorithm has been applied successfully in different games including tic-tac-toc, chess, backgammon and connect-4. However, the number of possible movements in Connect-4 is too high (~4.5x10^12 positions!) to allow an agile response when the algorithm is asked to explore all the possibilities. The optimization of the algorithm by alpha-beta pruning to reduce the memory requirements, is not enough to ensure fast movements of the computer when all possibilities are explored. To solve this I increased the efficiency of the algorithm including heuristics, which enables a fast response while keeping a high challenging level when playing against the computer (against AI)




I optimized the efficiency of the minimax algorithm with a heuristic function. To do this I firstly defined a variable “window” which is a set of 4 cells in line in any direction (horizontal, vertical, diagonal). For any “window” I gave different scores in function of the number of the discs of the same colour in the window. I realized that the AI worked better in attack mode (to win in opposition to avoid to lose). To enable this, I assigned a slightly lower value at the score of the game of the opponent player. In addition, it is well known that the central positions of the board give an advantage to win. Accordingly for any disc in the central column I gave a score of 3 points. Table 13 shows the values assigned accordingly to the different features. 

![image](https://github.com/user-attachments/assets/1fa172d5-7353-471d-94d1-80e1d9030abd)
