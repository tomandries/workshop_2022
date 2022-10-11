import win32com.client
import datetime
import time
from plyer import notification
import ctypes
from win10toast_click import ToastNotifier
import screen_brightness_control as sbc

# vérifie si l'utilisateur est en réunion
def inReu():
    day = datetime.datetime.now()
    # ouverture du calendrier Outlook

    # extraction du planing du jour même
    date = datetime.date(day.year, day.month, day.day)  # année, mois, jour

    try:

        outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        calender = outlook.GetDefaultFolder(9)  # "9" est le calendrier Outlook

        items = calender.Items  # récupération des rdv
        select_items = []  # liste des rdv du jour

        for item in items:
            if (item.start.date() == date):
                select_items.append(item)
        # affichage des détails des rdv
        for select_item in select_items:
            if (select_item.start.hour * 100 + select_item.start.minute <= day.hour*100 + day.minute <= select_item.end.hour * 100 + select_item.end.minute):
                return True
        return False

    except:
        print('L\'application n\'arrive pas à accéder à Outlook, veuillez réessayer')
        return True

# ajoute du temps à la prochaine notif
def addBreak(time):
    adding = datetime.timedelta(minutes=time)
    return datetime.datetime.now() + adding

# empêche le verrouillage de l'ordinateur
def willLock():
    global goLock
    goLock = False
    print("L'ordinateur ne se verrouillera pas")

# alerte pour s'étirer
def checkStretch() :
    notification.notify(
        title="Etirez-vous",
        message="Prennez deux petites minutes pour vous étirez",
        timeout=10,
        app_icon="setirer.ico"
    )

# alerte pour la luminosité
def checkEyes() :
    # get current brightness  value
    current_brightness = sbc.get_brightness()
    #print("current_brightness : " + str(current_brightness))

    # get the brightness of the primary display
    primary_brightness = sbc.get_brightness(display=0)
    #print("get_brightness : " + str(primary_brightness))

    # notification
    primary_brightness = sbc.get_brightness(display=0)
    if primary_brightness == [100]:
        notification.notify(
            title="Luminosité très forte !",
            message="Faîtes attention à vos yeux.",
            timeout=10,
            app_icon="oeilPleure.ico"
        )
        global eye_alert
        eye_alert = 1

# alerte pour la posture
def checkBack() :
    notification.notify(
        title="Posture",
        message="Faîtes attention à votre dos",
        timeout=10,
        app_icon="dos.ico"
    )

# variables & objets
delay = int(input("Délai avant le verrouillage (en minutes) : "))
toaster = ToastNotifier()
day = datetime.datetime.now()
timeLock = addBreak(delay)
goLock = False

hour_alert = day.hour

while True:
    day = datetime.datetime.now()
    print("heure actuelle : " + str(day))
    if (inReu() == False):
        # s'il est l'heure de verrouiller l'ordinateur 
        if (timeLock.hour * 10000 + timeLock.minute * 100 + timeLock.second <= day.hour * 10000 + day.minute * 100 + day.second):
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
                time.sleep(5)
                ctypes.windll.user32.LockWorkStation()
                time.sleep(15)
        else:
            time.sleep(5)
            print('Working hard...')
    else:
        time.sleep(5)
        print('In meeting...')
    if (hour_alert == day.hour):
        eye_alert = 0
        hour_alert += 1
        checkBack()
        checkStretch()
    if (eye_alert == 0):
        checkEyes()
