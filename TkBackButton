
import tkinter as tk


def back_command(window, buttons, back):

    def BACK():
        back.place_forget()

        for i, button in enumerate(buttons, start=1):
            button.place(x=40, y=40*i)
    
    return BACK

def b1_command(window, buttons, back):
    def clear():
        back.place(x=20,y=20)
        for button in buttons:
            button.place_forget()
    return clear





def BUTTONS(window):

    """
    
    
    
    """

    b1 = tk.Button(window, text='b1', font='Times 12 bold')
    b2 = tk.Button(window, text='b2', font='Times 12 bold')
    b3 = tk.Button(window, text='b3', font='Times 12 bold')

    back = tk.Button(window, text='BACK', font='Times 12 bold', bg='red')

    BUTTONS_LIST = [b1, b2, b3]

    for i, button in enumerate(BUTTONS_LIST, start=1):
        button.place(x=40, y=40*i)
    

    b1['command'] = b1_command(window=window, buttons=BUTTONS_LIST, back=back)
    back['command'] = back_command(window=window, buttons=BUTTONS_LIST, back=back)





window = tk.Tk()
window.geometry('500x500+2500+250')



BUTTONS(window)





window.mainloop()
