BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

data_file = pandas.read_csv(r"C:\udemy projects\flashcards\french_words.csv")
to_learn = data_file.to_dict(orient="records")

random_word = {}





def right_key():
    to_learn.remove(random_word)
    
    shuffle()
    


def wrong_key():
    shuffle()


def shuffle():
    global flip_timer, random_word
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(title, text = "French")
    canvas.itemconfig(word, text = random_word["French"])
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func=flip)
    

def flip():
    canvas.itemconfig(title, text = "English")
    canvas.itemconfig(word, text = random_word["English"])
    canvas.itemconfig(card_background, image = card_back)

   


window = Tk()
window.config(bg = BACKGROUND_COLOR, padx = 50, pady= 50)

flip_timer = window.after(3000, func=flip)

card_front = PhotoImage(file=r"C:\udemy projects\flashcards\images\card_front.png")
card_back = PhotoImage(file=r"C:\udemy projects\flashcards\images\card_back.png")
right = PhotoImage(file=r"C:\udemy projects\flashcards\images\right.png")
wrong = PhotoImage(file=r"C:\udemy projects\flashcards\images\wrong.png")


canvas = Canvas(width= 800, height=526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image= card_front)
title = canvas.create_text(400,150, text = "Title", font = ("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text = "word", font = ("Ariel", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row =0, columnspan=2)


#create right button 
right_button = Button(image = right, highlightthickness=0, command=right_key)
right_button.grid(column=1, row = 1)

#create left button
wrong_button = Button(image = wrong, highlightthickness=0, command= wrong_key)
wrong_button.grid(column=0, row = 1)



shuffle()

window.mainloop()
