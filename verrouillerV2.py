import ctypes
import datetime
import time
from win10toast_click import ToastNotifier

# ajoute du temps à la prochaine notif
def addBreak(time):
    adding = datetime.timedelta(minutes=time)
    return datetime.datetime.now() + adding

# empêche le verrouillage de l'ordinateur
def willLock():
    global goLock
    goLock = False
    print("L'ordinateur ne se verrouillera pas")


# variables & objets
delay = int(input("Délai avant le verrouillage (en minutes) : "))
toaster = ToastNotifier()
day = datetime.datetime.now()
timeLock = addBreak(delay)
goLock = False

while True:
    # prend l'heure actuelle
    day = datetime.datetime.now()
    # s'il est l'heure de verrouiller l'ordinateur
    if ((day.hour == timeLock.hour) and (day.minute == timeLock.minute)):
        goLock = True
        # notification
        toaster.show_toast(
            "Bien-être",  # titre
            "Votre ordinateur va se fermer dans 1 minute, cliquez pour ajouter " + str(delay) + " minutes",  # message
            icon_path="clock.ico",  # 'icon_path'
            duration=20,  # temps de visibilité
            threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
            callback_on_click=willLock  # click notification to run function
        )
        timeLock = addBreak(delay)
        time.sleep(30)  # pause de 30 secondes
        # verrouillage
        if (goLock == True):
            print("L'ordinateur va se verrouiller")
            time.sleep(10)
            ctypes.windll.user32.LockWorkStation()
    time.sleep(20)