from tkinter import *
import time
"""
lbl = Label
btn = Botón
"""
#Crea ventanas
ventana = Tk()
ventanaSecundaria= Toplevel(ventana) #Ventana Que se abre al presionar comenzar
ventanaSecundaria.title("Registro y Niveles")
ventanaNivel1 = Toplevel(ventanaSecundaria)
ventanaNivel1.title("Nivel 1")
ventanaNivel2 = Toplevel(ventanaSecundaria)
ventanaNivel2.title("Nivel 2")
ventanaNivel3 = Toplevel(ventanaSecundaria)
ventanaNivel3.title("Nivel 3")
ventanaNivel4 = Toplevel(ventanaSecundaria)
ventanaNivel4.title("Nivel 4")
ventanaNivel5 = Toplevel(ventanaSecundaria)
ventanaNivel5.title("Nivel 5")
#Define tamaño a ventanas
ventana.geometry("1233x907") #Ventana Principal
ventanaSecundaria.geometry("1233x907") #Ventana Secundaria Asiganción Niveles y Registro
ventanaNivel1.geometry("1233x907") #Ventana Primer Nivel
ventanaNivel2.geometry("1233x907") #Ventana Segundo Nivel
ventanaNivel3.geometry("1233x907") #Ventana Tercer Nivel
ventanaNivel4.geometry("1233x907") #Ventana Cuarto Nivel
ventanaNivel5.geometry("1233x907") #Ventana Quinto Nivel
#Ponemos fondo a La ventana d Asignación de nivel
imgfondo2 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/fondoSecundario.gif")
labelfondo = Label(ventanaSecundaria, image=imgfondo2).pack()
#Titulo de la ventana
ventana.title("Welcome to Mortal Cross.                   ¡¿Are You Ready for DEAD?!")
#Ponemos Imagen de Fondo
imgfondo = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Background.gif")
labelfondo = Label(ventana, image=imgfondo).pack()

#Funciones Para Abrir Ventana Secundaria
def mostrar(ventana):
    ventana.deiconify()
    time.sleep(1)
def ejecutar(f): ventana.after(200, f)
#Funcion Para minimizar ventana principal

#def minimizar(n):
    #ventana.iconify()
    #time.sleep(1)
#PRUEBA DE MEZCLAR FUNCIONES


    
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
#Botones Niveles
imgBtn1 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel1.png")
Btn1 = Button(ventanaSecundaria,image=imgBtn1,relief=("raised"),command=lambda:ejecutar(mostrar(ventanaNivel1))).place(x=390, y=710)
#################
imgBtn2 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel2.png")
Btn1 = Button(ventanaSecundaria,image=imgBtn2,relief=("raised"),command=lambda:ejecutar(mostrar(ventanaNivel2))).place(x=560, y=710)
################
imgBtn3 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel3.png")
Btn1 = Button(ventanaSecundaria,image=imgBtn3,relief=("raised"),command=lambda:ejecutar(mostrar(ventanaNivel3))).place(x=730, y=710)
###############
imgBtn4 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel4.png")
Btn1 = Button(ventanaSecundaria,image=imgBtn4,relief=("raised"),command=lambda:ejecutar(mostrar(ventanaNivel4)),).place(x=900, y=710)
##############
imgBtn5 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel5.png")
Btn1 = Button(ventanaSecundaria,image=imgBtn5,relief=("raised"),command=lambda:ejecutar(mostrar(ventanaNivel5))).place(x=1070, y=710)

#Ponemos Imagen de Fondo a los niveles
imgfondoNivel1 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel1Pista.gif")
labelfondo = Label(ventanaNivel1, image=imgfondoNivel1).pack()
imgfondoNivel2 = PhotoImage(file="C:/Users/lucho/Desktop/ProyectoProgramacion/Nivel2.gif")
labelfondo = Label(ventanaNivel2, image=imgfondoNivel2).pack()
#Aparecen respectivos nombres de Jugadores en el centro de la pantalla de cada nivel
lblNombreUser1=Label(ventanaNivel1,entradaUsuario1.get(), font=("Agency FB",16)).place(x=300, y=700)



#Ciclo Para Escucha Eventos (Dejar de ultimo)
ventana.mainloop()

    
