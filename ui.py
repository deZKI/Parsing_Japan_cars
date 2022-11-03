import threading
from tkinter import Frame, Button, Entry, OptionMenu, StringVar, Label, Checkbutton, IntVar, Tk

from core import start_search
from markers import MODELS, MARKERS


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.clickedMarker = StringVar()
        self.clickedModel = StringVar()
        self.start_search = start_search
        self.create_topic_menu()

    def create_topic_menu(self):
        self.text_marker = Label(text='Марка', font="ARIAL 15")
        self.text_marker.place(x=0, y=0, width=350)

        self.marker = OptionMenu(self.parent, self.clickedMarker, *MODELS.keys(), command=self.make_models)
        self.marker.place(x=0, y=24, width=350, height=24)

        self.text_model = Label(text='Модель', font="ARIAL 15")
        self.text_model.place(x=0, y=44, width=350, height=24)

        self.model = OptionMenu(self.parent, self.clickedModel, '-')
        self.model.place(x=0, y=70, width=350, height=24)

        self.text_year = Label(text='Год', font="ARIAL 15")
        self.text_year.place(x=0, y=100, width=350, height=24)

        self.year = Entry()
        self.year.place(x=0, y=130, width=350, height=24)

        self.text_page = Label(text='Страница', font="ARIAL 15")
        self.text_page.place(x=0, y=160, width=350, height=24)

        self.page = Entry()
        self.page.place(x=0, y=190, width=350, height=24)

        self.text_colors = Label(text='Цвета', font="ARIAL 15")
        self.text_colors.place(x=0, y=220, width=350, height=24)

        self.make_colors()

        self.text_transission = Label(text='Трансмиссия', font="ARIAL 15")
        self.text_transission.place(x=0, y=340, width=350, height=24)
        self.make_transmission()

        self.text_drive = Label(text='Привод', font="ARIAL 15")
        self.text_drive.place(x=0, y=410, width=350, height=24)
        self.make_drive()

        self.text_fuel = Label(text="Двигатель", font="ARIAL 15")
        self.text_fuel.place(x=0, y=465, width=350, height=24)
        self.make_fuel()

        self.text_handle = Label(text="Руль", font="ARIAL 15")
        self.text_handle.place(x=0, y=560, width=350, height=24)
        self.make_handle()

        self.root = Entry()
        self.root.place(x=0, y=650, width=350, height=35)

    def make_models(self, p):
        self.model = OptionMenu(self.parent, self.clickedModel, *MODELS[self.clickedMarker.get()].keys())
        self.model.place(x=0, y=70, width=350, height=24)

        self.btn_find_topic = Button(text='Найти', command=self.download)
        self.btn_find_topic.place(x=0, y=610, height=50, width=350)

    def make_colors(self):
        self.colors = []
        for i in range(14):
            self.colors.append(StringVar())
        self.color_white = Checkbutton(background='white', variable=self.colors[0], onvalue=1, offvalue="")
        self.color_white.place(x=0, y=250, width=30, height=30)

        self.color_black = Checkbutton(background='black', variable=self.colors[1], onvalue=2, offvalue="")
        self.color_black.place(x=40, y=250, width=30, height=30)

        self.color_grey = Checkbutton(background='grey', variable=self.colors[2], onvalue=3, offvalue="")
        self.color_grey.place(x=80, y=250, width=30, height=30)

        self.color_silver = Checkbutton(background='silver', variable=self.colors[3], onvalue=4, offvalue="")
        self.color_silver.place(x=120, y=250, width=30, height=30)

        self.color_red = Checkbutton(background='red', variable=self.colors[4], onvalue=5, offvalue="")
        self.color_red.place(x=160, y=250, width=30, height=30)

        self.color_green = Checkbutton(background='green', variable=self.colors[5], onvalue=6, offvalue="")
        self.color_green.place(x=200, y=250, width=30, height=30)

        self.color_blue = Checkbutton(background='blue', variable=self.colors[6], onvalue=7, offvalue="")
        self.color_blue.place(x=240, y=250, width=30, height=30)

        self.color_navy_blue = Checkbutton(background='navy', variable=self.colors[7], onvalue=8, offvalue="")
        self.color_navy_blue.place(x=280, y=250, width=30, height=30)

        self.color_yellow = Checkbutton(background='yellow', variable=self.colors[8], onvalue=9, offvalue="")
        self.color_yellow.place(x=40, y=290, width=30, height=30)

        self.color_gold = Checkbutton(background='gold', variable=self.colors[9], onvalue=10, offvalue="")
        self.color_gold.place(x=0, y=290, width=30, height=30)

        self.color_beige = Checkbutton(background='beige', variable=self.colors[10], onvalue=11, offvalue="")
        self.color_beige.place(x=40, y=290, width=30, height=30)

        self.color_purple = Checkbutton(background='purple', variable=self.colors[11], onvalue=12, offvalue="")
        self.color_purple.place(x=80, y=290, width=30, height=30)

        self.color_two_tone = Checkbutton(text="Два тона", variable=self.colors[12], background="white smoke",
                                          onvalue=13, offvalue="")
        self.color_two_tone.place(x=120, y=290, width=100, height=30)

        self.color_others = Checkbutton(text="Другие", variable=self.colors[13], background="snow", onvalue=14,
                                        offvalue="")
        self.color_others.place(x=220, y=290, width=100, height=30)

    def make_transmission(self):
        self.at = IntVar()
        self.cvt = IntVar()
        self.mt = IntVar()
        self.mission_at = Checkbutton(text='AT', variable=self.at)
        self.mission_at.place(x=0, y=370, width=50, height=30)

        self.mission_cvt = Checkbutton(text='CVT', variable=self.cvt)
        self.mission_cvt.place(x=60, y=370, width=50, height=30)

        self.mission_mt = Checkbutton(text='MT', variable=self.mt)
        self.mission_mt.place(x=120, y=370, width=50, height=30)

    def make_drive(self):
        self.drive = []
        self.drive.append(StringVar())
        self.drive.append(StringVar())
        self.drive_2wd = Checkbutton(text='2WD', variable=self.drive[0], onvalue=1, offvalue="")
        self.drive_2wd.place(x=0, y=440, width=50, height=30)

        self.drive_2wd = Checkbutton(text='4WD', variable=self.drive[1], onvalue=2, offvalue="")
        self.drive_2wd.place(x=60, y=440, width=50, height=30)

    def make_fuel(self):
        self.fuels = []
        for i in range(6):
            self.fuels.append(StringVar())
        self.fuel_gasoline = Checkbutton(text='бензин', variable=self.fuels[0], onvalue=1, offvalue="")
        self.fuel_gasoline.place(x=0, y=490, width=70, height=30)

        self.fuel_hybrid = Checkbutton(text='дизель', variable=self.fuels[1], onvalue=2, offvalue="")
        self.fuel_hybrid.place(x=80, y=490, width=70, height=30)

        self.fuel_hydrogen = Checkbutton(text='другие', variable=self.fuels[2], onvalue=3, offvalue="")
        self.fuel_hydrogen.place(x=150, y=490, width=80, height=30)

        self.fuel_diesel = Checkbutton(text='гибрид', variable=self.fuels[3], onvalue=4, offvalue="")
        self.fuel_diesel.place(x=240, y=490, width=70, height=30)

        self.fuel_electricity = Checkbutton(text='электро', variable=self.fuels[4], onvalue=5, offvalue="")
        self.fuel_electricity.place(x=0, y=530, width=90, height=30)

        self.fuel_others = Checkbutton(text='водород', variable=self.fuels[5], onvalue=6, offvalue="")
        self.fuel_others.place(x=100, y=530, width=80, height=30)

    def make_handle(self):
        self.streering = [StringVar(), StringVar()]

        self.handle_left = Checkbutton(text='левый', variable=self.streering[0], onvalue=2, offvalue="")
        self.handle_left.place(x=0, y=580, width=70, height=30)

        self.handle_right = Checkbutton(text='правый', variable=self.streering[1], onvalue=1, offvalue="")
        self.handle_right.place(x=80, y=580, width=70, height=30)

    def download(self):
        transmission = ""
        drive = []

        if self.at.get() == 1 and self.cvt.get() == 1 and self.mt.get() == 1:
            transmission = "7"
        elif self.at.get() == 1 and self.cvt.get() == 1:
            transmission = "2"
        elif self.at.get() == 1 and self.mt.get() == 1:
            transmission = "6"
        elif self.cvt.get() == 1 and self.mt.get() == 1:
            transmission = "5"
        elif self.at.get() == 1:
            transmission = "3"
        elif self.cvt.get() == 1:
            transmission = "1"
        elif self.mt.get() == 1:
            transmission = "4"

        a = threading.Thread(target=start_search,
                             args=(
                                 MARKERS[self.clickedMarker.get()],
                                 MODELS[self.clickedMarker.get()][self.clickedModel.get()], self.year.get().upper(),
                                 transmission,
                                 form(self.drive), form(self.fuels), form(self.colors), form(self.streering),
                                 self.page.get(), self.root.get()
                             ), daemon=True)
        a.start()


def form(iterator):
    s = ""
    for i in iterator:
        if i.get() != "":
            s = s + i.get() + ','
    return s[:-1] if s != "" else ""


def startapp():
    # get_markers()
    root = Tk()
    root.title('kakaku.com')
    root.geometry("350x700+0+0")
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()
