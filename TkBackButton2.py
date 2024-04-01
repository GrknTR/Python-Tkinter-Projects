import tkinter as tk








class MENU:



    def __init__(self, window):

        def back_button():

            self.back_button.pack_forget()
            self.button_1.pack()
            self.button_2.pack()
            self.button_3.pack()
            self.button_4.pack()
            

        def forget_button():
            self.button_1.pack_forget()
            self.button_2.pack_forget()
            self.button_3.pack_forget()
            self.button_4.pack_forget()

            self.back_button.pack()

            


        self.window = window

        self.button_1 = tk.Button(self.window, text='Button 1', font='Times 14 bold')
        self.button_1['command'] = forget_button
        self.button_2 = tk.Button(self.window, text='Button 2', font='Times 14 bold')
        self.button_3 = tk.Button(self.window, text='Button 3', font='Times 14 bold')
        self.button_4 = tk.Button(self.window, text='Button 4', font='Times 14 bold')

        self.back_button = tk.Button(self.window, text='Back', font='Times 14 bold')
        self.back_button['command'] = back_button

        self.button_place()
    
    
    def button_place(self):
    
        self.button_1.pack()
        self.button_2.pack()
        self.button_3.pack()
        self.button_4.pack()






def main():
    
    window = tk.Tk()
    window.geometry('500x500+2500+250')

    MENU(window=window)

    window.mainloop()



if __name__ == "__main__":
    main()

