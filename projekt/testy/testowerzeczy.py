# import sys
# import time
# import os


# # animowany tekst (dialogi)

# def animate_text(text, delay=0.03):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(delay)

# # Przykład użycia
# animate_text("abc")
# print('\n')



# from colorama import Fore, Back, Style, init
# import time
# import random

# # smieszny pozar
# init(autoreset=True)  # Inicjacja colorama

# def print_fire(fire_pixels):
#     for row in fire_pixels:
#         for pixel in row:
#             if pixel == 0:
#                 print(Fore.BLACK + Back.RED + ' ', end='')
#             elif pixel == 1:
#                 print(Fore.RED + Back.RED + ' ', end='')
#             elif pixel == 2:
#                 print(Fore.YELLOW + Back.RED + ' ', end='')
#         print()

# def update_fire(fire_pixels):
#     for row in range(len(fire_pixels) - 1):
#         for col in range(len(fire_pixels[0])):
#             decay = random.randint(0, 2)
#             decayed_pixel = max(0, fire_pixels[row + 1][col] - decay)
#             fire_pixels[row][col] = decayed_pixel

# def main():
#     width = 80
#     height = 24
#     fire_pixels = [[0 for _ in range(width)] for _ in range(height)]

#     try:
#         while True:
#             # Tworzenie nowego rzędu na górze z losowym płomieniem
#             for col in range(width):
#                 fire_pixels[0][col] = random.randint(0, 2)

#             update_fire(fire_pixels)
#             print_fire(fire_pixels)
#             time.sleep(0.05)
#             print('\033[H')  # Przenieś kursor na początek konsoli
#     except KeyboardInterrupt:
#         print("Koniec animacji.")


# czy_main = input('czy chcesz main? ')
# if czy_main == 'T':
#     main()
# else:
#     sys.exit

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def blink_text(text, blink_duration=0.1, num_blinks=10):
#     for _ in range(num_blinks):
#         clear_console()
#         print(text)
#         time.sleep(blink_duration)
#         clear_console()
#         time.sleep(blink_duration)

# # Tekst do migania
# text_to_blink = "ITS ME"

# # Czas trwania migania (w sekundach)
# blink_duration = 0.1

# # Ilość mignięć
# num_blinks = 10

# blink_text(text_to_blink, blink_duration, num_blinks)


# import time
# import random

# def clear_console():
#     # Wyczyść konsolę
#     print("\033c")

# def toggle_color():
#     # Funkcja do zmiany koloru tekstu na czarny lub biały
#     colors = ["\033[30m", "\033[97m"]
#     return random.choice(colors)

# def scary_effect(text, duration=0.1, num_iterations=20):
#     for _ in range(num_iterations):
#         clear_console()
#         print(toggle_color() + text)
#         time.sleep(duration)

# # Tekst, który będzie migotać
# text_to_flicker = "Coś tam w ciemności..."

# # Czas trwania migotania (w sekundach)
# duration = 0.1

# # Ilość iteracji migotania
# num_iterations = 20

# # Wywołaj funkcję do efektu "ciemności i oświetlenia"
# scary_effect(text_to_flicker, duration, num_iterations)


# import random
# import time
# import sys

# def gowno():
#     original_text = "To jest tekst z losowymi zakloceniami."
#     for _ in range(50):
#         clear_screen()
#         corrupted_text = generate_corrupted_text(original_text)
#         print(corrupted_text)
#         time.sleep(0.1)

# def generate_corrupted_text(text):
#     corrupted_text = list(text)
#     num_corruptions = random.randint(1, 5)

#     for _ in range(num_corruptions):
#         position = random.randint(0, len(text) - 1)
#         new_character = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>?/")
#         corrupted_text[position] = new_character

#     return ''.join(corrupted_text)

# def clear_screen():
#     if sys.platform.startswith('win'):
#         os.system('cls')
#     else:
#         os.system('clear')

# gowno()


# import time

# def fade_in(text, duration):
#     for i in range(1, 11):
#         brightness = i / 10  # Zwiększ jasność od 0 do 1
#         print(f"\033[1;37;40m\033[2;0f{text}")
#         time.sleep(duration / 10)

