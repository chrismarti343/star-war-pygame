
import pygame
from game import constants

class Setup():
    def __init__(self):
        self.title_font = pygame.font.SysFont("comicsans", 50)
        self.text_font = pygame.font.SysFont("comicsans", 30)
# live,score , level text
        self.main_font = pygame.font.SysFont("comicsans", 30)  
        self.lost_font = pygame.font.SysFont("comicsans", 60)

        
    def game_over_text(self):
        constants.WIN.blit(constants.BG, (0,00))
        title_label = self.title_font.render("Game Over", 1, constants.Red)
        constants.WIN.blit(title_label, (constants.WIDTH/2 - title_label.get_width()/2, 100))
        text_label = self.text_font.render("Would you like to play again? (Enter)", 1, constants.White)
        constants.WIN.blit(text_label, (constants.WIDTH/2 - text_label.get_width()/2, 250))
        text_label1 = self.text_font.render("Press the mouse to return to menu..", 1, constants.White)
        constants.WIN.blit(text_label1, (constants.WIDTH/2 - text_label.get_width()/2, 650))
        pygame.display.update()
    
    def get_main_font(self):
        return self.main_font
    
    def get_lost_font(self):
        return self.lost_font
    
