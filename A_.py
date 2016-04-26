import math
import copy
import time

# position of the best path search
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y   
    
class PathData:    
    def __init__(self):
        # list of paths that can be continued, containing: a path and Fscore
        self.openList = []
        # List of coordinates already visited 
        self.closedList = []
    
    # function to put a path as openPath in the open list
    def putInOpenList(self, path, F):
        openPath = [path, F]
        self.openList.append(openPath)
    
    # function to put an element in the closed list
    def putInClosedList(self, pos):
        self.closedList.append(pos)
    
    # function to check if a position is in the closed list
    def inClosedList(self, position):
        for element in self.closedList:
            if element.getX() == position.getX() and element.getY() == position.getY():
                return True
        return False 
    
    # function to delete element from the open list
    def deleteFromOpenList(self, path):
        counter = 0
        for element in self.openList:
            if path is element[0]:
                del self.openList[counter]
            counter += 1
            
    def getLowestFScore(self, endPos):
        lowestFscore = 10000
        H = 10000
        bestPath = self.openList[0]
        for possiblePath in self.openList:
            if possiblePath[1] < lowestFscore:
                lowestFscore = possiblePath[1]
                H = calcDistance(possiblePath[0][-1], endPos)
                bestPath = possiblePath[0]
            elif possiblePath[1] == lowestFscore and calcDistance(possiblePath[0][-1], endPos) < H:
                lowestFscore = possiblePath[1]
                H = len(possiblePath[0])
                bestPath = possiblePath[0]
        return bestPath

class Grid:
    # dus dit is voor het maken van het grid van 17 bij 12
    def __init__(self, width, height):
        self.grid = [[0 for x in range(height)] for x in range(width)]
        self.width = width
        self.height = height
    
    def setPointToValue(self, position, value):
        self.grid[position.getX()][position.getY()] = value

    def printGrid(self):
        for row in self.grid:
            print row
            
    def setStartEnd(self, startPos, endPos):
        self.start = startPos
        self.end = endPos
        self.grid[startPos.getX()][startPos.getY()] = 1
        self.grid[endPos.getX()][endPos.getY()] = 2
        
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    # find all possible next paths in the grid
    def getPossibleNextPaths(self, currentPath, pathData):
        nextPaths = []
        x = currentPath[-1].getX()
        y = currentPath[-1].getY()
        
        possiblePath = copy.copy(currentPath)
        
        rightx = x + 1
        if rightx <= self.width-1 and (self.grid[rightx][y] == 0 or self.grid[rightx][y] == 2) and not pathData.inClosedList(Position(rightx, y)):
            possiblePath.append(Position(rightx, y))
            nextPaths.append(possiblePath)

        possiblePath = copy.copy(currentPath)
        leftx = x - 1
        if leftx >= 0 and (self.grid[leftx][y] == 0 or self.grid[leftx][y] == 2) and not pathData.inClosedList(Position(leftx, y)):
            possiblePath.append(Position(leftx, y))
            nextPaths.append(possiblePath)

        possiblePath = copy.copy(currentPath)
        upy = y + 1
        if upy <= self.height-1 and (self.grid[x][upy] == 0 or self.grid[x][upy] == 2) and not pathData.inClosedList(Position(x, upy)):
            possiblePath.append(Position(x, upy))
            nextPaths.append(possiblePath)
            
        possiblePath = copy.copy(currentPath)
        downy = y - 1
        if downy >= 0 and (self.grid[x][downy] == 0 or self.grid[x][downy] == 2) and not pathData.inClosedList(Position(x, downy)):
            possiblePath.append(Position(x, downy))
            nextPaths.append(possiblePath)
            
        return nextPaths
        
    def drawPath(self, path):
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = 0
        for step in path:
            self.grid[step.getX()][step.getY()] = 1

def findPath(grid):

    pathData = PathData()
    
    currentPath = []
    currentPath.append(grid.getStart())
    endPos = grid.getEnd()
    
    while not(currentPath[-1].getX() == endPos.getX() and currentPath[-1].getY() == endPos.getY()):

        pathData.deleteFromOpenList(currentPath)    

        # add currentPos to closedList
        pathData.putInClosedList(currentPath[-1])
        # expand the openList
        continuationList = grid.getPossibleNextPaths(currentPath, pathData)

        for possiblePath in continuationList:
            # calculate cost and heuristic
            G = len(possiblePath) - 1
            H = calcDistance(possiblePath[-1], endPos)
            F = G + H
            # put path,cost and heuristic in the openList like [[path], F-score]
            pathData.putInOpenList(possiblePath, F)
            
        # set currentPath to the lowest F-score path in the openList
        currentPath = pathData.getLowestFScore(endPos)
        grid.setPointToValue(currentPath[-1], 1)
        # time.sleep(0.3)
        # print ""
        # grid.printGrid()
        # print pathData.closedList
    print "visited:"    
    grid.printGrid()    
    print "found path:"
    grid.drawPath(currentPath)
    grid.printGrid()

# function to calculate manhattan distance
def calcDistance(pos1, pos2):
    distance = abs(pos1.getX() - pos2.getX()) + abs(pos1.getY() - pos2.getY())
    return distance

if __name__ == "__main__":
    newGrid = Grid(5,10)

    start = Position(4,1)
    end = Position(4,9)

    newGrid.setStartEnd(start, end)
    
    # obstruction
    newGrid.setPointToValue(Position(4,3), 3)
    newGrid.setPointToValue(Position(1,3), 3)
    newGrid.setPointToValue(Position(2,3), 3)
    newGrid.setPointToValue(Position(3,3), 3)

    time1 = time.time()
    findPath(newGrid)
    time2 = time.time()
    print "time in seconds:"
    print (time2-time1)
    
    
    
    
    
    
    