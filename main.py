from select import select
from tkinter import *
from tkinter import ttk


class mainApp(Tk):
    entrada = None
    tipoUnidad = None

    __temperaturaAnt = '' #temperatura anterior

    def __init__(self):
        Tk.__init__(self)
        self.title('Termometro')
        self.geometry('200x150')
        self.configure(bg='#ded7b9')
        self.resizable(0, 0)

        self.temperatura = StringVar(value='')
        self.temperatura.trace('w', self.validateTemperature)
        self.tipoUnidad = StringVar(value='C')

        self.createLayout()

    def createLayout(self):
        self.entrada = ttk.Entry(
            self, textvariable=self.temperatura).place(x=10, y=10)

        self.lblUnidad = ttk.Label(self, text='Grados:').place(x=10, y=45)
        self.rb1 = ttk.Radiobutton(
            self, text='Fahrenheit', variable=self.tipoUnidad, value='F', command=self.selected).place(x=20, y=70)
        self.rb2 = ttk.Radiobutton(
            self, text='Celsius', variable=self.tipoUnidad, value='C', command=self.selected).place(x=20, y=95)


    def selected(self):
        resultado = 0
        toUnidad = self.tipoUnidad.get()
        grados = float(self.temperatura.get())

        if toUnidad =='F':
            resultado = grados * 9/5 +32
        elif toUnidad =='C':
            resultado = (grados-32) * 5/9
        else:
            resultado = grados
                
        self.temperatura.set(resultado)
            

    def start(self):
        self.mainloop()

    def validateTemperature(self, *args): # * espera una tupla o lista de argumentos
        nuevoValor = self.temperatura.get()
        print('nuevoValor', nuevoValor, 'vs valorAnterior', self.__temperaturaAnt)
        try:
            float(nuevoValor)
            self.__temperaturaAnt = nuevoValor
            print('fija valor anterior', self.__temperaturaAnt)
        except:
            self.temperatura.set(self.__temperaturaAnt)
            print('recupera valor anterior', self.__temperaturaAnt)

if __name__ == '__main__':
    app = mainApp()
    app.start()
