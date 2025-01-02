from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front)
canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
check_image = Button(image=right_image, highlightthickness=0)
check_image.grid(column=1, row=1)
window.mainloop()