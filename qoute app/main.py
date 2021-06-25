from tkinter import *
import requests


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    response.raise_for_status()
    data = response.json()
    quote = data[0]
    canvas.itemconfig(quote_text, text=quote["q"])


window = Tk()
window.title("Qoutes of the day...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(160, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Daily Quote Goes HERE", width=250, font=("Arial", 17, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, width=90, height=100, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()