import pygame
from sys import exit
from random import choice
import time

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
pygame.mixer.init()

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))

fps = 60
clock = pygame.time.Clock()

back = pygame.image.load('background/background.jpg').convert()
back_start = pygame.image.load('background/start-background.jpg').convert()
hero = pygame.image.load('sprite/hero/hero.png').convert_alpha()
hero_2 = pygame.image.load('sprite/hero/hero-2.png').convert_alpha()
enemy_1 = pygame.image.load('sprite/enemy/enemy_1.png').convert_alpha()
enemy_2 = pygame.image.load('sprite/enemy/enemy_2.png').convert_alpha()
enemy_3 = pygame.image.load('sprite/enemy/enemy_3.png').convert_alpha()
enemy_4 = pygame.image.load('sprite/enemy/enemy_4.png').convert_alpha()
enemy_5 = pygame.image.load('sprite/enemy/enemy_5.png').convert_alpha()
shot = pygame.image.load('sprite/hero/shot.png').convert_alpha()
shot_2 = pygame.image.load('sprite/hero/shot-2.png').convert_alpha()
heart = pygame.image.load('sprite/hp/hearts.png').convert_alpha()
heart_1 = pygame.image.load('sprite/hp/hearts-1.png').convert_alpha()
heart_2 = pygame.image.load('sprite/hp/hearts-2.png').convert_alpha()

pygame.display.set_caption('GuardianShip')

game = False
pause = False
two_player = False

text_font = pygame.font.Font('font/Iceberg-Regular.ttf', 40)
text_surface = text_font.render('GuardianShip', False, '#CCCCFF')
text_name_rect = text_surface.get_rect(center=(500, 550))

text_font_name_game = pygame.font.Font('font/Iceberg-Regular.ttf', 150)
text_newgame_1 = text_font_name_game.render('GuardianShip', False, '#CCCCFF')
text_newgame_rect1 = text_newgame_1.get_rect(center=(500, 250))

text_font_new_game = pygame.font.Font('font/Iceberg-Regular.ttf', 40)
text_newgame_2 = text_font_new_game.render('Press "Space" for start', False, '#CD00CD')
text_newgame_rect2 = text_newgame_2.get_rect(center=(500, 350))

pause_text_font = pygame.font.Font('font/Iceberg-Regular.ttf', 200)
pause_text = pause_text_font.render('Pause', False, 'White')
pause_text_rect = pause_text.get_rect(center=(500, 300))

text_font_score = pygame.font.Font('font/Iceberg-Regular.ttf', 30)
text_ts_font = pygame.font.Font('font/Iceberg-Regular.ttf', 60)


def display_score(score):
    score_surface = text_font_score.render(f'{score}', False, 'Blue')
    score_rect = score_surface.get_rect(topright=(950, 25))
    screen.blit(score_surface, score_rect)


def reset_game():
    global hero_rect, hero_2_rect, enemy_1_rect, enemy_2_rect, enemy_3_rect, enemy_4_rect, enemy_5_rect, shot_rect, shot_2_rect, heart_rect, heart_1_rect, heart_2_rect, enemy_2_flag, enemy_3_flag, enemy_4_flag, enemy_5_flag, shot_flag, shot_2_flag, game, y_pos, hp, speed_enemy, speed_hero, speed_shot, final_score, kill_sound, hp_loss, death_sound, shoot_sound, channel_0, channel_1, channel_2, channel_3

    hp = 3
    speed_enemy = 3
    speed_hero = 8
    speed_shot = 20

    final_score = 0

    y_pos = [100, 150, 200, 250, 300, 350, 400, 450]

    hero_x_pos = 75
    hero_y_pos = 300
    hero_2_x_pos = 925
    hero_2_y_pos = 300
    enemy_1_x_pos = 1200
    enemy_1_y_pos = choice(y_pos)
    enemy_2_x_pos = 1200
    enemy_2_y_pos = choice(y_pos)
    enemy_3_x_pos = 1200
    enemy_3_y_pos = choice(y_pos)
    enemy_4_x_pos = 1200
    enemy_4_y_pos = choice(y_pos)
    enemy_5_x_pos = 1200
    enemy_5_y_pos = choice(y_pos)

    hero_rect = hero.get_rect(center=(hero_x_pos, hero_y_pos))
    hero_2_rect = hero_2.get_rect(center=(hero_2_x_pos, hero_2_y_pos))
    enemy_1_rect = enemy_1.get_rect(center=(enemy_1_x_pos, enemy_1_y_pos))
    enemy_2_rect = enemy_2.get_rect(center=(enemy_2_x_pos, enemy_2_y_pos))
    enemy_3_rect = enemy_3.get_rect(center=(enemy_3_x_pos, enemy_3_y_pos))
    enemy_4_rect = enemy_4.get_rect(center=(enemy_4_x_pos, enemy_4_y_pos))
    enemy_5_rect = enemy_5.get_rect(center=(enemy_5_x_pos, enemy_5_y_pos))
    heart_rect = heart.get_rect(bottomleft=(50, 575))
    heart_1_rect = heart.get_rect(bottomleft=(50, 575))
    heart_2_rect = heart.get_rect(bottomleft=(50, 575))
    shot_rect = shot.get_rect(center=(120, hero_y_pos))
    shot_2_rect = shot_2.get_rect(center=(835, hero_2_y_pos))

    shot_flag = False
    shot_2_flag = False
    enemy_2_flag = False
    enemy_3_flag = False
    enemy_4_flag = False
    enemy_5_flag = False

    pygame.mixer.music.load('sound/game-sound.ogg')
    pygame.mixer.music.play(-1)

    kill_sound = pygame.mixer.Sound('sound/death-ship.ogg')
    channel_0 = pygame.mixer.Channel(0)
    death_sound = pygame.mixer.Sound('sound/death-sound.ogg')
    channel_1 = pygame.mixer.Channel(1)
    hp_loss = pygame.mixer.Sound('sound/healt-loss.ogg')
    channel_2 = pygame.mixer.Channel(2)
    shoot_sound = pygame.mixer.Sound('sound/shoot-sound.ogg')
    channel_3 = pygame.mixer.Channel(3)


