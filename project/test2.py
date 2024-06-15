from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")

frame = CTkFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2)
frame.pack(expand=True)

frame2 = CTkScrollableFrame(master=app, fg_color="#8D6F3A", border_color="#FFCC70", border_width=2, orientation="vertical", scrollbar_button_color="#FFCC70")
frame2.pack(expand=True)

tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

img = Image.open("lo.png")

def click_handler():
    print("Hello World")

def change_character(value):
    print(f"Selected Value {value}")

def entry_getter():
    print(f"Entered value: {entry.get()}")

def textbox_getter():
    print(f"Entered Value: {textbox.get('0.0', 'end')}")
count =0
def label_updater():
    global count
    count += 1
    label.configure(text=f"You've clicked the button {count} times")

label = CTkLabel(master=app, text="Some Text...", font=("Arial",20), text_color="#FFCC70")
label.place(relx=0.2, rely=0.2, anchor="center")

btn = CTkButton(master=tabview.tab("Tab 2"), text="Click Me", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2,command=click_handler, image=CTkImage(dark_image=img))
btn.place(relx=0.5, rely=0.5, anchor="center")

btn2 = CTkButton(master=frame, text="Click Me", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img), command=entry_getter)
btn2.place(relx=0.6, rely=0.5, anchor="center")

btn3 = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img), command=textbox_getter)
btn3.place(relx=0.8, rely=0.5, anchor="center")

btn4 = CTkButton(master=frame2, text="Click Me", corner_radius=32, fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img), command=label_updater)
btn4.place(relx=0.9, rely=0.5, anchor="center")

combobox = CTkComboBox(master=app, values=["option 1", "option 2", "option 3"], border_color="#FBAB7E", dropdown_fg_color="#0093E9", command=change_character)
combobox.place(relx=0.4, rely=0.4, anchor="center")

checkbox = CTkCheckBox(master=app, text="Option", fg_color="#C850C0", checkbox_height=30, checkbox_width=36)
checkbox.place(relx=0.3, rely=0.3, anchor="center")

switch = CTkSwitch(master=app, text="Option")
switch.place(relx=0.6, rely=0.6, anchor="center")

slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=5, button_color="#C850C0", progress_color="#C850C0", orientation="vertical")
slider.place(relx=0.7, rely=0.7, anchor="center")

entry = CTkEntry(master=app, placeholder_text="Start typing...", width=300, text_color="#FFCC70")
entry.place(relx=0.8, rely=0.8, anchor="center")

textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16, border_color="#FFCC70", border_width=2)
textbox.place(relx=0.8, rely=0.8, anchor="center")

app.mainloop() 