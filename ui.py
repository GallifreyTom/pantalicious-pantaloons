import tkinter as tk

#Create window and define parameters

window = tk.Tk()

window.title("Pantalicious Pantaloons")
window.iconbitmap("PantIcon.ico")
window.geometry("512x512")
window.resizable(False, False)

#Window Elements

#Title
titleName = tk.Label(window, text="Pantalicious Pantaloons", font=("Papyrus", 24, "bold"))
titleName.pack()

#Subtitle
subTitle = tk.Label(window, text="Order your pantaloons today!", font=("Papyrus", 16, "italic"))
subTitle.pack()

#checkboxes

#Blue
blue_pantaloon = tk.IntVar()
blue_pantaloon_button = tk.Checkbutton(window, text="Blue", variable=blue_pantaloon, onvalue=1, offvalue=0)
blue_pantaloon_button.pack()

#Red
red_pantaloon = tk.IntVar()
red_pantaloon_button = tk.Checkbutton(window, text="Red", variable=red_pantaloon, onvalue=1, offvalue=0)
red_pantaloon_button.pack()

#Cream
cream_pantaloon = tk.IntVar()
cream_pantaloon_button = tk.Checkbutton(window, text="Cream", variable=cream_pantaloon, onvalue=1, offvalue=0)
cream_pantaloon_button.pack()



window.mainloop()
