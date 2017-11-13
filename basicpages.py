from colors import ORANGE, CORNSILK, WHITE, BLACK
from fonts import XLARGE, LARGE, MEDLARGE
from properties import SCREEN_CENTER, HALF_WIDTH
from button import Button
from eventmanager import EventManager
import pygame
from properties import *

class Page(object):
    def __init__(self, screen, color, event_manager):
        self.color = color
        self.screen = screen
        self.buttons = []
        self.texts = []
        self.textboxes = []
        self.caption = "PONG!!!"
        self.event_manager = event_manager

    def display(self):
        pygame.display.set_caption(self.caption)
        self.screen.fill(self.color)
        for text, text_rect in self.texts:
            self.screen.blit(text, text_rect)
        for button in self.buttons:
            button.display()
        pygame.display.flip()

    def clean(self):
        for button in self.buttons:
            button.clean()

class SplashScreen(Page):
    def __init__(self, screen, event_manager):
        super(SplashScreen, self).__init__(screen, ORANGE, event_manager)

        splash = XLARGE.render("PONG!!!", True, WHITE)
        splash_rect = splash.get_rect()
        splash_rect.center = SCREEN_CENTER

        self.texts.append((splash, splash_rect))

class TextInput(Page):
    def __init__(self, screen, event_manager, prompt, callback):
        super(TextInput, self).__init__(screen, CORNSILK, event_manager)

        prompt = MEDLARGE.render(prompt, True, ORANGE)
        prompt_rect = prompt.get_rect()
        prompt_rect.topleft = (20, HALF_HEIGHT - 100)

        self.texts.append((prompt, prompt_rect))

        self.value = ""
        self.value_rect = pygame.Rect(0, HALF_HEIGHT, SCREEN_WIDTH, 140)
        self.value_surface = pygame.Surface((SCREEN_WIDTH, 140))

        def cb():
            callback(self.value)

        submit_rect = pygame.Rect(0, 0, 100, 60)
        submit_rect.bottomright = (SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        submit = Button("Submit", submit_rect, ORANGE, WHITE, cb, screen, event_manager)

        self.buttons.append(submit)
       
    def display(self):
        super(TextInput, self).display()
        self.event_manager.add_input_listener(self.add_text)
        self.show_value()
    
    def show_value(self):
        value_img = MEDLARGE.render(self.value, True, BLACK)
        self.value_surface.fill(WHITE)
        self.value_surface.blit(value_img, (20, 20))
        self.screen.blit(self.value_surface, (0, HALF_HEIGHT))
        pygame.display.update(self.value_rect)
    
    def add_text(self, letter):
        if letter == -1:
            self.value = self.value[:-1]
        else:
            self.value += letter
        
        self.show_value()
    
    def clean(self):
        super(TextInput, self).clean()
        self.event_manager.remove_input_listener(self.add_text)

class LeaderBoard(Page):
    def __init__(self, screen, event_manager):
        super(LeaderBoard, self).__init__(screen, CORNSILK, event_manager)

        header = LARGE.render("Leaderboard", True, ORANGE)
        header_rect = header.get_rect()
        header_rect.midtop = (HALF_WIDTH, 20)

        self.texts.extend([(header, header_rect)])



if __name__ == '__main__':
    B = Browser()
    B.run()