import tkinter as tk

counter = 0


def counter_lb(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()


window = tk.Tk()
window.title("Counter")
label = tk.Label(window, fg="blue", width=40, height=5)
label.pack()
counter_lb(label)
Button = tk.Button(window, width=20, text="count", command=window.destroy)
Button.pack()

window.mainloop( )
