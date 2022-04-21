from tkinter import *
from tkinter import ttk

"""root = Tk()
root.title('Calculator')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Hello World!').grid(column=0, row=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)
root.mainloop()"""

def create_button_frame(container):
    frame = ttk.Frame(container)

    # Numbers
    ttk.Button(frame, text='0').grid(column=0, row=4, columnspan=2)
    ttk.Button(frame, text='1').grid(column=0, row=3)
    ttk.Button(frame, text='2').grid(column=1, row=3)
    ttk.Button(frame, text='3').grid(column=2, row=3)
    ttk.Button(frame, text='4').grid(column=0, row=2)
    ttk.Button(frame, text='5').grid(column=1, row=2)
    ttk.Button(frame, text='6').grid(column=2, row=2)
    ttk.Button(frame, text='7').grid(column=0, row=1)
    ttk.Button(frame, text='8').grid(column=1, row=1)
    ttk.Button(frame, text='9').grid(column=2, row=1)

    # Functional Buttons
    ttk.Button(frame,text='Quit',command=container.destroy).grid(column=2,row=4)
    ttk.Button(frame,text='=').grid(column=3, row=4)
    ttk.Button(frame,text='+').grid(column=3, row=3)
    ttk.Button(frame,text='-').grid(column=3, row=2)
    ttk.Button(frame,text='*').grid(column=3, row=1)
    ttk.Button(frame,text='÷').grid(column=3, row=0)

    return frame

def create_calculator():
    # Create root window
    root = Tk()
    root.title('Calculator')

    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=5)

    button_frame = create_button_frame(root)
    button_frame.grid(row=1)

    root.mainloop()

if __name__ == '__main__':
    create_calculator()
