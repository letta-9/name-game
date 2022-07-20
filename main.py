# Import Modules #--------------------------------------------------------------------------------------------------

import pygame, sys
from button import Button
import random


# Initialize Game #-------------------------------------------------------------------------------------------------

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Game")


# Colors #----------------------------------------------------------------------------------------------------------

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 150, 0)
blue = (40, 53, 88)
yellow = (255, 255, 0)
forest_green = (0, 100, 0)
mustard_yellow = (200, 200, 0)
maroon = (150, 0, 0)
seafoam = (215, 252, 212)
powder_blue = (182, 208, 226)
gray = (121, 118, 119)


# Images #----------------------------------------------------------------------------------------------------------

gray_rect = pygame.image.load("Gray Rect.png")
input_bg = pygame.image.load("input.png") 


# Fonts #-----------------------------------------------------------------------------------------------------------

def press_start_font(size):
    return pygame.font.Font("font.ttf", size)


# Display Player Answer #-------------------------------------------------------------------------------------------

def disp_type(ans):
    TEXT = press_start_font(28).render(ans, True, gray)
    TEXT_RECT = TEXT.get_rect(center=(655, 595))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Player Answer #------------------------------------------------------------------------------------------

def disp_ans(ans):
    TEXT = press_start_font(28).render(ans, True, seafoam)
    TEXT_RECT = TEXT.get_rect(center=(655, 400))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display First Random Letter #------------------------------------------------------------------------------------------

def disp_first_letter(letter):
    FIRST_TEXT = press_start_font(100).render(letter, True, gray)
    FIRST_RECT = FIRST_TEXT.get_rect(center=(655, 200))
    SCREEN.blit(FIRST_TEXT, FIRST_RECT)


# Main Menu Game Loop #---------------------------------------------------------------------------------------------

def main_menu():
    while True:
        SCREEN.fill(white)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = press_start_font(100).render("NAME GAME", True, powder_blue)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 175))

        PLAY_BUTTON = Button(image=pygame.transform.scale(gray_rect, (300, 100)), pos=(640, 350), 
                            text_input="SINGLE PLAYER", font=press_start_font(20), base_color=seafoam, hovering_color=white)
        CONTACT_BUTTON = Button(image=pygame.transform.scale(gray_rect, (475, 100)), pos=(640, 475), 
                            text_input="CONTACT", font=press_start_font(50), base_color=seafoam, hovering_color=white)
        QUIT_BUTTON = Button(image=pygame.transform.scale(gray_rect, (300, 100)), pos=(640, 600), 
                            text_input="QUIT", font=press_start_font(50), base_color=seafoam, hovering_color=white)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CONTACT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_cat()
                if CONTACT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    contact()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


# Play Screen Game Loop #-------------------------------------------------------------------------------------------

