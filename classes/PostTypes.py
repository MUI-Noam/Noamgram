import pygame.draw

from classes.Post import Post
from constants import *
from helpers import screen


class TextPost(Post):
    def __init__(self, background_color, text, text_color, user_name, location, like_count, comments, description):
        super().__init__(user_name, location, like_count, comments, description)
        self.background_color = background_color
        self.text = text
        self.text_color = text_color

    def display(self):
        super().display()
        # Background
        background = pygame.Rect(POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT)
        pygame.draw.rect(screen, self.background_color, background)

        # Main Text
        font = pygame.font.SysFont("Tahoma", TEXT_POST_FONT_SIZE)
        render_text = font.render(self.text, True, self.text_color)
        screen.blit(render_text,
                    (POST_X_POS + POST_WIDTH / 2 - (TEXT_POST_FONT_SIZE / 4) * len(self.text),
                     POST_Y_POS + POST_HEIGHT / 2 - TEXT_POST_FONT_SIZE / 2))


class ImagePost(Post):
    def __init__(self, image, image_filter, user_name, location, like_count, comments, description):
        super().__init__(user_name, location, like_count, comments, description)
        self.image = image
        self.image_filter = image_filter

    def display(self):
        super().display()
        # Image
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img,(POST_WIDTH,POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))

