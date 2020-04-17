#######################
#imports
from Aleatorio import *
from tkinter import *
import time
########################

########################
#declaracion de variables
puntos = []
limites = []
restricciones = 0
########################

########################
#modificadores y creacion de ventana
window = Tk()                                #crea una nueva ventana
window.title("Examen Segundo Departamental") #Establece el titulo de la ventana
window.geometry('400x50')                    #Establece el tamaño de la ventana(en pixeles)
########################

window.iconbitmap('icono.ico')




###########################################################################################################
#Aqui estan las funciones que se llaman al apretar un boton

#######################
#Esta funcion se llama al colocar las coordenadas
def sig(cordenadas):

     if len(cordxentrada.get())>0:                                                   #Este if entra solo se coloco algo en la entrada de texto de las coordenadas
          puntos.append([float(cordxentrada.get()),float(cordyentrada.get()),float(distentrada.get())])  #Se concatenan las coordenadas x,y y distancia
     
     
     
     #################################
     #Se cambia el texto de las etiquetas para indicar en que coordenada va el usuario
     cordx.configure(text="Ingrese la coordenada {} en x:".format(cordenadas+1))
     cordy.configure(text="Ingrese la coordenada {} en y:".format(cordenadas+1))
     dist.configure(text="Distancia del punto {} de la cordenada {} : ".format(cordenadas+1,cordenadas+1))
     #################################


     if (int(coordenadas.cget("text")))==int(restric.cget("text")):                  #Este if entra solo si ya se colocaron todas las coordenadas

          #################################
          #Se destruyen los elementos que ya no se utilizan
          cordx.destroy()
          cordy.destroy()
          cordxentrada.destroy()
          cordyentrada.destroy()
          dist.destroy()
          distentrada.destroy()
          siguiente.destroy()
          lbl.destroy()
          lbl2.destroy()
          ################################

          ################################
          #Se configuran los elementos (tamaño de texto,texto,borde, y tamaño)
          advertencia.config(text="ADVERTENCIA: Ya que se usa el metodo de semillas aleatorias,")
          advertencia2.config(text="es necesario que se coloquen 5000 iteraciones como minimo")
          iteracionesEntrada.config(width=10,state='normal',bd=1)
          limiteIxEntrada.config(width=10, state='normal',bd=1)
          limiteSxEntrada.config(width=10, state='normal',bd=1)
          limiteIyEntrada.config(width=10, state='normal',bd=1)
          limiteSyEntrada.config(width=10, state='normal',bd=1)
          iteraciones.config(text="Numero de iteraciones:")
          limiteIx.config(text="Limite inferior en x:")
          limiteSx.config(text="Limite superior en x:")
          limiteIy.config(text="Limite inferior en y:")
          limiteSy.config(text="Limite superior en y:")
          btncalculo.configure(text="Calcular",bd=1)
          ###############################

          ###############################
          #Se muestran los elementos en la ventana
          iteracionesEntrada.grid(column=1,row=4)
          limiteIxEntrada.grid(column=1, row=0)
          limiteSxEntrada.grid(column=1, row=1)
          limiteIyEntrada.grid(column=1, row=2)
          limiteSyEntrada.grid(column=1, row=3)
          iteraciones.grid(column=0, row=4)
          limiteIx.grid(column=0, row=0)
          limiteSx.grid(column=0, row=1)
          limiteIy.grid(column=0, row=2)
          limiteSy.grid(column=0, row=3)
          btncalculo.grid(column=3, row=6)
          advertencia.place(x=0,y=150)
          advertencia2.place(x=0,y=170)
          ###############################
     
     coordenadas.configure(text =str(cordenadas+1))
#######################        

#######################
#Esta funcion se llama al tener todos los datos, para calcular el resultado
def calcular():

     if len(iteracionesEntrada.get())>0:                                        #Si se dejo la entrada de texto vacia, no deja avanzar

          if int(iteracionesEntrada.get())>4999:                                #Si se indicaron menos de 5000 iteraciones, no deja avanzar

               limites.append([float(limiteIxEntrada.get()),float(limiteSxEntrada.get())])     #Se concatenan los limites en x a una variable
               limites.append([float(limiteIyEntrada.get()),float(limiteSyEntrada.get())])     #Se concatenan los limites en y a una variable
 
               solucion = Aleatorio(puntos,limites,int(restric.cget("text")))                  #Se crea un nuevo objeto con los valores que ya nos dio el usuario
               temp = int(iteracionesEntrada.get())                                            
               solucionx,soluciony = solucion.iterar(temp)                                     #Se soluciona el problema

               ###############################
               #Se destruyen los elementos que ya no se usan
               iteraciones.destroy()
               iteracionesEntrada.destroy()
               limiteIx.destroy()
               limiteIxEntrada.destroy()
               limiteIy.destroy()
               limiteIyEntrada.destroy()
               limiteSx.destroy()
               limiteSxEntrada.destroy()
               limiteSy.destroy()
               limiteSyEntrada.destroy()
               btncalculo.destroy()
               advertencia.destroy()
               advertencia2.destroy()
               ###############################
               
               window.geometry('700x50')                                                #Modifica el tamaño de la pantalla
               Resultado = Label(window,text="Solucion: x = {} ; y = {} ".format(solucionx,soluciony))
               Resultado.config(font=("Courier", 20))
               Resultado.grid(column=1, row=1)
          else:                                                                          #Entra si solo se colocaron menos de 5000 iteraciones
               advertencia.config(text="Coloque mas de 5000 iteraciones por favor")      #Reafirma que son necesarias mas de 5000 iteraciones
               advertencia2.destroy()
