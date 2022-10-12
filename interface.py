#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nono
#
# Created:     11/10/2022
# Copyright:   (c) nono 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# coding: utf-8

from os import close
from tkinter import *
from tkinter.filedialog import *

import threading
from turtle import clone

import win32com.client
import datetime
import time
from plyer import notification
import ctypes
from win10toast_click import ToastNotifier
import screen_brightness_control as sbc

from subprocess import Popen

def launchNotif():
    global p
    p = Popen(['python', 'testfinal.py'])

def stopNotif():
    global p
    p.kill()
    print('finfinfin')
    global var_test
    var_test = False

t1 = threading.Thread(target=launchNotif)
t2 = threading.Thread(target=stopNotif)

def st1():
    t1.start()

def st2():
    t2.start()

fenetre = Tk()
fenetre.title("nomAppli")

label = Label(fenetre, text="Bienvenue sur nomAppli")
label.pack(pady=10)
label['bg']='#fed5cf'
label.config(font=("Roboto", 27))

photo = PhotoImage(file="bien-etre.png")
##photo.resize_contain()

canvas = Canvas(fenetre,width=45, height=45)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
canvas['bg']='#fed5cf'

label2 = Label(fenetre, text="Entrez ici les problèmes que vous souhaitez faire remonter :")
label2.pack(pady=10)
label2['bg']='#fed5cf'
label2.config(font=("Roboto", 14))
# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()
bouton=Button(fenetre, text="Envoyer", bg='#c1badb', font=("Roboto", 12)).pack(pady=10)

fenetre['bg']='#fed5cf'

fenetre.resizable(True, True)  # This code helps to disable windows from resizing

window_height = 500
window_width = 900

screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

fenetre.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
bouton=Button(fenetre, command=st1, text="Lancer l'application", bg='#c1badb', font=("Roboto", 12)).pack(pady=5)
bouton=Button(fenetre, command=st2, text="Stopper l'application", bg='#c1badb', font=("Roboto", 12)).pack(pady=5)
### frame 1
##Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
##Frame1.pack(side=LEFT, padx=30, pady=30)
##
### frame 2
##Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
##Frame2.pack(side=LEFT, padx=10, pady=10)
##
### frame 3 dans frame 2
##Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
##Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
##Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
##Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
##Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)
##
##Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
##Button(fenetre, text ='Bouton 1', bg='#c1badb').pack(side=LEFT, padx=5, pady=5)
##Button(fenetre, text ='Bouton 2', bg='#c1badb').pack(side=RIGHT, padx=5, pady=5)
# bouton de sortie
bouton=Button(fenetre, text="Fermer", bg='#c1badb', font=("Roboto", 12), command=fenetre.quit).pack(side=RIGHT, padx=5, pady=5)

##photo = PhotoImage(file="setirer.ico")
##
##canvas = Canvas(fenetre,width=350, height=200)
##canvas.create_image(0, 0, anchor=NW, image=photo)
##canvas.pack()

fenetre.mainloop()