# def fade_out(text, duration):
#     for i in range(1, 11):
#         brightness = 1 - i / 10  # Zmniejsz jasność od 1 do 0
#         print(f"\033[1;37;40m\033[2;0f{text}")
#         time.sleep(duration / 10)

# def sraka():
#     text = "Tekst z efektem Fade In i Fade Out"
#     duration = 2  # Czas trwania efektu w sekundach

#     fade_in(text, duration)
#     time.sleep(2)  # Poczekaj 2 sekundy
#     fade_out(text, duration)

# sraka()


# import random
# import time

# def koszmar():
#     for _ in range(10):
#         print("Znajdujesz się w mrocznym lesie...")
#         time.sleep(1)
#         print("Wszystko staje się niewyraźne...")
#         time.sleep(1)
#         print("Słyszysz dziwne dźwięki w oddali...")
#         time.sleep(1)

#         # Zmiana wizualna
#         if random.random() < 0.5:
#             print("Twój ekran zaczyna migotać i robi się coraz mroczniejszy...")
#         else:
#             print("Wszystko wokół zaczyna drżeć...")
        
#         time.sleep(2)

#         # Nagłe zdarzenia
#         if random.random() < 0.5:
#             print("Nagle coś przemknęło obok ciebie...")
#         else:
#             print("Zdajesz sobie sprawę, że jesteś sam w lesie...")
#         time.sleep(2)
    
#     print("Wszystko staje się niespójne i wydajesz się być w labiryncie...")
#     time.sleep(3)
#     print("Coś czujesz, że cię obserwuje...")
#     time.sleep(2)
#     print("Nagle jesteś otoczony przez duchy...")
#     time.sleep(2)
#     print("...")
#     time.sleep(1)
#     print("I nagle obudziłeś się z koszmaru.")

# koszmar()


import random
import time

# def przeniesienie_do_innego_swiat():
#     print("Nagle tracisz przytomność i czujesz, że jesteś przenoszony do innego świata...")
#     time.sleep(2)
#     print("Wokół Ciebie wszystko jest ciemne i niespójne...")
#     time.sleep(2)
#     print("Słyszysz przerażający dźwięk ogłuszenia...")
#     time.sleep(2)
#     print("Po 10 sekundach budzisz się w szpitalu...")
#     time.sleep(2)
#     print("Musisz uciekać z powrotem na walkę!")

# def walka():
#     print("Walczyłeś z przerażającymi stworzeniami przez całą noc...")
#     time.sleep(2)
#     print("Twoje siły opadają, ale wiesz, że musisz kontynuować walkę...")
#     time.sleep(2)
#     print("Nagle tracisz przytomność i zostajesz przeniesiony do innego świata...")

# def cycuszki():
#     while True:
#         print("Jesteś w ciemnym lesie, otoczony nieznanymi dźwiękami...")
#         time.sleep(2)
#         print("Musisz walczyć ze strachem i przerażającymi stworzeniami...")
#         time.sleep(2)

#         if random.random() < 0.1:
#             przeniesienie_do_innego_swiat()
#         else:
#             walka()

# cycuszki()

# import pygame
# def jumpscare():
#     pygame.mixer.init()
#     pygame.mixer.music.load('jumpscare_sound.mp3')
#     pygame.mixer.music.play()
# jumpscare()

# print("   /\ ")
# print("  /  \ ")
# print(" /    \ ")
# print(" \    / ")
# print("  \  / ")
# print("   \/ ")

# import curses

# # Inicjalizacja ekranu
# stdscr = curses.initscr()
# curses.curs_set(0)  # Wyłącz migający kursor
# stdscr.keypad(1)    # Włącz obsługę klawiatury
# curses.start_color() # Włącz obsługę kolorów

# # Tworzenie okna
# win = curses.newwin(10, 40, 0, 0)
# win.border(0)  # Dodaj obramowanie do okna

# # Wprowadź kod interfejsu konsolowego

# # Zakończenie trybu curses
# curses.endwin()

# print('s')
# print('s')
# print('s')
# print('s')
# print('s')


# import curses

