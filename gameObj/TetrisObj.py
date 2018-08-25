import pygame

#class which renders single block, implementation can change depending on how
#we want to do game logic
class TetrisBlock:
    def __init__(self, surface):
        self.x = 0
        self.y = 0
        self.imgPath = "img/block.png"
        self.img = pygame.image.load(self.imgPath)
        self._surface = surface

    def render(self):
    	self._surface.blit(self.img, (self.x,self.y))