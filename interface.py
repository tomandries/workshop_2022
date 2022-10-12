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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from dotenv import dotenv_values
import os

load_dotenv()

import threading
from turtle import clone

import win32com.client
import datetime
import time
from plyer import notification
import ctypes
from win10toast_click import ToastNotifier
import screen_brightness_control as sbc
import tkinter as Tkin

from subprocess import Popen

def launchNotif():
    global p
    p = Popen(['python', 'notifications.py'])

def stopNotif():
    global p
    p.kill()

t1 = threading.Thread(target=launchNotif)
t2 = threading.Thread(target=stopNotif)

def st1():
    t1.start()

def st2():
    t2.start()

fenetre = Tk()
fenetre.title("SmileTime")

label = Label(fenetre, text="Bienvenue sur SmileTime")
label.pack(pady=10)
label['bg']='#fed5cf'
label.config(font=("Roboto", 27))

photo = PhotoImage(file="logo100.png")

canvas = Canvas(fenetre,width=95, height=95, borderwidth=0)
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

def sendMail():
    #envoyer mail :
    msg = MIMEMultipart()
    msg['From'] = 'compte.workshop.i1@gmail.com'
    msg['To'] = 'compte.workshop.i1@gmail.com'
    msg['Subject'] = "Remonté d'un problème sur SmileTime"
    message = 'Bonjour, un problème vous a été remonté, le voici : ' + entree.get()
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('compte.workshop.i1@gmail.com', os.environ["PASSWORD"])
    mailserver.sendmail('compte.workshop.i1@gmail.com', 'compte.workshop.i1@gmail.com', msg.as_string())
    mailserver.quit()
    entree.delete(0,Tkin.END)
    label3 = Label(fenetre, text="Bien envoyé !")
    label3.pack(pady=10)
    label3['bg']='#fed5cf'
    label3.config(font=("Roboto", 14))

boutonEnvoyer=Button(fenetre, text="Envoyer", bg='#c1badb', font=("Roboto", 12), command=sendMail).pack(pady=10)

fenetre['bg']='#fed5cf'

fenetre.resizable(True, True)

window_height = 500
window_width = 900

screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

fenetre.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
bouton=Button(fenetre, command=st1, text="Lancer l'application", bg='#c1badb', font=("Roboto", 12)).pack(pady=5)
bouton=Button(fenetre, command=st2, text="Stopper l'application", bg='#c1badb', font=("Roboto", 12)).pack(pady=5)

bouton=Button(fenetre, text="Fermer", bg='#c1badb', font=("Roboto", 12), command=fenetre.quit).pack(side=RIGHT, padx=5, pady=5)

fenetre.mainloop()


