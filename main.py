# TO-DO #----------------------------------------------------------------------------------------------------------

# Eliminate duplicate answers
# Lives/Hearts
# Timer
# Scoring System (adding style points for double woubles & same first and last name, double streak)
# Lose/Restart menu
# Save high score
# Rules paragraph text
# No Letter U in baseball
# take out less frequent letters for the start
# fix alignment of all rects



# Import Modules #--------------------------------------------------------------------------------------------------
import pygame, sys
from button import Button
import random
import pandas as pd

# Initialize Game #-------------------------------------------------------------------------------------------------

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Game")


# Add Colors As Constants #----------------------------------------------------------------------------------------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 150, 0)
BLUE = (40, 53, 88)
YELLOW = (255, 255, 0)
FOREST_GREEN = (0, 100, 0)
MUSTARD_YELLOW = (200, 200, 0)
MAROON = (150, 0, 0)
SEAFOAM = (215, 252, 212)
POWDER_BLUE = (182, 208, 226)
GRAY = (121, 118, 119)


# Import Images #----------------------------------------------------------------------------------------------------------

GRAY_RECT = pygame.image.load("GRAY Rect.png")
INPUT_BG = pygame.image.load("input.png") 


# Define Font Functions Func #-----------------------------------------------------------------------------------------------------------

def press_start_font(size):
    return pygame.font.Font("font.ttf", size)

def arial(size):
    return pygame.font.SysFont("arial", size)


# Display Player Actively Typing Func #-------------------------------------------------------------------------------------------

def disp_type(ans):
    TEXT = press_start_font(28).render(ans, True, GRAY)
    TEXT_RECT = TEXT.get_rect(center=(655, 595))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Player Submitted Answer Func #------------------------------------------------------------------------------------------

def disp_ans(ans):
    TEXT = press_start_font(28).render(ans, True, SEAFOAM)
    TEXT_RECT = TEXT.get_rect(center=(655, 400))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Wrong Answer Text Func #------------------------------------------------------------------------------------------

def wrong_ans():
    TEXT = press_start_font(28).render("THAT ANSWER IS INCORRECT", True, RED)
    TEXT_RECT = TEXT.get_rect(center=(655, 400))
    SCREEN.blit(TEXT, TEXT_RECT)


# Display First Random Letter Func #------------------------------------------------------------------------------------------

def disp_play_letter(letter):
    TEXT = press_start_font(100).render(letter, True, GRAY)
    TEXT_RECT = TEXT.get_rect(center=(655, 200))
    SCREEN.blit(TEXT, TEXT_RECT)

# Hide Previous Letter Func #------------------------------------------------------------------------------------------

def hide_prev_letter():
    pygame.draw.rect(SCREEN, WHITE, (585, 140, 150, 150))

# Display Score Func #------------------------------------------------------------------------------------------

def disp_score(score):
    score = str(score)
    TEXT = press_start_font(30).render("SCORE:" + score, True, GRAY)
    TEXT_RECT = TEXT.get_rect(center=(1100, 50))
    SCREEN.blit(TEXT, TEXT_RECT)



# Main Menu Game Loop #---------------------------------------------------------------------------------------------

def main_menu():
    while True:
        
        SCREEN.fill(WHITE)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = press_start_font(100).render("NAME GAME", True, POWDER_BLUE)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 175))

        PLAY_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (300, 100)), pos=(640, 350), 
                            text_input="PLAY", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)
        CONTACT_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (475, 100)), pos=(640, 475), 
                            text_input="CONTACT", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)
        QUIT_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (300, 100)), pos=(640, 600), 
                            text_input="QUIT", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)

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


# Category Screen Game Loop #-------------------------------------------------------------------------------------------

def play_cat():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        PLAY_TEXT = press_start_font(45).render("CHOOSE A CATEGORY", True, POWDER_BLUE)
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Category Buttons #

        ATHLETES_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 225), 
                            text_input="ALL ATHLETES", font=press_start_font(20), base_color=SEAFOAM, hovering_color=WHITE)
        ATHLETES_CAT.changeColor(PLAY_MOUSE_POS)
        ATHLETES_CAT.update(SCREEN)

        BASEBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 285), 
                            text_input="BASEBALL", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        BASEBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASEBALL_CAT.update(SCREEN)

        BASKETBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 345), 
                            text_input="BASKETBALL", font=press_start_font(24), base_color=SEAFOAM, hovering_color=WHITE)
        BASKETBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASKETBALL_CAT.update(SCREEN)

        FOOTBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 405), 
                            text_input="FOOTBALL", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        FOOTBALL_CAT.changeColor(PLAY_MOUSE_POS)
        FOOTBALL_CAT.update(SCREEN)

        HOCKEY_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 465), 
                            text_input="HOCKEY", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        HOCKEY_CAT.changeColor(PLAY_MOUSE_POS)
        HOCKEY_CAT.update(SCREEN)

        SOCCER_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 525), 
                            text_input="SOCCER", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        SOCCER_CAT.changeColor(PLAY_MOUSE_POS)
        SOCCER_CAT.update(SCREEN)

        GOLF_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 585), 
                            text_input="GOLF", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        GOLF_CAT.changeColor(PLAY_MOUSE_POS)
        GOLF_CAT.update(SCREEN)

        TENNIS_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 645), 
                            text_input="TENNIS", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        TENNIS_CAT.changeColor(PLAY_MOUSE_POS)
        TENNIS_CAT.update(SCREEN)

        # Back Button #

        PLAY_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                            text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

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
                    baseball_rules()

        pygame.display.update()
  