def play_cat():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(white)

        PLAY_TEXT = press_start_font(45).render("CHOOSE A CATEGORY", True, powder_blue)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # SPORTS_TEXT = press_start_font(30).render("SPORTS", True, powder_blue)
        # SPORTS_RECT = PLAY_TEXT.get_rect(center=(715, 165))
        # SCREEN.blit(SPORTS_TEXT, SPORTS_RECT)

        # CELEBS_TEXT = press_start_font(30).render("CELEBS", True, powder_blue)
        # CELEBS_RECT = PLAY_TEXT.get_rect(center=(1150, 165))
        # SCREEN.blit(CELEBS_TEXT, CELEBS_RECT)

        # Categories #

        ATHLETES_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 225), 
                            text_input="ALL ATHLETES", font=press_start_font(20), base_color=seafoam, hovering_color=white)
        ATHLETES_CAT.changeColor(PLAY_MOUSE_POS)
        ATHLETES_CAT.update(SCREEN)

        BASEBALL_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 285), 
                            text_input="BASEBALL", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        BASEBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASEBALL_CAT.update(SCREEN)

        BASKETBALL_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 345), 
                            text_input="BASKETBALL", font=press_start_font(24), base_color=seafoam, hovering_color=white)
        BASKETBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASKETBALL_CAT.update(SCREEN)

        FOOTBALL_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 405), 
                            text_input="FOOTBALL", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        FOOTBALL_CAT.changeColor(PLAY_MOUSE_POS)
        FOOTBALL_CAT.update(SCREEN)

        HOCKEY_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 465), 
                            text_input="HOCKEY", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        HOCKEY_CAT.changeColor(PLAY_MOUSE_POS)
        HOCKEY_CAT.update(SCREEN)

        SOCCER_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 525), 
                            text_input="SOCCER", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        SOCCER_CAT.changeColor(PLAY_MOUSE_POS)
        SOCCER_CAT.update(SCREEN)

        GOLF_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 585), 
                            text_input="GOLF", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        GOLF_CAT.changeColor(PLAY_MOUSE_POS)
        GOLF_CAT.update(SCREEN)

        TENNIS_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(645, 645), 
                            text_input="TENNIS", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        TENNIS_CAT.changeColor(PLAY_MOUSE_POS)
        TENNIS_CAT.update(SCREEN)

        # ACTORS_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 225), 
        #                     text_input="ACTORS/ACTRESSES", font=press_start_font(15), base_color=seafoam, hovering_color=white)
        # ACTORS_CAT.changeColor(PLAY_MOUSE_POS)
        # ACTORS_CAT.update(SCREEN)

        # MUSICIANS_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 285), 
        #                     text_input="MUSICIANS", font=press_start_font(26), base_color=seafoam, hovering_color=white)
        # MUSICIANS_CAT.changeColor(PLAY_MOUSE_POS)
        # MUSICIANS_CAT.update(SCREEN)

        # MOVIE_CHAR_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 345), 
        #                     text_input="MOVIE CHARACTERS", font=press_start_font(15), base_color=seafoam, hovering_color=white)
        # MOVIE_CHAR_CAT.changeColor(PLAY_MOUSE_POS)
        # MOVIE_CHAR_CAT.update(SCREEN)

        # TV_CHAR_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 405), 
        #                     text_input="TV CHARACTERS", font=press_start_font(18), base_color=seafoam, hovering_color=white)
        # TV_CHAR_CAT.changeColor(PLAY_MOUSE_POS)
        # TV_CHAR_CAT.update(SCREEN)

        # HIST_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 465), 
        #                     text_input="HISTORICAL FIGURES", font=press_start_font(13), base_color=seafoam, hovering_color=white)
        # HIST_CAT.changeColor(PLAY_MOUSE_POS)
        # HIST_CAT.update(SCREEN)

        # ART_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 525), 
        #                     text_input="ARTISTS", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        # ART_CAT.changeColor(PLAY_MOUSE_POS)
        # ART_CAT.update(SCREEN)

        # AUTH_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 585), 
        #                     text_input="AUTHORS", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        # AUTH_CAT.changeColor(PLAY_MOUSE_POS)
        # AUTH_CAT.update(SCREEN)

        # CEO_CAT = Button(image=pygame.transform.scale(gray_rect, (250, 50)), pos=(853, 645), 
        #                     text_input="CEOs", font=press_start_font(30), base_color=seafoam, hovering_color=white)
        # CEO_CAT.changeColor(PLAY_MOUSE_POS)
        # CEO_CAT.update(SCREEN)


        PLAY_BACK = Button(image=pygame.transform.scale(gray_rect, (130, 50)), pos=(80, 50), 
                            text_input="BACK", font=press_start_font(30), base_color=seafoam, hovering_color=white)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if BASEBALL_CAT.checkForInput(PLAY_MOUSE_POS):
                    baseball()

        pygame.display.update()
  

# Contact Screen Game Loop #----------------------------------------------------------------------------------------

