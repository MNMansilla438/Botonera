from tkinter import *
import tkinter
import winsound


#titulos y fotos
class funcionBotonera:
    def __init__(self, Titulo,fotos,NomBoton, NomBoton2 ,sonidos1,sonidos2): 
        self.sampleTitle(Titulo)
        self.samplePictures(fotos)
        self.sampleButtons(NomBoton, NomBoton2 ,sonidos1,sonidos2)
#titulos        
    def sampleTitle(self, Titulo):
        for x in range(7):           
            Label(text= Titulo[x]).grid(column = x, row = 1, pady = 10)
#fotitos
    def samplePictures(self,fotos):
        fotos2 = []
        for z in fotos:
            self.img = PhotoImage(file = z)
            fotos2.append(self.img)
        for x in range(7): 
            j = Label(self.Ventana, image = fotos2[x])
            j.grid(column = x , row = 2, padx = 12, pady = 10)
            j.image = fotos2[x]
 #Botones y sonidos   
    def sampleButtons(self, NomBoton, NomBoton2 , sonidos1,sonidos2):
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[0]), text=NomBoton[0]).grid(column = 0 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[1]), text=NomBoton[1]).grid(column = 1 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[2]), text=NomBoton[2]).grid(column = 2 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[3]), text=NomBoton[3]).grid(column = 3 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[4]), text=NomBoton[4]).grid(column = 4 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[5]), text=NomBoton[5]).grid(column = 5 , row= 3 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds(sonidos1[6]), text=NomBoton[6]).grid(column = 6 , row= 3 , pady = 20) 

        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[0]), text=NomBoton2[0]).grid(column = 0 , row= 4 , pady = 20)
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[1]), text=NomBoton2[1]).grid(column = 1 , row= 4 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[2]), text=NomBoton2[2]).grid(column = 2 , row= 4 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[3]), text=NomBoton2[3]).grid(column = 3 , row= 4 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[4]), text=NomBoton2[4]).grid(column = 4 , row= 4 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[5]), text=NomBoton2[5]).grid(column = 5 , row= 4 , pady = 20) 
        Button(self.Ventana,command=lambda:self.sounds2(sonidos2[6]), text=NomBoton2[6]).grid(column = 6 , row= 4 , pady = 20) 
    

    def sounds(self, x):
       self.audio= winsound.PlaySound(x , winsound.SND_ASYNC)
        
    def sounds2(self, z):
        winsound.PlaySound(z , winsound.SND_ASYNC)

     
        
#ventana
class botonera(funcionBotonera):
    
    def __init__(self, Titulo,fotos,NomBoton, NomBoton2 ,sonidos1,sonidos2):
        self.Ventana = Tk()
        self.Ventana.geometry("900x300")
        self.Ventana.title("Botonera")
        self.Ventana.iconbitmap("fotos/Boton.ico")
        self.Ventana.resizable(width=False, height=False)
        self.fondo()
        super().__init__(Titulo,fotos,NomBoton, NomBoton2 ,sonidos1,sonidos2)
        self.Ventana.mainloop()
        

    def fondo(self):
        self.fondo = PhotoImage(file = "fotos/fondo.gif")
        self.lblimagen = Label(self.Ventana, image = self.fondo).place(x=0,y=0)


#inicializador
Titulo=["Vaca","Caballo","Cabra","Robot","Rerro","Pato","Gato"]
fotos=["fotos/foto1.gif","fotos/foto2.gif","fotos/foto3.gif","fotos/foto4.gif","fotos/foto5.gif","fotos/foto6.gif","fotos/foto7.gif"]
NomBoton=["Vaca1","Caballo1","Cabra1","Robot1","Perro1","Pato1","Gato1"]
NomBoton2=["Vaca2","Caballo2","Cabra2","Robot2","Perro2","Pato2","Gato2"]
sonidos1=["sonidos/vaca1.wav","sonidos/caballo1.wav","sonidos/cabra1.wav","sonidos/robot1.wav","sonidos/perro1.wav","sonidos/pato1.wav","sonidos/gato1.wav"]
sonidos2=["sonidos/vaca2.wav","sonidos/caballo2.wav","sonidos/cabra2.wav","sonidos/robot2.wav","sonidos/perro2.wav","sonidos/pato2.wav","sonidos/gato2.wav"]


def main():
    arrancar=botonera(Titulo, fotos, NomBoton, NomBoton2, sonidos1, sonidos2)
    return(0)

if __name__ == "__main__":
    main()