# Contact Screen Game Loop #----------------------------------------------------------------------------------------

def contact():
    while True:
        CONTACT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        CONTACT_TEXT = press_start_font(45).render("CREATED BY MATT BARLETTA", True, POWDER_BLUE)
        CONTACT_RECT = CONTACT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CONTACT_TEXT, CONTACT_RECT)

        EMAIL_TEXT = press_start_font(30).render("CONTACT AT MATTBARLETTA7@GMAIL.COM", True, POWDER_BLUE)
        EMAIL_RECT = EMAIL_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(EMAIL_TEXT, EMAIL_RECT)

        CONTACT_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                            text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

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


def baseball_rules():
    while True:
        BASEBALL_RULES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        pygame.draw.rect(SCREEN, GRAY, (390, 110, 500, 500))

        RULES_TEXT = press_start_font(30).render("RULES", True, POWDER_BLUE)
        RULES_RECT = RULES_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(RULES_TEXT, RULES_RECT)

        BASEBALL_RULES_PLAY = Button(None, pos=(640, 535), 
                        text_input="PLAY", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        BASEBALL_RULES_PLAY.changeColor(BASEBALL_RULES_MOUSE_POS)
        BASEBALL_RULES_PLAY.update(SCREEN)

        BASEBALL_RULES_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        BASEBALL_RULES_BACK.changeColor(BASEBALL_RULES_MOUSE_POS)
        BASEBALL_RULES_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BASEBALL_RULES_BACK.checkForInput(BASEBALL_RULES_MOUSE_POS):
                    main_menu()
                if BASEBALL_RULES_PLAY.checkForInput(BASEBALL_RULES_MOUSE_POS):
                    baseball()

        pygame.display.update()

# Baseball Page Game Loop #
def baseball():

    PLAYER_INPUT = ""
    PLAYER_ANS = ""
    CHECK_ANS = ""
    SCORE = 0
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    RANDOM_START = random.choice(ALPHABET)
    USED_WORDS = []
    DISPLAY = ""
    BASEBALL_LIST = pd.read_csv('baseball_list_py.csv')

    while True:
        BASEBALL_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill(WHITE)

        BASEBALL_TEXT = press_start_font(45).render("BASEBALL", True, POWDER_BLUE)
        BASEBALL_RECT = BASEBALL_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(BASEBALL_TEXT, BASEBALL_RECT)

        LETTER_TEXT = press_start_font(20).render("NAME A BASEBALL PLAYER WHOSE NAME STARTS WITH:", True, GRAY)
        LETTER_RECT = LETTER_TEXT.get_rect(center=(640, 110))
        SCREEN.blit(LETTER_TEXT, LETTER_RECT)

  
        BASEBALL_QUIT = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="QUIT", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        BASEBALL_QUIT.changeColor(BASEBALL_MOUSE_POS)
        BASEBALL_QUIT.update(SCREEN)

        SCREEN.blit(INPUT_BG, [250,550])

        disp_play_letter(RANDOM_START)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BASEBALL_QUIT.checkForInput(BASEBALL_MOUSE_POS):
                    play_cat()
            if event.type == pygame.KEYDOWN:
                char = pygame.key.name(event.key)
                PLAYER_INPUT += char
                
                if PLAYER_INPUT == "return":
                    PLAYER_INPUT = ""
                
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

                    if SCORE == 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6][0] == RANDOM_START and BASEBALL_LIST['Name'].str.contains(PLAYER_INPUT[:-6]).any():
                            CHECK_ANS = PLAYER_INPUT[:-6]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"
                            USED_WORDS.append(CHECK_ANS)

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]

                            SCORE += 100

                        else:
                            PLAYER_INPUT = ""                        
                            DISPLAY = "incorrect"
                            
                    elif SCORE > 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6][0] == PLAY_LETTER and BASEBALL_LIST['Name'].str.contains(PLAYER_INPUT[:-6]).any():

                            CHECK_ANS = PLAYER_INPUT[:-6]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"  
                            USED_WORDS.append(CHECK_ANS)

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]

                            SCORE += 100

                        else:
                            DISPLAY = "incorrect"
                            PLAYER_INPUT = ""
                            
                            
        # Change display whether the answer is correct or incorrect #

        if DISPLAY == "correct":
            disp_ans(CHECK_ANS)
            hide_prev_letter()
            disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "incorrect":
            wrong_ans()
            hide_prev_letter()
            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        
        # Call Functions to display elements that are always on the screen #            
               
        disp_type(PLAYER_INPUT)
        disp_score(SCORE)
            

        pygame.display.update()
                


# Start the Game #--------------------------------------------------------------------------------------------------

main_menu()