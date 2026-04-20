import pygame
from gpiozero import Button
from gpiozero import LED

pygame.init()

#wall positions for lvl1
walls_one = [(0, 0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0), (600, 0), (700, 0), (800, 0), (900, 0), (1000, 0), (1100, 0), (1200, 0), 
            (1300, 0), (1400, 0), (1500, 0), 
            (0, 100), (100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100), (800, 100), (900, 100), (1000, 100), 
            (1100, 100), (1200, 100), (1300, 100), (1400, 100), (1500, 100),
            (0, 200), (100, 200), (200, 200), (300, 200), (400, 200), (500, 200), (600, 200), (700, 200), (1500, 200),
            (0, 300), (100, 300), (200, 300), (300, 300), (400, 300), (500, 300), (600, 300), (700, 300), (900, 300), (1000, 300), (1100, 300),
            (1200, 300), (1300, 300), (1400, 300), (1500, 300),
            (0, 400), (100, 400), (200, 400), (300, 400), (400, 400), (500, 400), (600, 400), (700, 400), (900, 400), (1000, 400), (1100, 400), 
            (1200, 400), (1300, 400), (1400, 400), (1500, 400),
            (0, 500), (100, 500), (200, 500), (300, 500), (400, 500), (500, 500), (600, 500), (700, 500), (900, 500), (1000, 500), (1100, 500),
            (1200, 500), (1300, 500), (1400, 500), (1500, 500),
            (-100, 600), (900, 600), (1000, 600), (1100, 600), (1200, 600), (1300, 600), (1400, 600), (1500, 600),
            (0, 700), (100, 700), (200, 700), (300, 700), (400, 700), (500, 700), (600, 700), (700, 700), (800, 700), (900, 700), (1000, 700), 
            (1100, 700), (1200, 700), (1300, 700), (1400, 700), (1500, 700),
            (0, 800), (100, 800), (200, 800), (300, 800), (400, 800), (500, 800), (600, 800), (700, 800), (800, 800), (900, 800), (1000, 800), 
            (1100, 800), (1200, 800), (1300, 800), (1400, 800), (1500, 800)]

#wall positions for lvl2
walls_two = [(0, 0), (70, 0), (140, 0), (210, 0), (280, 0), (350, 0), (420, 0), (490, 0), (560, 0), (630, 0), (700, 0), (770, 0), (840, 0), (910, 0), 
            (980, 0), (1050, 0), (1120, 0), (1190, 0), (1260, 0), (1330, 0), (1400, 0), (1470, 0),
            (0, 70), (70, 70), (140, 70), (1400, 70), (1470, 70),
            (0, 140), (70, 140), (140, 140), (280, 140), (350, 140), (420, 140), (490, 140), (560, 140), (630, 140), (700, 140), (770, 140), (840, 140), (910, 140), (980, 140), (1050, 140), (1120, 140), (1190, 140), (1260, 140), (1400, 140), (1470, 140),
            (0, 210), (70, 210), (140, 210), (280, 210), (350, 210), (420, 210), (490, 210), (560, 210), (630, 210), (700, 210), (840, 210), (910, 210), (1400, 210), (1470, 210),
            (0, 280), (70, 280), (140, 280), (280, 280), (350, 280), (420, 280), (490, 280), (560, 280), (630, 280), (700, 280), (840, 280), (910, 280), (1050, 280), (1120, 280), (1190, 280), (1260, 280), (1330, 280), (1400, 280), (1470, 280),
            (0, 350), (70, 350), (140, 350), (560, 350), (630, 350), (700, 350), (840, 350), (910, 350), (980, 350), (1050, 350), (1120, 350), (1470, 350),
            (0, 420), (70, 420), (140, 420), (210, 420), (280, 420), (350, 420), (420, 420), (560, 420), (630, 420), (700, 420), (1050, 420), (1120, 420), (1260, 420), (1330, 420), (1400, 420), (1470, 420),
            (0, 490), (70, 490), (140, 490), (210, 490), (280, 490), (350, 490), (420, 490), (700, 490), (840, 490), (1050, 490), (1120, 490), (1260, 490), (1330, 490), (1400, 490), (1470, 490),
            (0, 560), (70, 560), (140, 560), (210, 560), (280, 560), (350, 560), (420, 560), (560, 560), (630, 560), (700, 560), (840, 560), (980, 560), (1050, 560), (1260, 560), (1330, 560), (1400, 560), (1470, 560),
            (0, 630), (560, 630), (630, 630), (700, 630), (840, 630), (910, 630), (980, 630), (1190, 630), (1260, 630), (1330, 630), (1400, 630), (1470, 630),
            (0, 700), (140, 700), (210, 700), (280, 700), (350, 700), (420, 700), (1120, 700), (1190, 700), (1260, 700), (1330, 700), (1400, 700), (1470, 700),
            (0, 770), (70, 770), (140, 770), (210, 770), (280, 770), (350, 770), (420, 770), (490, 770), (560, 770), (630, 770), (770, 770), (840, 770), (910, 770), (980, 770), (1050, 770), (1120, 770), (1190, 770), (1260, 770), (1330, 770), (1400, 770), (1470, 770),
            (0, 840), (70, 840), (140, 840), (210, 840), (280, 840), (350, 840), (420, 840), (490, 840), (560, 840), (630, 840), (770, 840), (840, 840), (910, 840), (980, 840), (1050, 840), (1120, 840), (1190, 840), (1260, 840), (1330, 840), (1400, 840), (1470, 840),
            (700, 864)]