# def main(stdscr):
#     # Ustaw konsolę
#     curses.curs_set(0)
#     stdscr.nodelay(1)
#     stdscr.timeout(100)

#     # Lista opcji menu
#     menu_options = ["Start", "Opcje", "Wyjście"]
#     current_option = 0

#     while True:
#         stdscr.clear()

#         # Wyświetl opcje menu
#         for i, option in enumerate(menu_options):
#             if i == current_option:
#                 stdscr.addstr(i, 0, option, curses.A_BOLD)
#             else:
#                 stdscr.addstr(i, 0, option)

#         # Odczytaj klawisze
#         key = stdscr.getch()

#         if key == ord('q'):
#             break  # Wyjście z gry
#         elif key == curses.KEY_UP and current_option > 0:
#             current_option -= 1
#         elif key == curses.KEY_DOWN and current_option < len(menu_options) - 1:
#             current_option += 1
#         elif key == 10:  # Enter
#             # Obsłuż wybór opcji
#             if current_option == 0:
#                 stdscr.addstr(len(menu_options) + 1, 0, "Rozpoczęto grę!")
#             elif current_option == 1:
#                 stdscr.addstr(len(menu_options) + 1, 0, "Otworzono opcje.")
#             elif current_option == 2:
#                 return


# curses.wrapper(main)

# import time

# # Inicjalizacja zegara
# start_time = time.time()

# # Główna pętla gry
# while True:
#     # Oblicz czas, jaki minął od rozpoczęcia gry
#     current_time = time.time()
#     elapsed_time = current_time - start_time

#     # Przekształć czas na bardziej przyjazny dla odczytu format (np. minuty i sekundy)
#     minutes = int(elapsed_time // 60)
#     seconds = int(elapsed_time % 60)

#     # Wyświetl czas w konsoli
#     print(f"Czas gry: {minutes:02}:{seconds:02}")

#     # Tutaj dodaj kod obsługujący główną logikę gry

#     # Przerwij pętlę gry po jakimś czasie lub z jakiegoś innego powodu
#     if elapsed_time > 600:  # Przykładowo, gra trwa maksymalnie 10 minut
#         break

# # Koniec gry


# import time

# def display_game_timer(start_time, max_duration=600):
#     while True:
#         current_time = time.time()
#         elapsed_time = current_time - start_time

#         minutes = int(elapsed_time // 60)
#         seconds = int(elapsed_time % 60)

#         time_str = f"Czas gry: {minutes:02}:{seconds:02}"
#         print(time_str, end='\r')

#         if elapsed_time > max_duration:
#             break

#         time.sleep(1)  # Opóźnienie na 1 sekundę

#     # Wyczyść linię po zakończeniu timera
#     print(" " * len(time_str), end='\r')

# # Rozpocznij grę
# def start_game():
#     start_time = time.time()
    
#     # Tutaj umieść logikę rozgrywki

#     display_game_timer(start_time)  # Rozpocznij zegar

#     # Tutaj umieść więcej logiki gry

# # Rozpocznij grę
# start_game()


# import pygame
# import sys

# pygame.init()

# # Ustawienia menu
# menu_items = ["Nowa gra", "Opcje", "Wyjście"]
# selected_item = 0
# font = pygame.font.Font(None, 36)

# # Funkcja do wyboru elementu menu
# def select_item(item):
#     if item == "Nowa gra":
#         # Tutaj możesz dodać kod obsługi rozpoczęcia nowej gry
#         print("Rozpocznij nową grę")
#     elif item == "Opcje":
#         # Tutaj możesz dodać kod obsługi opcji
#         print("Otwórz opcje")
#     elif item == "Wyjście":
#         pygame.quit()
#         sys.exit()

# # Główna pętla gry
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 selected_item = (selected_item - 1) % len(menu_items)
#             elif event.key == pygame.K_DOWN:
#                 selected_item = (selected_item + 1) % len(menu_items)
#             elif event.key == pygame.K_RETURN:
#                 selected = menu_items[selected_item]
#                 select_item(selected)
#                 # Tutaj możesz dodać animację "fade out" lub "zmniejszenia"
#                 menu_items.pop(selected_item)  # Usuń wybrany element
#                 if not menu_items:
#                     pygame.quit()
#                     sys.exit()

