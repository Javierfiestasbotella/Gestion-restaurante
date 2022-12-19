# -*- coding: utf-8 -*-
#!/usr/bin/python
import pandas
import numpy as np
import os
from tkinter import * 
from tkinter import PhotoImage
from tkinter import messagebox
import datetime
from datetime import datetime
import time




class Gestion:
    #constructor
    def __init__(self):
        self.lista01=[]
        self.sepa=''
        self.n=100000
        self.hora=datetime.now().strftime('%H:%M')
        self.d=datetime.now().strftime('%Y-%m-%d')
    
    #interfaz donde se rellena para crear el resumen del sepa    
    def datos_sepa(self):
        global vmes
        vmes=StringVar()
        self.etiqueta_nombre=Label(self.raiz,text="mes").place(x=30, y=0)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vmes).place(x=130, y=0)
        button = Button(self.raiz,  
                text = 'Enviar', 
                height = 2, 
                width = 25, 
                bg='blue',command=s.resumen_sepa).place(x=250, y=150) 
        
    #interfaz donde se rellena para crear la factura
    def factura(self):
        global vnombre
        vnombre=StringVar()
        global vcif
        vcif=StringVar()
        global vdireccion
        vdireccion=StringVar()
        global vcp
        vcp=StringVar()
        global vpoblacion
        vpoblacion=StringVar()
        global vpais
        vpais=StringVar()
        global vprecio
        vprecio=StringVar()

        self.etiqueta_nombre=Label(self.raiz,text="Precio").place(x=30, y=0)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vprecio).place(x=130, y=0)

        self.etiqueta_nombre=Label(self.raiz,text="Nombre").place(x=30, y=50)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vnombre).place(x=130, y=50)

        self.etiqueta_nombre=Label(self.raiz,text="CIF/NIF/NIE").place(x=30, y=100)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vcif).place(x=130, y=100)

        self.etiqueta_nombre=Label(self.raiz,text="Dirección").place(x=30, y=150)
        self.espacio1=Entry(self.raiz,justify=RIGHT,width=50,textvariable=vdireccion).place(x=130, y=150)

        self.etiqueta_nombre=Label(self.raiz,text="C.P.").place(x=30, y=200)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vcp).place(x=130, y=200)

        self.etiqueta_nombre=Label(self.raiz,text="Población").place(x=30, y=250)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vpoblacion).place(x=130, y=250)

        self.etiqueta_nombre=Label(self.raiz,text="País").place(x=30, y=300)
        self.espacio1=Entry(self.raiz,justify=RIGHT,textvariable=vpais).place(x=130, y=300)

        self.etiqueta_nombre=Label(self.raiz,text="Email").place(x=30, y=350)
        self.espacio1=Entry(self.raiz,justify=RIGHT).place(x=130, y=350)

        C2 = Checkbutton(self.raiz,text="Guardar en BBDD",height=5,width=20).place(x=30, y=400)

        button = Button(self.raiz,  
                text = 'Enviar', 
                height = 2, 
                width = 25, 
                bg='blue',command=s.crea_factura).place(x=250, y=400)  
    
    #montaje de factura
    def crea_factura(self):
        
        file = open(f"calafate_sepa\\informes\\factura{self.n}.txt", "w",encoding="utf-8")
        file.write(f'''  
                                  FACTURA 
Fecha: {self.d} factura Nº{self.n}

EMISOR                                                                      RECEPTOR 
____________________________                             ____________________________________
Vegetariano El Calafate S.L.                                            {vnombre.get()} 
CIF: B-93480127                                                         {vcif.get()}
C/Andrés Pérez,6                                                        {vdireccion.get()} 
29008  Málaga                                                           {vcp.get()} {vpoblacion.get()}
952229344                                                               {vpais.get()} 
_________________________
DESCRIPCIÓN DEL PROYECTO
_________________________________________________________________________________________ 
SERVICIO PRESTADO                  CANTIDAD                                                   PRECIO  

------------------------------------------------------------------------------------
Servicio de Hosteleria
Comida(Menú) 
____________________________________________________________________TOTAL ({round(float(vprecio.get())-float(vprecio.get())*0.21,2)}€) 100 
____________________________________________________________________IVA (21%) 
____________________________________________________________________TOTAL ({vprecio.get()}€)  
 
Pago: efectivo-tarjeta.
nombre:Vegetariano el Calafate''') 
        self.n+=1
        messagebox.showinfo(title='Factura creada',message='Su factura se ha creado satisfactoriamente')   
        q=messagebox.askquestion(title='Continue',message='¿Desea continuar creando facturas?')
        if q =='yes':
            s.factura()
        else:
            s.interfaz() 
    #interfaz() ok!        
    def interfaz(self):#pantalla interfaz principal
      
        self.raiz=Tk()
        self.nombre_usuario="El Calafate"
        self.raiz.geometry("600x450+0+0")#cambio18/12
        self.raiz.configure(background='#F2F2F2')
        imagen= PhotoImage(file="calafate_sepa\\imagenes\\logo.gif")#cambio18/12
        Label(self.raiz, image=imagen, bd=0).pack()#cambio18/12
        #self.raiz.iconbitmap("rubik.ico")
        self.raiz.title(self.nombre_usuario)
        
        menubarra=(self.raiz)
        #self.mnu_archivo=Menu(self.barra_menu)
        menubarra = Menu(self.raiz)
      
      #----------------------
       # Crea un menu desplegable y lo agrega al menu barra
        menuarchivo = Menu(menubarra, tearoff=0)
        menuarchivo.add_command(label="Generar Factura",command=s.factura)
        menuarchivo.add_command(label="Generar resumen Sepa",command=s.datos_sepa)

        menuarchivo.add_separator()
        menuarchivo.add_command(label="Salir")
        menubarra.add_cascade(label="Movimientos", menu=menuarchivo)

        # Crea dos menus desplegables mas
        menueditar = Menu(menubarra, tearoff=0)
        menueditar.add_command(label="Borrar campos")
        menubarra.add_cascade(label="Borrar", menu=menueditar)
        
        menuayuda = Menu(menubarra, tearoff=0)
        menuayuda.add_command(label="Crear")
        menuayuda.add_command(label="Leer")
        menuayuda.add_command(label="Actualizar")
        menuayuda.add_command(label="Borrar")
        menubarra.add_cascade(label="CRUD", menu=menuayuda)

        menuayuda2 = Menu(menubarra, tearoff=0)
        menuayuda2.add_command(label="CIERRE")
        menuayuda2.add_command(label="Acerca de...")
        menubarra.add_cascade(label="Opciones Avanzadas", menu=menuayuda2)
        
        
          
        #Label(self.raiz).pack()
        self.raiz.config(menu=menubarra)
      
        self.raiz.mainloop()

    #funcion que crea los datos resumidos de gastos de un mes de sepa
    def resumen_sepa(self):
        
        df = pandas.read_excel(f'calafate_sepa\\sepas2022\\{vmes.get()}.xls')
        file = open(f"calafate_sepa\\informes\\resumen_sepa_{vmes.get()}.txt", "w",encoding="utf-8")
        file.write(f'GASTOS GENERADOS DURANTE EL MES DE <<{vmes.get()}>>' + os.linesep)
        file.write('\n')

        lista01=list(df.Observaciones)
        lista02=list(df.Importe)

        comisiones_tarjeta=list()
        for i,j in zip(lista01,lista02):
            if i[:3]=='COM':
                comisiones_tarjeta.append(j)
            elif j<0:
                
                file.write(f'''{i[:12]} ------------------> {j} € \n''')
        file.write('\n-----------RESUMEN-----------\n')
        
        total=0
        for i in list(df.Importe):
            if i <0:
                total+=i
        
        file.write(f'''La suma total de comisiones por tarjeta ---------> {round(sum(comisiones_tarjeta),2)} €
        La suma total de otros gastos -------------------> {round(total-sum(comisiones_tarjeta),2)} €
        Total--------------------------------------------> {round(sum(comisiones_tarjeta)+round(total-sum(comisiones_tarjeta),2),2)} €''')
        file.close()
      
 #------------------------------------------------------------- 
if __name__ == "__main__":
    s=Gestion()
    s.interfaz()

