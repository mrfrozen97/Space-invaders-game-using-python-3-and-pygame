import pygame
import sys
import random
import time
#import pandas as pd

pygame.init()

screen_size = (1400,800)
game_over = False
rect_color = (250,0,0)
rect_width = 40
rect_height = 40
rect_position = [500, 700]
rec_movement = 50
enemy_count = 10
enemy_size = [30,30]
enemy_color = [0,0,200]
enemy_position = [random.randint(0,screen_size[1]-enemy_size[1]),0]
enemy_speed = 10
score = 0
kills = 0
fps = 15
flag1 = 0
flag2 = 0

enemy_color_list = [[0,0,200], [200,0,0], [0,200,0], [230,101,166]]

golden_enemy_size = [50,50]
golden_enemy_position = []
golden_enemy_color = (255,205,42)

bullet_size = [3,10]
bullet_position = []
bullet_color = [250, 150,0]
bullet_speed = 10
bullet_color_list = [[250, 150,0], [0,0,200], [200,0,0], [0,200,0], [230,101,166]]

start_button_color = [200, 10, 50]
start_button_position = [550, 400]
start_button_size = [300,50]
start_button_image = "button.png"

quit_button_color = [0,10,250]
quit_button_position = [555, 500]
quit_button_size = [280, 50]
quit_button_image = "button1.png"

flag_gun = 0
enemies_position = [enemy_position]
font = pygame.font.SysFont("monospace", 50)


enemy_img_list = ["ship1.png", "ship2.png", "ship3.png", "ship4.png", "ship5.png", "ship6.png", "ship7.png"]
enemy_imgt = "ship1.png"
enemy_img = pygame.image.load(enemy_imgt)
enemy_img = pygame.transform.scale(enemy_img, (30, 30))

background_option = "button3.png"

flag3 =0


option_back = "button3.png"
right_button = "right.png"
left_button = "left.png"

image_list = ["space1.jpg", "space2.jpg", "space3.jpg", "space4.jpg", "space5.jpg", "space6.jpg", "space7.jpg"]
player_list = ["ship1.png", "ship2.png", "ship3.png", "ship4.png", "ship5.png", "ship6.png", "ship7.png"]
temp_image = "space1.jpg"
player_image = "ship1.png"








def options_display(pos, flag3, temp_image, image_listm, enemy_imgt, bullet_color, player_image):
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.QUIT:
            sys.exit()

    if (pos[0] > 1180 and pos[0] < 1350) and (pos[1] > 670 and pos[1] < 723) and (event.type == pygame.MOUSEBUTTONUP):
        flag3 = 0


    if (pos[0] > 965 and pos[0] < 1036) and (pos[1] > 274 and pos[1] < 330) and (event.type == pygame.MOUSEBUTTONUP):
        temp = image_list.index(temp_image)
        if temp+1 >= len(image_list):
            temp_image = image_list[0]
        else:
            temp_image = image_list[temp + 1]

    if (pos[0] > 165 and pos[0] < 227) and (pos[1] > 274 and pos[1] < 330) and (event.type == pygame.MOUSEBUTTONUP):
        temp = image_list.index(temp_image)
        if temp == 0:
            temp_image = image_list[-1]
        else:
            temp_image = image_list[temp - 1]



    if (pos[0] > 407 and pos[0] < 440) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp1 = enemy_img_list.index(enemy_imgt)
        if temp1+1 >= len(enemy_img_list):
            enemy_imgt = enemy_img_list[0]
        else:
            enemy_imgt = enemy_img_list[temp1 + 1]

    if (pos[0] > 114 and pos[0] < 147) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp1 = enemy_img_list.index(enemy_imgt)
        if temp1 == 0:
            enemy_imgt = enemy_img_list[-1]
        else:
            enemy_imgt = enemy_img_list[temp1 - 1]


    if (pos[0] > 708 and pos[0] < 738) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp2 = bullet_color_list.index(bullet_color)
        if temp2+1 >= len(bullet_color_list):
            bullet_color = bullet_color_list[0]
        else:
            bullet_color = bullet_color_list[temp2 + 1]

    if (pos[0] > 535 and pos[0] < 574) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp2 = bullet_color_list.index(bullet_color)
        if temp2 == 0:
            bullet_color = bullet_color_list[-1]
        else:
            bullet_color = bullet_color_list[temp2 - 1]


    if (pos[0] > 1058 and pos[0] < 1093) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp3 = player_list.index(player_image)
        if temp3+1 >= len(player_list):
            player_image = player_list[0]
        else:
            player_image = player_list[temp3 + 1]

    if (pos[0] > 807 and pos[0] < 842) and (pos[1] > 660 and pos[1] < 690) and (event.type == pygame.MOUSEBUTTONUP):
        temp3 = player_list.index(player_image)
        if temp3 == 0:
            player_image = player_list[-1]
        else:
            player_image = player_list[temp3 - 1]




    return flag3, temp_image, enemy_imgt, bullet_color, player_image