reset_game()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not game and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_game()
            game = True

        if not two_player and event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
            reset_game()
            two_player = True

        if not pause and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = True
            pygame.mixer.music.pause()
        elif pause and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pause = False
            pygame.mixer.music.unpause()

    if game and not pause:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            hero_rect.top -= speed_hero
            if hero_rect.top <= 0:
                hero_rect.top = 0

        if keys[pygame.K_DOWN]:
            hero_rect.bottom += speed_hero
            if hero_rect.bottom >= 525:
                hero_rect.bottom = 525

        if keys[pygame.K_RIGHT]:
            if not shot_flag:
                channel_3.play(shoot_sound)
                shot_rect.centery = hero_rect.centery
            shot_flag = True

        if shot_flag:
            shot_rect.right += speed_shot
            if shot_rect.left >= 1000:
                shot_rect.centerx = hero_rect.right
                shot_flag = False

        if shot_rect.colliderect(enemy_1_rect):

            channel_0.play(kill_sound)

            final_score += 200

            enemy_1_rect.left = 1000
            enemy_1_rect.centery = choice(y_pos)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        elif shot_rect.colliderect(enemy_2_rect):

            channel_0.play(kill_sound)

            final_score += 200

            enemy_2_rect.left = 1000
            enemy_2_rect.centery = choice(y_pos)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        elif shot_rect.colliderect(enemy_3_rect):

            channel_0.play(kill_sound)

            final_score += 200

            enemy_3_rect.left = 1000
            enemy_3_rect.centery = choice(y_pos)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        elif shot_rect.colliderect(enemy_4_rect):

            channel_0.play(kill_sound)

            final_score += 200

            enemy_4_rect.left = 1000
            enemy_4_rect.centery = choice(y_pos)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        elif shot_rect.colliderect(enemy_5_rect):

            channel_0.play(kill_sound)

            final_score += 200

            enemy_5_rect.left = 1000
            enemy_5_rect.centery = choice(y_pos)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        screen.blit(back, (0, 0))
        back.blit(text_surface, text_name_rect)
        screen.blit(hero, hero_rect)
        screen.blit(enemy_1, enemy_1_rect)
        screen.blit(enemy_2, enemy_2_rect)
        screen.blit(enemy_3, enemy_3_rect)
        screen.blit(enemy_4, enemy_4_rect)
        screen.blit(enemy_5, enemy_5_rect)
        if shot_flag:
            screen.blit(shot, shot_rect)

        enemy_1_rect.left -= speed_enemy
        if enemy_1_rect.left <= 800:
            enemy_2_flag = True
        if enemy_2_flag:
            enemy_2_rect.left -= speed_enemy

        if enemy_2_rect.left <= 800:
            enemy_3_flag = True
        if enemy_3_flag:
            enemy_3_rect.left -= speed_enemy

        if enemy_3_rect.left <= 800:
            enemy_4_flag = True
        if enemy_4_flag:
            enemy_4_rect.left -= speed_enemy

        if enemy_4_rect.left <= 800:
            enemy_5_flag = True
        if enemy_5_flag:
            enemy_5_rect.left -= speed_enemy

        if enemy_1_rect.right <= 0 or enemy_1_rect.colliderect(hero_rect):
            enemy_1_rect.left = 1000
            enemy_1_rect.centery = choice(y_pos)
            channel_2.play(hp_loss)
            hp -= 1

        if enemy_2_rect.right <= 0 or enemy_2_rect.colliderect(hero_rect):
            enemy_2_rect.left = 1000
            enemy_2_rect.centery = choice(y_pos)
            channel_2.play(hp_loss)
            hp -= 1

        if enemy_3_rect.right <= 0 or enemy_3_rect.colliderect(hero_rect):
            enemy_3_rect.left = 1000
            enemy_3_rect.centery = choice(y_pos)
            channel_2.play(hp_loss)
            hp -= 1

        if enemy_4_rect.right <= 0 or enemy_4_rect.colliderect(hero_rect):
            enemy_4_rect.left = 1000
            enemy_4_rect.centery = choice(y_pos)
            channel_2.play(hp_loss)
            hp -= 1

        if enemy_5_rect.right <= 0 or enemy_5_rect.colliderect(hero_rect):
            enemy_5_rect.left = 1000
            enemy_5_rect.centery = choice(y_pos)
            channel_2.play(hp_loss)
            hp -= 1

        if hp == 0:
            channel_1.play(death_sound)
            pygame.mixer.music.pause()
            text_ts_text = text_ts_font.render(f'Total point: {final_score}', False, 'White')
            text_ts_rect = text_ts_text.get_rect(center=(500, 300))

            screen.blit(text_ts_text, text_ts_rect)

            pygame.display.flip()

            time.sleep(3)

            game = False

        display_score(final_score)

        if hp == 3:
            screen.blit(heart, heart_rect)
        elif hp == 2:
            screen.blit(heart_1, heart_1_rect)
        elif hp == 1:
            screen.blit(heart_2, heart_2_rect)

    elif two_player and not pause:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            hero_rect.top -= speed_hero
            if hero_rect.top <= 0:
                hero_rect.top = 0

        if keys[pygame.K_s]:
            hero_rect.bottom += speed_hero
            if hero_rect.bottom >= 525:
                hero_rect.bottom = 525

        if keys[pygame.K_d]:
            if not shot_flag:
                channel_3.play(shoot_sound)
                shot_rect.centery = hero_rect.centery
            shot_flag = True

        if shot_flag:
            shot_rect.right += speed_shot
            if shot_rect.left >= 1000:
                shot_rect.centerx = hero_rect.right
                shot_flag = False

        if keys[pygame.K_UP]:
            hero_2_rect.top -= speed_hero
            if hero_2_rect.top <= 0:
                hero_2_rect.top = 0

        if keys[pygame.K_DOWN]:
            hero_2_rect.bottom += speed_hero
            if hero_2_rect.bottom >= 525:
                hero_2_rect.bottom = 525

        if keys[pygame.K_LEFT]:
            if not shot_2_flag:
                channel_3.play(shoot_sound)
                shot_2_rect.centery = hero_2_rect.centery
            shot_2_flag = True

        if shot_2_flag:
            shot_2_rect.right -= speed_shot
            if shot_2_rect.left <= 0:
                shot_2_rect.centerx = hero_2_rect.left
                shot_2_flag = False

        if shot_rect.colliderect(hero_2_rect):

            channel_0.play(kill_sound)

            shot_rect.centerx = hero_rect.right
            shot_flag = False

        if shot_2_rect.colliderect(hero_rect):

            channel_0.play(kill_sound)

            shot_2_rect.centerx = hero_2_rect.left
            shot_2_flag = False

        screen.blit(back, (0, 0))
        back.blit(text_surface, text_name_rect)
        screen.blit(hero, hero_rect)
        screen.blit(hero_2, hero_2_rect)
        if shot_flag:
            screen.blit(shot, shot_rect)
        if shot_2_flag:
            screen.blit(shot_2, shot_2_rect)

    elif (game and pause) or (two_player and pause):
        screen.blit(pause_text, pause_text_rect)

    else:
        screen.blit(back_start, (0, 0))
        screen.blit(text_newgame_1, text_newgame_rect1)
        screen.blit(text_newgame_2, text_newgame_rect2)
        pygame.mixer.music.unpause()

    pygame.display.update()
    clock.tick(fps)
