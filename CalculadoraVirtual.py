from tkinter import *
import math

windows = Tk()
#Se crea la ventana de la aplicacion
windows.title("CALCULADORA")
windows.config(background="black")
#con eso se coloco el titulo
#Entrada
texto= Entry(windows, font=("Roboto 20"),background="#B6B6B6")
#Campo donde se va escribir los numeros
texto.grid(row = 0, column=0, columnspan=4, padx=5, pady=5)
#Logica
#Insertar
i = 0
numero = 0
def clic(valor):
    global i
    texto.insert(i,valor)
    i+=1
#Borrar desde indice cero, hasta el final
def borrar():
    texto.delete(0, END)
    i = 0
#funsion operaciones
def calcular():
    datos= texto.get()
    resultado = eval(datos)
    texto.delete(0,END)
    texto.insert(0, resultado)
    i = 0
    
def factorial():
    datos= texto.get()
    resultado = int(eval(datos))
    dos = math.factorial(resultado)
    texto.delete(0,END)
    texto.insert(0, dos)
    return math.factorial(numero)

def raiz_cuadrada():
    datos= texto.get()
    resultado = int(eval(datos))
    uno = math.sqrt(resultado)
    texto.delete(0,END)
    texto.insert(0, uno)
    return math.sqrt(numero)
    

#BOTONES
box1 = Button(windows, text="1", width=5, height=2, background="#B6B6B6", command=lambda: clic(1))
box2 = Button(windows, text="2", width=5, height=2, background="#B6B6B6",command=lambda: clic(2))
box3 = Button(windows, text="3", width=5, height=2, background="#B6B6B6", command=lambda: clic(3))
box4 = Button(windows, text="4", width=5, height=2, background="#B6B6B6", command=lambda: clic(4))
box5 = Button(windows, text="5", width=5, height=2, background="#B6B6B6", command=lambda: clic(5))
box6 = Button(windows, text="6", width=5, height=2, background="#B6B6B6", command=lambda: clic(6))
box7 = Button(windows, text="7", width=5, height=2, background="#B6B6B6", command=lambda: clic(7))
box8 = Button(windows, text="8", width=5, height=2, background="#B6B6B6", command=lambda: clic(8))
box9 = Button(windows, text="9", width=5, height=2, background="#B6B6B6", command=lambda: clic(9))
box0 = Button(windows, text="0", width=5, height=2, background="#B6B6B6", command=lambda: clic(0))

boxSuma = Button(windows, text="+", width=5, height=2, background="#586770",command=lambda: clic("+"))
boxResta = Button(windows, text="-", width=5, height=2, background="#586770",command=lambda: clic("-"))
boxFactorial = Button(windows, text="F", width=5, height=2, background="#586770",command=lambda: factorial())
boxPotenciacion = Button(windows, text="^", width=5, height=2, background="#586770",command=lambda: clic("**"))
boxRaiz = Button(windows, text="√", width=5, height=2, background="#586770",command=lambda: raiz_cuadrada())
boxPorcentaje = Button(windows, text="%", width=5, height=2, background="#586770",command=lambda: clic("%"))
boxMultiplicacion = Button(windows, text="*", width=5, height=2, background="#586770",command=lambda: clic("*"))
boxDivision = Button(windows, text="/", width=5, height=2, background="#586770",command=lambda: clic("/"))
boxPunto = Button(windows, text=".", width=5, height=2, background="#586770",command=lambda: clic("."))
boxIgual = Button(windows, text="=", width=5, height=2, background="#4da1a2",command=lambda: calcular())
boxBorrar = Button(windows, text="CE", width=5, height=2, background="#586770",command=lambda: borrar())
boxParentesis1 = Button(windows, text="(", width=5, height=2, background="#586770",command=lambda: clic("("))
boxParentesis2 = Button(windows, text=")", width=5, height=2, background="#586770",command=lambda: clic(")"))
boxComa = Button(windows, text=",", width=5, height=2, background="#586770",command=lambda: clic(","))
#Mostrarlos en pantalla
boxBorrar.grid(row=1, column=0, padx=5, pady=5)
boxParentesis1.grid(row=1, column=1, padx=5, pady=5)
boxParentesis2.grid(row=1, column=2, padx=5, pady=5)
boxRaiz.grid(row=1, column=3, padx=5, pady=5)


boxPorcentaje.grid(row=2, column=0, padx=5, pady=5)
boxFactorial.grid(row=2, column=1, padx=5, pady=5)
boxPotenciacion.grid(row=2, column=2, padx=5, pady=5)
boxDivision.grid(row=2, column=3, padx=3, pady=5)

box1.grid(row=3, column=0, padx=5, pady=5)
box2.grid(row=3, column=1, padx=5, pady=5)
box3.grid(row=3, column=2, padx=5, pady=5)
boxSuma.grid(row=3, column=3, padx=5, pady=5)



box4.grid(row=4, column=0, padx=5, pady=5)
box5.grid(row=4, column=1, padx=5, pady=5)
box6.grid(row=4, column=2, padx=5, pady=5)
boxResta.grid(row=4, column=3, padx=5, pady=5)

box7.grid(row=5, column=0, padx=5, pady=5)
box8.grid(row=5, column=1, padx=5, pady=5)
box9.grid(row=5, column=2, padx=5, pady=5)
boxMultiplicacion.grid(row=5, column=3, padx=5, pady=5)


boxPunto.grid(row=6, column=0, padx=5, pady=5)
box0.grid(row=6, column=1, padx=5, pady=5)
boxComa.grid(row=6, column=2, padx=5, pady=5)
boxIgual.grid(row=6, column=3, padx=5, pady=5, )


windows.mainloop()

