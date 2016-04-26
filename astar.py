#bladiebla
import math

# position of the best path search
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y   
    
    
class Path:    
    def __init__(self):
    
    # list of paths that can be continued, containing: a cost, heuristic and current coordinate
        self.openList = []
        self.closedList = []
    
    # function to put an element in the open list
    # def putInOpenList:
    
    # function to put an element in the closed list
    # def putInClosedList:
    
    # function to delete element from the open list
    # def deleteFromOpenList:

class Grid:
    
    # dus dit is voor het maken van het grid van 17 bij 12
    def __init__(self, width, height):
        self.grid = [[0 for x in range(width)] for x in range(height)]
        self.width = width
        self.height = height
    
    def setPointToValue(self, position, value):
        self.grid[position.getX()][position.getY()] = value
    
    # def setGates(value):
    #     gates = [0,0], [3,3]
    
    # def setPointStart(self, gateStart):
    #     start = [0,4]

    # def setPointEnd(self, gateEnd):
    #     end = [4,0]

    def printGrid(self):
        for row in self.grid:
            print row



def findPath(grid):
    grid=grid

if __name__ == "__main__":
    newGrid = Grid(4,4)
    otherGrid = Grid(17,12)

    pos = Position(0,3)
    used = 1
    newGrid.setPointToValue(pos, used)

    newGrid.printGrid()
    