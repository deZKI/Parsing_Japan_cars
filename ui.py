from tkinter import Tk, Frame, Button, messagebox, Listbox, SINGLE, END, Text, Entry, Label
from core import start
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.create_topic_menu()

    def create_topic_menu(self):
        self.marker = Entry()
        self.marker.place(x=0, y=0, width=250, height=60)

        self.model = Entry()
        self.model.place(x=270, y=0, width=250, height=60)

        self.year = Entry()
        self.year.place(x=527, y=0, width=120, height=60)

        self.page = Entry()
        self.page.place(x=667, y=0, width=120, height=60)

        self.root = Entry()
        self.root.place(x=0, y=70, height=60, width=850)



        self.btn_find_topic = Button(text='Найти', command=self.download)
        self.btn_find_topic.place(x=0, y=140, height=60, width=850)
    def download(self):
        a = start(self.marker.get().upper(), self.model.get().upper(), self.year.get().upper(), self.root.get(), self.page.get())
        if a != 1:
            msgbox = messagebox.showinfo('ошибка', a)
