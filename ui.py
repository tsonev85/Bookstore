from tkinter import *
from backend import Database


class UI:
    
    def __init__(self, window):
        
        self.db = Database()

        window.wm_title("BookStore")

        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)
        l2 = Label(window, text="Year")
        l2.grid(row=1, column=0)
        l3 = Label(window, text="Author")
        l3.grid(row=0, column=2)
        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)
        self.year_value = StringVar()
        self.e2 = Entry(window, textvariable=self.year_value)
        self.e2.grid(row=1, column=1)
        self.author_value = StringVar()
        self.e3 = Entry(window, textvariable=self.author_value)
        self.e3.grid(row=0, column=3)
        self.isbn_value = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # buttons
        b1 = Button(window, text='View all', width=12, command=self.view_command)
        b1.grid(row=2, column=3)
        b2 = Button(window, text='Search entry', width=12, command=self.search_command)
        b2.grid(row=3, column=3)
        b3 = Button(window, text='Add entry', width=12, command=self.add_command)
        b3.grid(row=4, column=3)
        b4 = Button(window, text='Update', width=12, command=self.update_command)
        b4.grid(row=5, column=3)
        b5 = Button(window, text='Delete', width=12, command=self.delete_command)
        b5.grid(row=6, column=3)
        b6 = Button(window, text='Close', width=12, command=window.destroy)
        b6.grid(row=7, column=3)
        
    def get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[3])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[2])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])
    
    def view_command(self):
        self.list1.delete(0, END)
        for row in self.db.query():
            self.list1.insert(END, row)
    
    def search_command(self):
        self.list1.delete(0, END)
        for row in self.db.search(self.title_text.get(), self.author_value.get(), self.year_value.get(), 
                                  self.isbn_value.get()):
            self.list1.insert(END, row)
    
    def add_command(self):
        self.db.insert(self.title_text.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_value.get(), self.year_value.get(),
                                self.isbn_value.get()))
    
    def delete_command(self):
        self.db.delete(self.selected_tuple[0])
    
    def update_command(self):
        self.db.update(self.selected_tuple[0], self.title_text.get(), self.author_value.get(), self.year_value.get(), 
                       self.isbn_value.get())


window = Tk()
UI(window)
window.mainloop()
