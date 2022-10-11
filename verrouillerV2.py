import ctypes
import datetime
import time
from win10toast_click import ToastNotifier


# variables & objets
toaster = ToastNotifier()
day = datetime.datetime.now()
pause = datetime.timedelta(minutes=1) # première notif dans 1 minutes
timeLock = day + pause
goLock = False

# ajoute du temps à la prochaine notif
def addBreak(time) :
    adding = datetime.timedelta(minutes=time)
    return datetime.datetime.now() + adding

def willLock() :
    global goLock
    goLock = False

toaster = ToastNotifier()
day = datetime.datetime.now()
pause = datetime.timedelta(minutes=1) # première notif dans 1 minutes
timeLock = day + pause

while True:
    day = datetime.datetime.now()
    print("timeLock : " + str(timeLock))
    if ((day.hour == timeLock.hour) and (day.minute == timeLock.minute)):
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
    print("timeLock : " + str(timeLock))
    print("goLock : " + str(goLock))
    time.sleep(30) # pause de 30 secondes
    if (goLock == True) :
        ctypes.windll.user32.LockWorkStation()
    goLock = True
    time.sleep(10)



"""
1. Déclaration des variables
2. TEST : verrouiller dans 5 minutes
3. notification demande ajout 15 minutes
4. ajouter 15 minutes
5. ou verrouiller dans 1 minutes



"""