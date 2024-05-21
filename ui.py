import tkinter as tk

#Create window and define parameters

window = tk.Tk()

window.title("Pantalicious Pantaloons")
window.iconbitmap("PantIcon.ico")
window.geometry("512x512")
window.resizable(False, False)

#Window Elements

titleName = tk.Label(window, text="Pantalicious Pantaloons", font=("Papyrus", 24, "bold"))
titleName.pack()
subTitle = tk.Label(window, text="Order your pantaloons today!", font=("Papyrus", 16, "italic"))
subTitle.pack()

window.mainloop()
