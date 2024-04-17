import pygame


def music(screen, screen_width, screen_height):
    pygame.init()

    color_start = pygame.Color('Black')
    color_end = (139, 0, 139)

    songs = ['Song № 1', 'Song № 2', 'Song № 3']
    text_font = pygame.font.SysFont('Times New Roman', 28)
    texts_coords = [(10, 100), (10, 210), (10, 320)]

    exit_button = pygame.Rect(10, 0, 96, 96)
    exit_image = pygame.image.load("data/left_arrow.png")

    check_coords = [(300, 80), (300, 190), (300, 300)]
    check_list = [pygame.image.load("music/check.png") for _ in range(3)]
    cross_list = [pygame.image.load("music/cross.png") for _ in range(3)]
    check_rects = []
    for button in range(3):
        check_rect = pygame.Rect(check_coords[button][0], check_coords[button][1], 96, 96)
        check_rects.append(check_rect)
    checked_list = [0]

    play_coords = [(170, 80), (170, 190), (170, 300)]
    play_list = [pygame.image.load("music/play.png") for _ in range(3)]
    pause_list = [pygame.image.load("music/pause.png") for _ in range(3)]
    play_rects = []
    for button in range(3):
        play_rect = pygame.Rect(play_coords[button][0], play_coords[button][1], 96, 96)
        play_rects.append(play_rect)
    playing_song = 0
    pygame.mixer.music.load(f'Music/music{playing_song}.mp3')
    pygame.mixer.music.play(-1)

    image = pygame.image.load("volume/no_volume.png")
    image_rect = pygame.Rect(500, 0, 96, 96)
    volume = 0
    pictures = ['no_volume', 'low', 'medium', 'high']
    pygame.mixer.music.set_volume(volume)
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if image_rect.collidepoint(event.pos):
                    volume = 1 if volume == 0.66 else volume + 0.33 if volume < 1 else 0
                    image = pygame.image.load(f"volume/{pictures[int(volume / 0.33)]}.png")
                    pygame.mixer.music.set_volume(volume)
                if exit_button.collidepoint(event.pos):
                    return checked_list
                for i in range(len(check_rects)):
                    if check_rects[i].collidepoint(event.pos):
                        if i not in checked_list:
                            checked_list.append(i)
                        else:
                            del checked_list[checked_list.index(i)]
                for i in range(len(play_rects)):
                    if play_rects[i].collidepoint(event.pos):
                        if i != playing_song:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(f'Music/music{i}.mp3')
                            playing_song = i
                            pygame.mixer.music.play(-1)
                        else:
                            playing_song = 5
                            pygame.mixer.music.stop()
        for y in range(screen_height):
            r = int((color_end[0] - color_start[0]) * (y / screen_height) + color_start[0])
            g = int((color_end[1] - color_start[1]) * (y / screen_height) + color_start[1])
            b = int((color_end[2] - color_start[2]) * (y / screen_height) + color_start[2])
            pygame.draw.rect(screen, (r, g, b), pygame.Rect(0, y, screen_width, 1))

        for i in range(len(texts_coords)):
            text = text_font.render(songs[i], True, (123, 104, 238))
            x, y = text.get_rect().size
            text_rect = pygame.Rect(texts_coords[i][0], texts_coords[i][1], x, y)
            screen.blit(text, text_rect)

        text = text_font.render('Выберите музыку', True, (123, 104, 238))
        text_rect = text.get_rect()
        text_rect.center = (screen_width // 2, 50)
        screen.blit(text, text_rect)

        text = text_font.render('галочка / крестик для выбора песен, которые будут', True, (123, 104, 238))
        text_rect = text.get_rect()
        text_rect.center = (320, 490)
        screen.blit(text, text_rect)

        text = text_font.render('проигрываться во время игры', True, (123, 104, 238))
        text_rect = text.get_rect()
        text_rect.center = (445, 530)
        screen.blit(text, text_rect)

        text = text_font.render('пауза / возобновление для предпросмотра песен', True, (123, 104, 238))
        text_rect = text.get_rect()
        text_rect.center = (300, 450)
        screen.blit(text, text_rect)

        for button in range(3):
            play = play_list[button] if button != playing_song else pause_list[button]
            screen.blit(play, play_coords[button])

        for button in range(3):
            check = check_list[button] if button in checked_list else cross_list[button]
            screen.blit(check, check_coords[button])

        screen.blit(image, (500, 0))
        screen.blit(exit_image, (10, 0))

        pygame.display.flip()
    pygame.quit()
