import pygame
from classes.PostTypes import *
from buttons import *
from classes.Button import Button
from classes import *
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))
    post1 = TextPost(GREY, "AAA", WHITE, "a", "a", 0, [])
    post2 = TextPost(GREY, "BBB", WHITE, "a", "a", 0, [])
    posts = [post1, post2]
    post_index = 0
    clicked = False

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last\ clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if click_post_button.is_pushed() and not clicked:
            if post_index == len(posts) - 1:
                post_index = 0
            else:
                post_index += 1
            clicked = True
        if like_button.is_pushed() and not clicked:
            posts[post_index].like_count += 1
            clicked = True
        if not pygame.mouse.get_pressed()[0] and clicked:
            clicked = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        posts[post_index].display()

        # Update display - without input update everything

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
