# Import Modules #--------------------------------------------------------------------------------------------------

import webbrowser
import pygame, sys
from button import Button
import random
import pandas as pd

# Initialize Game #-------------------------------------------------------------------------------------------------

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Game")

CLOCK = pygame.time.Clock()
TOTAL_TIME = 0
START_TIME = 0



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
TWITTER = pygame.image.load("twitter.png")
HEART = pygame.transform.scale(pygame.image.load("heart.png"), (100, 100))
BASEBALL_RULES = pygame.transform.scale(pygame.image.load("baseball_rules.png"), (400, 350))

# Import Sounds #----------------------------------------------------------------------------------------------------------

CLICK = pygame.mixer.Sound('click.wav')
CORRECT = pygame.mixer.Sound('correct.wav')
INCORRECT = pygame.mixer.Sound('incorrect.wav')

# Define Font Functions Func #-----------------------------------------------------------------------------------------------------------

def press_start_font(size):
    return pygame.font.Font("font.ttf", size)

def arial(size):
    return pygame.font.SysFont("arial", size)


# Display Player Actively Typing Func #-------------------------------------------------------------------------------------------

def disp_type(ans, color, x, y):
    TEXT = press_start_font(28).render(ans, True, color)
    TEXT_RECT = TEXT.get_rect(center=(x, y))
    SCREEN.blit(TEXT, TEXT_RECT)


# Display Player Submitted Answer Func #------------------------------------------------------------------------------------------

def disp_ans(ans):
    TEXT = press_start_font(28).render(ans, True, GREEN)
    TEXT_RECT = TEXT.get_rect(center=(655, 500))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Wrong Answer Text Func #------------------------------------------------------------------------------------------

def wrong_ans():
    TEXT = press_start_font(28).render("THAT ANSWER IS INCORRECT", True, RED)
    TEXT_RECT = TEXT.get_rect(center=(655, 500))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Dupe Text Func #------------------------------------------------------------------------------------------

def dupe_ans():
    TEXT = press_start_font(22).render("THAT NAME HAS ALREADY BEEN USED. TRY AGAIN", True, RED)
    TEXT_RECT = TEXT.get_rect(center=(655, 500))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Text when time runs out #---------------------------------------------------------------------------------------------------

def no_time_1():
    TEXT = press_start_font(28).render("OUT OF TIME. 2 LIVES LEFT", True, RED)
    TEXT_RECT = TEXT.get_rect(center=(655, 500))
    SCREEN.blit(TEXT, TEXT_RECT)

def no_time_2():
    TEXT = press_start_font(28).render("OUT OF TIME. 1 LIFE LEFT", True, RED)
    TEXT_RECT = TEXT.get_rect(center=(655, 500))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display First Random Letter Func #------------------------------------------------------------------------------------------

def disp_play_letter(letter):
    TEXT = press_start_font(100).render(letter, True, POWDER_BLUE)
    TEXT_RECT = TEXT.get_rect(center=(655, 200))
    SCREEN.blit(TEXT, TEXT_RECT)

# Hide Previous Letter Func #------------------------------------------------------------------------------------------

def hide_prev_letter():
    pygame.draw.rect(SCREEN, WHITE, (585, 140, 150, 150))

# Display Score Func #------------------------------------------------------------------------------------------

def disp_score(score, x, y, color):
    score = str(score)
    TEXT = press_start_font(30).render("SCORE:" + score, True, color)
    TEXT_RECT = TEXT.get_rect(center=(x, y))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Timer #-----------------------------------------------------------------------------------------------------

def disp_timer(num,color):
    TEXT = press_start_font(60).render(num, True, color)
    TEXT_RECT = TEXT.get_rect(center=(655, 360))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Lives #-----------------------------------------------------------------------------------------------------

def disp_lives(lives, color):
    lives = str(lives)
    TEXT = press_start_font(30).render("LIVES:" + lives, True, color)
    TEXT_RECT = TEXT.get_rect(center=(1100, 350))
    SCREEN.blit(TEXT, TEXT_RECT)

# Hide Hearts #

def hide_hearts(x, y, l, h):
    pygame.draw.rect(SCREEN, WHITE, (x, y, l, h))


# Display Double Streak #-----------------------------------------------------------------------------------------------------

def disp_streak(streak):
    streak = str(streak)
    TEXT = press_start_font(20).render("DOUBLE STREAK x" + streak, True, GREEN)
    TEXT_RECT = TEXT.get_rect(center=(160, 400))
    SCREEN.blit(TEXT, TEXT_RECT)

# Display Leaderboard #

