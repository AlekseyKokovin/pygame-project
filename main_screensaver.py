import sys

import pygame
from music import music


def start_screen(screen, screen_width, screen_height):
    pygame.init()
    pygame.display.set_caption("Welcoming Screen")

    color_start = pygame.Color('Black')
    color_end = (139, 0, 139)

    music_choose_rect = pygame.Rect(screen_width // 2 + 75, 155, 96, 96)
    music_choose_image = pygame.image.load("data/settings.png")

    buttons = {0: (10, 20), 1: (12, 24), 2: {8, 16}, 3: (10, 10)}
    button_width, button_height = 150, 50
    buttons_coords = [(10, 100), (170, 100), (330, 100), (490, 100)]
    buttons_texts = ['10X20', '12X24', '8X16', '10X10']
    button_font = pygame.font.SysFont('Times New Roman', 28)
    button_rects = []
    button_pressed = -1
    for button in range(4):
        button_rect = pygame.Rect(buttons_coords[button][0], buttons_coords[button][1], button_width, button_height)
        button_rects.append(button_rect)

    image = pygame.image.load("volume/no_volume.png")
    image_rect = pygame.Rect(400, 0, 96, 96)
    volume = 0
    pictures = ['no_volume', 'low', 'medium', 'high']
    pygame.mixer.music.load('Music/music0.mp3')
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
    current_song_index = 0
    play_songs = [0]

    play = button_font.render('И̲г̲р̲а̲т̲ь̲', True, (123, 104, 238))
    play_rect = pygame.Rect(525, 25, 96, 96)

    left_arrow = pygame.image.load("rules/arrow_left.png")
    right_arrow = pygame.image.load("rules/arrow_right.png")
    down_arrow = pygame.image.load("rules/arrow_down.png")
    up_arrow = pygame.image.load("rules/arrow_up.png")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if music_choose_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    play_songs = music(screen, screen_width, screen_height)
                    if play_songs is None:
                        sys.exit()
                    current_song_index = -1
                    pygame.mixer.music.stop()
                if play_rect.collidepoint(event.pos):
                    return buttons[button_pressed if 0 <= button_pressed <= 3 else 0], play_songs
                if image_rect.collidepoint(event.pos):
                    volume = 1 if volume == 0.66 else volume + 0.33 if volume < 1 else 0
                    image = pygame.image.load(f"volume/{pictures[int(volume / 0.33)]}.png")
                    pygame.mixer.music.set_volume(volume)
                for i in range(len(button_rects)):
                    if button_rects[i].collidepoint(event.pos):
                        button_pressed = i
        screen.fill((0, 0, 0))
        for y in range(screen_height):
            r = int((color_end[0] - color_start[0]) * (y / screen_height) + color_start[0])
            g = int((color_end[1] - color_start[1]) * (y / screen_height) + color_start[1])
            b = int((color_end[2] - color_start[2]) * (y / screen_height) + color_start[2])
            pygame.draw.rect(screen, (r, g, b), pygame.Rect(0, y, screen_width, 1))

        text = button_font.render('Выберите размер поля', True, (123, 104, 238))
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2 - 100, 50)
        screen.blit(text, text_rect)

        music_choose = button_font.render('Выберите музыку -> ', True, (123, 104, 238))
        music_choose_text = text.get_rect()
        music_choose_text.center = (screen_width // 2 - 143, 200)
        screen.blit(music_choose, music_choose_text)

        screen.blit(image, (400, 0))
        screen.blit(music_choose_image, (screen_width // 2 + 75, 155))

        screen.blit(up_arrow, (35, 250))
        text = button_font.render(' - перевернуть фигуру', True, (123, 104, 238))
        text_rect = pygame.Rect(120, 280, 96, 96)
        screen.blit(text, text_rect)

        screen.blit(play, play_rect)

        screen.blit(down_arrow, (35, 330))
        text = button_font.render(' - спустить фигуру на одну клетку', True, (123, 104, 238))
        text_rect = pygame.Rect(120, 360, 96, 96)
        screen.blit(text, text_rect)

        screen.blit(left_arrow, (35, 410))
        text = button_font.render(' - подвинуть фигуру на одну клетку влево', True, (123, 104, 238))
        text_rect = pygame.Rect(120, 440, 96, 96)
        screen.blit(text, text_rect)

        screen.blit(right_arrow, (35, 490))
        text = button_font.render(' - подвинуть фигуру на одну клетку вправо', True, (123, 104, 238))
        text_rect = pygame.Rect(120, 520, 96, 96)
        screen.blit(text, text_rect)

        for button in range(4):
            button_rect = button_rects[button]
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                color_start_button = (238, 160, 238)
                color_end_button = (255, 135, 180)
            elif button_pressed == button:
                color_start_button = (148, 20, 211)
                color_end_button = (147, 125, 219)
            else:
                color_start_button = (238, 130, 238)
                color_end_button = (255, 105, 180)

            for y in range(button_height):
                r = int((color_end_button[0] - color_start_button[0]) * (y / button_height) + color_start_button[0])
                g = int((color_end_button[1] - color_start_button[1]) * (y / button_height) + color_start_button[1])
                b = int((color_end_button[2] - color_start_button[2]) * (y / button_height) + color_start_button[2])
                pygame.draw.rect(screen, (r, g, b),
                                 pygame.Rect(buttons_coords[button][0], buttons_coords[button][1] + y, button_width, 1))

            text_surface = button_font.render(buttons_texts[button], True, pygame.Color('BLACK'))
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)

            if not pygame.mixer.music.get_busy() and play_songs:
                current_song_index = (current_song_index + 1) % len(play_songs)
                pygame.mixer.music.load(f"Music/music{play_songs[current_song_index]}.mp3")
                pygame.mixer.music.play()

        pygame.display.flip()
    pygame.quit()