def home_button(pos, flag3, start_button_image, quit_button_image, background_option):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
            flag3 = 1

    if event.type == pygame.QUIT:
        sys.exit()

    if event.type == pygame.MOUSEBUTTONUP and ((pos[0] > 550 and pos[0] < 850) and (pos[1] > 400 and pos[1] < 450)):
        flag3 = 1

    if (pos[0] > 550 and pos[0] < 850) and (pos[1] > 400 and pos[1] < 450):
        start_button_image = "button1.png"
    else:
        start_button_image = "button.png"

    if (pos[0] > 555 and pos[0] < 835) and (pos[1] > 500 and pos[1] < 550) and (event.type == pygame.MOUSEBUTTONUP):
        flag3 = -1

    if (pos[0] > 555 and pos[0] < 835) and (pos[1] > 500 and pos[1] < 550):
        quit_button_image = "button.png"
    else:
        quit_button_image = "button1.png"

    if (pos[0] > 550 and pos[0] < 825) and (pos[1] > 620 and pos[1] < 710) and (event.type == pygame.MOUSEBUTTONUP):
        flag3 = 3

    if (pos[0] > 550 and pos[0] < 825) and (pos[1] > 620 and pos[1] < 710):
        background_option = "button.png"
    else:
        background_option = "button3.png"

    print(pos)
    return flag3, start_button_image, quit_button_image, background_option



def shoot_bullet():
    bullet_position.append([rect_position[0] + 25, rect_position[1]])

def shoot_bullet_2():
    bullet_position.append([rect_position[0] + 45, rect_position[1]-10])
    bullet_position.append([rect_position[0] + 5, rect_position[1]-10])

def display_bullet():
    for i in bullet_position:
        pygame.draw.rect(screen, bullet_color, (i[0], i[1], bullet_size[0], bullet_size[1]))

def move_bullet():
    for i in bullet_position:
        if i[1] >= 10:
              i[1] = i[1] - bullet_speed
        else:
            bullet_position.pop(bullet_position.index(i))






def kill_enemies(kills, flag2):
    for i in bullet_position:
        for j in enemies_position:
            if ((i[0] >= j[0] and i[0] < (j[0] + enemy_size[0])) and (i[1] < j[1])):
                enemies_position.pop(enemies_position.index(j))
                kills+=1
        for j in golden_enemy_position:
            if ((i[0]>=j[0] and i[0]<(j[0] + golden_enemy_size[0]))and (i[1]<j[1])):
                golden_enemy_position.pop(golden_enemy_position.index(j))
                flag2 = 1
    return kills, flag2

def drop_enemies(fps, enemy_count):
    delay = random.random()
    if delay <= 0.02:
        fps = fps +1
        if delay <= 0.01:
            enemy_count = enemy_count + 1

    if len(enemies_position) <enemy_count and delay<=0.1:
        x_pos = random.randint(0,screen_size[0])
        y_pos = 0
        enemies_position.append([x_pos,y_pos])

    return fps, enemy_count


