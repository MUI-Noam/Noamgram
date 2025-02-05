import pygame.mouse


class Button:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def is_pushed(self):
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        return (self.x_pos <= mouse_x <= (self.x_pos + self.width)
                and self.y_pos <= mouse_y <= (self.y_pos + self.height)
                and pygame.mouse.get_pressed()[0])
