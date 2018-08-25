import os
import pygame
from pygame.locals import *

from gameObj import TetrisObj

class Game:
    def __init__(self):
        self._running = True
        self.screen = None

        #this sets the screen size
        self.size = self.weight, self.height = 400, 300
 
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self._running = True

        #temporarily put a single tetris obj here to test screen rendering
        self.tetrisObj = TetrisObj.TetrisBlock(self.screen)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: self.tetrisObj.y -= 3
        if pressed[pygame.K_DOWN]: self.tetrisObj.y += 3
        if pressed[pygame.K_LEFT]: self.tetrisObj.x -= 3
        if pressed[pygame.K_RIGHT]: self.tetrisObj.x += 3

    def on_render(self):
        #this function clears the screen with the color black (0,0,0)
        self.screen.fill((0,0,0))

        #this function renders the block to the screen
        self.tetrisObj.render() 

        #this function flips the render buffer which will show the rendered object
        pygame.display.flip()
        
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        #infinite loop which will continue running game until player presses quit
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    mainGame = Game()
    mainGame.on_execute()