def draw_enemies(img_img):
    for i in enemies_position:
       # pygame.draw.rect(screen, enemy_color, (i[0], i[1], enemy_size[0], enemy_size[1]))
        screen.blit(img_img, (i[0], i[1]))

    for i in golden_enemy_position:
        pygame.draw.rect(screen, golden_enemy_color, (i[0], i[1], golden_enemy_size[0], golden_enemy_size[1]))



def fall_enemies(score, flag2):
    for i in enemies_position:
        if i[1] >= 0 and i[1] <= screen_size[1]:
            i[1] += enemy_speed
        else:
            score+=1
          #  print(score)
            enemies_position.pop(enemies_position.index(i))
    for i in golden_enemy_position:
        flag2 = 0
        golden_enemy_position[0][1]+=enemy_speed
    return score, flag2





def detect_collision(i):
    p_x = rect_position[0]
    p_y = rect_position[1]

    e_x = i[0]
    e_y = i[1]

    if (e_x >= p_x and e_x < (p_x+rect_width)) or (p_x >= e_x and p_x < (e_x+enemy_size[0])):
        if (e_y+enemy_size[1] >= p_y and e_y <= p_y+rect_height):
            return True
    return False

def detect_collisions():
    for i in enemies_position:
        value = detect_collision(i)
        if value == True:
            return True
    return False

no_quit = True

