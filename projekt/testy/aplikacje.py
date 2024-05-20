import tkinter as tk
from tkinter import Button

def rozpocznij_nowa_gre():
    # Tutaj umieść kod rozpoczynający nową grę
    pass  # zastąp 'pass' kodem, który rozpocznie nową grę

root = tk.Tk()
root.title("Menu Główne")

label = tk.Label(root, text="Witaj w grze RPG")
label.pack()

new_game_button = tk.Button(root, text="Nowa Gra", command=rozpocznij_nowa_gre)
new_game_button.pack()

quit_button = tk.Button(root, text="Wyjście", command=root.quit)
quit_button.pack()

root.mainloop()
