# importy i inne

import random
# importy z plików
from characters import Character, Sombra, Reinhardt, Widowmaker, Freddy, test, Ana, Zarya, dodatkowefunkcjepostaci
from enemies import Bastion, Kiriko, Roadhog, Echo, Cassidy, Lucio, Ashe, Springtrap, Hanzo, Roadhog
from boss import Orisa, Mauga
from straszaki import toggle_color, scary_effect, mrygnij, blink_random_characters, apply_glitch_effect, gowno, generate_corrupted_text, clear_screen

#importy modułów pythona

import music
import pygame
import time
import sys
import description
import webbrowser
from colorama import init, Fore, Back, Style
import os
import threading
import pickle
import json
import subprocess

game_started = False


bossy = [Mauga(), Orisa()]

# Początek gry

def display_main_menu():
    print("\n--- MENU GŁÓWNE ---")
    print("1. Rozpocznij grę")
    print("2. Zasady gry")
    print("3. Leaderboard")
    print("4. Wyjście")
    print("--------------------")

def show_game_rules():
    clear_console()
    print("Zasady gry:")
    print("Twoim celem jest pokonanie przeciwników, a następnie głównego bossa Orisy lub Maugi.")
    print("Jeśli przegrasz, odczujesz niespodziankę...")
    print("W trakcie gry możesz wybrać jednego z dostępnych bohaterów: Sombra, Reinhardt, Widowmaker lub Ana.")
    print("Każdy bohater ma unikalne umiejętności i zdolności specjalne.")
    print("Podczas walki możesz atakować przeciwników, używać umiejętności specjalnych lub leczyć się.")
    print("Pamiętaj o zarządzaniu swoją ilością many i zdrowia.")
    print("Powodzenia!")
    input("Naciśnij Enter, aby wrócić do menu...")


