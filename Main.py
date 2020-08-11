import pygame
import random
import time
from pygame.locals import *
import threading
from queue import Queue
import math as mt
from src.Settings import *
from src.Road import *
from src.Player import *
from src.Bullet import *
from src.Enemy import *
from src.Smoke import *

def create_new_road(road_id,start):
    road_info = Level1[road_id]
    #print(road_info)
    if start == True:
        y = road_info[3] + HEIGHT +5
    else:
        y = road_info[3]  +5
    new_road = Road(road_info[0],road_info[1],road_info[2],y,road_info[4])
    return new_road

def draw_smoke_destroy_enemies(enemy_list,x,y,screen,SCORE):
    smoke_sound = pygame.mixer.Sound('src/spray.wav')
    smoke_sound.set_volume(0.01)
    explosion_sound = pygame.mixer.Sound('src/explosion.wav')
    explosion_sound.set_volume(0.6)
    smoke_list = pygame.sprite.Group()
    explosion = pygame.image.load('src/explosion.png')
    smoke = Smoke('src/smoke.png',x-25,y+80)
    smoke_list.add(smoke)
    for i in [-55,55]:
        smoke = Smoke('src/smoke.png', x + i-25, y + 140)
        smoke_list.add(smoke)
    for i in [-110,0,110]:
        smoke = Smoke('src/smoke.png', x + i-25, y + 190)
        smoke_list.add(smoke)

    for enemies in enemy_list:
        if pygame.sprite.spritecollide(enemies,smoke_list,False):
            enemy_list.remove(enemies)
            screen.blit(explosion, [enemies.rect.x - 35, enemies.rect.y])
            explosion_sound.play()
            for enemies2 in enemy_firing_list:
                if enemies2[0]==enemies:
                    enemy_firing_list.remove(enemies2)
            SCORE += 20
    smoke_sound.play()
    print('hello')
    smoke_list.draw(screen)
    return enemy_list,SCORE
def info_screen(screen):
    bg_image = pygame.image.load('src/bg_info_screen.png')
    road_list = []
    road_list.append(create_new_road(0, True))
    road_list.append(create_new_road(1, False))

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return 1

        for road in road_list:
            if road.get_y() == 0:
                next_road = create_new_road(road.get_next(), False)
                road_list.append(next_road)
            road.update()
            road.draw(screen)

        screen.blit(bg_image, [0, 0])
        clock.tick(60)
        pygame.display.flip()


def start_screen(screen):
    bg_image = pygame.image.load('src/bg_main_screen.png')
    font = pygame.font.Font('src/Pixel.otf', 30)
    road_list = []
    road_list.append(create_new_road(0, True))
    road_list.append(create_new_road(1, False))

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 1
                if event.key == pygame.K_i:
                    return 10

        for road in road_list:
            if road.get_y() == 0:
                next_road = create_new_road(road.get_next(), False)
                road_list.append(next_road)
            road.update()
            road.draw(screen)

        text = font.render("Press Space to Start the Game", True, WHITE)
        screen.blit(text, [290, 460])
        screen.blit(bg_image,[0,0])
        clock.tick(60)
        pygame.display.flip()

