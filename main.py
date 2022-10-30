from ui import Example
from tkinter import Tk
if __name__ == '__main__':
    # get_markers()
    root = Tk()
    root.title('kakaku.com')
    root.geometry("850x650+300+300")
    root.resizable(False, False)
    app = Example(root)
    root.mainloop()
