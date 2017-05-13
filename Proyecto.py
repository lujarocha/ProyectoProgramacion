from tkinter import *
import time
"""
"""
#Crea ventana
ventana = Tk()
ventanaSecundaria= Toplevel(ventana) #Ventana Que se abre al presionar comenzar
ventanaSecundaria.title("Asignacion Nivel")
#Define tamaño a ventana
ventana.geometry("1233x907")
#Define tamaño venta secundaria
ventanaSecundaria.geometry("1233x907")
#
imgfondo2 = PhotoImage(file="C:/Users/lucho/Desktop/Proyecto Programación/fondoSecundario.gif")
labelfondo = Label(ventanaSecundaria, image=imgfondo2).pack()
#Titulo de la ventana
ventana.title("Welcome to Fatal Cross.                   ¡¿Are You Ready for DEAD?!")
#Ponemos Imagen de Fondo
imgfondo = PhotoImage(file="C:/Users/lucho/Desktop/Proyecto Programación/Background.gif")
labelfondo = Label(ventana, image=imgfondo).pack()

#Funciones Para Abrir Ventana Secundaria
def mostrar(ventana): ventana.deiconify()
def ejecutar(f): ventana.after(200, f)
#Funcion Para minimizar ventana principal
def minimizar(n):
    ventana.iconify()
    time.sleep(1)
    
#Creamos Boton de Iniciar y damos instrucción de abrir la otra ventana
botonIniciar= Button(ventana, text="Comenzar",command=lambda: ejecutar(mostrar(ventanaSecundaria)))

botonIniciar.pack()
botonIniciar.place(x=260, y=720)








#Ciclo Para Escucha Eventos (Dejar de ultimo)
ventana.mainloop()
    
