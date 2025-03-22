import pygame, sys, json

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
        self.e['Assets'].load_folder('data/images/cards', colorkey=(0, 0, 0))

        self.g = G()

        self.e['Renderer'].set_groups(['default', 'ui', 'game'])
        
        self.camera = pp.Camera(self.display.get_size(), slowness=0.3, pos=[0,0])

    def update(self):
        
        self.game_surf.fill((40, 35, 40))
        self.display.fill((0, 0, 0, 0))
        self.ui_surf.fill((0, 0, 0))
        self.light_surf.fill((0, 0, 0))
        
        self.e['Renderer'].cycle({'default': self.display, 'ui': self.ui_surf, 'game': self.game_surf})
        self.camera.update()
        
        self.g.update(round(self.e['Window'].runtime_, 1))
        
        if self.e['Input'].pressed('quit'):
            pygame.quit()
            sys.exit()
            
        self.e['Window'].cycle({'surface': self.display, 'game_surf': self.game_surf,  'ui_surf': self.ui_surf, 'light_surf': self.light_surf})
            
Game().run()
