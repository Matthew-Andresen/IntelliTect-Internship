import random

roomSprites = (
# One exit rooms
    (1,0,0,0,
     " ___| |___ ",
     "|         |",
     "|         |",
     "|         |",
     "+=========+"),

    (0,1,0,0,
     " _________ ",
     "|         [",
     "|          ",
     "|         [",
     "+=========+"),

    (0,0,1,0,
     " _________ ",
     "|         |",
     "|         |",
     "|         |",
     "+===| |===+"),

    (0,0,0,1,
     " _________ ",
     "]         |",
     "          |",
     "]         |",
     "+=========+"),

# Two exit rooms
    (1,1,0,0,
     " ___| |___ ",
     "|         [",
     "|          ",
     "|         [",
     "+=========+"),

    (1,0,1,0,
     " ___| |___ ",
     "|         |",
     "|         |",
     "|         |",
     "+===| |===+"),

    (1,0,0,1,
     " ___| |___ ",
     "]         |",
     "          |",
     "]         |",
     "+=========+"),

    (0,1,1,0,
     " _________ ",
     "|         [",
     "|          ",
     "|         [",
     "+===| |===+"),

    (0,1,0,1,
     " _________ ",
     "]         [",
     "           ",
     "]         [",
     "+=========+"),

    (0,0,1,1,
     " _________ ",
     "]         |",
     "          |",
     "]         |",
     "+===| |===+"),

# Three exit rooms
    (1,1,1,0,
     " ___| |___ ",
     "|         [",
     "|          ",
     "|         [",
     "+===| |===+"),

    (1,0,1,1,
     " ___| |___ ",
     "]         |",
     "          |",
     "]         |",
     "+===| |===+"),

    (1,1,0,1,
     " ___| |___ ",
     "]         [",
     "           ",
     "]         [",
     "+=========+"),

    (0,1,1,1,
     " _________ ",
     "]         [",
     "           ",
     "]         [",
     "+===| |===+"),

# Four exit room    
    (1,1,1,1,
     " ___| |___ ",
     "]         [",
     "           ",
     "]         [",
     "+===| |===+"),

# null sprite
    (0,0,0,0,"","","","","")
    )

class Room:
    def __init__(self, xPos, yPos):
        self.viableNeighbors = [0,3,4,5,6,8,9,10,11,12,13,14]
        self.aboveNeighbors = (0,4,5,6,10,11,12,14)
        self.leftNeighbors = (3,6,8,9,11,12,13,14)
        self.bothNeighbors = (0,4,5,8,9,10,13)
        self.sprite = roomSprites[15]
        self.xPos = xPos
        self.yPos = yPos

    def __str__(self):
        return f"Position: ({self.xPos},{self.yPos})"

# assigns sprite    
    def setSprite(self, sprite):
        self.sprite = sprite

# prints the room to the console
    def pr(self):
        r = 4
        while r < len(self.sprite):
            print(self.sprite[r])
            r += 1

# lists the neighbors and their exits
    def listNeighbors(self, above, left):
        if above.sprite[2] == 1 and left.sprite[1] == 1:
            for x in self.bothNeighbors:
                self.viableNeighbors.remove(x)

        if above.sprite[2] == 0:
            for x in self.aboveNeighbors:
                try:
                    self.viableNeighbors.remove(x)
                except:
                    pass
                

        if left.sprite[1] == 0:
            for x in self.leftNeighbors:
                try:
                    self.viableNeighbors.remove(x)
                except:
                    pass

        if above.sprite[2] == 0 and left.sprite[1] == 0:
            self.viableNeighbors.append(15)

        return self.viableNeighbors

# builds square grid of rooms with length gridSize
gridSize = 6
grid = [[Room(x,y) for x in range(gridSize)] for y in range(gridSize)]

# generates map and populates room sprites
y = 0
for row in grid:
    x = 0
    for col in row:
        if y == 0 and x == 0:
            col.setSprite(roomSprites[7])
        else:
            col.setSprite(
                roomSprites[col.listNeighbors(grid[y-1][x], grid[y][x-1])[random.randint(0,len(col.viableNeighbors) - 1)]]
            )

# print rooms to console
        print(grid[y][x])
        grid[y][x].pr()
        x += 1   
    y += 1