from tkinter import Tk, Frame, Button, messagebox, Entry, OptionMenu, StringVar
from core import start_search
from cars import MARKERS, MODELS, get_markers
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.create_topic_menu()
        self.clicked = StringVar()

    def create_topic_menu(self):
        self.marker = OptionMenu(root, clickedMarker, *MODELS.keys(), command=self.make_models)
        self.marker.place(x=0, y=0, width=250, height=60)


        self.year = Entry()
        self.year.place(x=527, y=0, width=120, height=60)

        self.page = Entry()
        self.page.place(x=667, y=0, width=120, height=60)

        self.root = Entry()
        self.root.place(x=0, y=70, height=60, width=850)

    def make_models(self, p):
        self.model = OptionMenu(root, clickedModel, *MODELS[clickedMarker.get()].keys())
        self.model.place(x=270, y=0, width=250, height=60)

        self.btn_find_topic = Button(text='Найти', command=self.download)
        self.btn_find_topic.place(x=0, y=140, height=60, width=850)
    def download(self):
        a = start_search(clickedMarker.get(), clickedModel.get(), self.year.get().upper(), self.root.get(), self.page.get())
        if a is not int:
            msgbox = messagebox.showinfo('ошибка', a)
        else:
            msgbox = messagebox.showinfo('всего машин', a)
if __name__ == '__main__':
    #get_markers()
    root = Tk()
    root.title('kakaku.com')
    root.geometry("850x650+300+300")
    clickedMarker = StringVar()
    clickedModel = StringVar()
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()