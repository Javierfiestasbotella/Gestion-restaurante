# -*- coding: utf-8 -*-
#!/usr/bin/python
import pandas
import numpy as np
import os
import tkinter as tk
from tkinter import * 
from tkinter import PhotoImage
from tkinter import messagebox
import datetime
from datetime import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pathlib
import webbrowser

class Gestion:
    #constructor
    def __init__(self):
        self.lista01=[]
        self.sepa=''
        self.n=100000
        self.hora=datetime.now().strftime('%H:%M')
        self.d=datetime.now().strftime('%Y-%m-%d')
        self.seudo=pathlib.Path(__file__).parent.absolute()
    
    #envio2 intenta enviar adjuntos, pero de momento no funciona
    def envio2(self):
        # Crear una instancia con archivos adjuntos
        msg = MIMEMultipart()
        
        # Anexo de estructura 1
        att1 = MIMEText(open('calafate_sepa\\informes\\facturas\\javi.txt', 'rb').read(), 'base64', 'gb2312')
        #att1["Content-Type"] = 'application/octet-stream'
        #att1 ["Content-Disposition"] = 'adjunto; filename = "javi.txt"' # El nombre de archivo aquí se puede escribir arbitrariamente, qué nombre se escribe, qué nombre se muestra en el correo electrónico
        msg.attach(att1)
        #   Encabezado de correo
        msg ['to'] = ";". join (['vegetarianoelcalafate@gmail.com']) # correo electrónico del destinatario
        msg ['from'] = 'javierfiestasbotella@gmail.com' # correo electrónico del remitente
        msg ['subject'] = 'hello world soy yo' # Encabezado de correo electrónico enviado
        #Enviar correo
        try:
            server = smtplib.SMTP()
            server.connect('vegetarianoelcalafate@gmail.com')
            server.login ('javierfiestasbotella@gmail.com','vxmavinbhhykaler') #XXX es el nombre de usuario y XXXXX es el código de autorización
            server.sendmail(msg['from'], msg['to'], msg.as_string())
            server.quit()
            print ('Enviar correctamente')
        except (Exception):
                print ("Está terminado ...")

    #envía un email al email del argumento y mensaje del argumento
    def envio_email(self,email,message):
        fromaddr = 'javierfiestasbotella@gmail.com'
        toaddrs  = email
        msg =message.encode('utf-8')

        # Datos
        username = 'javierfiestasbotella@gmail.com'
        password = 'vxmavinbhhykaler'

        # Enviando el correo
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    
    #interfaz donde se rellena para crear el resumen del sepa    
    def datos_sepa(self):
        
        self.raiz2=tk.Toplevel()
        self.raiz2.title("Resumen Sepa")
        self.raiz2.geometry("300x250+0+0")#cambio18/12
        self.raiz2.configure(background='#F2F2F2')
        global vmes
        vmes=StringVar()
        self.etiqueta_nombre=Label(self.raiz2,text="Mes").place(x=30, y=50)
        self.espacio1=Entry(self.raiz2,justify=RIGHT,textvariable=vmes).place(x=130, y=50)
        button = Button(self.raiz2,  
                text = 'Enviar', 
                height = 2, 
                width = 25, 
                bg='blue',command=s.resumen_sepa).place(x=50, y=100) 
   
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
        global vemail
        vemail=StringVar()
        self.raiz=tk.Toplevel()
        self.raiz.geometry("650x550+0+0")#cambio18/12
        self.raiz.configure(background='#F2F2F2')
        dist_y=0
        
        #Label(self.raiz, image=imagen, bd=0).pack()#cambio18/12

        self.etiqueta_titulo=Label(self.raiz,text="Rellene datos de la factura", font=("Helvetica", 14)).place(x=200, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="Precio", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio1=Entry(self.raiz,justify=LEFT,textvariable=vprecio).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="Nombre", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio2=Entry(self.raiz,justify=LEFT,textvariable=vnombre).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="CIF/NIF/NIE", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio3=Entry(self.raiz,justify=LEFT,textvariable=vcif).place(x=150, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="Dirección", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio4=Entry(self.raiz,justify=LEFT,width=50,textvariable=vdireccion).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="C.P.", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio5=Entry(self.raiz,justify=LEFT,textvariable=vcp).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="Población", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio6=Entry(self.raiz,justify=LEFT,textvariable=vpoblacion).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="País", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio7=Entry(self.raiz,justify=LEFT,textvariable=vpais).place(x=130, y=dist_y)
        dist_y+=50
        self.etiqueta_nombre=Label(self.raiz,text="Email", font=("Helvetica", 14)).place(x=30, y=dist_y)
        self.espacio8=Entry(self.raiz,justify=LEFT,width=50,textvariable=vemail).place(x=130, y=dist_y)
        dist_y+=50
        C2 = Checkbutton(self.raiz,text="Guardar en BBDD", font=("Helvetica", 14),height=5,width=20).place(x=30, y=dist_y)
        dist_y+=50
        chk=None
        if chk == 'yes':
            chk==True
        else:
            chk==False
        button = Button(self.raiz,  
                text = 'Enviar', 
                height = 2, 
                width = 25, 
                bg='blue',command = s.crea_factura).place(x=280, y=dist_y)  
    
    #montaje de factura
    def crea_factura(self):
        
        file = open(f"{self.seudo}\\informes\\facturas\\factura{self.n}.txt", "w",encoding="utf-8")
        mesage=(f'''  
                                  FACTURA 
Fecha: {self.d} factura Nº{self.n}

EMISOR                                                                      RECEPTOR 
____________________________                             ____________________________________
Vegetariano El Calafate S.L.                                         {vnombre.get()} 
CIF: B-93480127                                                       {vcif.get()}
C/Andrés Pérez,6                                                       {vdireccion.get()} 
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
        file.write(mesage)
        self.n+=1
        print(mesage)
        
        messagebox.showinfo(title='Factura creada',message='Su factura se ha creado satisfactoriamente')   
        q=messagebox.askquestion(title='Continue',message='¿Desea continuar creando facturas?')
        if q =='yes':
            self.nombre=vnombre.set('')
            self.direccion=vdireccion.set('')
            self.cif=vcif.set('')
            self.cp=vcp.set('')
            self.poblacion=vpoblacion.set('')
            self.pais=vpais.set('')
            self.email=vemail.set('')
            self.precio=vprecio.set('')
            self.raiz.focus()

        else:
            self.raiz.destroy()
            self.raiz0.focus()
    
    def EjecutarEvento(self,event=None): #Event, el argumento se debe poner para ejecutar la 
                                #acción, "None", para evitar agregar el argumento
                                #event en cada widget o label.
            webbrowser.open('https://vegetarianoelcalafate.es')
    

    #interfaz() ok!        
    def interfaz(self):#pantalla interfaz principal
      
        self.raiz0=Tk()
        self.nombre_usuario="El Calafate"
        self.raiz0.geometry("600x450+0+0")#cambio18/12
        self.raiz0.configure(background='#F2F2F2')
        imagen= PhotoImage(file=f"{self.seudo}\\imagenes\\logo.gif")#cambio18/12
        Label(self.raiz0, image=imagen, bd=0).pack()#cambio18/12
        self.labelEjemplo = tk.Label(self.raiz0, text="WEB-SITE", font=("Microsoft Sans Serif", 12, 
            "underline"), foreground="green")
        self.labelEjemplo.place(x=250, y=200)
        self.labelEjemplo.bind("<Button-1>", s.EjecutarEvento)
        #---------------------------------
    
            

        #----------------------

        #self.raiz.iconbitmap("rubik.ico")
        self.raiz0.title(self.nombre_usuario)
        
        menubarra=(self.raiz0)
        #self.mnu_archivo=Menu(self.barra_menu)
        menubarra = Menu(self.raiz0)
      
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
        self.raiz0.config(menu=menubarra)
      
        self.raiz0.mainloop()

    #funcion que crea los datos resumidos de gastos de un mes de sepa
    def resumen_sepa(self):
        
        df = pandas.read_excel(f'{self.seudo}\\sepas2022\\{vmes.get()}.xls')
        file = open(f"{self.seudo}\\informes\\sepas\\resumen_sepa_{vmes.get()}.txt", "w",encoding="utf-8")
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
        self.raiz2.destroy()
        self.raiz0.focus()
 #------------------------------------------------------------- 
if __name__ == "__main__":
    s=Gestion()
    s.interfaz()


#s.envio_email('vegetarianoelcalafate@gmail.com','prueba 1')

