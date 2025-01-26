from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
from openpyxl import Workbook, load_workbook


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()

root.geometry("650x386")
root.title("Password Generator")

filename=PhotoImage(file=relative_to_assets("new.png"))
background_label=Label(root,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)




characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            '~', '`', '@', '#', '$', '%', '&', '*']


easy_pass = ''
normal_pass = ''
hard_pass = ''
generated = ''
name = ''


def easy():
    global easy_pass
    global generated
    for i in range(6):
        easy_pass = easy_pass + characters[random.randint(1, 52)]
        generated = easy_pass

def normal():
    global normal_pass
    global generated
    for i in range(12):
        normal_pass = normal_pass + characters[random.randint(1, 62)]
        generated = normal_pass


def hard():
    global hard_pass
    global generated
    for i in range(24):
        hard_pass = hard_pass + characters[random.randint(1, len(characters) - 1)]
        generated = hard_pass


def generator():
    entry_1.insert(tk.END, generated)


def clear():
    global easy_pass
    global hard_pass
    global normal_pass
    global generated
    entry_1.delete(0, tk.END)
    easy_pass = ''
    hard_pass = ''
    normal_pass = ''
    generated = ''

def copy():
    root.clipboard_append(generated),




def save():
    new = Tk()
    new.geometry("300x150")
    new.configure(bg = "#030036")

    
    headline = Label(new, text="What is your password for?", font = ("Didot", 14))
    headline.place(x=30,y=10)   

    ask = Entry(new)
    ask.place(x=45, y=50, width=200.0, height=30.0)
    
    def excel_saver(generated): 
        name = ask.get()
        wb = load_workbook("passwords.xlsx")
        ws = wb.active
        

        ws.append([name, generated])
        wb.save("passwords.xlsx")
        new.destroy()
    
    save_button = Button(new, text="SAVE", command=lambda: excel_saver(generated))
    save_button.place(x=105, y=90, width=81.0, height=29.0)
    
    
    new.mainloop()






button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: easy(),
    relief="flat"
)
button_1.place(
    x=35.0,
    y=178.0,
    width=81.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: normal(),
    relief="flat"
)
button_2.place(
    x=156.0,
    y=178.0,
    width=81.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: hard(),
    relief="flat"
)
button_3.place(
    x=275.0,
    y=178.0,
    width=81.0,
    height=29.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear(),
    relief="flat"
)
button_4.place(
    x=55.0,
    y=325.0,
    width=76.0,
    height=26.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:  
    copy(),
    relief="flat"
)
button_5.place(
    x=152.0,
    y=325.0,
    width=76.0,
    height=26.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: save(),
    relief="flat"
)
button_6.place(
    x=248.0,
    y=325.0,
    width=76.0,
    height=26.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: generator(),
    relief="flat"
)
button_7.place(
    x=113.0,
    y=229.0,
    width=162.0,
    height=31.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))



entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=24.0,
    y=281.0,
    width=331.0,
    height=22.0
)
root.resizable(False, False)
root.mainloop()
