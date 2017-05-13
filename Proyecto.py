from tkinter import *
import time
"""
lbl = Label
btn = Botón
"""
#Crea ventana
ventana = Tk()
ventanaSecundaria= Toplevel(ventana) #Ventana Que se abre al presionar comenzar
ventanaSecundaria.title("Registro y Niveles")
#Define tamaño a ventana
ventana.geometry("1233x907")
#Define tamaño venta secundaria
ventanaSecundaria.geometry("1233x907")
#Ponmos fondo a La ventana d Asignación de nivel
imgfondo2 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/fondoSecundario.gif")
labelfondo = Label(ventanaSecundaria, image=imgfondo2).pack()
#Titulo de la ventana
ventana.title("Welcome to Mortal Cross.                   ¡¿Are You Ready for DEAD?!")
#Ponemos Imagen de Fondo
imgfondo = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Background.gif")
labelfondo = Label(ventana, image=imgfondo).pack()

#Funciones Para Abrir Ventana Secundaria
def mostrar(ventana): ventana.deiconify()
def ejecutar(f): ventana.after(200, f)
#Funcion Para minimizar ventana principal

def minimizar(n):
    ventana.iconify()
    time.sleep(1)
    
#Creamos Boton de Iniciar y damos instrucción de abrir la otra ventana
botonComenzar = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/BotonComenzar.png")
botonIniciar= Button(ventana,image=botonComenzar,relief=("raised"), text="Comenzar",command=lambda:ejecutar(mostrar(ventanaSecundaria)))
#Se crea Boton "SALIR" para cerrar la ventana principal 
botonCerrar= PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/BotonSalir.png")
botonSalir=Button(ventana,image=botonCerrar, command=ventana.destroy).place(x=258, y=800)
#Funcion para dar bienvenida a Usuarios
def bienvenido1():
    lblsaludo1=Label(ventanaSecundaria, text="Hola " + entradaUsuario1.get() + ", Listo Para Morir?!",font=("Agency FB",20)).place(x=750, y=320)
def bienvenido2():
    lblsaludo1=Label(ventanaSecundaria, text="Hola " + entradaUsuario2.get() + ", Listo Para Morir?!",font=("Agency FB",22)).place(x=750, y=500)
    

#Label con Imagen y Cuadro de texto para insertar nombre del Juagdor # 1
imglblUser1 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/fondolabelUser1.png")
lblUser1 = Label(ventanaSecundaria,relief=("raised"),image=imglblUser1).place(x=400, y=340)
entradaUsuario1 = StringVar()
txtUsuario1=Entry(ventanaSecundaria, textvariable=entradaUsuario1, width=40).place(x=750, y=365)

#Label con Imagen y Cuadro de texto para insertar nombre del Juagdor # 2
imglblUser2 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/fondolabelUser2.png")
lblUser2 = Label(ventanaSecundaria,relief=("raised"),image=imglblUser2).place(x=400, y=440)
entradaUsuario2 = StringVar()
txtUsuario2=Entry(ventanaSecundaria, textvariable=entradaUsuario2, width=40).place(x=750, y=465)
#Botones Para Saluadar Usuarios
btnHiUser1= Button(ventanaSecundaria,text="Aceptar",command=bienvenido1,font=("Agency FB",18)).place(x=1010,y=335)
btnHiUser2= Button(ventanaSecundaria,text="Aceptar",command=bienvenido2,font=("Agency FB",18)).place(x=1010,y=435)

botonIniciar.pack()
botonIniciar.place(x=260, y=720)








#Ciclo Para Escucha Eventos (Dejar de ultimo)
ventana.mainloop()
    
