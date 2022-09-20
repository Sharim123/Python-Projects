from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609)
    my_label_4.config(text=f'{km}')

window = Tk()

window.title("Mile to Km converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


#label

my_label_1 = Label(text="Miles")
my_label_2 = Label(text='Km')
my_label_3 = Label(text='is equal to')
my_label_4 = Label(text='0')

my_label_1.grid(row=0, column=3)
my_label_2.grid(row=1, column=3)
my_label_3.grid(row=1, column=1)
my_label_4.grid(row=1, column=2)
#input

input = Entry(width=10)
input.grid(row=0, column=2)

#button



button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=2)







window.mainloop()