#######################

#######################
#Esta funcion se llama al dar clic al primer boton, indicando el numero de  restricciones
def clicked():

    if len(rest.get())>0:                                                  #Si se dejo la entrada de texto vacia, no deja avanzar

          window.geometry('400x200')                                            #Cambia el tamaño de la ventana
          restricciones = int(rest.get())                                       #Guarda la entrada de las restricciones  en una variable                   
          tmp = "Se usaran " + rest.get() + " restricciones"                    #Se guarda la nueva etiqueta en una variable
          restric.configure(text=rest.get())

          #####################
          #Se destruyen los elementos que ya no se usaran
          btn.destroy()
          rest.destroy()
          #####################


          #####################
          #Se cambian las configuraciones de las etiquetas y entradas, cambiando su texto y mostrandolas
          lbl.configure(text= tmp)
          lbl2.configure(text="Ingrese las cordenadas de sus puntos")
          cordxentrada.configure(width=10,bd=1, state='normal')
          cordyentrada.configure(width=10,bd=1, state='normal')
          distentrada.configure(width=10,bd=1, state='normal')
          siguiente.configure(bd=1,text="siguiente")
          cordx.configure(text="Ingrese la coordenada 1 en x:")
          cordy.configure(text="Ingrese la coordenada 1 en y:")
          dist.configure(text="Distancia del punto 1 de la cordenada 1: ")
          #####################

#######################

###########################################################################################################

##############################
# Creacion de elementos de la ventana (etiquetas, botones,entradas)          
siguiente = Button(window, text="", bd=0,command=lambda: sig(int(coordenadas.cget("text"))))
iteracionesEntrada = Entry(window,width=0, state='disabled',bd=0)
lbl = Label(window, text="Ingrese el numero de restricciones:")
limiteIxEntrada = Entry(window,width=0, state='disabled', bd=0)
limiteSxEntrada = Entry(window,width=0, state='disabled', bd=0)
limiteIyEntrada = Entry(window,width=0, state='disabled', bd=0)
limiteSyEntrada = Entry(window,width=0, state='disabled', bd=0)
cordxentrada = Entry(window,width=0, state='disabled',bd=0)
cordyentrada = Entry(window,width=0, state='disabled',bd=0)
btncalculo = Button(window, text="", bd=0,command=calcular)
distentrada = Entry(window,width=0, state='disabled',bd=0)
btn = Button(window, text="Aceptar", command=clicked)
rest = Entry(window,width=10, state='normal')
coordenadas = Label(window, text="1")
advertencia2 = Label(window,text="")
iteraciones = Label(window,text="")
advertencia = Label(window,text="")
limiteIx = Label(window,text="")
limiteSx = Label(window,text="")
limiteIy = Label(window,text="")
limiteSy = Label(window,text="")
restric=Label(window, text="")
cordx = Label(window, text="")
cordy = Label(window, text="")
lbl2 = Label(window, text="")
dist = Label(window, text="")
##############################


##############################
#En esta parte se acomodan los elementos en la pantalla mediante una cuadricula siendo column las columnas y row las filas
iteracionesEntrada.grid(column=11,row=4)
advertencia2.grid(column=100, row=100)
limiteSyEntrada.grid(column=11, row=3)
limiteIyEntrada.grid(column=11, row=2)
limiteSxEntrada.grid(column=11, row=1)
limiteIxEntrada.grid(column=11, row=0)
advertencia.grid(column=100, row=100)
btncalculo.grid(column=30, row=60)
iteraciones.grid(column=10, row=4)
cordyentrada.grid(column=1, row=3)
cordxentrada.grid(column=1, row=2)
distentrada.grid(column=1, row=4)
siguiente.grid(column=3, row=6)
limiteSy.grid(column=10, row=3)
limiteIy.grid(column=10, row=2)
limiteSx.grid(column=10, row=1)
limiteIx.grid(column=10, row=0)
cordy.grid(column=0, row=3)
cordx.grid(column=0, row=2)
dist.grid(column=0, row=4)
lbl2.grid(column=0, row=1)
rest.grid(column=1, row=0)
btn.grid(column=2, row=0)
lbl.grid(column=0, row=0)
##############################


rest.focus() #Esta instruccion permite que la entrada de texto inicie seleccionada



#############################
window.mainloop() #El loop de la ventana permite que siempre se muestre
#############################