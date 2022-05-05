from tkinter import *
from tkinter import ttk


def create_calculator_frame(container):

    # Create the tkinter window
    frame = ttk.Frame(container)

    # Initially equation is empty
    equation = ""

    # Function to update the equation widget content
    def number_press(num, equation):
        # Uses the global variable "equation"
        equation += str(num)

        # Configure the label
        equation_label.config(text = equation)


    # Numbers
    ttk.Button(frame, text='0', command=lambda num=0, equation = equation: number_press(num, equation)).grid(column=0, row=6)
    ttk.Button(frame, text='1', command=lambda num=1, equation = equation: number_press(num, equation)).grid(column=0, row=5)
    ttk.Button(frame, text='2', command=lambda num=2, equation = equation: number_press(num, equation)).grid(column=1, row=5)
    ttk.Button(frame, text='3', command=lambda num=3, equation = equation: number_press(num, equation)).grid(column=2, row=5)
    ttk.Button(frame, text='4', command=lambda num=4, equation = equation: number_press(num, equation)).grid(column=0, row=4)
    ttk.Button(frame, text='5', command=lambda num=5, equation = equation: number_press(num, equation)).grid(column=1, row=4)
    ttk.Button(frame, text='6', command=lambda num=6, equation = equation: number_press(num, equation)).grid(column=2, row=4)
    ttk.Button(frame, text='7', command=lambda num=7, equation = equation: number_press(num, equation)).grid(column=0, row=3)
    ttk.Button(frame, text='8', command=lambda num=8, equation = equation: number_press(num, equation)).grid(column=1, row=3)
    ttk.Button(frame, text='9', command=lambda num=9, equation = equation: number_press(num, equation)).grid(column=2, row=3)
    ttk.Button(frame, text='.').grid(column=1, row=6)

    # Functional Buttons
    ttk.Button(frame, text='Quit', command=container.destroy).grid(column=2, row=6)
    ttk.Button(frame, text='Clear').grid(column=0, row=2)
    ttk.Button(frame,text='=').grid(column=3, row=6)
    ttk.Button(frame,text='+').grid(column=3, row=5)
    ttk.Button(frame,text='-').grid(column=3, row=4)
    ttk.Button(frame,text='*').grid(column=3, row=3)
    ttk.Button(frame,text='÷').grid(column=3, row=2)

    # Create the equation display widget
    equation_label = ttk.Label(frame, text = equation)
    equation_label.grid(column=0, row=0, columnspan=4, rowspan=2, padx=10, pady=10)

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
