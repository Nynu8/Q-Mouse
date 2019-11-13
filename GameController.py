import pygame

from Map import Map
from Enums import Direction, TileType

class MouseGame:
    def __init__(self):
        self.gameMap = Map()
        self.mouse = [0, 0]
        done = False

    def take_action(self, action):
        reward = 0
        if action == Direction.UP:
            if self.mouse[1] > 0:
                self.mouse[1] -= 1
            else:
                reward -= 100
        if action == Direction.RIGHT:
            if self.mouse[0] < 7:
                self.mouse[0] += 1
            else:
                reward -= 100
        if action == Direction.DOWN:
            if self.mouse[1] < 7:
                self.mouse[1] += 1
            else:
                reward -= 100
        if action == Direction.LEFT:
            if self.mouse[0] > 0:
                self.mouse[0] -= 1
            else:
                reward -= 100

        tile = self.gameMap.getTileInfo(self.mouse[0], self.mouse[1])
        if tile == TileType.GROUND:
            reward -= 1
        if tile == TileType.CAT:
            reward -= 1000
            self.reset()
        if tile == TileType.CHEESE:
            reward += 10000
            print("Found cheese")
            self.reset()

        #self.gameMap.draw(self.mouse)
        return self.mouse, reward
        

    def reset(self):
        self.mouse = [0, 0]
        return self.mouse