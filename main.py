from tkinter import *
import random


def build_deck(packs):
    new_deck = []
    number_of_packs = packs
    label_card.config(text="")
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = ["♠", "♥", "♦", "♣"]
    while number_of_packs > 0:
        for card in cards:
            for suit in suits:
                new_deck.append(f"{card}{suit}")
        number_of_packs -= 1
    return new_deck


def draw_card():
    next_card = random.choice(deck)
    if "♦" in next_card or "♥" in next_card:
        label_card.config(foreground="#f00")
    else:
        label_card.config(foreground="#000")

    label_card.config(text=next_card, font=("Arial", 44))
    deck.remove(next_card)
    label_remaining.config(text=f"{len(deck)} cards left")
    if len(deck) == 0:
        button_draw.config(text="No Cards Left", state="disabled")


def exit_app():
    window.destroy()


def reset_deck(packs):
    global deck
    deck = build_deck(packs)
    label_remaining.config(text=f"{len(deck)} cards left")
    button_draw.config(text="D R A W", state="active")


window = Tk()
window.config(pady=20, padx=20)
window.title("CARD DRAW")

label_card = Label(text="", height=5, width=5, font=("Arial", 44), borderwidth=1, relief="solid")
label_card.grid(column=1, row=1)
button_draw = Button(text="D R A W", width=20, command=draw_card, font=("Arial", 16))
button_draw.grid(column=1, row=2, pady=8)
label_remaining = Label(text="52 cards left", font=("Arial", 8))
label_remaining.grid(column=1, row=3)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset", command=lambda: reset_deck(1))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

options_menu = Menu(menu_bar, tearoff=0)
options_menu.add_command(label="1 Pack", command=lambda: reset_deck(1))
options_menu.add_command(label="2 Packs", command=lambda: reset_deck(2))
options_menu.add_command(label="3 Packs", command=lambda: reset_deck(3))
options_menu.add_command(label="4 Packs", command=lambda: reset_deck(4))

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Options", menu=options_menu)

deck = build_deck(1)

window.config(menu=menu_bar)
window.mainloop()
