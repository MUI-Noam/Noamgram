import pygame
import pygame_textinput
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
    post1 = TextPost((255, 166, 252), "I LOVE TEXT!!",
                     (156, 240, 255), "TextLover69", "Textland", 0, [], "TEXT! I WANNA BABIES WITH TEXT! I LOVE TEXT")
    post2 = ImagePost("C:\\Users\\User\\PycharmProjects\\Noamgram\\Images\\noa_kirel.jpg",
                      "", "Noa Kirel", "Israel", 0, [], "Got a silly lil guy :>")
    post3 = ImagePost("C:\\Users\\User\\PycharmProjects\\Noamgram\\Images\\ronaldo.jpg",
                      "", "Ronaldo", "Spain", 0, [], "Scored a goal!!")
    posts = [post1, post2, post3]
    post_index = 0
    clicked = False
    typing = False

    font = pygame.font.SysFont("Tahona", UI_FONT_SIZE)
    comment_box = pygame_textinput.TextInputVisualizer(font_object=font)

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last\ clock tick
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if (typing and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN
                    and comment_box.value != ""):
                posts[post_index].comments.append(comment_box.value)
                comment_box.value = ""
                typing = False

        comment_box.update(events)

        if click_post_button.is_pushed() and not clicked:
            if post_index == len(posts) - 1:
                post_index = 0
            else:
                post_index += 1
            clicked = True

        if like_button.is_pushed() and not clicked:
            posts[post_index].like_count += 1
            clicked = True

        if comment_button.is_pushed() and not clicked:
            typing = not typing
            comment_box.value = ""
            clicked = True
            print(typing)

        if not pygame.mouse.get_pressed()[0] and clicked:
            clicked = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        posts[post_index].display()
        # Update display - without input update everything
        if typing:
            screen.blit(comment_box.surface, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * 4))

        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()
main()