while no_quit:
    flag3 = 0
    screen = pygame.display.set_mode(screen_size)
    golden_enemy_position = []
    clock = pygame.time.Clock()
    enemies_position = []
    enemy_speed = 10
    score = 0
    kills = 0
    fps = 15
    flag_gun =0
    enemy_count =10

    while flag3 == 0 or flag3 == 3 and no_quit:

        for event in pygame.event.get():
            bgimage1 = pygame.image.load("home.jpg")
            bgimage1 = pygame.transform.scale(bgimage1, (1400, 800))
            screen.blit(bgimage1, (0, 0))
            pos = pygame.mouse.get_pos()
            #       pygame.draw.rect(screen, start_button_color, (start_button_position[0], start_button_position[1], start_button_size[0], start_button_size[1]))
            #      pygame.draw.rect(screen, quit_button_color, (
            #     quit_button_position[0], quit_button_position[1], quit_button_size[0], quit_button_size[1]))
            if event.type == pygame.QUIT:
                no_quit = False
                sys.exit()

            if flag3 == 3:

                print(pos)
                flag3, temp_image, enemy_imgt, bullet_color, player_image = options_display(pos, flag3, temp_image,
                                                                                             image_list, enemy_imgt,
                                                                                             bullet_color, player_image)

                bgimagee = pygame.image.load(option_back)  # .convert_alpha()
                bgimagee = pygame.transform.scale(bgimagee, (start_button_size[0] - 70, start_button_size[1] + 40))
                screen.blit(bgimagee, (start_button_position[0] + 600, start_button_position[1] + 250))

                text = "Back"
                label = font.render(text, 1, (0, 0, 0))
                screen.blit(label, (screen_size[0] - 190, screen_size[1] - 123))

                rightim = pygame.image.load(right_button)  # .convert_alpha()
                rightim = pygame.transform.scale(rightim, (100, 100))
                screen.blit(rightim, (start_button_position[0] + 400, start_button_position[1] - 150))

                leftim = pygame.image.load(left_button)  # .convert_alpha()
                leftim = pygame.transform.scale(leftim, (100, 100))
                screen.blit(leftim, (start_button_position[0] - 400, start_button_position[1] - 150))

                show_image = pygame.image.load(temp_image)  # .convert_alpha()
                show_image = pygame.transform.scale(show_image, (600, 400))
                screen.blit(show_image, (start_button_position[0] - 250, start_button_position[1] - 300))

                rightim = pygame.image.load(right_button)  # .convert_alpha()
                rightim = pygame.transform.scale(rightim, (50, 50))
                screen.blit(rightim, (start_button_position[0] - 150, start_button_position[1] + 250))

                leftim = pygame.image.load(left_button)  # .convert_alpha()
                leftim = pygame.transform.scale(leftim, (50, 50))
                screen.blit(leftim, (start_button_position[0] - 445, start_button_position[1] + 250))

                rightim = pygame.image.load(right_button)  # .convert_alpha()
                rightim = pygame.transform.scale(rightim, (50, 50))
                screen.blit(rightim, (start_button_position[0] + 150, start_button_position[1] + 250))

                leftim = pygame.image.load(left_button)  # .convert_alpha()
                leftim = pygame.transform.scale(leftim, (50, 50))
                screen.blit(leftim, (start_button_position[0] - 20, start_button_position[1] + 250))

                pygame.draw.rect(screen, bullet_color,(start_button_position[0] + 80, start_button_position[1] + 240, 21, 70))

                enmimg = pygame.image.load(enemy_imgt) #.convert_alpha()
                enmimg = pygame.transform.scale(enmimg, (100, 100))
                screen.blit(enmimg, (start_button_position[0] -320, start_button_position[1] + 226))


                rightim = pygame.image.load(right_button)  # .convert_alpha()
                rightim = pygame.transform.scale(rightim, (50, 50))
                screen.blit(rightim, (start_button_position[0] + 500, start_button_position[1] + 250))

                leftim = pygame.image.load(left_button)  # .convert_alpha()
                leftim = pygame.transform.scale(leftim, (50, 50))
                screen.blit(leftim, (start_button_position[0] + 250, start_button_position[1] + 250))

                show_image1 = pygame.image.load(player_image)  # .convert_alpha()
                show_image1 = pygame.transform.scale(show_image1, (150, 150))
                screen.blit(show_image1, (start_button_position[0] + 325, start_button_position[1] + 200))

              #  pygame.draw.rect(screen, enemy_color,
               #                  (start_button_position[0] - 320, start_button_position[1] + 226, 100, 100))




            else:
                bgimages = pygame.image.load(start_button_image)  # .convert_alpha()
                bgimages = pygame.transform.scale(bgimages, (start_button_size[0] + 55, start_button_size[1] + 40))
                screen.blit(bgimages, (start_button_position[0] - 30, start_button_position[1] - 20))

                bgimageq = pygame.image.load(quit_button_image)  # .convert_alpha()
                bgimageq = pygame.transform.scale(bgimageq, (quit_button_size[0] + 55, quit_button_size[1] + 50))
                screen.blit(bgimageq, (quit_button_position[0] - 30, quit_button_position[1] - 20))

                bgimageb = pygame.image.load(background_option)  # .convert_alpha()
                bgimageb = pygame.transform.scale(bgimageb, (quit_button_size[0] + 55, quit_button_size[1] + 80))
                screen.blit(bgimageb, (quit_button_position[0] - 30, quit_button_position[1] + 100))

                text = "Start Game "
                font = pygame.font.SysFont("italic bold", 60)
                label = font.render(text, 100, (255, 255, 0))
                # pygame.font.SysFont(text, (10), "bold italic")
                screen.blit(label, (screen_size[0] - 820, screen_size[1] - 395))

                text3 = "Settings"
                label = font.render(text3, 1, (255, 240, 53))
                screen.blit(label, (screen_size[0] - 800, screen_size[1] - 155))

                flag3, start_button_image, quit_button_image, background_option = home_button(pos, flag3,
                                                                                              start_button_image,
                                                                                              quit_button_image,
                                                                                              background_option)

                text1 = "Quit Game "
                label = font.render(text1, 1, (0, 255, 250))
                screen.blit(label, (screen_size[0] - 820, screen_size[1] - 290))

            pygame.display.update()

    charImage = pygame.image.load(player_image)
    bgimage = pygame.image.load(temp_image)
    bgimage = pygame.transform.scale(bgimage, (1400, 800))
    enemy_img = pygame.image.load(enemy_imgt)
    enemy_img = pygame.transform.scale(enemy_img, (30, 30))
    enemy_img = pygame.transform.rotate(enemy_img, 180)

    if flag3 == -1:
        pygame.quit()
    game_over = False
    while not game_over and flag3 != -1 and no_quit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                no_quit = False
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    rect_position[0] = rect_position[0] - rec_movement
                    pass

                elif event.key == pygame.K_RIGHT:
                    rect_position[0] = rect_position[0] + rec_movement
                    pass

                elif event.key == pygame.K_SPACE:
                    if (flag_gun == 0):
                        shoot_bullet()
                    elif (flag_gun  == 1):
                        shoot_bullet_2()

                    pass

        #    bgimage = pygame.image.load("space7.jpg")
        #   bgimage = pygame.transform.scale(bgimage, (1400, 800))
        #  screen.blit(bgimage,(0,0))
        #  screen.fill((0,0,0))
        screen.blit(bgimage, (0, 0))

        if (detect_collisions()):
            game_over = True

        if (score > 20 and flag1 == 0):
            pos = random.randint(0, screen_size[0])
            golden_enemy_position.append([pos, 0])
            flag1 = 1

        #  charImage = pygame.image.load("ship1.png").convert_alpha()

        # charImage = pygame.image.load("ship7.png")#.convert_alpha()
        # charImage.set_alpha(200)
        if (score>100):
            flag_gun = 1
        charImage = pygame.transform.scale(charImage, (70, 70))
        screen.blit(charImage, (rect_position[0] - 10, rect_position[1] - 10))

        text = "Score: " + str(score)
        label = font.render(text, 1, (255, 255, 0))
        screen.blit(label, (screen_size[0] - 400, screen_size[1] - 120))

        text1 = "Kills: " + str(kills)
        label = font.render(text1, 1, (255, 150, 0))
        screen.blit(label, (screen_size[0] - 400, screen_size[1] - 50))

        clock.tick(fps)

        display_bullet()
        move_bullet()
        kills, check_gol = kill_enemies(kills, flag2)
        if check_gol == 1:
            score = score + 20

        fps, enemy_count = drop_enemies(fps, enemy_count)
        draw_enemies(enemy_img)
        score, flag2 = fall_enemies(score, flag2)
        # pygame.draw.rect(screen, rect_color, (rect_position[0], rect_position[1], rect_width, rect_height))
        pygame.display.update()

    back_home = True

    while back_home and no_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            screen.blit(bgimage, (0, 0))
            posi = pygame.mouse.get_pos()

            if (((posi[0] > 550 and posi[0] < 845) and (posi[1] > 350 and posi[1] < 450)) and (event.type == pygame.MOUSEBUTTONUP)):
                print("abcdef.....")
                back_home = False



            print(posi)

            if back_home == False:
                break


            bgimages = pygame.image.load(start_button_image)  # .convert_alpha()
            bgimages = pygame.transform.scale(bgimages, (start_button_size[0] + 55, start_button_size[1] + 40))
            screen.blit(bgimages, (start_button_position[0] - 30, start_button_position[1] - 20))

            text3 = "Main Menu"
            label = font.render(text3, 1, (0, 255,255))
            screen.blit(label, (screen_size[0] - 818, screen_size[1] - 397))

            font1 = pygame.font.SysFont("monospace", 100)
            text4 = "Score: " + str(score)
            label = font1.render(text4, 1, (255, 204, 0))
            screen.blit(label, (screen_size[0] - 948, screen_size[1] - 720))

            text5 = "Kills: " + str(kills)
            label = font1.render(text5, 1, (255, 102, 0))
            screen.blit(label, (screen_size[0] - 948, screen_size[1] - 600))

            pygame.display.update()




print("Game over...........")
print("Score = " + str(score))
print("Kills = " + str(kills))






