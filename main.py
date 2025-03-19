import pygame, sys, json

import scripts.pygpen as pp

from scripts.deck import Deck
from scripts.game_session import G
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
        
        self.background_surf = pygame.Surface((340, 220))
        self.display = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.ui_surf = pygame.Surface((340, 220), pygame.SRCALPHA)
        self.light_surf = pygame.Surface((340, 220))
        
        self.e['Assets'].load_folder('data/images/entities/enemy', colorkey=(0, 0, 0))

        self.deck = Deck()
        self.g = G([340/2, 220])

        self.e['Renderer'].set_groups(['default', 'ui', 'bg'])
        
        self.camera = pp.Camera(self.display.get_size(), slowness=0.3, pos=[0,0])

    def update(self):
        
        self.background_surf.fill((0, 0, 0))
        self.display.fill((0, 0, 0, 0))
        self.ui_surf.fill((0, 0, 0, 0))
        self.light_surf.fill((0, 0, 0))
        
        self.e['Renderer'].cycle({'default': self.display, 'ui': self.ui_surf, 'bg': self.background_surf})
        self.camera.update()
        
        self.background_surf.fill((40, 35, 40))
        self.g.render(int(self.e['Window'].runtime_))
        
        if self.e['Input'].pressed('quit'):
            pygame.quit()
            sys.exit()
            
        if self.e['Input'].pressed('first_card'):
            self.deck.cards[0].use_card()
        elif self.e['Input'].pressed('second_card'):
            self.deck.cards[1].use_card()
        elif self.e['Input'].pressed('third_card'):
            self.deck.cards[2].use_card()
            
        self.e['Window'].cycle({'surface': self.display, 'background_surf': self.background_surf,  'ui_surf': self.ui_surf, 'light_surf': self.light_surf})
            
Game().run()