def game_over_screen(screen,SCORE):
    time.sleep(1)
    bg_image = pygame.image.load('src/trans_grey.png')
    fail_sound = pygame.mixer.Sound('src/fail.wav')
    fail_sound.set_volume(0.3)
    font = pygame.font.Font('src/Pixel.otf', 50)
    font1 = pygame.font.Font('src/Pixel.otf', 30)
    road_list = []
    road_list.append(create_new_road(0, True))
    road_list.append(create_new_road(1, False))
    fail_sound.play()
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fail_sound.stop()
                return -1
            elif event.type == pygame.KEYDOWN:
                fail_sound.stop()
                return 1

        for road in road_list:
            if road.get_y() == 0:
                next_road = create_new_road(road.get_next(), False)
                road_list.append(next_road)
            road.update()
            road.draw(screen)
        screen.blit(bg_image, [0, 0])

        text = font.render(" YOU    LOST ", True, WHITE)
        screen.blit(text, [420, 260])
        text = font.render("Score:  " + str(SCORE), True, WHITE)
        screen.blit(text, [425, 360])
        text = font1.render("Press any key to return to the Menu", True, WHITE)
        screen.blit(text, [225, 460])

        clock.tick(60)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("My Game")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    '''road_list = []
    road_list.append(create_new_road(0,True))
    road_list.append(create_new_road(1,False))

    player_list = pygame.sprite.Group()
    player = Player('player.png',500,600)
    player_list.add(player)

    bullet_list = pygame.sprite.Group()
    enemy_bullet_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()
    enemy_firing_list = []
    rect = road_list[1].get_y_line(0)
    #print(rect)
    if rect:
        enemy = Enemy('src/enemy.png',rect,' ',20)
    enemy_list.add(enemy)'''
    explosion_sound = pygame.mixer.Sound('src/explosion.wav')
    explosion_sound.set_volume(0.6)
    laser_player_sound = pygame.mixer.Sound('src/laser.wav')
    laser_player_sound.set_volume(0.1)
    laser_enemy_sound = pygame.mixer.Sound('src/laser1.wav')
    laser_enemy_sound.set_volume(0.1)
    bg_sound = pygame.mixer.Sound('src/main_song.wav')
    clock = pygame.time.Clock()
    done = False
    font = pygame.font.Font('src/Pixel.otf', 20)
    explosion = pygame.image.load('src/explosion.png')
    start = True
    game_over = False
    choice = 0
    while not done:
        #start_screen(screen)
        # --- Main event loop
        if start:
            bg_sound.play()
            choice = start_screen(screen)
            if choice == -1:
                done = True
            elif choice == 1:
                health = 20
                SCORE = 0
                pygame.time.set_timer(USEREVENT + 1, 1000)
                pygame.time.set_timer(USEREVENT + 2, 200)
                pygame.time.set_timer(USEREVENT + 3, 500)
                road_list = []
                road_list.append(create_new_road(0, True))
                road_list.append(create_new_road(1, False))

                player_list = pygame.sprite.Group()
                player = Player('src/player.png', 500, 600)
                player_list.add(player)

                bullet_list = pygame.sprite.Group()
                enemy_bullet_list = pygame.sprite.Group()
                enemy_list = pygame.sprite.Group()
                enemy_firing_list = []
                rect = road_list[1].get_y_line(0)
                # print(rect)
                if rect:
                    enemy = Enemy('src/enemy.png', rect, 'top', 20)
                enemy_list.add(enemy)

            start = False
        elif game_over:
            bg_sound.stop()
            choice = game_over_screen(screen,SCORE)
            game_over = False
            if choice == -1:
                done = True
            else:
                start = True
                choice = 0

        if choice == 1:
            #screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.player_movement(-5, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.player_movement(5, 0)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.player_movement(0, -5)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.player_movement(0, 7)
                    if event.key == pygame.K_SPACE:
                        Bullets = player.fire_lasers()
                        laser_player_sound.play()
                        if Bullets:
                            for Bullet in Bullets:
                                bullet_list.add(Bullet)


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.player_movement(5, 0)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        player.player_movement(-5, 0)
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.player_movement(0, 5)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.player_movement(0, -7)
                if event.type == USEREVENT+1:
                    for enemies in enemy_list:
                        if enemies.get_hunt() == True:
                            enemy_firing_list.append([enemies,0])
                if event.type == USEREVENT+2:
                    if player.check_isalive():
                        for enemies in enemy_firing_list:
                            if enemies[1]<3:
                                enemies[1] += 1
                                bullet = enemies[0].enemy_fire(player.get_x())
                                laser_enemy_sound.play()
                                enemy_bullet_list.add(bullet)
                            else:
                                enemy_firing_list.remove(enemies)
                if event.type == USEREVENT+3:
                    SCORE += 5



            hit_list = []
            for road in road_list:
                if road.get_y() == 0:
                    next_road = create_new_road(road.get_next(),False)
                    spawn = False
                    for i in Enemy_spawn:
                        if i[0] == road.get_next():
                            spawn = True
                            break
                    if spawn :
                        rect = next_road.get_y_line(-30)

                        if rect:
                            enemy = Enemy('src/enemy.png', rect,i[1],i[2])
                        enemy_list.add(enemy)

                    road_list.append(next_road)
                road.update()
                road.draw(screen)
                hit_list.append( road.check_collide(player_list,True))
                if road.get_y() > 2 * HEIGHT:
                    #print('deleted')
                    road_list.remove(road)


            in_road = False
            #print(hit_list)
            for inroad in hit_list:
                #print(inroad)
                if len(inroad) > 0:
                    in_road = True
            if not in_road:
                player_list.remove(player)
                screen.blit(explosion, [player.rect.x - 35, player.rect.y])
                explosion_sound.play()
                health = 0
                game_over = True
                player.lost()
            for bullet in bullet_list:
                hit_list = pygame.sprite.spritecollide(bullet,enemy_list,False)
                for item in hit_list:
                    enemy_list.remove(item)
                    screen.blit(explosion,[item.rect.x-35,item.rect.y])
                    explosion_sound.play()
                    for enemies in enemy_firing_list:
                        if enemies[0] == item:
                            enemy_firing_list.remove(enemies)
                    SCORE += 40
                    bullet_list.remove(bullet)

            for bullet in enemy_bullet_list:
                hit_list = pygame.sprite.spritecollide(bullet, enemy_list, False)
                for item in hit_list:
                    enemy_list.remove(item)
                    screen.blit(explosion, [item.rect.x - 35, item.rect.y])
                    explosion_sound.play()
                    for enemies in enemy_firing_list:
                        if enemies[0] == item:
                            enemy_firing_list.remove(enemies)
                    SCORE += 40
                    enemy_bullet_list.remove(bullet)


            if  player.check_isalive():
                hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
                for item in hit_list:
                    enemy_list.remove(item)
                    screen.blit(explosion,[item.rect.x-35,item.rect.y])
                    explosion_sound.play()
                    for enemies in enemy_firing_list:
                        if enemies[0] == item:
                            enemy_firing_list.remove(enemies)
                    health = 0
                    game_over = True
                    player_list.remove(player)
                    screen.blit(explosion, [player.rect.x - 35, player.rect.y])
                    explosion_sound.play()
                for enemies in enemy_list:
                    if enemies.get_y() > player.get_y() - 150 and enemies.get_y() < player.get_y() + 150:
                        enemies.hunt_player(True,player.get_y())
                    else:
                        enemies.hunt_player(False, player.get_y())

                hit_list = pygame.sprite.spritecollide(player,enemy_bullet_list,False)
                for item in hit_list:
                    enemy_bullet_list.remove(item)
                    health -= 1

                    if health < 1:
                        player_list.remove(player)
                        screen.blit(explosion, [player.rect.x - 35, player.rect.y])
                        explosion_sound.play()
                        player.lost()
                        game_over = True

                keys = pygame.key.get_pressed()
                if keys[pygame.K_n]:

                    x = player.get_x()
                    y = player.get_y()
                    enemy_list,SCORE = draw_smoke_destroy_enemies(enemy_list,x,y,screen,SCORE)


            player_list.update()
            player_list.draw(screen)

            bullet_list.update()
            bullet_list.draw(screen)

            enemy_bullet_list.update()
            enemy_bullet_list.draw(screen)

            for enemies in enemy_list:
                enemy_in_road = False
                temp_list = pygame.sprite.Group()
                temp_list.add(enemies)
                for street in road_list:
                    if street.get_y() <=enemies.get_y() and street.get_y() + HEIGHT >= enemies.get_y():
                        #print(street.get_next())
                        enemies.update(street)
            text2 = font.render("Score:   " + str(SCORE), True, WHITE)
            screen.blit(text2, [850, 0])


            #print(enemy_list)

            enemy_list.draw(screen)
        elif choice == 10:
            choice = info_screen(screen)
            if choice == -1:
                done = True
            else:
                start = True
                choice = 0


        clock.tick(60)
        pygame.display.flip()
