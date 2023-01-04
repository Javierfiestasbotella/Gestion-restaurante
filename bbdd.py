# -*- coding: utf-8 -*-
import mysql.connector
import getpass
from tkinter import messagebox
import pathlib

print(f'direccion---->{pathlib.Path(__file__).parent.absolute()}')

dbConnect={
    'host':'lldk499.servidoresdns.net',
    'user':'qadr270',
    'password':'Calafate1123',
    'database':'qadr270',
    
}
conexion=mysql.connector.connect(**dbConnect)
cursor=conexion.cursor()