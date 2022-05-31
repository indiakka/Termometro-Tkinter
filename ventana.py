from tkinter import *
from tkinter import Tk

class mainApp(Tk):
#la cabecera se usa para atributos
    size = '1024x768'

    def __init__(self):
        Tk.__init__(self)

        self.geometry(self.size)
        self.title('Mi ventana')
        self.configure(bg='gray')

    def start(self):
        self.mainloop()

if __name__ =='__main__':
    app = mainApp()

    app.start()
