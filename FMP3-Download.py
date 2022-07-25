import codecs
from tkinter.tix import COLUMN
from pytube import YouTube,Search
import os
from tkinter import  messagebox as MessageBox
from tkinter import *
from tkinter import ttk


archivo =  "canciones.txt"
def leer_archivo(nombre):
    f=open(nombre, "r")
    array=[]
    rep=0;
    try:

        for linea in f:
            array.append(linea)
            rep+=1
        f.close()
    except:
        MessageBox.showerror("Error", "Se ha eliminado el fichero")
        array.clear()
    
    return array


def buscar_videos(array):
    array_resultado=[]
    for data in array:
       busqueda= Search(data).results

       array_resultado.append(busqueda[0].watch_url)
    return array_resultado

def escribir_archivo(Cancion):
    try:

        fichero=codecs.open(archivo,"a","utf-8")
        fichero.write(Cancion+"\n")
        fichero.close()
    except:
        pass
    pass
def add_Cancion():
    valor_Canciones=Entrada_Canciones.get()
    if(len(valor_Canciones)!=0):
        
        escribir_archivo(valor_Canciones)
        etiqueta.config(text=valor_Canciones+"\n se ha añadido al archivo")

        pass
    else:
        etiqueta.config(text="Inserta una canción")
        
    


def convertir(array):
    ciclo=0;
    while ciclo<len(array):
        
        try:

            video=YouTube(array[ciclo])
            cancion=video.streams.filter(only_audio=True).first()
            cancion_archivo=cancion.download()
            base,ext = os.path.splitext(cancion_archivo)
            new_file = base + '.mp3'
            try:
                os.rename(cancion_archivo, new_file)
                print(cancion.title + " Se ha descargado")
            except:
                MessageBox.showerror("Error", "Ya tiene descargado esta cancion")
                os.remove(cancion_archivo)
                #break;
        except:
            MessageBox.showerror("Error", "Ha ocurrido un error inesperado. Revise el archivo")
            #break;
        ciclo+=1

def descargar_cancion():
    array=leer_archivo(archivo)
    videos=buscar_videos(array)
    if(len(videos)!=0):
        convertir(videos)
    else:
        MessageBox.showerror("Error","El archivo esta vacio como el corazon de ella o los pechos de lidia")

MessageBox.showinfo("Instrucciones","Biembenido a FMP3-Download \n para descargar sus canciones de youtube ponga los titulos de las canciones en el archivo canciones.txt \n Tenga en cuenta que en cada linea va el titulo de una cancion una vez tenga todas las canciones solo de 2 click a este ejecutable y se descargaran en esta misma carpeta")

#Ventanas


Ventana=Tk()
Ventana.title("FMP3")
Ventana.geometry('500x500')

valor_Canciones="";
Entrada_Canciones= Entry(Ventana,width=50,)
Entrada_Canciones.place(x=125,y=10)

Boton_add = Button(Ventana,text="Añadir",command=add_Cancion)
Boton_add.place(x=70,y=10)

etiqueta=Label(Ventana,text="Inserte arriba las canciones para añadirlas al archivo ")
etiqueta.place(x=125,y=50)

Boton_Descargar = Button(Ventana,text="Descargar canciones",command=descargar_cancion)
Boton_Descargar.place(x=125,y=190)



Ventana.mainloop()