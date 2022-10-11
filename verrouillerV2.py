import ctypes
import datetime
import time
from win10toast_click import ToastNotifier

# ajoute du temps à la prochaine notif


def addBreak(time):
    adding = datetime.timedelta(minutes=time)
    return datetime.datetime.now() + adding


def willLock():
    global goLock
    goLock = False
    print("L'ordinateur ne se verrrouillera pas")


# variables & objets
toaster = ToastNotifier()
day = datetime.datetime.now()
timeLock = addBreak(1)
goLock = False

while True:
    day = datetime.datetime.now()
    print("heure actuelle : \t\t" + str(day))
    print("heure de notificaiton : \t" + str(timeLock))
    if ((day.hour == timeLock.hour) and (day.minute == timeLock.minute)):
        #goLock = True
        # notification
        toaster.show_toast(
            "Bien-être",  # titre
            "Votre ordinateur va se fermer dans 1 minute, cliquez pour ajouter 15 minutes",  # message
            icon_path="clock.ico",  # 'icon_path'
            duration=20,  # temps de visibilité
            threaded=True,  # True = run other code in parallel; False = code execution will wait till notification disappears
            callback_on_click=willLock  # click notification to run function
        )
        timeLock = addBreak(1)
        time.sleep(30)  # pause de 30 secondes
        if (goLock == True):
            print("L'ordinateur va se verrouiller")
            time.sleep(30)
            #ctypes.windll.user32.LockWorkStation()
    time.sleep(20)