#     # Rysowanie menu
#     screen = pygame.display.set_mode((400, 300))
#     screen.fill((0, 0, 0))

#     for i, item in enumerate(menu_items):
#         if i == selected_item:
#             text = font.render(item, True, (255, 0, 0))
#         else:
#             text = font.render(item, True, (255, 255, 255))
#         screen.blit(text, (150, 100 + i * 50))

#     pygame.display.update()


import pygame
import sys

# # Inicjalizacja Pygame
# pygame.init()

# # Ustawienia ekranu
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Moja Gra")

# # Kolor tła
# background_color = (0, 0, 0)

# # Funkcja do rozpoczęcia gry
# def start_game():
#     # Tutaj możesz dodać kod, który rozpocznie grę w trybie konsolowym
#     print("Gra rozpoczęta w trybie konsolowym")

# # Główna pętla gry
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_q:
#                 running = False
#             elif event.key == pygame.K_s:
#                 start_game()

#     # Wypełnienie tła
#     screen.fill(background_color)

#     # Wyświetlenie menu
#     font = pygame.font.Font(None, 36)
#     start_text = font.render("Start gry (S)", True, (255, 255, 255))
#     exit_text = font.render("Wyjście (Q)", True, (255, 255, 255))
#     screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 200))
#     screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, 300))

#     pygame.display.flip()

# # Zakończenie Pygame
# pygame.quit()
# sys.exit()

# import pygame
# from pygame.locals import *

# pygame.init()

# # Ustawienia ekranu
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Gra Retro")

# # Kolor tła
# background_color = (0, 0, 0)

# # Czcionka pixel art
# font = pygame.font.Font("pixel_font.ttf", 32)  # Pobierz odpowiednią czcionkę pixel art

# # Tekst w stylu retro
# retro_text = font.render("Gra Retro", True, (255, 255, 255))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False

#     screen.fill(background_color)

#     # Wyświetlenie tekstu w stylu retro na ekranie
#     screen.blit(retro_text, (screen_width // 2 - retro_text.get_width() // 2, screen_height // 2 - retro_text.get_height() // 2))

#     pygame.display.flip()

# pygame.quit()


import pygame

def kupsko():
    pygame.mixer.init()
    pygame.mixer.music.load('ultsombra.ogg')
    pygame.mixer.music.play()

kupsko()

import colorama
import random
import time

colorama.init()

def clear_console():
    print('\033c', end='')

def print_fire(fire_matrix):
    for row in fire_matrix:
        for cell in row:
            print(cell, end='')
        print()

# Zmiana warunku w update_fire
def update_fire(fire_matrix):
    for row in range(1, len(fire_matrix) - 1):
        for col in range(len(fire_matrix[row])):
            # Suma komórek sąsiednich
            neighbors_sum = (
                fire_matrix[row - 1][col - 1] +
                fire_matrix[row - 1][col] +
                fire_matrix[row - 1][col + 1] +
                fire_matrix[row][col - 1] +
                fire_matrix[row][col + 1] +
                fire_matrix[row + 1][col - 1] +
                fire_matrix[row + 1][col] +
                fire_matrix[row + 1][col + 1]
            )

            # Symulacja spadania iskier
            if random.randint(0, 10) > 7:
                fire_matrix[row - 1][col] = fire_matrix[row][col]
                fire_matrix[row][col] = ' '

            # Symulacja nowego płomienia
            elif neighbors_sum > 3 and fire_matrix[row][col] != ' ':
                fire_matrix[row][col] = random.choice(['#', ' ', ' ', ' '])

# Zmiana generowania macierzy ognia
def generate_fire(width, height):
    return [[' ' for _ in range(width)] for _ in range(height)]

def animate_fire(width, height):
    fire_matrix = generate_fire(width, height)

    while True:
        clear_console()
        update_fire(fire_matrix)
        print_fire(fire_matrix)
        time.sleep(0.1)

if __name__ == "__main__":
    animate_fire(80, 30)