door_button = Button(4)
inventory_button = Button(17)
inv_button_pressed = False
pickup_button = Button(27)
red_button = Button(5)
green_button = Button(6)
blue_button = Button(13)
red_led = LED(18)
green_led = LED(23)
blue_led = LED(24)

def lvl_one(wall_pos):
    #creating a full screen display

    screen = pygame.display.set_mode((1536, 864))

    #font and size of text
    font_one = pygame.font.Font(None, 70)
    font_two = pygame.font.SysFont("verdana", 30)

    #loading image of player
    player_image = pygame.image.load("tuxedo_cat.png")
    #resizing image, right side facing player
    player_right_image = pygame.transform.scale(player_image, (53, 40))
    #left side facing player
    player_left_image = pygame.transform.flip(player_right_image, True, False)
    current_image = player_right_image

    #creating rectangle same size as player
    player_rect = player_right_image.get_rect(topleft = (25, 640))

    #loading image of wall
    wall = pygame.image.load("wall.png")
    wall = pygame.transform.scale(wall, (100, 100))

    #loading heart
    heart = pygame.image.load("heart.png")
    heart = pygame.transform.scale(heart, (50, 50))
    #creating rectangle for treat
    heart_rect_one = heart.get_rect(topleft = (30,800))
    heart_rect_two = heart.get_rect(topleft = (90,800))
    heart_rect_three = heart.get_rect(topleft = (150,800))

    #text displayed on lvl1, colour white
    wasd_one = font_one.render("USE WASD OR THE ARROWS", True, (255, 255, 255))
    wasd_two = font_one.render("TO MOVE", True, (255, 255, 255))
    enter_one = font_one.render("PRESS THE TOP RED", True, (255, 255, 255))
    enter_two = font_one.render("BUTTON TO GO", True, (255, 255, 255))
    enter_three = font_one.render("THROUGH THE DOOR", True, (255, 255, 255))
    lives_txt = font_two.render("<-- lives", True, (255, 255, 255))

    #loading image of closed and open door
    closed_door = pygame.image.load("closed_door.png")
    closed_door = pygame.transform.scale(closed_door, (110, 90))
    open_door = pygame.image.load("open_door.png")
    open_door = pygame.transform.scale(open_door, (60, 90))

    #creating rectangle for door
    door_rect = closed_door.get_rect(topleft = (1400, 208))

    #speed of player
    speed = 10

    run = True
    while run:
        #black background
        screen.fill((0, 0, 0))

        #creating rectangles for the walls
        wall_rects = []
        for i in wall_pos:
            wall_rect = wall.get_rect(topleft = i)
            wall_rects.append(wall_rect)
        
        #drawing the walls
        for i in wall_rects:
            screen.blit(wall, i)

        screen.blit(heart, heart_rect_one)
        screen.blit(heart, heart_rect_two)
        screen.blit(heart, heart_rect_three)

        #checks if player is by the door and opens if they are
        if player_rect.colliderect(door_rect):
            door = open_door
        else:
            door = closed_door

        #displaying the appropriate door
        screen.blit(door, door_rect)

        #displays appropriate text based off where player is
        if player_rect.y > 400:
            screen.blit(wasd_one, (50, 320))
            screen.blit(wasd_two, (270, 410))
            screen.blit(lives_txt, (220, 805))
        else:
            screen.blit(enter_one, (970, 420))
            screen.blit(enter_two, (1050, 500))
            screen.blit(enter_three, (970, 580))

        #inserting image of player and player rectangle
        screen.blit(current_image, player_rect)

        #checks which key is pressed and acts accordingly
        key = pygame.key.get_pressed()
        #move left
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            new_rect = player_rect.move(-speed, 0)
            #check if this results in a collision and only moves player if not
            if not any(new_rect.colliderect(i) for i in wall_rects):
                player_rect = new_rect
                current_image = player_left_image
        #move right
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            new_rect = player_rect.move(speed, 0)
            if not any(new_rect.colliderect(i) for i in wall_rects):
                player_rect = new_rect
                current_image = player_right_image
        #move up
        if key[pygame.K_w] or key[pygame.K_UP]:
            new_rect = player_rect.move(0, -speed)
            if not any(new_rect.colliderect(i) for i in wall_rects):
                player_rect = new_rect
        #move_down
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            new_rect = player_rect.move(0, speed)
            if not any(new_rect.colliderect(i) for i in wall_rects):
                player_rect = new_rect


        #if they press the red button after reaching the door it goes to lvl 2
        if door == open_door and door_button.is_pressed:
            run = False
            return "lvl_two"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #updates the display
        pygame.display.flip()

