import sys

import pygame, asyncio

from ..utils.elements import ElementSingleton

class PygpenGame(ElementSingleton):
    def __init__(self):
        super().__init__()
        
    def load(self):
        pass
    
    def update(self):
        pass
    
    async def run(self):
        self.load()
        while True:
            self.update()
            await asyncio.sleep(0)
            
    def quit(self):
        pygame.quit()
        sys.exit()