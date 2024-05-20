import time
import random
from colorama import init, Fore, Back, Style
import sys
import os

# Sidenote: Tak szczerze kompletnie nie jest to potrzebne do niczego ale i tak tego używam

def clear_console():
    # Wyczyść konsolę
    print("\033c")

def toggle_color():
    # Funkcja do zmiany koloru tekstu na czarny lub biały
    colors = ["\033[30m", "\033[97m"]
    return random.choice(colors)

def scary_effect(text, duration=0.1, num_iterations=20):
    for _ in range(num_iterations):
        clear_console()
        print(toggle_color() + text)
        time.sleep(duration)

# Tekst, który będzie migotać
text_to_flicker = "Coś tam w ciemności..."

# Czas trwania migotania (w sekundach)
duration = 0.1

# Ilość iteracji migotania
num_iterations = 20

# Wywołaj funkcję do efektu "ciemności i oświetlenia": scary_effect(text_to_flicker, duration, num_iterations)

def mrygnij(text, blink_duration=0.1, num_blinks=10):
    for _ in range(num_blinks):
        clear_console()
        print(text)
        time.sleep(blink_duration)
        clear_console()
        time.sleep(blink_duration)



def clear_console():
    # Wyczyść konsolę
    print("\033c")


def blink_random_characters(text, num_blinks, blink_duration=0.1):
    for _ in range(num_blinks):
        clear_console()
        modified_text = ""
        for char in text:
            if random.random() < 0.5:  # Przy około 50% prawdopodobieństwa migaj znak
                modified_text += " "
            else:
                modified_text += char
        print(modified_text)
        time.sleep(blink_duration)
text_to_blink = "ITS ME"
num_blinks = 15
blink_duration = 0.1

def apply_glitch_effect():
    for _ in range(10):  # Losowa liczba glitchy
        x = random.randint(0, 79)  # Losowa kolumna
        y = random.randint(0, 24)  # Losowy wiersz
        char = chr(random.randint(32, 126))  # Losowy znak ASCII
        color = random.choice([Fore.RED, Fore.YELLOW, Fore.GREEN])  # Losowy kolor
        print(f"\033[{y};{x}H{color}{char}", end="")

def gowno():
    original_text = "Halo? Słychać mnie?"
    for _ in range(50):
        clear_screen()
        corrupted_text = generate_corrupted_text(original_text)
        print(corrupted_text)
        time.sleep(0.1)

def generate_corrupted_text(text):
    corrupted_text = list(text)
    num_corruptions = random.randint(1, 5)

    for _ in range(num_corruptions):
        position = random.randint(0, len(text) - 1)
        new_character = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>?/")
        corrupted_text[position] = new_character

    return ''.join(corrupted_text)

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

import pygame

def jumpscare():
    pygame.mixer.init()
    pygame.mixer.music.load('jumpscare_sound.mp3')
    pygame.mixer.music.play()
