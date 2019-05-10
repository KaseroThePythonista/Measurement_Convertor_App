# this file contains tkinter code for the GUI
from tkinter import *
from tkinter import ttk
from logic import celsius_fahrenheit, pounds_kilograms, miles_kilometers, millilitres_litres


root = Tk()
# ==================== settings ===============
root.geometry('760x440')
root.resizable(width=False, height=False)
root.title('Measurements Conversion.')
color_window = 'Light Green'
root.configure(bg=color_window)

# common variables
color = 'green'
border = 4


# this function selects the choice to which you want to operate on.
def set_choice():
    global radio_var

    if radio_var.get() is 1:  # Celsius-to-Fahrenheit
        return 1
    elif radio_var.get() is 2:  # Pounds-to-Kilograms
        return 2
    elif radio_var.get() is 3:  # Miles-to-Kilometers
        return 3
    elif radio_var.get() is 4:  # Millilitre-to-Liters
        return 4
    else:
        return 0


# this function converts the selected choice and displays the results in the list box
def convert():
    choice = set_choice()
    global entry_from_var
    global lb

    if choice is 1:   # Celsius-to-Fahrenheit
        ans1 = celsius_fahrenheit(entry_from_var.get())
        lb.delete(0, END)
        lb.insert(END, str(entry_from_var.get()) + ' degree celsius is equivalent to ' + ans1 + ' degrees fahrenheit.')
    elif choice is 2:  # Pounds-to-Kilograms
        ans2 = pounds_kilograms(entry_from_var.get())
        lb.delete(0, END)
        lb.insert(END, str(entry_from_var.get()) + ' pounds is equivalent to ' + ans2 + ' kilograms.')
    elif choice is 3:  # Miles-to-Kilometers
        ans3 = miles_kilometers(entry_from_var.get())
        lb.delete(0, END)
        lb.insert(END, str(entry_from_var.get()) + ' miles is equivalent to ' + ans3 + ' kilometers')
    elif choice is 4:  # Millilitre-to-Liters
        ans4 = millilitres_litres(entry_from_var.get())
        lb.delete(0, END)
        lb.insert(END, str(entry_from_var.get()) + ' millilitres is equivalent to ' + ans4 + ' litres')
    else:
        pass


# ==================== label-frames ===========
label_frame1 = ttk.LabelFrame(root, text='Choose Here:', width=350, height=300)
label_frame1.place(x=5, y=10)

label_frame2 = ttk.LabelFrame(root, text='Enter Value:', width=350, height=200)
label_frame2.place(x=400, y=10)

label_frame3 = ttk.LabelFrame(root, text='See Outcome Here:', width=745, height=90)
label_frame3.place(x=5, y=330)

# ==================== convert button ==================
btn_convert = Button(root, text='CONVERT HERE...', width=29, height=3, fg='Green', command=lambda: convert())
btn_convert.place(x=400, y=234)

# ==================== radio buttons in label-frame1 =============
radio_var = IntVar()
radio1 = Radiobutton(label_frame1, text='Degrees Celsius-to-Fahrenheit', variable=radio_var, value=1,
                     fg=color, command=lambda: set_choice())
radio1.place(x=5, y=15)

radio2 = Radiobutton(label_frame1, text='Pounds-to-Kilograms', variable=radio_var, value=2, fg=color,
                     command=lambda: set_choice())
radio2.place(x=5, y=75)

radio3 = Radiobutton(label_frame1, text='Miles-to-Kilometers', variable=radio_var, value=3, fg=color,
                     command=lambda: set_choice())
radio3.place(x=5, y=135)

radio4 = Radiobutton(label_frame1, text='Milliliter-to-Liters', variable=radio_var, value=4, fg=color,
                     command=lambda: set_choice())
radio4.place(x=5, y=195)

# ==================== entry and a label in label_frame2 ===============
label_from = Label(label_frame2, text='FROM', fg=color, width=20, font=(15, ))
label_from.place(x=50, y=10)

entry_from_var = IntVar()
entry_from = Entry(label_frame2, width=20, bd=border, textvariable=entry_from_var)
entry_from.place(x=60, y=50)

# ====================== Scrollbar and a list box on label-frame3 =============
sb = Scrollbar(label_frame3)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(label_frame3, xscrollcommand=sb.set, bd=border, fg='green', width=65, height=3)
lb.pack(side=LEFT)

sb.configure(command=lb.yview)

root.mainloop()
