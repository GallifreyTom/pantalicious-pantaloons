import tkinter as tk

#Defining functions


#Define test function

def test():
    print(forename_field.get())



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


#Checkboxes

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


#Text fields
#To get variable you nee to use .get from the widget :)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Forename

forename_field = tk.Entry(window)
forename_field.pack()

#Surname
surname_field = tk.Entry(window)
surname_field.pack()


#Button!!!!!!

#Submit button
submit_button = tk.Button(window, text="Submit", command=test, background="red", activebackground="pink")
submit_button.pack()

#Database stuff













window.mainloop()
