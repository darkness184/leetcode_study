"""
Aim is control robot move in 2D plane (x,y) and avoid obstacles.
Then calculate the maximum distance from the origin (0,0) that the robot can reach.
                    N
                    |
                    |
                    |
                    |
      w __________[0,0]__________ E
                    |          
                    |
                    |
                    |
                    |
                    s

conditions:
- Robot starts at the origin (0,0)
- Robot can move in four directions: N, E, S, W
- Robot can move in a sequence of its commands
- Robot can turn left or right
- Robot can move forward
- Robot can't move to the cell containing obstacles
- If robot reach obstacle, it will stop at the cell before the obstacle

solution:
    Clarify input:
        - Commands: list of integers
        - Obstacles: list of lists with two integers (x,y) coreesponding to the position of the obstacle
        => Need to convert obstacles to set of tuples to efficiently track.
    Move:
        - Robot move with 1 unit in the direction until it reach the obstacle or the end of the command
        - If robot reach the obstacle, it will stop and switch to the next command
        - Calculate maximum distance for each unit the robot move
    Direction:
        - Using +1 or -1 to change the direction (+1 for right, -1 for left)
        - Using list to store the direction (N, E, S, W) - [(0, 1), (1, 0), (0, -1), (-1, 0)]
        - Using index to get the current direction with range 0-3 representing N, E, S, W
        - With %4 will help to switch the direction to the next or previous direction
        1 % 4  = 1
        2 % 4  = 2
        3 % 4  = 3
        4 % 4  = 0
        -4 % 4 = 0
        -3 % 4 = 1
        -2 % 4 = 2
        -1 % 4 = 3

note:
1. List
 - syntax: []
 - Mutable: yes
 - Duplicate: yes
2. Tuple
 - syntax: ()
 - Mutable: no
 - Duplicate: yes
3. Set
 - syntax: {}
 - Mutable: yes
 - Duplicate: no
==> Set can't contant list, but can contain tuple (due to list is mutable therefore can't be hashed)
"""


class Solution:
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W
        direction_index = 0 
        position = [0, 0]
        obstacle_set = set(map(tuple, obstacles)) 
        max_distance = 0

        for command in commands:
            if command == -1:
                direction_index = (direction_index + 1) % 4
            elif command == -2:
                direction_index = (direction_index - 1) % 4
            else:
                for _ in range(command):
                    next_position = [position[0] + directions[direction_index][0],
                                     position[1] + directions[direction_index][1]]
                    if tuple(next_position) in obstacle_set:
                        break
                    position = next_position
                    max_distance = max(max_distance, position[0] ** 2 + position[1] ** 2)

        return max_distance