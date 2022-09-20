from tkinter import *

window = Tk()

window.title('My First GUI Program')
window.minsize(width=500, height=300)

my_label = Label(text='I am not a Label', font=("Arial", 24, 'bold'))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)



def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())




button = Button(text="Click me", command=button_clicked)

# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Press this", command=button_clicked)
new_button.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
# print(input.get())
input.grid(column=3, row=2)









window.mainloop()