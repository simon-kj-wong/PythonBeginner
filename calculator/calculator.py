from tkinter import *
from tkinter import ttk


def create_calculator_frame(container):

    # Button functions
    def button_clear():
        display = None

    def number_press(num):
        display = str(num)
        ttk.Label(frame, text = str(display)).grid(column=0, row=0, columnspan=4, rowspan=2, padx=10, pady=10)

    def decimal_press(display):
        if '.' not in display:
            display += '.'
        ttk.Label(frame, text = str(display)).grid(column=0, row=0, columnspan=4, rowspan=2, padx=10, pady=10)

    frame = ttk.Frame(container)

    # Functions contains both buttons and display to account for direct interactions between the two
    # Display only holds what should be labelled with computations running in background
    display = None
    if display is None:
        ttk.Label(frame, text = '0').grid(column=0, row=0, columnspan=4, rowspan=2, padx=10, pady=10)
    else:
        ttk.Label(frame, text = str(display)).grid(column=0, row=0, columnspan=4, rowspan=2, padx=10, pady=10)

    # Numbers
    ttk.Button(frame, text='0', command=lambda num=0: number_press(num)).grid(column=0, row=6)
    ttk.Button(frame, text='1', command=lambda num=1: number_press(num)).grid(column=0, row=5)
    ttk.Button(frame, text='2', command=lambda num=2: number_press(num)).grid(column=1, row=5)
    ttk.Button(frame, text='3', command=lambda num=3: number_press(num)).grid(column=2, row=5)
    ttk.Button(frame, text='4', command=lambda num=4: number_press(num)).grid(column=0, row=4)
    ttk.Button(frame, text='5', command=lambda num=5: number_press(num)).grid(column=1, row=4)
    ttk.Button(frame, text='6', command=lambda num=6: number_press(num)).grid(column=2, row=4)
    ttk.Button(frame, text='7', command=lambda num=7: number_press(num)).grid(column=0, row=3)
    ttk.Button(frame, text='8', command=lambda num=8: number_press(num)).grid(column=1, row=3)
    ttk.Button(frame, text='9', command=lambda num=9: number_press(num)).grid(column=2, row=3)
    ttk.Button(frame, text='.').grid(column=1, row=6)

    # Functional Buttons
    ttk.Button(frame, text='Quit', command=container.destroy).grid(column=2, row=6)
    ttk.Button(frame, text='Clear', command=button_clear()).grid(column=0, row=2)
    ttk.Button(frame,text='=').grid(column=3, row=6)
    ttk.Button(frame,text='+').grid(column=3, row=5)
    ttk.Button(frame,text='-').grid(column=3, row=4)
    ttk.Button(frame,text='*').grid(column=3, row=3)
    ttk.Button(frame,text='÷').grid(column=3, row=2)

    return frame

def create_calculator():
    # Create root window
    root = Tk()
    root.title('Calculator')

    frame = create_calculator_frame(root)
    frame.pack()

    root.mainloop()

if __name__ == '__main__':
    create_calculator()
