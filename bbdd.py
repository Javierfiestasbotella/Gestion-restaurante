# -*- coding: utf-8 -*-
import mysql.connector
import getpass
from tkinter import messagebox
import pathlib

print(f'direccion---->{pathlib.Path(__file__).parent.absolute()}')

dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'#######',
    'password':'##########',
    'database':'#######',
    
}
conexion=mysql.connector.connect(**dbConnect)
cursor=conexion.cursor()
