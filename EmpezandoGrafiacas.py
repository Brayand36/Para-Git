import tkinter

ventana = tkinter.Tk()#contenedor de graficos
ventana.geometry("400x400")

etiqueta=tkinter.Label(ventana, text="Hola Mundo",bg="green")
etiqueta.pack(fill=tkinter.X)#mostrar etiqueta

cajaNumero1=tkinter.Entry(ventana, font="Helvetica 20")
cajaNumero1.pack()
cajaNumero2=tkinter.Entry(ventana, font="Helvetica 20")
cajaNumero2.pack()

def numerosDeLaCasa():
    num1=int(cajaNumero1.get())
    num2=int(cajaNumero2.get())
    ResultadoMultiplicacion=num1*num2
    etiquetaResult["Text"]=ResultadoMultiplicacion
    #print("El resultado de la multiplicacion es: ",ResultadoMultiplicacion)



boton=tkinter.Button(ventana, text="Multiplicar", command=numerosDeLaCasa)
boton.pack()

etiquetaResult=tkinter.Label(ventana, text="",bg="blue", font="Helvetica 20")
etiquetaResult.pack(fill=tkinter.X) #mostrar etiqueta
ventana.mainloop()