def contact():
    while True:
        CONTACT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(white)

        CONTACT_TEXT = press_start_font(45).render("CREATED BY MATT BARLETTA", True, powder_blue)
        CONTACT_RECT = CONTACT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CONTACT_TEXT, CONTACT_RECT)

        EMAIL_TEXT = press_start_font(30).render("CONTACT AT MATTBARLETTA7@GMAIL.COM", True, powder_blue)
        EMAIL_RECT = EMAIL_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(EMAIL_TEXT, EMAIL_RECT)

        CONTACT_BACK = Button(image=pygame.transform.scale(gray_rect, (130, 50)), pos=(80, 50), 
                            text_input="BACK", font=press_start_font(30), base_color=seafoam, hovering_color=white)

        CONTACT_BACK.changeColor(CONTACT_MOUSE_POS)
        CONTACT_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTACT_BACK.checkForInput(CONTACT_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# Baseball Page Game Loop #
def baseball():

    PLAYER_INPUT = ""
    PLAYER_ANS = ""
    ANS_TWO = ""
    ANS_THREE = ""
    ANS_FOUR = ""
    ANS_FIVE = ""
    TURN = 1
    TURN_STR = str(TURN)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    random_start = random.choice(alphabet)
    used_words = []


    while True:
        BASEBALL_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill(white)

        BASEBALL_TEXT = press_start_font(45).render("BASEBALL", True, powder_blue)
        BASEBALL_RECT = BASEBALL_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(BASEBALL_TEXT, BASEBALL_RECT)

        LETTER_TEXT = press_start_font(20).render("NAME A BASEBALL PLAYER WHOSE NAME STARTS WITH:", True, gray)
        LETTER_RECT = LETTER_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(LETTER_TEXT, LETTER_RECT)

  
        BASEBALL_BACK = Button(image=pygame.transform.scale(gray_rect, (130, 50)), pos=(80, 50), 
                        text_input="BACK", font=press_start_font(30), base_color=seafoam, hovering_color=white)

        BASEBALL_BACK.changeColor(BASEBALL_MOUSE_POS)
        BASEBALL_BACK.update(SCREEN)

        SCREEN.blit(input_bg, [250,550])

        disp_first_letter(random_start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BASEBALL_BACK.checkForInput(BASEBALL_MOUSE_POS):
                    play_cat()
            if event.type == pygame.KEYDOWN:
                char = pygame.key.name(event.key)
                PLAYER_INPUT += char

                if event.key == pygame.K_BACKSPACE:
                    PLAYER_INPUT = PLAYER_INPUT[:-10]
                if event.key == pygame.K_SPACE:
                    PLAYER_INPUT = PLAYER_INPUT[:-5]
                    PLAYER_INPUT += " "
                if event.key == pygame.K_TAB:
                    PLAYER_INPUT = PLAYER_INPUT[:-3]
                if event.key == pygame.K_CAPSLOCK:
                    PLAYER_INPUT = PLAYER_INPUT[:-9]                   
                if event.key == pygame.K_RSHIFT:
                    PLAYER_INPUT = PLAYER_INPUT[:-11]
                if event.key == pygame.K_LSHIFT:
                    PLAYER_INPUT = PLAYER_INPUT[:-10]
                if event.key == pygame.K_RCTRL:
                    PLAYER_INPUT = PLAYER_INPUT[:-10]  
                if event.key == pygame.K_LCTRL:
                    PLAYER_INPUT = PLAYER_INPUT[:-9]  
                if event.key == pygame.K_RALT:
                    PLAYER_INPUT = PLAYER_INPUT[:-9]
                if event.key == pygame.K_LALT:
                    PLAYER_INPUT = PLAYER_INPUT[:-8] 
                if event.key == pygame.K_UP:
                    PLAYER_INPUT = PLAYER_INPUT[:-2]
                if event.key == pygame.K_DOWN:
                    PLAYER_INPUT = PLAYER_INPUT[:-4]
                if event.key == pygame.K_LEFT:
                    PLAYER_INPUT = PLAYER_INPUT[:-4]
                if event.key == pygame.K_RIGHT:
                    PLAYER_INPUT = PLAYER_INPUT[:-5]
                if event.key == pygame.K_RMETA:
                    PLAYER_INPUT = PLAYER_INPUT[:-10]
                if event.key == pygame.K_LMETA:
                    PLAYER_INPUT = PLAYER_INPUT[:-9]
                if event.key == pygame.K_NUMLOCK:
                    PLAYER_INPUT = PLAYER_INPUT[:-7]
                if event.key == pygame.K_KP_ENTER:
                    PLAYER_INPUT = PLAYER_INPUT[:-5]
                if event.key == pygame.K_RETURN:
                    PLAYER_ANS = PLAYER_INPUT[:-6]
                    used_words.append(PLAYER_ANS)
                    PLAYER_INPUT = ""



        disp_ans(PLAYER_ANS)                
        disp_type(PLAYER_INPUT)
        
        # disp_ans_two(ANS_TWO)
        # disp_ans_three(ANS_THREE)
        # disp_ans_four(ANS_FOUR)
                                

            

        pygame.display.update()
                


# Start the Game #--------------------------------------------------------------------------------------------------

main_menu()