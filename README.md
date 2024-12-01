# Connect-4 with Minimax AI

## Project Overview
This project implements a Connect-4 game with an artificial intelligence opponent using the Minimax algorithm enhanced with alpha-beta pruning and heuristic evaluation. Originally developed as a school project, it demonstrates advanced game-playing algorithms while maintaining efficient performance.

## Game Rules
Connect-4 is a two-player strategy game played on a 7x6 board (7 columns, 6 rows). Players take turns dropping colored discs into columns, with pieces falling to the lowest unoccupied position. The goal is to connect four discs of your color horizontally, vertically, or diagonally.

## Technical Implementation

### Core Algorithms

1. **Win Detection Algorithm**
   - Checks for winning combinations in all directions (horizontal, vertical, diagonal)
   - Evaluates board state after each move
   - Implements efficient pattern recognition for connected pieces

2. **AI Implementation (Minimax with Optimizations)**
   - Base algorithm: Minimax with alpha-beta pruning
   - Challenge: Large search space (~4.5×10¹² possible positions)
   - Optimizations implemented:
     - Alpha-beta pruning for reduced memory usage
     - Heuristic evaluation for faster decision-making
     - Position-based scoring system

3. **Leaderboard Management**
   - Tracks top 3 winners
   - Maintains persistent score history
   - Updates rankings dynamically

### Heuristic Evaluation System

The AI uses a sophisticated scoring system based on "windows" - sets of four consecutive cells in any direction. The scoring system incorporates:

- Position-based evaluation
  - Central column positions receive 3 bonus points
  - Strategic advantage recognition
- Pattern recognition
  - Different scores for various piece configurations
  - Weighted scoring favoring offensive play
- Optimized decision making
  - Balance between computation speed and play strength
  - Asymmetric scoring between player and opponent positions

## Technical Notes

- Originally developed in PyCharm
- Implements efficient board state evaluation
- Balances AI challenge level with response time
- Focuses on aggressive play strategy while maintaining defensive capabilities

## Original Development

This project was initially developed in PyCharm before being migrated to GitHub. The codebase reflects academic research and implementation of game-playing algorithms, with particular attention to performance optimization and user experience.


![image](https://github.com/user-attachments/assets/1fa172d5-7353-471d-94d1-80e1d9030abd)
