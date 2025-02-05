import pygame

from constants import *
from helpers import screen


class Post:
    def __init__(self, user_name, location, like_count, comments, description):
        self.user_name = user_name
        self.comments = comments
        self.location = location
        self.like_count = like_count
        self.description = description

    def display(self):
        # Like Count
        font = pygame.font.SysFont("Tahoma", UI_FONT_SIZE)
        render_text = font.render(str(self.like_count), True, BLACK)
        screen.blit(render_text, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS - 6))

        # Username
        font = pygame.font.SysFont("Tahoma", UI_FONT_SIZE)
        render_text = font.render(self.user_name, True, BLACK)
        screen.blit(render_text, (USER_NAME_X_POS, USER_NAME_Y_POS - 5))

        # Location
        font = pygame.font.SysFont("Tahoma", COMMENT_TEXT_SIZE)
        render_text = font.render(self.location, True, BLACK)
        screen.blit(render_text, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS + 2))

        self.display_comments()

        #Description
        font = pygame.font.SysFont("Tahoma", COMMENT_TEXT_SIZE)
        render_text = font.render(self.description, True, BLACK)
        screen.blit(render_text, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))

    def display_comments(self):
        font = pygame.font.SysFont("Tahoma", COMMENT_TEXT_SIZE)
        for i in range(0, min(len(self.comments), NUM_OF_COMMENTS_TO_DISPLAY)):
            render_text = font.render(self.comments[i], True, GREY)
            screen.blit(render_text, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * i))
