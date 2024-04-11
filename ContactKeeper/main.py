


import tkinter as tk
from tkinter import messagebox

class SYSTEM:

    def __init__(self, window):
        self.window = window
        self.list = 'list.txt' #Open a list.txt file
        self.MENU()
        self.Data = []
        self.listbox = ListBox

        self.Data_Load()

        self.window.bind('<Return>', self.Data_Add)
    

    def Data_Add(self, event=None):

        name_data = name_entry.get()
        surname_data = surname_entry.get()
        phone_number_data = phone_number_entry.get()

        if name_data and surname_data and phone_number_data:
            self.Data.append((name_data,surname_data,phone_number_data))
            self.listbox.insert(tk.END, f'{name_data} - {surname_data} - {phone_number_data}')

            name_entry.delete(0,tk.END)
            surname_entry.delete(0,tk.END)
            phone_number_entry.delete(0,tk.END)
        
        else:
            messagebox.showerror('Error', 'Fill in all fields')
        
        self.Data_Save()



    def Data_Delete(self):
        
        try:
            insert_delete = self.listbox.curselection()[0]
            self.listbox.delete(insert_delete)
            del self.Data[insert_delete]
            self.Data_Save()
        
        except IndexError:
            messagebox.showwarning('Warning', 'Please select the product you want to delete')
            

    
    def Data_Save(self):

        with open(self.list, 'w', encoding='utf-8') as file:
            for i in self.Data:
                file.write(f'{i[0]},{i[1]},{i[2]}\n')


    

    def Data_Load(self):

        with open(self.list, 'r', encoding='utf-8') as file:

            for line in file:

                name,surname,phone_number = line.strip().split(',')

                self.Data.append((name,surname,phone_number))
                self.listbox.insert(tk.END, f'{name} - {surname} - {phone_number}')
                



    
        
        

    def MENU(self):

        send_button = tk.Button(self.window, text='SEND', font='Times 12 bold', command=self.Data_Add)
        send_button.place(x=90, y=160)

        delete_button = tk.Button(self.window, text='DELETE', font='Times 12 bold', command=self.Data_Delete)
        delete_button.place(x=160, y=160)

        name_label = tk.Label(self.window, text='NAME', font='Times 10 bold')
        name_label.place(x=50, y=60)

        surname_label = tk.Label(self.window, text='SURNAME', font='Times 10 bold')
        surname_label.place(x=50, y=90)

        phone_number_label = tk.Label(self.window, text='PHONE NUMBER', font='Times 10 bold')
        phone_number_label.place(x=50, y=120)

        global name_entry, surname_entry, phone_number_entry, ListBox

        name_entry = tk.Entry(self.window)
        name_entry.place(x=160, y=60)

        surname_entry = tk.Entry(self.window)
        surname_entry.place(x=160, y=90)

        phone_number_entry = tk.Entry(self.window)
        phone_number_entry.place(x=160, y=120)

        ListBox = tk.Listbox(self.window)
        ListBox.place(x=300, y=50, width=270, height=100)

def main():
    window = tk.Tk()
    window.geometry('700x250+2500+250')
    app = SYSTEM(window=window)
    window.mainloop()

if __name__ == '__main__':
    main()