def disp_high_scores(cat):
    LEADERBOARD = pd.read_csv(f"{cat}_highscores.csv")
    LEADERBOARD = LEADERBOARD.sort_values(by='score', ascending=False)
    LEADERBOARD['new'] = LEADERBOARD['name'] + " " + LEADERBOARD['score'].astype(str)

    if len(LEADERBOARD) == 1:
        FIRST = LEADERBOARD['new'].iloc[0]
        FIRST_TEXT = press_start_font(30).render(FIRST, True, SEAFOAM)
        FIRST_TEXT_RECT = FIRST_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(FIRST_TEXT, FIRST_TEXT_RECT)
        
    elif len(LEADERBOARD) == 2:
        FIRST = LEADERBOARD['new'].iloc[0]
        FIRST_TEXT = press_start_font(30).render(FIRST, True, SEAFOAM)
        FIRST_TEXT_RECT = FIRST_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(FIRST_TEXT, FIRST_TEXT_RECT)

        SEC = LEADERBOARD['new'].iloc[1]
        SEC_TEXT = press_start_font(30).render(SEC, True, SEAFOAM)
        SEC_TEXT_RECT = SEC_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(SEC_TEXT, SEC_TEXT_RECT)

    elif len(LEADERBOARD) > 2:
        FIRST = LEADERBOARD['new'].iloc[0]
        FIRST_TEXT = press_start_font(30).render(FIRST, True, SEAFOAM)
        FIRST_TEXT_RECT = FIRST_TEXT.get_rect(center=(640, 300))
        SCREEN.blit(FIRST_TEXT, FIRST_TEXT_RECT)

        SEC = LEADERBOARD['new'].iloc[1]
        SEC_TEXT = press_start_font(30).render(SEC, True, SEAFOAM)
        SEC_TEXT_RECT = SEC_TEXT.get_rect(center=(640, 350))
        SCREEN.blit(SEC_TEXT, SEC_TEXT_RECT)

        THIRD = LEADERBOARD['new'].iloc[2]
        THIRD_TEXT = press_start_font(30).render(THIRD, True, SEAFOAM)
        THIRD_TEXT_RECT = THIRD_TEXT.get_rect(center=(640, 400))
        SCREEN.blit(THIRD_TEXT, THIRD_TEXT_RECT) 


# Main Menu Game Loop #---------------------------------------------------------------------------------------------

def main_menu():
    while True:
        
        SCREEN.fill(WHITE)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = press_start_font(100).render("NAME GAME", True, POWDER_BLUE)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        SPORTS_TEXT = press_start_font(30).render("SPORTS EDITION", True, POWDER_BLUE)
        SPORTS_RECT = SPORTS_TEXT.get_rect(center=(640, 225))
        SCREEN.blit(SPORTS_TEXT, SPORTS_RECT)

        PLAY_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (300, 100)), pos=(640, 350), 
                            text_input="PLAY", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)
        CONTACT_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (475, 100)), pos=(640, 475), 
                            text_input="CONTACT", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)
        QUIT_BUTTON = Button(image=pygame.transform.scale(GRAY_RECT, (300, 100)), pos=(640, 600), 
                            text_input="QUIT", font=press_start_font(50), base_color=SEAFOAM, hovering_color=WHITE)

        

        for button in [PLAY_BUTTON, CONTACT_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    CLICK.play()
                    play_cat()
                if CONTACT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    CLICK.play()
                    contact()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    CLICK.play()
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

        BASEBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 225), 
                            text_input="MLB", font=press_start_font(25), base_color=SEAFOAM, hovering_color=WHITE)
        BASEBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASEBALL_CAT.update(SCREEN)        
        

        FOOTBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 285), 
                            text_input="NFL", font=press_start_font(22), base_color=SEAFOAM, hovering_color=WHITE)
        FOOTBALL_CAT.changeColor(PLAY_MOUSE_POS)
        FOOTBALL_CAT.update(SCREEN)  

    
        BASKETBALL_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 345), 
                            text_input="NBA", font=press_start_font(25), base_color=SEAFOAM, hovering_color=WHITE)
        BASKETBALL_CAT.changeColor(PLAY_MOUSE_POS)
        BASKETBALL_CAT.update(SCREEN)


        HOCKEY_CAT = Button(image=pygame.transform.scale(GRAY_RECT, (250, 50)), pos=(645, 405), 
                            text_input="NHL", font=press_start_font(22), base_color=SEAFOAM, hovering_color=WHITE)
        HOCKEY_CAT.changeColor(PLAY_MOUSE_POS)
        HOCKEY_CAT.update(SCREEN)


        # Back Button #

        PLAY_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                            text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    CLICK.play()
                    main_menu()
                if BASEBALL_CAT.checkForInput(PLAY_MOUSE_POS):
                    CLICK.play()
                    baseball_rules()
                if FOOTBALL_CAT.checkForInput(PLAY_MOUSE_POS):
                    CLICK.play()
                    football_rules()

        pygame.display.update()
  

