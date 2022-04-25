from tkinter import *
import random


def build_deck():
    new_deck = []
    number_of_packs = 1
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
    print(f"Cards Drawn: {52 - len(deck)}")
    if len(deck) == 0:
        button_draw.config(text="No Cards Left", state="disabled")


def exit_app():
    window.destroy()


def reset_deck():
    global deck
    deck = build_deck()


window = Tk()
window.config(pady=20, padx=20)
window.title("CARD DRAW")

label_card = Label(text="", height=5, width=5, font=("Arial", 44), borderwidth=1, relief="solid")
label_card.grid(column=1, row=1)
button_draw = Button(text="D R A W", width=20, command=draw_card, font=("Arial", 16))
button_draw.grid(column=1, row=2, pady=8)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset", command=reset_deck)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)

deck = build_deck()
print(len(deck))

window.config(menu=menu_bar)
window.mainloop()
