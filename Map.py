import pygame
from Enums import TileType

class Map:
    def __init__(self, xsize=8, ysize=8):
        self.xsize = xsize
        self.ysize = ysize
        self.screen = pygame.display.set_mode((800, 800))
        pygame.init()
        self.mapData = [[TileType.GROUND]*xsize for x in range(ysize)]

        #could be randomized later on but for now cba
        self.mapData[1][1] = TileType.CAT
        self.mapData[1][2] = TileType.CAT
        self.mapData[1][3] = TileType.CAT
        self.mapData[1][5] = TileType.CAT
        self.mapData[1][6] = TileType.CAT
        self.mapData[1][7] = TileType.CAT

        self.mapData[2][0] = TileType.CAT
        self.mapData[2][5] = TileType.CAT

        self.mapData[3][1] = TileType.CAT
        self.mapData[3][3] = TileType.CAT
        self.mapData[3][4] = TileType.CAT
        self.mapData[3][5] = TileType.CAT

        self.mapData[4][4] = TileType.CAT
        self.mapData[5][4] = TileType.CAT
        self.mapData[6][4] = TileType.CAT
        self.mapData[6][6] = TileType.CAT
        self.mapData[7][6] = TileType.CAT

        #init
        self.mapData[7][5] = TileType.CHEESE #extra cheese for less RNG
        self.mapData[7][7] = TileType.CHEESE

    def draw(self, mousepos):
        for i in range(len(self.mapData)):
            for j in range(len(self.mapData[i])):
                if self.mapData[i][j] == TileType.CAT:
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(i*100, j*100, 100, 100))
                if self.mapData[i][j] == TileType.CHEESE:
                    pygame.draw.rect(self.screen, (255, 255, 0), pygame.Rect(i*100, j*100, 100, 100))
                if self.mapData[i][j] == TileType.GROUND:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(i*100, j*100, 100, 100))

        pygame.draw.rect(self.screen, (128, 128, 128), pygame.Rect(mousepos[0]*100, mousepos[1]*100, 100, 100))
        pygame.display.flip()   #draw

    # def updateMouse(self, xpos, ypos):
    #     for i in range(len(self.mapData)):
    #         for j in range(len(self.mapData[i])):
    #             if self.mapData[j][i] == TileType.MOUSE:
    #                 mapData[j][i] = TileType.GROUND
    #     mapData[ypos][xpos] = TileType.MOUSE

    def getTileInfo(self, xpos, ypos):
        return self.mapData[xpos][ypos]
        
