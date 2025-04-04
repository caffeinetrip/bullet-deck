import pygame, sys, asyncio

import scripts.pygpen as pp

from scripts.g import G
class Game(pp.PygpenGame):
    def load(self):
        pp.init(
            (1020, 660),
            fps_cap=165,
            caption='sq',
            opengl=True,
            entity_path='data/images/entities',
            input_path='data/key_configs/config.json',
            frag_path='shaders/shader.frag',
        )
        
        self.game_surf = pygame.Surface((340, 220))
        self.display = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.ui_surf = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.light_surf = pygame.Surface((340, 220))
        
        self.e['Assets'].load_folder('data/images/entities/enemy', colorkey=(0, 0, 0))
        self.e['Assets'].load_folder('data/images/entities/bullet', colorkey=(0, 0, 0))
        self.e['Assets'].load_folder('data/images/cards', colorkey=(0, 0, 0))
        self.e['Assets'].load_folder('data/images/background', colorkey=(0, 0, 0))

        self.g = G()

        self.e['Renderer'].set_groups(['default', 'ui', 'game'])
        
        self.camera = pp.Camera(self.display.get_size(), slowness=0.3, pos=[0,0])
    
    def update(self):
        self.e['Renderer'].cycle({'default': self.display, 'ui': self.ui_surf, 'game': self.game_surf})
        self.camera.update()
        
        self.e['Renderer'].blit(self.e['Assets'].images['background']['bg'], (0,0), group='game')
        
        self.display.fill((0, 0, 0, 0))
        self.ui_surf.fill((0, 0, 0))
        self.light_surf.fill((0, 0, 0))
        
        self.g.update(round(self.e['Window'].runtime_, 1))
        
        if self.e['Input'].pressed('quit'):
            pygame.quit()
            sys.exit()
            
        self.e['Window'].cycle({'surface': self.display, 'game_surf': self.game_surf,  'ui_surf': self.ui_surf, 'light_surf': self.light_surf})

asyncio.run(Game().run())


'''
-- card description
-- object shader 
-- wbgl build
-- particles
-- ui (learn)
-- sounds
'''

