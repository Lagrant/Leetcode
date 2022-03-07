# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
from collections import defaultdict
from collections import deque
import types
class Solution:
    def __init__(self) -> None:
        self.visited = defaultdict(bool)
        self.dirs = ['up', 'left', 'down', 'right']
        self.dir_vecs = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def turnDown(self):
            self.turnRight()
            self.turnRight()
        robot.turnDown = types.MethodType(turnDown, robot)
        self.action = {
            'up': {
                'up': lambda : None,
                'left': robot.turnLeft,
                'right': robot.turnRight,
                'down': robot.turnDown
            },
            'left': {
                'up': robot.turnRight,
                'left': lambda : None,
                'down': robot.turnLeft,
                'right': robot.turnDown
            },
            'right': {
                'up': robot.turnLeft,
                'down': robot.turnRight,
                'right': lambda : None,
                'left': robot.turnDown
            },
            'down': {
                'up': robot.turnDown,
                'left': robot.turnRight,
                'right': robot.turnLeft,
                'down': lambda : None
            }
        }
        self.visited['0,0'] = True
        robot.clean()
        self.next_step(robot, [0,0], 'up')
    
    def next_step(self, robot, pos, status):
        # self.visited[','.join([str(i) for i in pos])] = True
        for dir in self.dirs:
            # self.dirs = ['up', 'left', 'down', 'right']
            new_pos = [pos[0] + self.dir_vecs[dir][0], pos[1] + self.dir_vecs[dir][1]]
            
            new_pos_str = ','.join([str(i) for i in new_pos])
            # print(new_pos_str)
            if (not self.visited[new_pos_str]):
                # if (pos == [3,-3]):
                    # print(f'status: {status}, dir: {dir}')
                self.action[status][dir]()
                status = dir
                moved = robot.move()
                # print(f'moved: {moved}')
                if (moved):
                    self.visited[new_pos_str] = True
                    robot.clean()
                    self.next_step(robot, new_pos, status)

class Solution {
    private static int[][] dirs = new int[][] {{-1 , 0}, {0, 1}, {1, 0}, {0, -1}}; // 0 up, 1 right, 2 down, 3 left  
   
    public void cleanRoom(Robot robot) {
        dfs(robot, 0, 0, new HashSet<>(), 0);
    }
    
    private void dfs(Robot robot, int x, int y, Set<String> visited, int dir) {
        visited.add(x + "," + y);
        robot.clean(); // clean the current cell.

        for (int i=0; i<4; i++) { // iterate all 4 directions, make a right turn each time.
            int[] newDir = dirs[(dir + i) % 4];
            int newX = x + newDir[0], newY = y + newDir[1];
            if (!visited.contains(newX + "," + newY) && robot.move()) { // check if we can visit the next cell in the current direction.
                dfs(robot, newX, newY, visited, (dir + i) % 4); // if so, visit it.
            }
            robot.turnRight(); // make a right turn to try next direction.
        }
        
        robot.turnRight(); robot.turnRight(); // after we finished explore all possibilities at current cell, turn back
        robot.move(); // move back
		robot.turnRight(); robot.turnRight(); // turn back again so that we return to the same state before the current recursion.
    }
}