def show_loading_screen():
    screen.fill(background_color)
    
    # Losowy czas trwania ładowania między 1 a 5 sekundami
    loading_time = random.uniform(1, 5)
    
    # Początkowy czas
    start_time = time.time()
    
    font = pygame.font.Font(None, 36)
    loading_text = font.render("Ładowanie...", True, (255, 255, 255))
    screen.blit(loading_text, (screen_width // 2 - loading_text.get_width() // 2, 200))
    pygame.display.flip()

    while time.time() - start_time < loading_time:
        # Tutaj możesz dodać dowolne operacje ładowania, np. wczytywanie zasobów

        # Aktualizacja ekranu ładowania (np. pasek postępu)
        postep = (time.time() - start_time) / loading_time
        pygame.draw.rect(screen, (255, 255, 255), (100, 300, postep * 600, 20))
        pygame.display.update()


# Funkcja do zapisywania wyników
def get_player_nickname():
    nickname = input("Podaj swój nick: ")
    return nickname

def load_leaderboard():
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []
    return leaderboard

def save_leaderboard(leaderboard):
    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=2)

def update_leaderboard(player_name, defeated_enemies, manas):
    leaderboard = load_leaderboard()
    leaderboard.append({"player_name": player_name, "defeated_enemies": defeated_enemies, "mana": manas})
    leaderboard.sort(key=lambda x: x["defeated_enemies"], reverse=True)
    save_leaderboard(leaderboard)

def display_leaderboard():
    leaderboard = load_leaderboard()
    print("Leaderboard:")
    for idx, entry in enumerate(leaderboard, start=1):
        print(f"{idx}. {entry['player_name']} - {entry['defeated_enemies']} defeated enemies")


def rozwal_gre():
    print('kys')
    sys.exit

from colorama import init, Fore, Back, Style


# Inicjalizacja modułu Colorama

init(autoreset=True)

def clear_console1():
    # Wyczyść konsolę
    print("\033c")

def print_color_text(text, color):
    # Wydrukuj kolorowy tekst
    print(color + text)

def cinematic_effect(text, delay):
    clear_console1()
    print_color_text(text, Fore.WHITE + Back.BLACK + Style.BRIGHT)
    time.sleep(delay)


# Funkcja do animowanego tekstu
def animated_text(text, delay=0.1):
    for color in [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]:
        print(f"{color}{text}")
        time.sleep(delay)


# Funkcja do pokazywania healthbaru
def display_health_bar(character):
    max_health = character.max_health
    current_health = character.current_health
    bar_length = 10
    health_percentage = current_health / max_health

    # Sprawdź, czy zdrowie jest poniżej 15% i zmień kolor tekstu na czerwony
    if health_percentage < 0.15:
        color_code = "\033[91m"  # ANSI Escape Code dla czerwonego koloru
    elif health_percentage < 0.50:
        color_code = "\033[93m"  # ANSI Escape Code dla żółtego koloru
    elif health_percentage > 0.51:
        color_code = "\033[92m"  # ANSI Escape Code dla zielonego koloru
    else:
        color_code = ""  # Domyślny kolor

    health_bar = '█' * int(bar_length * health_percentage)
    empty_bar = '▒' * (bar_length - len(health_bar))

    # Wydrukuj pasek zdrowia z odpowiednim kolorem
    print(f"{character.name}: {color_code}{health_bar}{empty_bar} {current_health} HP\033[0m")

    if isinstance(character, Character):
        max_mana = character.max_mana
        current_mana = character.current_mana
        mana_bar = '-' * int(bar_length * (current_mana / max_mana))
        empty_mana_bar = '.' * (bar_length - len(mana_bar))
        print(f"Mana: {mana_bar}{empty_mana_bar} ({current_mana} Mana)")

# Animowane teksty itp.

def animated_loading():
    frames = ["[      ]", "[=     ]", "[==    ]", "[===   ]", "[ ===  ]", "[  === ]", "[   == ]", "[    = ]","[     =]"]
    for frame in frames:
        sys.stdout.write('\r' + 'Wysyłanie... ' + frame)
        sys.stdout.flush()
        time.sleep(0.2)

def animate_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_airplane():
    airplane = ">===✈===<"
    width = 50
    position = -len(airplane)  # Inicjalizacja pozycji samolotu poza lewą krawędzią konsoli
    while position < width:
        clear_console()
        print(" " * position + airplane)
        position += 1
        time.sleep(0.1)

def animate_fire(duration=3):
    width = 50  # Szerokość konsoli
    fire = "🔥"  # Symbol ognia

    # Przygotuj początkową pozycję ognia poza lewą krawędzią konsoli
    position = -1
    while position < width:
        clear_console()
        print(" " * position + fire)
        position += 1
        time.sleep(0.1)

    # Zatrzymaj ognia przez podany czas
    time.sleep(duration)

    # Animacja gaśnięcia ognia
    while position > -len(fire):
        clear_console()
        print(" " * position + fire)
        position -= 1
        time.sleep(0.1)

logo_frames = [
    """
    ⠀⠀⠀⠀⠀⠀⠀⠀⡀⢄⢢⠢⡕⢣⠚⡔⢣⠎⡔⡠⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⣾⣧⡈⢱⠪⢴⠌⠓⠈⠂⠀⠀⠙⠈⠒⠡⢞⡸⡰⢁⣴⣷⣄⠀⠀
    ⠀⣼⣿⣿⣿⣿⣿⣿⡆⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣦⠀
    ⢸⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⢀⡆⢰⡀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣧
    ⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⣾⡇⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇⢸⣿⣧⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣀⣼⣿⣿⡇⢸⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⣿⣿⣇⠀⠀⠀⣠⣾⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣷⣀⠀⠀⠀⢸⣿⣿⣿⣿
    ⢸⣿⣿⣿⣿⡄⣠⣾⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⣿⣿⣿⣷⣄⢠⣿⣿⣿⣿⡇
    ⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
    ⠀⠀⢻⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⡟⠀⠀
    ⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣶⣤⣀⣀⣀⣀⣀⣀⣤⣶⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀
    """
]

def animate_overwatch_logo():
    for frame in logo_frames:
        clear_console()
        print(frame)
        time.sleep(0.5)  # Czas wyświetlania klatki



# MUZYCZNE RZECZY \/


def play_intro_music():
    pygame.mixer.init()
    pygame.mixer.music.load('paraiso.mp3')  # Wprowadź nazwę lub ścieżkę do pliku dźwiękowego
    pygame.mixer.music.play()

def play_boss_music():
    pygame.mixer.init()
    pygame.mixer.music.load('boss.mp3')  # Wprowadź nazwę lub ścieżkę do pliku dźwiękowego bosza
    pygame.mixer.music.play()

def play_sombra_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('sombra.ogg')  # Wprowadź nazwę lub ścieżkę do pliku dźwiękowego Sombry
    pygame.mixer.music.play()

def play_reinhardt_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('reinhardt.ogg')  # Wprowadź nazwę lub ścieżkę do pliku dźwiękowego Sombry
    pygame.mixer.music.play()

def play_widowmaker_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('widowmaker.ogg')
    pygame.mixer.music.play()

def play_ana_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('ana.ogg')
    pygame.mixer.music.play()

def play_zarya_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('Zarya.ogg')
    pygame.mixer.music.play()

def hurhurhurhur():
    pygame.mixer.init()
    pygame.mixer.music.load('hurhur.mp3')
    pygame.mixer.music.play()

def print_welcome_message():
    # Ustaw kolor czerwony
    red_color = "\033[91m"
    # Ustaw rozmiar tekstu na większy
    big_text = "\033[1m"

    # Tekst, który ma być wyświetlony
    message = "Witaj w Paraiso!"

    # Połącz kolory i rozmiar z tekstem
    formatted_message = f"{red_color}{big_text}{message}\033[0m"

    print(formatted_message)

# Atak
def attack_player(player, enemy):
    damage = player.attack()
    if isinstance(player, Character):
        if player.current_mana >= 10:  # Sprawdź, czy gracz ma wystarczającą ilość many
            player.current_mana -= 10  # Odejmij koszt many
            enemy.take_damage(damage)
            print(f"Atakowałeś {enemy.name} i zadałeś {damage} obrażeń!")
        else:
            print("Masz za mało many, aby wykonać atak zwykły.")
    else:
        enemy.take_damage(damage)
        print(f"Atakowałeś {enemy.name} i zadałeś {damage} obrażeń!")
def use_shield_ability(player):
    if isinstance(player, Reinhardt) and player.current_mana >= 50:
        player.current_mana -= 50  # Odejmij 50 many za użycie tarczy
        player.activate_shield()  # Wywołaj metodę używania tarczy dla Reinhardta
        print(f"{player.name} używa tarczy i zyskuje dodatkową ochronę!")

def use_special_ability(player, enemy):  # Odejmij 30 many za umiejętność specjalną
    damage = player.use_special_ability(enemy)
    print("-" * 50)

def enemy_attack(player, enemy):
    damage = enemy.attack()
    player.take_damage(damage)
    print(f"{enemy.name} zadaje {damage} obrażeń {player.name}!")
    print("-" * 50)


# Randomowi przeciwnicy
def select_random_enemies():
    enemies = [Bastion(), Kiriko(), Roadhog(), Echo(), Cassidy(), Lucio(), Ashe(), Springtrap(), Hanzo()]
    random.shuffle(enemies)
    return enemies

# Kolej gracza
def player_turn(player, enemy):
    print("Twoja kolej! Wybierz akcję:")
    print("1. " + Fore.LIGHTGREEN_EX + "Atak zwykły" + Style.RESET_ALL)
    print("2. " + Fore.LIGHTBLUE_EX + "Umiejętność specjalna" + Style.RESET_ALL)
    print("3. " + Fore.LIGHTYELLOW_EX + "Leczenie" + Style.RESET_ALL)

    if isinstance(player, Reinhardt):
        print("T. " + Fore.LIGHTMAGENTA_EX + "Tarcza" + Style.RESET_ALL)

    choice = input("Podaj numer wybranej akcji: ")

    is_healing = False

    if choice == "1":
        if player.current_mana >= 10:
            attack_player(player, enemy)
        else:
            print("Masz za mało many, aby wykonać atak zwykły.")
    elif choice == "2":
        use_special_ability(player, enemy)
    elif choice == "3":
        if not is_healing:
            heal_player(player, is_healing)
    elif choice == "T" and isinstance(player, Reinhardt):
        use_shield_ability(player)
    elif choice == "was that the bite of 87":
        play_boss_music()
        boss = Orisa()
        print("Boss, Orisa, pojawił się!")

        while not boss.is_defeated() and not player.is_defeated():
            display_health_bar(player)
            display_health_bar(boss)

            is_healing = False

            player_turn(player, boss)
            if boss.is_defeated():
                print(Fore.LIGHTGREEN_EX + "Gratulacje! Pokonałeś Orisę i wygrałeś grę." + Style.RESET_ALL)
                break
        else:
            print("Nie możesz jeszcze przeskoczyć do bossa, ponieważ nie pokonałeś wystarczającej liczby przeciwników.")

    elif choice == 'kys':
        rozwal_gre()

def heal_player(player, is_healing):
    if is_healing:
        print(f"{player.name} jest w trakcie leczenia i nie może być zaatakowany.")
    elif player.current_mana >= 35:  # Sprawdź, czy gracz ma wystarczającą ilość many
        player.current_mana -= 35  # Odejmij 35 many za leczenie
        amount_healed = 30
        player.current_health += amount_healed
        if player.current_health > player.max_health:
            player.current_health = player.max_health
        print(f"{player.name} leczy się za {amount_healed} HP.")
    else:
        print(f"{player.name} nie ma wystarczająco many do użycia leczenia.")


# Tekst do migania
text_to_blink = "ITS ME"

# Czas trwania migania (w sekundach)
blink_duration = 0.1

# Ilość mignięć
num_blinks = 10
# wywolanie: mrygnij(text_to_blink, blink_duration, num_blinks)





# Główna część gry
def main():
    print("Witaj w grze RPG!")
    print('jak przegrasz niespodzianka...')
    print("Ja chce tylko powiedziec ze zrobienie tego gówna zajelo mi kilkanascie dobrych godzin spedzonych przy komputerze ze spotifyem w tle i biblioteka pythona w przegladarce. zabijcie sie programisci pythona")
    time.sleep(0.5)
    czy_dotknales = input("czy chcesz obejrzec film wprowadzający (T/N)")
    if czy_dotknales == 'T':
        time.sleep(0.3)
        czy_dotknalem_piersi = 'https://clips.twitch.tv/TallEnthusiasticLyrebirdShazBotstix-p-8Gj38w9JLwsCOI'
        webbrowser.open(czy_dotknalem_piersi)
        time.sleep(5)
        czytobyloto = 'https://clips.twitch.tv/BlueVastWallabySSSsss-C3C6b9WveZxKrOfe?tt_medium=clips&tt_content=recommendation'
        webbrowser.open(czytobyloto)
        skonczone = input('Skończyłeś oglądać? T/N: ')
        if skonczone == 'T':
            pass
        if skonczone == 'N':
            print('W takim razie wylaczam gre 🤷‍♂️')
            sys.exit

    skip_intro = input("Czy chcesz pominąć początkowy dialog? (T/N): ")
    skip_intro = skip_intro.lower()  # Konwersja odpowiedzi na małe litery

    if skip_intro == "t":
        show_intro = False
        print('\n')
        clear_console()
        apply_glitch_effect()
        time.sleep(3)
        clear_console()
        blink_random_characters(text_to_blink, num_blinks, blink_duration)
        clear_console()
        time.sleep(1)
    else:
        show_intro = True    
    if show_intro:
        time.sleep(2)
        print('-' * 50)
        gowno()
        print('\n')
        time.sleep(0.3)
        print('...')
        time.sleep(0.2)
        animate_text('Dobra, powinno działać.')
        print('\n')
        time.sleep(0.2)
        animate_text('- Abby: Potrzebujemy pomocy! Ludzie zbuntowali się i wysłali frakcje anty-watch na nasze miasto! Do miasta przedostają się roboty i ludzie z franckji anty-watch!')
        print('\n')
        time.sleep(0.5)
        animate_text('- Mike: Witaj Abby! Słyszymy cię. Z tej strony frakcja overwatch. Przyjęliśmy do wiadomości potrzebę pomocy! Pomoc zostanie wysłana jak najszybciej.')
        print('\n')
        time.sleep(0.3)
        animate_text('- Abby: Witaj Mike! Dziękujemy za pomoc. Wysyłam ci dokładne koordynaty naszego miasta!')
        time.sleep(1)
        print('\n')
        animated_loading()
        time.sleep(0.3)
        print('\n')
        print('Niepowodzenie.')
        time.sleep(0.2)
        print('\n')
        animate_text('- Abby: Błąd połączenia, spróbuje jeszcze raz.')
        time.sleep(1)
        print('\n')
        animated_loading()
        print('\n')
        print('Wysłano!')
        time.sleep(0.2)
        animate_text('- Abby: Udało się! Wysłałam ci dokładne koordynaty miasta!')
        print('\n')
        time.sleep(0.3)
        animate_text('- Mike: Przyszło! Wysyłam jednostki specjalne.')
        print('\n')
        time.sleep(0.2)
        animate_text('- Mike: Abby? Czy twoje miasto to Paraiso?')
        print('\n')
        time.sleep(0.1)
        animate_text('- Abby: Tak.')
        print('\n')
        time.sleep(0.2)
        animate_text('- Mike: Zrozumiano!')
        time.sleep(1)
        print('\n')
        animate_text('Wylatujesz do Paraiso.')
        time.sleep(1)
        print('\n')
        animate_airplane()
        time.sleep(1)
        print('\n')
        cinematic_effect('Przyleciałeś do paraiso...',2)
        time.sleep(2)
        print('\n')
        animate_text('- Mike: Coś tu jest nie tak. Zbyt cicho tutaj jak na tak duże miasto...')
        time.sleep(2)
        print('\n')
        cinematic_effect('Słyszysz coś w oddali...',2)
        time.sleep(1)
        print('\n')
        animate_text('- Mike: Słyszę coś... brzmi jak odgłos burzącego się budynku')
        print('\n')
        time.sleep(0.5)
        print('\n')
        animate_text('- Mike: Tam się pali! Nie mogę wysłać tam bohaterów overwatch... Bohaterowie pójdą w drugą stronę, ponieważ tam słyszę większe krzyki i tam potrzebna jest pomoc. Straż pożarna ugasi ogien.')
        print('\n')
        time.sleep(0.1)
        cinematic_effect('Mike zadzwonił do samolotu overwatch, aby zasygnalizować gdzie powinni udać się bohaterowie...',2)
        time.sleep(0.3)
        animate_overwatch_logo()
        time.sleep(1)
    print_welcome_message()
    play_intro_music()
    time.sleep(3)
    clear_console()
    display_main_menu()
    choice = input("Wybierz opcję z menu: ")

    if choice == "1":
        pass
    elif choice == "2":
        show_game_rules()
    elif choice == "3":
        display_leaderboard()
    elif choice == "4":
        print("Dziękujemy za grę! Do zobaczenia następnym razem!")
        sys.exit
    else:
        print("Niepoprawny wybór. Wybierz opcję z menu.")
        time.sleep(1)
    
    character_choice = input("Wybierz swoją postać (1. Sombra, 2. Reinhardt, 3. Widowmaker, 4. Ana, 5. Zarya) ")
    
    if character_choice == "1":
        player = Sombra()  # Rozpocznij grę z 100 many
        animate_text('Sombra, jeden z najbardziej znanych hakerów na świecie, wykorzystuje informacje do manipulowania osobami u władzy. Jej umiejętności ukrywania się i wyniszczające ataki czynią z niej potężnego infiltratora, a także trudny cel do unieruchomienia. ')
        play_sombra_sound()
        print('\n')
        print('-' * 50)
    
    elif character_choice == "2":
        player = Reinhardt()  # Rozpocznij grę z 100 many
        play_reinhardt_sound()
        animate_text('Wysoko odznaczony żołnierz, Reinhardt Wilhelm, stylizuje się na mistrza minionej epoki, który żyje według rycerskich kodeksów męstwa, sprawiedliwości i odwagi. Posiadając „aktywną wyobraźnię”, lubi jeść currywurst, jest rozmowny i jest fanem muzyki Davida Hasselhoffa. Codziennie sparinguje z Brigitte, po czym idą odpocząć do pubu lub tawerny.' )
        print('\n')
        print('-' * 50)
    
    elif character_choice == "3":
        player = Widowmaker()  # Rozpocznij grę z 100 many
        play_widowmaker_sound()
        animate_text('Widowmaker to doskonały zabójca: cierpliwy, bezwzględnie skuteczny zabójca, który nie okazuje emocji ani wyrzutów sumienia. Kiedyś tańczyły jej jedyne miłości i mąż, ale teraz jedyną radość daje jej moment zabójstwa. Niepowstrzymany zabójca, celownik Widowmakera jest prawdopodobnie najniebezpieczniejszym miejscem na świecie.')
        print('\n')
        print('-' * 50)
    
    elif character_choice == "fred":
        player = Freddy()
        hurhurhurhur()
        print('Co? Jak ty to zrobiłeś? Nie miałeś tego zrobić! Freddy został uwolniony do świata bohaterów overwatch! Jeżeli przegrasz, freddy zostanie na wolności!')
        time.sleep(3)
        print('A więc wybrałeś dobro. Freddy ci pomoże, a raczej ty jemu! Od teraz kontrolujesz freda, i jeżeli on zginie... ty też zginiesz...')
        time.sleep(3)
        print('Freddy teraz ci służy! Jego umiejętność specjalna pozwoli ci łatwo zabić przeciwników, jednak kosztuje ona 100 many. Wykorzystuj ją ostrożnie, i nie zabijesz nią orisy.')
        time.sleep(3)
        print('Widzimy się po drugiej stronie...')
    
    elif character_choice == "1234567890":
        print('UWAGA! TO JEST OBIEKT TESTOW! ZNISZCZY ON CALA ROZGRYWKE! JEST TO TYLKO DLA MNIE (CZY DLA OLUSIA :3)')
        time.sleep(0.5)
        test_chcesz = input('Czy na pewno chcesz wybrać tą postać? T/N ')
        if test_chcesz == 'T':
            player = test()
        else:
            player = Sombra()
            play_sombra_sound()
            print('Odpowiedziałeś N albo źle odpowiedziałeś. Domyślnie wybrana postać: Sombra')
    
    elif character_choice == '4':
        player = Ana()
        animate_text('Ana, jedna z założycielek Overwatch, wykorzystuje swoje umiejętności i wiedzę, aby bronić swojego domu i ludzi, na których się troszczy. Pochodząca z długiej linii odznaczonych żołnierzy, Ana wzbudziła zaufanie i lojalność u swoich kolegów, a także obdarzyła swoją córkę, Fareeha Amari – Pharah, intensywnym poczuciem obowiązku i honoru. Podobnie jak jej córka, nosiła tatuaż przedstawiający Oko Horusa jako symbol ochrony. Podobnie jej znak wywoławczy w egipskiej armii podczas kryzysu omnickiego brzmiał „Horus”. Do dziś Ana jest uważana przez Egipcjan za bohaterkę.')
        play_ana_sound()
        print('\n')
        print('-' * 50)
    
    elif character_choice == '5':
        player = Zarya()
        animate_text('Aleksandra Zaryanova to jedna z najsilniejszych kobiet na świecie, znana sportsmenka, która w czasie wojny poświęciła osobistą chwałę, aby chronić swoją rodzinę, przyjaciół i kraj. Jako żołnierz Rosyjskich Sił Obronnych jest dumna, że ​​wykorzystuje swoją siłę, aby chronić tych, których kocha.')
        play_zarya_sound()
        print('\n')
        print('-' * 50)
    
    elif character_choice == "olus":
        player = dodatkowefunkcjepostaci()
        animate_text('olus')
        print('\n')
        print('-'*50)
    else:
        print("Niepoprawny wybór. Domyślnie wybrano postać Sombra.")
        player = Sombra()  # Domyślnie rozpocznij grę z 100 many
        play_sombra_sound()
        description.sombra_opis()
    boss_activated = False
    defeated_enemies = 0
    while True:
        enemies = select_random_enemies()
        for enemy in enemies:
            print(f"Dziki {enemy.name} się pojawił!")
            while not enemy.is_defeated() and not player.is_defeated():
                display_health_bar(player)
                display_health_bar(enemy)

                player_turn(player, enemy)
                if enemy.is_defeated():
                    defeated_enemies += 1
                    player.gain_mana(100)  # Dodaj 70 many za pokonanie przeciwnika
                    print(f"Pokonałeś {enemy.name} i zdobyłeś 70 many!")

                    print("-" * 50)
                    break
                enemy_attack(player, enemy)
                print("-" * 50)


        if player.is_defeated():
            clear_console()

            jumpscare_links = [
            "https://www.youtube.com/watch?v=c1fsIquzQ7I",
            "https://www.youtube.com/watch?v=FUaaGInT_R8",
            "https://www.youtube.com/watch?v=uwXy7TYkLv8",
            # Dodaj więcej linków, jeśli potrzebujesz
            ]

            jumpscare_url = random.choice(jumpscare_links)
            webbrowser.open(jumpscare_url)  # Liczba pokonanych przeciwników
            player_name = get_player_nickname()  # Imię gracza
            update_leaderboard(player_name, defeated_enemies, manas = player.current_mana)
            print(f"Zostałeś pokonany przez {defeated_enemies} przeciwników.")
            display_leaderboard()  # Wyświetl leaderboard
            break
            
        if defeated_enemies >= 10:
            boss_activated = True
            play_boss_music()
            boss = random.choice(bossy)
            print(f"Boss, {boss}, pojawił się!")
            if boss == Orisa:
                animate_text('Orisa, skonstruowana przez genialną jedenastolatkę, Efi Oladele, powstała, aby bronić miasto Numbani przed wszelkimi zagrożeniami. Kiedy ten duet skutecznie odparł atak Pięści Zagłady ze Szponu, uznano je za bohaterki narodowe. Teraz Orisa jest gotowa chronić tych, którzy jej potrzebują, wykorzystując swoją moc w imię dobra.')
                print('\n')
                animate_text(f'{player.name} - No nie wydaje mi sie ze jest ona dobra... doslownie zaatakowala miasto, jak mialaby byc niby dobra?')
                print('\n')
            elif boss == Mauga:
                clear_console()
                animate_text('Wysoki i muskularny, rozmiar i siła Maugi zostały zwiększone. Przynajmniej według samego Maugi, zanim dokonał wspomnianej augmentacji, był poważniejszy, zanim zyskał „nowe spojrzenie na życie”. W swojej obecnej postaci Mauga często przedstawia siebie jako „wielkiego, głupiego brutala”. Jest to jednak fasada, ponieważ posiada przebiegłe cechy. Mówi szybko i swobodnie, ma tendencję do traktowania nieznajomych jak przyjaciół. Jest biegły w walce w zwarciu; Baptiste uważał go za „podobnego do demona”; Socjopata i sadysta Mauga szybko przełącza się między jaśniejszą i ciemniejszą stroną, choć może się w niej zatracić. Tylko Baptisteowi udało się go wyprowadzić z tego stanu w terenie. Sam Baptiste jest ślepym punktem dla Maugi, który okazał mu miłosierdzie tam, gdzie inaczej by tego nie zrobił.')
                print('\n')
                animate_text(f'{player.name} - Zaczyna sie...')
            while not boss.is_defeated() and not player.is_defeated():
                display_health_bar(player)
                display_health_bar(boss)

                player_turn(player, boss)
                if boss.is_defeated():
                    print(Fore.RED + "Gratulacje! Pokonałeś Orisę i wygrałeś grę.")
                    animated_text("Dzięki za grę! Do zobaczenia następnym razem!", delay=0.2)
                    for _ in range(3):
                        sys.stdout.write("\033[1;31mWygrałeś!\033[0m")
                        sys.stdout.flush()
                        time.sleep(0.5)
                        sys.stdout.write("\r" + " " * 12)  # Wyczyść napis
                        sys.stdout.flush()
                        time.sleep(0.5)
                    time.sleep(1)
                    cinematic_effect('Kilka minut później, w samolocie overwatch...',2)
                    print('\n')
                    animate_text('- Mike: Udało się! Orisa została zwyciężona. Ale to nie koniec zmagań overwatch z any-watchem')
                    print('\n')
                    animate_text('- Abby: Dziękuję za pomoc! Bez was by to się nie udało.')
                    print('\n')
                    animate_text(f'- Mike: {player.name}, bez ciebie by się nie udało.')
                    time.sleep(0.5)
                    print('\n')
                    animate_text(f'- {player.name}: Dziękuję!')
                    print('\n')
                    print('Wyniki')
                    print('\n')
                    defeated_enemies = defeated_enemies  # Liczba pokonanych przeciwników
                    player_name = get_player_nickname()  # Imię gracza
                    update_leaderboard(player_name, defeated_enemies)
                    time.sleep(3)
                    cinematic_effect('Kilka dni później, w siedzibie overwatch:', 2)
                    print('*dźwięk dzwoniącego telefonu*')
                    time.sleep(0.9)
                    print('\n')
                    animate_text('- Mike: Halo? Kto dzwoni')
                    print('\n')
                    animate_text('- #@$^&*: ten co jajami dzwoni.')
                    print('\n')
                    animate_text('- Mike: Przekomiczne...')
                    time.sleep(2)
                    clear_console()
                    sys.exit()

# Inicjacja gry
if __name__ == "__main__":
    pygame.init()

    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moja Gra")

    background_color = (0, 0, 0)

    def start_game():
        global game_started
        show_loading_screen()
        game_started = True
        clear_console()
        print("Gra odpaliła się w konsoli")
        pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_s:
                    if not game_started:
                        start_game()

        screen.fill(background_color)

        font = pygame.font.Font(None, 36)
        if game_started:
            start_text = font.render("Gra odpaliła się w konsoli", True, (255, 255, 255))
            time.sleep(5)
            main()
        else:
            start_text = font.render("Start gry (S)", True, (255, 255, 255))
        exit_text = font.render("Wyjście (Q)", True, (255, 255, 255))
        screen.blit(start_text, (screen_width // 2 - start_text.get_width() // 2, 200))
        screen.blit(exit_text, (screen_width // 2 - exit_text.get_width() // 2, 300))

        pygame.display.flip()
    pygame.quit()