# Contact Screen Page #

def contact():
    while True:
        CONTACT_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        CONTACT_TEXT = press_start_font(30).render("CREATED BY MATT BARLETTA", True, POWDER_BLUE)
        CONTACT_RECT = CONTACT_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(CONTACT_TEXT, CONTACT_RECT)

        EMAIL_TEXT = press_start_font(30).render("CONTACT AT MATTBARLETTA7@GMAIL.COM", True, POWDER_BLUE)
        EMAIL_RECT = EMAIL_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(EMAIL_TEXT, EMAIL_RECT)

        DONATE_TEXT = press_start_font(30).render("DONATE VENMO @BARLETTA8413", True, POWDER_BLUE)
        DONATE_RECT = DONATE_TEXT.get_rect(center=(640, 380))
        SCREEN.blit(DONATE_TEXT, DONATE_RECT)        

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
                    CLICK.play()
                    main_menu()

        pygame.display.update()

# Baseball Rules Page #

def baseball_rules():
    while True:
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        pygame.draw.rect(SCREEN, GRAY, (390, 110, 500, 500))

        RULES_TEXT = press_start_font(30).render("RULES", True, POWDER_BLUE)
        RULES_RECT = RULES_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(RULES_TEXT, RULES_RECT)

        RULES_PLAY = Button(None, pos=(640, 555), 
                        text_input="PLAY", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        RULES_PLAY.changeColor(RULES_MOUSE_POS)
        RULES_PLAY.update(SCREEN)

        RULES_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        # RULES_BODY = BASEBALL_RULES.get_rect(center=(640,350))
        # SCREEN.blit(BASEBALL_RULES, RULES_BODY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    CLICK.play()
                    play_cat()
                if RULES_PLAY.checkForInput(RULES_MOUSE_POS):
                    CLICK.play()
                    baseball()

        pygame.display.update()

# Baseball Page Game Loop #

def baseball():
    START_TIME = pygame.time.get_ticks()
    PLAYER_INPUT = ""
    CHECK_ANS = ""
    SCORE = 0
    LIVES = 3
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    RANDOM_START = random.choice(ALPHABET)
    USED_NAMES = []
    DISPLAY = ""
    MLB_LIST = pd.read_csv('mlb_list.csv')
    TURNS = 0
    DOUBLE_STREAK = 0



    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill(WHITE)

        TITLE_TEXT = press_start_font(45).render("MLB", True, POWDER_BLUE)  #
        TITLE_RECT = TITLE_TEXT.get_rect(center=(655, 50))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        LETTER_TEXT = press_start_font(20).render("NAME A BASEBALL PLAYER WHOSE NAME STARTS WITH:", True, GRAY)     #
        LETTER_RECT = LETTER_TEXT.get_rect(center=(640, 110))
        SCREEN.blit(LETTER_TEXT, LETTER_RECT)

        QUIT_BUT = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="QUIT", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        QUIT_BUT.changeColor(MOUSE_POS)
        QUIT_BUT.update(SCREEN)

        SCREEN.blit(INPUT_BG, [250,550])

        SCREEN.blit(HEART, [1020, 300])
        SCREEN.blit(HEART, [1070, 300])
        SCREEN.blit(HEART, [1120, 300])
        
        disp_play_letter(RANDOM_START)

        TOTAL_TIME = pygame.time.get_ticks()

        if TOTAL_TIME - START_TIME > 15000:
            DISPLAY = "out of time"
            INCORRECT.play()
            START_TIME = TOTAL_TIME
            LIVES -= 1

        if 1000 > TOTAL_TIME - START_TIME > 0:
            disp_timer("15", GRAY) 
        if 2000 > TOTAL_TIME - START_TIME > 1000:
            disp_timer("14", GRAY) 
        if 3000 > TOTAL_TIME - START_TIME > 2000:
            disp_timer("13", GRAY)  
        if 4000 > TOTAL_TIME - START_TIME > 3000:
            disp_timer("12", GRAY)   
        if 5000 > TOTAL_TIME - START_TIME > 4000:
            disp_timer("11", GRAY)           
        if 6000 > TOTAL_TIME - START_TIME > 5000:
            disp_timer("10", GRAY)
        elif 7000 > TOTAL_TIME - START_TIME > 6000:
            disp_timer("9", GRAY)
        elif 8000 > TOTAL_TIME - START_TIME > 7000:
            disp_timer("8", GRAY)
        elif 9000 > TOTAL_TIME - START_TIME > 8000:
            disp_timer("7", GRAY)
        elif 10000 > TOTAL_TIME - START_TIME > 9000:
            disp_timer("6", GRAY)
        elif 11000 > TOTAL_TIME - START_TIME > 10000:
            disp_timer("5", GRAY)
        elif 12000 > TOTAL_TIME - START_TIME > 11000:
            disp_timer("4", GRAY)
        elif 13000 > TOTAL_TIME - START_TIME > 12000:
            disp_timer("3", RED)
        elif 14000 > TOTAL_TIME - START_TIME > 13000:
            disp_timer("2", RED)
        elif 15000 > TOTAL_TIME - START_TIME > 14000:
            disp_timer("1", RED)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUT.checkForInput(MOUSE_POS):
                    CLICK.play()
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
                    START_TIME = TOTAL_TIME

                    if SCORE == 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6][0] == RANDOM_START and MLB_LIST['name'].eq(PLAYER_INPUT[:-6]).any():
                            CHECK_ANS = PLAYER_INPUT[:-6]
                            FIRST_LETTER = PLAYER_INPUT[0]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"
                            CORRECT.play()
                            USED_NAMES.append(CHECK_ANS)

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]
                            
                            TURNS += 1

                            if FIRST_LETTER == PLAY_LETTER:
                                SCORE += 200
                                DOUBLE_STREAK += 1
                            else:
                                SCORE += 100
                                DOUBLE_STREAK = 0

                            if DOUBLE_STREAK > 1:
                                BONUS = (DOUBLE_STREAK - 1) * 100
                                SCORE += BONUS
                                DISPLAY = "streak"
                        else:
                            PLAYER_INPUT = ""                        
                            DISPLAY = "incorrect"
                            INCORRECT.play()
                            LIVES -= 1
                            
                    elif SCORE > 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6] in USED_NAMES:
                            PLAYER_INPUT = ""                        
                            DISPLAY = "dupe"
                            INCORRECT.play()
                            LIVES -= 1
                        elif PLAYER_INPUT[:-6][0] == PLAY_LETTER and MLB_LIST['name'].eq(PLAYER_INPUT[:-6]).any():

                            CHECK_ANS = PLAYER_INPUT[:-6]
                            FIRST_LETTER = PLAYER_INPUT[0]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"
                            CORRECT.play()  
                            USED_NAMES.append(CHECK_ANS)

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]
			    
                            TURNS += 1

                            if FIRST_LETTER == PLAY_LETTER:
                                SCORE += 200
                                DOUBLE_STREAK += 1
                            else:
                                SCORE += 100
                                DOUBLE_STREAK = 0

                            if DOUBLE_STREAK > 1:
                                BONUS = (DOUBLE_STREAK - 1) * 100
                                SCORE += BONUS
                                DISPLAY = "streak"
                            
                        else:
                            DISPLAY = "incorrect"
                            INCORRECT.play()
                            PLAYER_INPUT = ""
                            LIVES -= 1
                    
                        
                          
        # Change display whether the answer is correct or incorrect #
        if DISPLAY == "correct":
            disp_ans(CHECK_ANS)
            hide_prev_letter()
            disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "dupe":
            dupe_ans()
            hide_prev_letter()
            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "incorrect":
            wrong_ans()
            hide_prev_letter()
            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "out of time":
            if LIVES == 2:
                no_time_1()
                hide_prev_letter()
            elif LIVES == 1:
                no_time_2()
                hide_prev_letter()

            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "streak":
            disp_streak(DOUBLE_STREAK)
            disp_ans(CHECK_ANS)
            hide_prev_letter()
            disp_play_letter(PLAY_LETTER)
        
        # Call Functions to display elements that are always on the screen #            
               
        disp_type(PLAYER_INPUT, GRAY, 655, 595)
        disp_score(SCORE, 150, 350, GRAY)
        if LIVES == 2:
            hide_hearts(975, 325, 120, 50)
        elif LIVES == 1:
            hide_hearts(975, 325, 170, 50)

        # Game Over Page #
        def game_over():
            INITIALS = ''
            SAVES = 0

            while True:
                GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.fill(WHITE)

                pygame.draw.rect(SCREEN, GRAY, (390, 50, 500, 600))

                GAME_OVER_TEXT = press_start_font(30).render("GAME OVER", True, POWDER_BLUE)
                GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 100))
                SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

                NAME_TEXT = press_start_font(30).render("NAME:", True, POWDER_BLUE)
                NAME_RECT = NAME_TEXT.get_rect(center=(560, 510))
                SCREEN.blit(NAME_TEXT, NAME_RECT)

                HIGH_TEXT = press_start_font(30).render("HIGHSCORES", True, POWDER_BLUE)
                HIGH_RECT = HIGH_TEXT.get_rect(center=(640, 230))
                SCREEN.blit(HIGH_TEXT, HIGH_RECT)


                disp_score(SCORE, 640, 150, SEAFOAM)
                

                PLAY_AGAIN = Button(None, pos=(639, 565), 
                                text_input="PLAY AGAIN", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
                PLAY_AGAIN.changeColor(GAME_OVER_MOUSE_POS)
                PLAY_AGAIN.update(SCREEN)

                SHARE_TEXT = press_start_font(30).render("SHARE", True, POWDER_BLUE)
                SHARE_RECT = SHARE_TEXT.get_rect(center=(563, 620))
                SCREEN.blit(SHARE_TEXT, SHARE_RECT)

        

                GAME_OVER_HOME = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                                text_input="HOME", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

                GAME_OVER_HOME.changeColor(GAME_OVER_MOUSE_POS)
                GAME_OVER_HOME.update(SCREEN)

                TWIT_BUT = Button(image=pygame.transform.scale(TWITTER, (100, 50)), pos=(700, 620), 
                                text_input="", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
                TWIT_BUT.update(SCREEN)

                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        CLICK.play()
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if GAME_OVER_HOME.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            main_menu()
                        if PLAY_AGAIN.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            baseball()
                        if TWIT_BUT.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            webbrowser.open(f"https://twitter.com/intent/tweet?text=I%20Named%20{TURNS}%20MLB%20Baseball%20Players%20For%20{SCORE}%20Points%20via%20the%20NAME%20GAME%20%3A&url=http%3A%2F%2Fcbb-elo.com")     #

                    if event.type == pygame.KEYDOWN:
                        char_int = pygame.key.name(event.key)
                        INITIALS += char_int
                                                
                        if len(INITIALS) > 3:
                            INITIALS = INITIALS[:3]
                        
                        if event.key == pygame.K_BACKSPACE:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_SPACE:
                            INITIALS = INITIALS[:-5]
                            INITIALS += " "
                        if event.key == pygame.K_TAB:
                            INITIALS = INITIALS[:-3]
                        if event.key == pygame.K_CAPSLOCK:
                            INITIALS = INITIALS[:-9]                   
                        if event.key == pygame.K_RSHIFT:
                            INITIALS = INITIALS[:-11]
                        if event.key == pygame.K_LSHIFT:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_RCTRL:
                            INITIALS = INITIALS[:-10]  
                        if event.key == pygame.K_LCTRL:
                            INITIALS = INITIALS[:-9]  
                        if event.key == pygame.K_RALT:
                            INITIALS = INITIALS[:-9]
                        if event.key == pygame.K_LALT:
                            INITIALS = INITIALS[:-8] 
                        if event.key == pygame.K_UP:
                            INITIALS = INITIALS[:-2]
                        if event.key == pygame.K_DOWN:
                            INITIALS = INITIALS[:-4]
                        if event.key == pygame.K_LEFT:
                            INITIALS = INITIALS[:-4]
                        if event.key == pygame.K_RIGHT:
                            INITIALS = INITIALS[:-5]
                        if event.key == pygame.K_RMETA:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_LMETA:
                            INITIALS = INITIALS[:-9]
                        if event.key == pygame.K_NUMLOCK:
                            INITIALS = INITIALS[:-7]
                        if event.key == pygame.K_KP_ENTER:
                            INITIALS = INITIALS[:-5]
                        if event.key == pygame.K_RETURN:
                            if SAVES == 0:
                                #INITIALS = INITIALS[:-6]

                                if INITIALS == "":
                                    INITIALS = "aaa"

                                SCORE_INIT = {'name': [INITIALS], 
                                                'score': [SCORE]
                                                }
                                HIGHSCORE_DF = pd.DataFrame(SCORE_INIT)
                                HIGHSCORE_DF = HIGHSCORE_DF.sort_values(by=['score'])
                                HIGHSCORE_DF.to_csv('mlb_highscores.csv', mode='a', index=False, header=False)              #
                                INITIALS = ""
                            else:
                                INITIALS = ""
                            
                            SAVES += 1
                            
                        
                disp_type(INITIALS, WHITE, 700, 510)
                disp_high_scores('mlb')

                pygame.display.update()     

        if LIVES == 0:
            game_over()

        pygame.display.update()
        
# Football Rules Page

def football_rules():
    while True:
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(WHITE)

        pygame.draw.rect(SCREEN, GRAY, (390, 110, 500, 500))

        RULES_TEXT = press_start_font(30).render("RULES", True, POWDER_BLUE)
        RULES_RECT = RULES_TEXT.get_rect(center=(640, 150))
        SCREEN.blit(RULES_TEXT, RULES_RECT)

        RULES_PLAY = Button(None, pos=(640, 555), 
                        text_input="PLAY", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
        RULES_PLAY.changeColor(RULES_MOUSE_POS)
        RULES_PLAY.update(SCREEN)

        RULES_BACK = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="BACK", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        # RULES_BODY = FOOTBALL_RULES.get_rect(center=(640,350))
        # SCREEN.blit(FOOTBALL_RULES, RULES_BODY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                    CLICK.play()
                    play_cat()
                if RULES_PLAY.checkForInput(RULES_MOUSE_POS):
                    CLICK.play()
                    football()

        pygame.display.update()

# Football Game Loop #

def football():
    START_TIME = pygame.time.get_ticks()
    PLAYER_INPUT = ""
    CHECK_ANS = ""
    SCORE = 0
    LIVES = 3
    ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    RANDOM_START = random.choice(ALPHABET)
    USED_NAMES = []
    DISPLAY = ""
    NFL_LIST = pd.read_csv('nfl_list.csv')
    TURNS = 0
    DOUBLE_STREAK = 0



    while True:
        MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill(WHITE)

        TITLE_TEXT = press_start_font(45).render("NFL", True, POWDER_BLUE)
        TITLE_RECT = TITLE_TEXT.get_rect(center=(655, 50))
        SCREEN.blit(TITLE_TEXT, TITLE_RECT)

        LETTER_TEXT = press_start_font(20).render("NAME A FOOTBALL PLAYER WHOSE NAME STARTS WITH:", True, GRAY)
        LETTER_RECT = LETTER_TEXT.get_rect(center=(640, 110))
        SCREEN.blit(LETTER_TEXT, LETTER_RECT)

  
        QUIT_BUT = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                        text_input="QUIT", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

        QUIT_BUT.changeColor(MOUSE_POS)
        QUIT_BUT.update(SCREEN)

        SCREEN.blit(INPUT_BG, [250,550])

        SCREEN.blit(HEART, [1020, 300])
        SCREEN.blit(HEART, [1070, 300])
        SCREEN.blit(HEART, [1120, 300])
        
        disp_play_letter(RANDOM_START)

        TOTAL_TIME = pygame.time.get_ticks()

        if TOTAL_TIME - START_TIME > 15000:
            DISPLAY = "out of time"
            INCORRECT.play()
            START_TIME = TOTAL_TIME
            LIVES -= 1

        if 1000 > TOTAL_TIME - START_TIME > 0:
            disp_timer("15", GRAY) 
        if 2000 > TOTAL_TIME - START_TIME > 1000:
            disp_timer("14", GRAY) 
        if 3000 > TOTAL_TIME - START_TIME > 2000:
            disp_timer("13", GRAY)  
        if 4000 > TOTAL_TIME - START_TIME > 3000:
            disp_timer("12", GRAY)   
        if 5000 > TOTAL_TIME - START_TIME > 4000:
            disp_timer("11", GRAY)           
        if 6000 > TOTAL_TIME - START_TIME > 5000:
            disp_timer("10", GRAY)
        elif 7000 > TOTAL_TIME - START_TIME > 6000:
            disp_timer("9", GRAY)
        elif 8000 > TOTAL_TIME - START_TIME > 7000:
            disp_timer("8", GRAY)
        elif 9000 > TOTAL_TIME - START_TIME > 8000:
            disp_timer("7", GRAY)
        elif 10000 > TOTAL_TIME - START_TIME > 9000:
            disp_timer("6", GRAY)
        elif 11000 > TOTAL_TIME - START_TIME > 10000:
            disp_timer("5", GRAY)
        elif 12000 > TOTAL_TIME - START_TIME > 11000:
            disp_timer("4", GRAY)
        elif 13000 > TOTAL_TIME - START_TIME > 12000:
            disp_timer("3", RED)
        elif 14000 > TOTAL_TIME - START_TIME > 13000:
            disp_timer("2", RED)
        elif 15000 > TOTAL_TIME - START_TIME > 14000:
            disp_timer("1", RED)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CLICK.play()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUT.checkForInput(MOUSE_POS):
                    CLICK.play()
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
                    START_TIME = TOTAL_TIME

                    if SCORE == 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6][0] == RANDOM_START and NFL_LIST['name'].eq(PLAYER_INPUT[:-6]).any():
                            CHECK_ANS = PLAYER_INPUT[:-6]
                            FIRST_LETTER = PLAYER_INPUT[0]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"
                            USED_NAMES.append(CHECK_ANS)
                            CORRECT.play()

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]
                            
                            TURNS += 1

                            if FIRST_LETTER == PLAY_LETTER:
                                SCORE += 200
                                DOUBLE_STREAK += 1
                            else:
                                SCORE += 100
                                DOUBLE_STREAK = 0

                            if DOUBLE_STREAK > 1:
                                BONUS = (DOUBLE_STREAK - 1) * 100
                                SCORE += BONUS
                                DISPLAY = "streak"
                        else:
                            PLAYER_INPUT = ""                        
                            DISPLAY = "incorrect"
                            INCORRECT.play()
                            LIVES -= 1
                            
                    elif SCORE > 0 and len(PLAYER_INPUT) > 6:
                        if PLAYER_INPUT[:-6] in USED_NAMES:
                            PLAYER_INPUT = ""                        
                            DISPLAY = "dupe"
                            INCORRECT.play()
                            LIVES -= 1
                        elif PLAYER_INPUT[:-6][0] == PLAY_LETTER and NFL_LIST['name'].eq(PLAYER_INPUT[:-6]).any():

                            CHECK_ANS = PLAYER_INPUT[:-6]
                            FIRST_LETTER = PLAYER_INPUT[0]
                            PLAYER_INPUT = ""
                            DISPLAY = "correct"
                            CORRECT.play() 
                            USED_NAMES.append(CHECK_ANS)

                            NAME_BREAK_INDEX = CHECK_ANS.find(" ")
                            PLAY_LETTER_INDEX = NAME_BREAK_INDEX + 1
                            PLAY_LETTER = CHECK_ANS[PLAY_LETTER_INDEX]
			    
                            TURNS += 1

                            if FIRST_LETTER == PLAY_LETTER:
                                SCORE += 200
                                DOUBLE_STREAK += 1
                            else:
                                SCORE += 100
                                DOUBLE_STREAK = 0

                            if DOUBLE_STREAK > 1:
                                BONUS = (DOUBLE_STREAK - 1) * 100
                                SCORE += BONUS
                                DISPLAY = "streak"
                            
                        else:
                            DISPLAY = "incorrect"
                            INCORRECT.play()
                            PLAYER_INPUT = ""
                            LIVES -= 1
                    
                        
                          
        # Change display whether the answer is correct or incorrect #
        if DISPLAY == "correct":
            disp_ans(CHECK_ANS)
            hide_prev_letter()
            disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "dupe":
            dupe_ans()
            hide_prev_letter()
            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "incorrect":
            wrong_ans()
            hide_prev_letter()
            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "out of time":
            if LIVES == 2:
                no_time_1()
                hide_prev_letter()
            elif LIVES == 1:
                no_time_2()
                hide_prev_letter()

            if SCORE == 0:
                disp_play_letter(RANDOM_START)
            else:
                disp_play_letter(PLAY_LETTER)
        elif DISPLAY == "streak":
            disp_streak(DOUBLE_STREAK)
            disp_ans(CHECK_ANS)
            hide_prev_letter()
            disp_play_letter(PLAY_LETTER)
        
        # Call Functions to display elements that are always on the screen #            
               
        disp_type(PLAYER_INPUT, GRAY, 655, 595)
        disp_score(SCORE, 150, 350, GRAY)
        if LIVES == 2:
            hide_hearts(975, 325, 120, 50)
        elif LIVES == 1:
            hide_hearts(975, 325, 170, 50)

        # Game Over Page #
        def game_over():
            INITIALS = ''
            SAVES = 0

            while True:
                GAME_OVER_MOUSE_POS = pygame.mouse.get_pos()

                SCREEN.fill(WHITE)

                pygame.draw.rect(SCREEN, GRAY, (390, 50, 500, 600))

                GAME_OVER_TEXT = press_start_font(30).render("GAME OVER", True, POWDER_BLUE)
                GAME_OVER_RECT = GAME_OVER_TEXT.get_rect(center=(640, 100))
                SCREEN.blit(GAME_OVER_TEXT, GAME_OVER_RECT)

                NAME_TEXT = press_start_font(30).render("NAME:", True, POWDER_BLUE)
                NAME_RECT = NAME_TEXT.get_rect(center=(560, 510))
                SCREEN.blit(NAME_TEXT, NAME_RECT)

                HIGH_TEXT = press_start_font(30).render("HIGHSCORES", True, POWDER_BLUE)
                HIGH_RECT = HIGH_TEXT.get_rect(center=(640, 230))
                SCREEN.blit(HIGH_TEXT, HIGH_RECT)


                disp_score(SCORE, 640, 150, SEAFOAM)
                

                PLAY_AGAIN = Button(None, pos=(639, 565), 
                                text_input="PLAY AGAIN", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
                PLAY_AGAIN.changeColor(GAME_OVER_MOUSE_POS)
                PLAY_AGAIN.update(SCREEN)

                SHARE_TEXT = press_start_font(30).render("SHARE", True, POWDER_BLUE)
                SHARE_RECT = SHARE_TEXT.get_rect(center=(563, 620))
                SCREEN.blit(SHARE_TEXT, SHARE_RECT)

        

                GAME_OVER_HOME = Button(image=pygame.transform.scale(GRAY_RECT, (130, 50)), pos=(80, 50), 
                                text_input="HOME", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)

                GAME_OVER_HOME.changeColor(GAME_OVER_MOUSE_POS)
                GAME_OVER_HOME.update(SCREEN)

                TWIT_BUT = Button(image=pygame.transform.scale(TWITTER, (100, 50)), pos=(700, 620), 
                                text_input="", font=press_start_font(30), base_color=SEAFOAM, hovering_color=WHITE)
                TWIT_BUT.update(SCREEN)

                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        CLICK.play()
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if GAME_OVER_HOME.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            main_menu()
                        if PLAY_AGAIN.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            football()
                        if TWIT_BUT.checkForInput(GAME_OVER_MOUSE_POS):
                            CLICK.play()
                            webbrowser.open(f"https://twitter.com/intent/tweet?text=I%20Named%20{TURNS}%20NFL%20Football%20Players%20For%20{SCORE}%20Points%20via%20the%20NAME%20GAME%20%3A&url=http%3A%2F%2Fcbb-elo.com")

                    if event.type == pygame.KEYDOWN:
                        char_int = pygame.key.name(event.key)
                        INITIALS += char_int
                                                
                        if len(INITIALS) > 3:
                            INITIALS = INITIALS[:3]
                        
                        if event.key == pygame.K_BACKSPACE:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_SPACE:
                            INITIALS = INITIALS[:-5]
                            INITIALS += " "
                        if event.key == pygame.K_TAB:
                            INITIALS = INITIALS[:-3]
                        if event.key == pygame.K_CAPSLOCK:
                            INITIALS = INITIALS[:-9]                   
                        if event.key == pygame.K_RSHIFT:
                            INITIALS = INITIALS[:-11]
                        if event.key == pygame.K_LSHIFT:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_RCTRL:
                            INITIALS = INITIALS[:-10]  
                        if event.key == pygame.K_LCTRL:
                            INITIALS = INITIALS[:-9]  
                        if event.key == pygame.K_RALT:
                            INITIALS = INITIALS[:-9]
                        if event.key == pygame.K_LALT:
                            INITIALS = INITIALS[:-8] 
                        if event.key == pygame.K_UP:
                            INITIALS = INITIALS[:-2]
                        if event.key == pygame.K_DOWN:
                            INITIALS = INITIALS[:-4]
                        if event.key == pygame.K_LEFT:
                            INITIALS = INITIALS[:-4]
                        if event.key == pygame.K_RIGHT:
                            INITIALS = INITIALS[:-5]
                        if event.key == pygame.K_RMETA:
                            INITIALS = INITIALS[:-10]
                        if event.key == pygame.K_LMETA:
                            INITIALS = INITIALS[:-9]
                        if event.key == pygame.K_NUMLOCK:
                            INITIALS = INITIALS[:-7]
                        if event.key == pygame.K_KP_ENTER:
                            INITIALS = INITIALS[:-5]
                        if event.key == pygame.K_RETURN:
                            if SAVES == 0:
                                #INITIALS = INITIALS[:-6]

                                if INITIALS == "":
                                    INITIALS = "aaa"

                                SCORE_INIT = {'name': [INITIALS], 
                                                'score': [SCORE]
                                                }
                                HIGHSCORE_DF = pd.DataFrame(SCORE_INIT)
                                HIGHSCORE_DF = HIGHSCORE_DF.sort_values(by=['score'])
                                HIGHSCORE_DF.to_csv('nfl_highscores.csv', mode='a', index=False, header=False)
                                INITIALS = ""
                            else:
                                INITIALS = ""
                            
                            SAVES += 1
                            
                        
                disp_type(INITIALS, WHITE, 700, 510)
                disp_high_scores('nfl')

                pygame.display.update()     

        if LIVES == 0:
            game_over()

        pygame.display.update()


# Start the Game #--------------------------------------------------------------------------------------------------


CLOCK.tick(60)

main_menu()