def lvl_two(wall_pos):
    
    pattern_active = False
    last_second = -1
    
    #creating a full screen display
    screen = pygame.display.set_mode((1536, 864))
    
    #font and size of text
    font = pygame.font.Font(None, 70)

    #loading image of player
    player_image = pygame.image.load("tuxedo_cat.png").convert_alpha()
    #resizing image, right side facing player
    player_right_image = pygame.transform.scale(player_image, (46, 35))
    #left side facing player
    player_left_image = pygame.transform.flip(player_right_image, True, False)
    current_image = player_right_image

    #creating rectangle same size as player
    player_rect = player_right_image.get_rect(topleft = (710, 800))

    #loading image of wall
    wall = pygame.image.load("wall.png")
    wall = pygame.transform.scale(wall, (70, 70))
    wall_monitor_bg = pygame.transform.scale(wall, (1000, 570))
    wall_monitor_bg_rect = pygame.Rect(250, 150, 1000, 570)

    #loading image of closed and open door
    closed_door = pygame.image.load("closed_door.png")
    closed_door = pygame.transform.scale(closed_door, (84, 70))
    open_door = pygame.image.load("open_door.png")
    open_door = pygame.transform.scale(open_door, (46, 70))
    #creating rectangle for door
    door_rect = closed_door.get_rect(topleft = (1417, 348))

    #loading sign for security room
    security_room = pygame.image.load("security_room.png")
    security_room = pygame.transform.scale(security_room, (100, 50))

    #loading desk in security room
    desk = pygame.image.load("desk.png")
    desk = pygame.transform.scale(desk, (55, 40))
    #creating rectangle for desk
    desk_rect = desk.get_rect(topleft = (917, 583))

    #loading treat
    treat = pygame.image.load("treat.png")
    treat = pygame.transform.scale(treat, (48, 30))
    #creating rectangle for treat
    treat_rect = treat.get_rect(topleft = (83, 725))

    #loading escape key
    escape_key = pygame.image.load("key.png")
    escape_key = pygame.transform.scale(escape_key, (45, 25))
    #creating rectangle for treat
    escape_key_rect = escape_key.get_rect(topleft = (640, 513))

    #loading led console with colour code on it
    colour_code = pygame.image.load("map_led_console.png")
    colour_code = pygame.transform.scale(colour_code, (80, 50))
    #creating rectangle for led console
    colour_code_rect = colour_code.get_rect(topleft = (975,290))

    #loading heart
    heart = pygame.image.load("heart.png")
    heart = pygame.transform.scale(heart, (50, 50))
    #creating rectangle for treat
    heart_rect_one = heart.get_rect(topleft = (30,800))
    heart_rect_two = heart.get_rect(topleft = (90,800))
    heart_rect_three = heart.get_rect(topleft = (150,800))

    #loading door for security room
    security_door = pygame.image.load("room_door.png")
    security_door = pygame.transform.scale(security_door, (12, 70))
    #creating rectangle for security room door
    security_door_rect = security_door.get_rect(topleft = (875, 420))
    #separate collision rect (to detect if player is interacting with security door)
    collision_rect_door = security_door_rect.copy()
    #expand collision rect to the left
    collision_rect_door.left -= 7
    collision_rect_door.width += 7 

    #loading lasers
    lasers = pygame.image.load("lasers.png")
    lasers = pygame.transform.scale(lasers, (73, 70))
    #creating rectangle for lasers
    lasers_rect = lasers.get_rect(topleft = (1188, 450))
    #separate collision rect (to detect if player is interacting with lasers)
    collision_rect_lasers = lasers_rect.copy()
    #expand collision rect to the left
    collision_rect_lasers.height -= 25
    danger_rect_lasers = lasers_rect.copy()
    danger_rect_lasers.height -= 15
    #lasers that are turned off
    lasers_off = pygame.image.load("lasers_off.png")
    lasers_off = pygame.transform.scale(lasers_off, (73, 70))
    #creating rectangle for lasers that are off
    lasers_off_rect = lasers_off.get_rect(topleft = (1188, 450))

    #loading monitor
    monitor_font = pygame.font.SysFont("consolas", 25)
    monitor = pygame.image.load("monitor.png")
    monitor = pygame.transform.scale(monitor, (700, 490))
    monitor_rect = monitor.get_rect(topleft = (410, 190))
    monitor_txt_one = monitor_font.render("CODE TO DE-ACTIVATE LASERS", True, (255, 255, 255))

    #checking if the colour code is right
    def colour_code_check(computer_input):
        full_code = "".join(computer_input)
        if full_code == "RGRBRG":
            return True
        else:
            return False

    #endgame popup display
    def endgame(end):
        font_big = pygame.font.Font(None, 80)
        font_small = pygame.font.SysFont("timesnewroman", 30)
        endgame_txt_one = font_big.render("YOU DIED :(", True, (255, 0, 0))
        endgame_txt_two = font_small.render("Press ENTER to try again or press ESCAPE to close the game", True, (255, 255, 255))
        endgame_rect = pygame.Rect(325, 140, 880, 550)
        pygame.draw.rect(screen, (0, 0, 100), endgame_rect)
        pygame.draw.rect(screen, (0, 0, 0), endgame_rect, 20)
        screen.blit(endgame_txt_one, (600, 300))
        screen.blit(endgame_txt_two, (400, 500))
        end = True
        return end
    
    #endoftime popup display
    def endtime(end):
        font_big = pygame.font.Font(None, 80)
        font_small = pygame.font.SysFont("timesnewroman", 30)
        endgame_txt_one = font_big.render("YOU RAN OUT OF TIME :(", True, (255, 0, 0))
        endgame_txt_two = font_small.render("Press ENTER to try again or press ESCAPE to close the game", True, (255, 255, 255))
        endgame_rect = pygame.Rect(325, 140, 880, 550)
        pygame.draw.rect(screen, (0, 0, 100), endgame_rect)
        pygame.draw.rect(screen, (0, 0, 0), endgame_rect, 20)
        screen.blit(endgame_txt_one, (425, 300))
        screen.blit(endgame_txt_two, (400, 500))
        end = True
        return end
    
    #popup display when you win
    def win_display(end_win):
        font_big = pygame.font.Font(None, 80)
        font_small = pygame.font.SysFont("timesnewroman", 30)
        endgame_txt_one = font_big.render("YOU WON :)", True, (0, 255, 0))
        endgame_txt_two = font_small.render("Press ESCAPE to close the game", True, (255, 255, 255))
        endgame_rect = pygame.Rect(325, 140, 880, 550)
        pygame.draw.rect(screen, (0, 0, 100), endgame_rect)
        pygame.draw.rect(screen, (0, 0, 0), endgame_rect, 20)
        screen.blit(endgame_txt_one, (605, 300))
        screen.blit(endgame_txt_two, (565, 500))
        end_win = True
        return end_win

    #colour pattern to display
    def colour_pattern(last_second):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - pattern_start_time) // 1000

        if elapsed_time > 11:
            red_led.off()
            green_led.off()
            blue_led.off()
            return last_second, False  # stop pattern

        if elapsed_time != last_second:
            last_second = elapsed_time

            # reset LEDs each step
            red_led.off()
            green_led.off()
            blue_led.off()

            if elapsed_time == 0:
                red_led.on()
            elif elapsed_time == 1:
                green_led.on()
            elif elapsed_time == 2:
                red_led.on()
            elif elapsed_time == 3:
                blue_led.on()
            elif elapsed_time == 4:
                red_led.on()
            elif elapsed_time == 5:
                green_led.on()

        return last_second, True

    # INSTRUCTIONS (text on the side of the screen)
    def main_instructions():
        font = pygame.font.Font(None, 40)
        inventory_access_txt_one = font.render("=>  PRESS THE", True, (255, 255, 255))
        inventory_access_txt_two = font.render("BLUE BUTTON", True, (255, 255, 255))
        inventory_access_txt_three = font.render("TO ACCESS", True, (255, 255, 255))
        inventory_access_txt_four = font.render("YOUR", True, (255, 255, 255))
        inventory_access_txt_five = font.render("INVENTORY", True, (255, 255, 255))
        pickup_instruction_one = font.render("=>  PRESS THE", True, (255, 255, 255))
        pickup_instruction_two = font.render("LOWER RED", True, (255, 255, 255))
        pickup_instruction_three = font.render("BUTTON TO", True, (255, 255, 255))        
        pickup_instruction_four = font.render("PICKUP ITEMS", True, (255, 255, 255))
        screen.blit(inventory_access_txt_one, (1280, 510))
        screen.blit(inventory_access_txt_two, (1328, 545))
        screen.blit(inventory_access_txt_three, (1328, 580))
        screen.blit(inventory_access_txt_four, (1328, 615))
        screen.blit(inventory_access_txt_five, (1328, 650))
        screen.blit(pickup_instruction_one, (1280, 715))
        screen.blit(pickup_instruction_two, (1328, 750))
        screen.blit(pickup_instruction_three, (1328, 785))
        screen.blit(pickup_instruction_four, (1328, 820))
    
    def locked_door_instructions():
        font = pygame.font.Font(None, 60)
        locked_door_txt_one = font.render("THIS DOOR IS", True, (150, 0, 0))
        locked_door_txt_two = font.render("LOCKED", True, (150, 0, 0))
        screen.blit(locked_door_txt_one, (400, 200))
        screen.blit(locked_door_txt_two, (450, 260))
    
    def key_door_instructions():
        font = pygame.font.Font(None, 60)
        key_door_txt_one = font.render("PRESS ENTER TO USE", True, (0, 255, 0))
        key_door_txt_two = font.render("YOUR KEY AND OPEN", True, (0, 255, 0))
        key_door_txt_three = font.render("THE", True, (0, 255, 0))
        key_door_txt_four = font.render("DOOR", True, (0, 255, 0))
        screen.blit(key_door_txt_one, (300, 200))
        screen.blit(key_door_txt_two, (305, 270))
        screen.blit(key_door_txt_three, (625, 335))
        screen.blit(key_door_txt_four, (605, 390))

    def desk_interact_instructions():
        font = pygame.font.Font(None, 60)
        desk_interact_txt_one = font.render("PRESS ENTER TO", True, (0, 0, 255))
        desk_interact_txt_two = font.render("USE THE COMPUTER", True, (0, 0, 255))
        screen.blit(desk_interact_txt_one, (345, 200))
        screen.blit(desk_interact_txt_two, (310, 260))
    
    def inventory_instructions():
        font = pygame.font.Font(None, 40)
        inventory_close_txt_one = font.render("=>  PRESS THE", True, (255, 255, 255))
        inventory_close_txt_two = font.render("BLUE BUTTON", True, (255, 255, 255))
        inventory_close_txt_three = font.render("TO CLOSE", True, (255, 255, 255))
        inventory_close_txt_four = font.render("INVENTORY", True, (255, 255, 255))
        inspect_instruction_one = font.render("=>  PRESS ENTER", True, (255, 255, 255))
        inspect_instruction_two = font.render("TO VIEW ITEM", True, (255, 255, 255))
        move_instruction_one = font.render("=>  USE ARROWS", True, (255, 255, 255))
        move_instruction_two = font.render("TO MOVE", True, (255, 255, 255))
        move_instruction_three = font.render("THROUGH", True, (255, 255, 255))
        move_instruction_four = font.render("ITEMS", True, (255, 255, 255))
        screen.blit(inventory_close_txt_one, (1280, 445))
        screen.blit(inventory_close_txt_two, (1328, 480))
        screen.blit(inventory_close_txt_three, (1328, 515))
        screen.blit(inventory_close_txt_four, (1328, 550))
        screen.blit(inspect_instruction_one, (1280, 615))
        screen.blit(inspect_instruction_two, (1328, 650))
        screen.blit(move_instruction_one, (1280, 715))
        screen.blit(move_instruction_two, (1328, 750))
        screen.blit(move_instruction_three, (1328, 785))
        screen.blit(move_instruction_four, (1328, 820))

    def monitor_instructions():
        font = pygame.font.Font(None, 30)
        rgb_txt_one = font.render("=>   PRESS LED", True, (255, 255, 255))
        rgb_txt_two = font.render("BUTTONS TO ENTER", True, (255, 255, 255))
        rgb_txt_three = font.render("COLOUR CODE", True, (255, 255, 255))
        colour_check_txt_one = font.render("=>   PRESS ENTER TO", True, (255, 255, 255))
        colour_check_txt_two = font.render("CHECK COLOUR", True, (255, 255, 255))
        colour_check_txt_three = font.render("CODE", True, (255, 255, 255))
        escape_txt_one = font.render("=>   PRESS ESCAPE", True, (255, 255, 255))
        escape_txt_two = font.render("TO CLOSE", True, (255, 255, 255))
        screen.blit(rgb_txt_one, (1280, 480))
        screen.blit(rgb_txt_two, (1323, 510))
        screen.blit(rgb_txt_three, (1323, 540))
        screen.blit(colour_check_txt_one, (1280, 600))
        screen.blit(colour_check_txt_two, (1323, 630))
        screen.blit(colour_check_txt_three, (1323, 660))
        screen.blit(escape_txt_one, (1280, 720))
        screen.blit(escape_txt_two, (1323, 750))

    # INVENTORY BOX:

    font = pygame.font.SysFont("timesnewroman", 30)
    small_font = pygame.font.SysFont("timesnewroman", 20)

    #loading inventory box
    inventory_box = pygame.image.load("inventory.png")
    inventory_box = pygame.transform.scale(inventory_box, (1000, 600))
    inventory_box_rect = inventory_box.get_rect(topleft = (250, 100))
    #inventory box 1
    inventory_one = 381
    inventory_one_rect = pygame.Rect(378, 262, 125, 95)
    #inventory box 2
    inventory_two = 535
    inventory_two_rect = pygame.Rect(532, 262, 125, 95)
    #inventory box 3
    inventory_three = 689
    inventory_three_rect = pygame.Rect(686, 262, 125, 95)

    #loading key in inventory box
    key_inventory = pygame.image.load("key.png")
    key_inventory = pygame.transform.scale(key_inventory, (120, 65))
    #loading treat in inventory box
    treat_inventory = pygame.image.load("treat.png")
    treat_inventory = pygame.transform.scale(treat_inventory, (130, 80))
    #loading secret note with colour code in inventory box
    note_inventory = pygame.image.load("map_led_console.png")
    note_inventory = pygame.transform.scale(note_inventory, (160, 100))
    note_x = [362, 517, 670]
    
    # Key Popup
    key_popup = pygame.image.load("key.png")
    key_popup = pygame.transform.scale(key_inventory, (240, 130))
    key_popup_rect = key_popup.get_rect(topleft = (620, 290))
    #text for the key popup
    key_explanation_one = font.render("This key can be used to open a door.", True, (255, 255, 255))
    key_explanation_two = font.render("Try looking around...", True, (255, 255, 255))
    # Treat Popup
    treat_popup = pygame.image.load("treat.png")
    treat_popup = pygame.transform.scale(treat_inventory, (240, 130))
    treat_popup_rect = treat_popup.get_rect(topleft = (630, 290))
    #text for the treat popup
    treat_explanation_one = font.render("Looks like a treat.", True, (255, 255, 255))
    treat_explanation_two = font.render("Press 'E' to eat it and get one life back", True, (255, 255, 255))
    lives_full_txt = small_font.render("You already have 3 lives (max)", True, (255, 0, 0))
    # Note Popup
    note_popup = pygame.image.load("led_console.png")
    note_popup = pygame.transform.scale(note_popup, (230, 200))
    note_popup_rect = note_popup.get_rect(topleft = (640, 265))
    #note for the treat popup
    note_explanation_one = font.render("Press C to display the colour", True, (255, 255, 255))
    note_explanation_two = font.render("code on the console", True, (255, 255, 255))
    #rectangle for the popups
    popup_rect = pygame.Rect(400, 225, 700, 400)

    inventory_rects = [inventory_one_rect, inventory_two_rect, inventory_three_rect]

    inventory_positions = [inventory_one, inventory_two, inventory_three]
    inventory_y = {
        "treat": 273,
        "key": 277,
        "note": 260
    }

    inventory_images = {
        "treat": treat_inventory,
        "key": key_inventory,
        "note": note_inventory
    }

    speed = 6

    inventory = ["empty", "empty", "empty"]
    computer_input = ["_", " ", " ", " ", " ", " "]
    computer_input_pos = [500, 565, 630, 695, 760, 825]
    inventory_open = False
    inventory_pos = 0
    show_item = None
    showing_item = False
    treat_interact = False
    display_treat = True
    key_interact = False
    display_key = True
    key_obtained = False
    colour_code_interact = False
    display_colour_code = True
    wrong_colour_code = False
    current_letter = 0
    correct_code = False
    display_security_door = True
    security_door_interact = False
    desk_interact = False
    monitor_open = False
    lasers_interact = False
    lasers_on = True
    collision = False
    player_alpha = 255
    fading = False
    eat_treat = False
    lives = 3
    lives_full = False
    end = False
    start_time = pygame.time.get_ticks()
    timer_running = True
    duration = 600
    win = False
    end_win = False
    show_colour = False
    red_pressed = False
    green_pressed = False
    blue_pressed = False
    pattern_start_time = 0

    run = True
    while run:

        screen.fill((0, 0, 0))
        
        #creating rectangles for the walls
        wall_rects = []
        for i in wall_pos:
            wall_rect = wall.get_rect(topleft = i)
            wall_rects.append(wall_rect)
        
        #drawing the walls
        for i in wall_rects:
            screen.blit(wall, i)

        #timer
        time_font = pygame.font.SysFont("consolas", 50)
        current_time = pygame.time.get_ticks()
        if timer_running:    
            elapsed_time = (current_time - start_time) // 1000
            time_left = max(0, duration - elapsed_time)
        minutes = time_left // 60
        seconds = time_left % 60
        minutes_left = elapsed_time // 60
        seconds_left = elapsed_time % 60
        timer_txt = time_font.render(f"{minutes:02}:{seconds:02}", True, (0, 255, 0))
        timer_bg_rect = pygame.Rect(20, 10, 155, 65)
        pygame.draw.rect(screen, (0, 0, 0), timer_bg_rect)
        screen.blit(timer_txt, (22, 20))

        #displaying instructions
        if not inventory_open and not end and not end_win and not monitor_open:
            main_instructions()
        elif not end and not end_win and not monitor_open:
            inventory_instructions()
        elif not end and not end_win and monitor_open:
            monitor_instructions()

        #checks if player is by the door and opens if they are
        if player_rect.colliderect(door_rect):
            door = open_door
        else:
            door = closed_door

        #checks if player is by the desk in the security room
        if player_rect.colliderect(desk_rect) and lasers_on:
            desk_interact = True
            desk_interact_instructions()
        else:
            desk_interact = False

        #displaying the appropriate door
        screen.blit(door, door_rect)
        #display security room sign
        screen.blit(security_room, (930, 430))
        #display desk
        screen.blit(desk, desk_rect)
        #display treat and check if the player is interacting with it
        if display_treat == True:
            screen.blit(treat, treat_rect)
            if player_rect.colliderect(treat_rect):
                treat_interact = True
            else:
                treat_interact = False
        #display key and check if the player is interacting with it
        if display_key == True:
            screen.blit(escape_key, escape_key_rect)
            if player_rect.colliderect(escape_key_rect):
                key_interact = True
            else:
                key_interact = False
        #display colour code and check if the player is interacting with it
        if display_colour_code == True:
            screen.blit(colour_code, colour_code_rect)
            if player_rect.colliderect(colour_code_rect):
                colour_code_interact = True
            else:
                colour_code_interact = False
        #display door for security room and check if the player is interacting with it
        if display_security_door == True:
            screen.blit(security_door, security_door_rect)
            if player_rect.colliderect(collision_rect_door):
                security_door_interact = True
                if key_obtained:
                    key_door_instructions()
                else:
                    locked_door_instructions()
            else:
                security_door_interact = False
        #display appropriate lasers
        if lasers_on:
            screen.blit(lasers, lasers_rect)
        else:
            screen.blit(lasers_off, lasers_off_rect)
        #turns on or off collision rect for lasers based off if they're on or off
        if lasers_on:
            if player_rect.colliderect(collision_rect_lasers):
                collision = True
            else:
                collision = False
        #if the player collides with the lasers
        if player_rect.colliderect(danger_rect_lasers) and not lasers_interact and lasers_on:
            lives -= 1
            lasers_interact = True
            saved_position = player_rect.topleft
            fading = True

        #the player fades away and is moved down by 70 (happens when hit by the laser), then fades back
        if fading:
            player_alpha -= 4
            if player_alpha <= 0:
                player_rect.topleft = (saved_position[0], saved_position[1] + 70)
                player_alpha = 255
                fading = False
            current_image.set_alpha(player_alpha)

        if not player_rect.colliderect(danger_rect_lasers):
            lasers_interact = False

        #display player
        screen.blit(current_image, player_rect)

        #adding an item to inventory
        def add_item(item):
            for i in range(3):
                if inventory[i] == "empty":
                    inventory[i] = item
                    return True
            return False

        #displaying the inventory box and its contents
        bright_box = pygame.Surface((125, 95), pygame.SRCALPHA)
        bright_box.fill((0, 0, 0, 160))
        
        if inventory_open and not end and not end_win:
            screen.blit(inventory_box, inventory_box_rect)

            # draw items in the correct slot with proper y
            for i, item in enumerate(inventory):
                if item != "empty":
                    img = inventory_images[item]
                    if item == "note":
                        img_rect = img.get_rect(topleft=(note_x[i], inventory_y[item]))
                    else:
                        img_rect = img.get_rect(topleft=(inventory_positions[i], inventory_y[item]))
                    screen.blit(img, img_rect)

            # highlight the selected slot
            if inventory[inventory_pos] != "empty" and not showing_item:
                screen.blit(bright_box, inventory_rects[inventory_pos].topleft)
                pygame.draw.rect(screen, (255, 255, 255), inventory_rects[inventory_pos], 3)

            #displaying the selected item
            if show_item == "key":
                pygame.draw.rect(screen, (60, 30, 10), popup_rect)
                pygame.draw.rect(screen, (10, 10, 10), popup_rect, 20)
                screen.blit(key_explanation_one, (530, 480))
                screen.blit(key_explanation_two, (630, 525))
                screen.blit(key_popup, key_popup_rect)
            if show_item == "treat":
                eat_treat = True
                pygame.draw.rect(screen, (60, 30, 10), popup_rect)
                pygame.draw.rect(screen, (10, 10, 10), popup_rect, 20)
                screen.blit(treat_explanation_one, (645, 480))
                screen.blit(treat_explanation_two, (520, 525))
                screen.blit(treat_popup, treat_popup_rect)
                if lives_full:
                    screen.blit(lives_full_txt, (623, 572))
            if show_item == "note":
                show_colour = True
                pygame.draw.rect(screen, (60, 30, 10), popup_rect)
                pygame.draw.rect(screen, (10, 10, 10), popup_rect, 20)
                screen.blit(note_explanation_one, (585, 490))
                screen.blit(note_explanation_two, (640, 535))
                screen.blit(note_popup, note_popup_rect)

        #if monitor screen is open
        if monitor_open and not end and not end_win:
            screen.blit(wall_monitor_bg, wall_monitor_bg_rect)  #background wall
            pygame.draw.rect(screen, (128, 128, 128), (350, 435, 800, 285)) #desk
            pygame.draw.rect(screen, (0, 0, 0), (350, 435, 800, 285), 10)   #desk border
            pygame.draw.rect(screen, (50, 50, 50), wall_monitor_bg_rect, 20)    #popup border
            screen.blit(monitor, monitor_rect)  #monitor
            screen.blit(monitor_txt_one, (490, 280))    #text on monitor
            # six white squares
            pygame.draw.rect(screen, (255, 255, 255), (500, 360, 45, 40))
            pygame.draw.rect(screen, (255, 255, 255), (565, 360, 45, 40))
            pygame.draw.rect(screen, (255, 255, 255), (630, 360, 45, 40))
            pygame.draw.rect(screen, (255, 255, 255), (695, 360, 45, 40))
            pygame.draw.rect(screen, (255, 255, 255), (760, 360, 45, 40))
            pygame.draw.rect(screen, (255, 255, 255), (825, 360, 45, 40))
            computer_code_font = pygame.font.SysFont("lucidaconsole", 40)
            for i in range(6):
                if computer_input[i] == "R":
                    pygame.draw.rect(screen, (255, 0, 0), (computer_input_pos[i], 360, 45, 40))
                elif computer_input[i] == "G":
                    pygame.draw.rect(screen, (0, 255, 0), (computer_input_pos[i], 360, 45, 40))
                elif computer_input[i] == "B":
                    pygame.draw.rect(screen, (0, 0, 255), (computer_input_pos[i], 360, 45, 40))   
                else:
                    current_letter_colour = computer_code_font.render(computer_input[i], True, (0, 0, 0))
            if wrong_colour_code:
                small_computer_font = pygame.font.SysFont("consolas", 20)
                wrong_colour_txt = small_computer_font.render("Wrong colour code", True, (255, 0, 0))
                screen.blit(wrong_colour_txt, (590, 430))

        #displaying lives
        if lives == 3:
            screen.blit(heart, heart_rect_one)            
            screen.blit(heart, heart_rect_two)            
            screen.blit(heart, heart_rect_three)
        elif lives == 2:
            screen.blit(heart, heart_rect_one)            
            screen.blit(heart, heart_rect_two)
        elif lives == 1:
            screen.blit(heart, heart_rect_one)
        else:
            end = endgame(end)

        #if timer ends
        if time_left == 0:
            end = endtime(end)

        if win == True:
            end_win = win_display(end_win)

        #checks which key is pressed and acts accordingly
        key = pygame.key.get_pressed()
        #move left
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            new_rect = player_rect.move(-speed, 0)
            #check if this results in a collision and only moves player if not
            if not any(new_rect.colliderect(i) for i in wall_rects) and (not display_security_door or not new_rect.colliderect(security_door_rect)) and not collision and not inventory_open and not monitor_open and not end and not end_win:
                player_rect = new_rect
                current_image = player_left_image
        #move right
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            new_rect = player_rect.move(speed, 0)
            if not any(new_rect.colliderect(i) for i in wall_rects) and (not display_security_door or not new_rect.colliderect(security_door_rect)) and not collision and not inventory_open and not monitor_open and not end and not end_win:
                player_rect = new_rect
                current_image = player_right_image
        #move up
        if key[pygame.K_w] or key[pygame.K_UP]:
            new_rect = player_rect.move(0, -speed)
            if not any(new_rect.colliderect(i) for i in wall_rects) and (not display_security_door or not new_rect.colliderect(security_door_rect)) and not collision and not inventory_open and not monitor_open and not end and not end_win:
                player_rect = new_rect
        #move_down
        if key[pygame.K_s] or key[pygame.K_DOWN]:
            new_rect = player_rect.move(0, speed)
            if not any(new_rect.colliderect(i) for i in wall_rects) and (not display_security_door or not new_rect.colliderect(security_door_rect)) and not collision and not inventory_open and not monitor_open and not end and not end_win:
                player_rect = new_rect
        #opening and closing inventory using blue button
        if inventory_button.is_pressed and not monitor_open and not inv_button_pressed:
            inventory_open = not inventory_open
            lives_full = False
            show_item = None
            showing_item = False
            if inventory_open:
                available = [i for i, item in enumerate(inventory) if item != "empty"]
                if available:
                    inventory_pos = available[0]
        #if they open the final door
        if door_button.is_pressed and door == open_door and not inventory_open and not end and not end_win:
            timer_running = False
            print(f"Time Taken: {minutes_left}mins {seconds_left}sec")
            win = True
        #if they pick up the treat
        if pickup_button.is_pressed and treat_interact == True and not inventory_open and not end and not end_win:
            if add_item("treat"):
                display_treat = False
                treat_interact = False
        #if they pick up the key
        if pickup_button.is_pressed and key_interact == True and not inventory_open and not end and not end_win:
            if add_item("key"):
                display_key = False
                key_interact = False
                key_obtained = True
        #if they pick up the note with the colour code
        if pickup_button.is_pressed and colour_code_interact == True and not inventory_open and not end and not end_win:
            if add_item("note"):
                display_colour_code = False
                colour_code_interact = False
        
        inv_button_pressed = inventory_button.is_pressed
        
        if pattern_active:
            last_second = colour_pattern(last_second)
        
        if monitor_open and current_letter <= 5:
            if red_button.is_pressed and not red_pressed:
                computer_input[current_letter] = "R"
                current_letter += 1
                red_led.on()
                wrong_colour_code = False
            if not red_button.is_pressed:
                red_led.off()
            if green_button.is_pressed and not green_pressed:
                computer_input[current_letter] = "G"
                current_letter += 1
                green_led.on()
                wrong_colour_code = False
            if not green_button.is_pressed:
                green_led.off()
            if blue_button.is_pressed and not blue_pressed:
                computer_input[current_letter] = "B"
                current_letter += 1
                blue_led.on()
                wrong_colour_code = False
            if not blue_button.is_pressed:
                blue_led.off()
            if current_letter > 5:
                red_led.off()
                green_led.off()
                blue_led.off()
    
        red_pressed = red_button.is_pressed
        green_pressed = green_button.is_pressed
        blue_pressed = blue_button.is_pressed

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #while on the endgame screen
                if end:
                    if event.key == pygame.K_RETURN:
                        end = False
                        return "restart"
                    if event.key == pygame.K_ESCAPE:
                        run  = False
                        return "quit"
                if end_win:
                    if event.key == pygame.K_ESCAPE:
                        run  = False
                        return "quit"
                #if they try opening the security door while the key is in their inventory
                if event.key == pygame.K_RETURN and security_door_interact and key_obtained and not inventory_open:
                    inventory[inventory.index("key")] = "empty"
                    display_security_door = False
                    security_door_interact = False
                #open monitor
                if event.key == pygame.K_RETURN and desk_interact and not monitor_open and not inventory_open:
                    monitor_open = True
                    wrong_colour_code = False
                    continue
                #close monitor
                elif event.key == pygame.K_ESCAPE and monitor_open and not inventory_open:
                    monitor_open = False
                    wrong_colour_code = False
                    current_letter = 0
                    computer_input = ["_", " ", " ", " ", " ", " "]
                #check colour code
                elif event.key == pygame.K_RETURN and monitor_open:
                    correct_code = colour_code_check(computer_input)
                    red_led.off()
                    green_led.off()
                    blue_led.off()
                    if correct_code:
                        lasers_on = False
                        monitor_open = False
                        wrong_colour_code = False
                    else:
                        computer_input = ["_", " ", " ", " ", " ", " "]
                        current_letter = 0
                        wrong_colour_code = True
                elif event.key != pygame.K_RETURN and monitor_open:
                    wrong_colour_code = False
            #when inventory is open
            if event.type == pygame.KEYDOWN and inventory_open:
                available = [i for i, item in enumerate(inventory) if item != "empty"]
                #if they go to the right while in inventory
                if event.key == pygame.K_RIGHT and available and not showing_item:
                    if inventory_pos not in available:
                        inventory_pos = available[0]
                    else:
                        index = available.index(inventory_pos)
                        index = min(index + 1, len(available) - 1)
                        inventory_pos = available[index]
                #if they go to the left while in inventory
                elif event.key == pygame.K_LEFT and available and not showing_item:
                    if inventory_pos not in available:
                        inventory_pos = available[0]
                    else:
                        index = available.index(inventory_pos)
                        index = max(index - 1, 0)
                        inventory_pos = available[index]
                #if they select an item while in inventory
                if event.key == pygame.K_RETURN and available and not showing_item:
                    show_item = inventory[inventory_pos]
                    showing_item = True
                elif event.key == pygame.K_RETURN and available and showing_item:
                    show_item = None
                    showing_item = False
                    eat_treat = False
                    lives_full = False
                #pressing e when viewing treat in inventory
                if event.key == pygame.K_e and eat_treat:
                    if lives < 3:
                        lives += 1
                        show_item = None
                        showing_item = False
                        inventory[inventory.index("treat")] = "empty"
                        index = available.index(inventory_pos)
                        inventory_pos = available[index]
                        lives_full = False
                    else:
                        lives_full = True
                #pressing c to see the colour pattern
                if event.key == pygame.K_c and show_colour:
                    pattern_active = True
                    pattern_start_time = pygame.time.get_ticks()
                    last_second = -1
            if event.type == pygame.QUIT:
                run = False
                return "quit"

        #updates the display
        pygame.display.flip() 

if lvl_one(walls_one) == "lvl_two":
    running = True
    while running:
        result = lvl_two(walls_two)
        if result == "quit":
            running = False

pygame.quit()
