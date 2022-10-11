d = 1

import win32com.client
import datetime
from plyer import notification

def inReu():
    day = datetime.datetime.now()
    # ouverture du calendrier Outlook
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    calender = outlook.GetDefaultFolder(9)  # "9" est le calendrier Outlook

    # extraction du planing du jour même
    start_date = datetime.date(day.year, day.month, day.day)  # année, mois, jour
    end_date = datetime.date(day.year, day.month, day.day)  # année, mois, jour

    items = calender.Items  # récupération des rdv
    select_items = []  # liste des rdv du jour

    for item in items:
        if start_date <= item.start.date() <= end_date:
            select_items.append(item)

    # affichage des détails des rdv
    for select_item in select_items:
        if (select_item.start.hour * 100 + select_item.start.minute <= day.hour*100 + day.minute <= select_item.end.hour * 100 + select_item.end.minute):
            return True
    return False

while True:

    # affichage de la date
    day = datetime.datetime.now()

    pause = datetime.timedelta(minutes=d)
    future_day = day + pause

    print("Prochaine alerte à : " +
        str(future_day.hour) + "h" + str(future_day.minute))

    print("heure actuelle : " + str(day))

    etatNotif = False
    while etatNotif == False:
        day = datetime.datetime.now()
        if (inReu() == False):
            """
            print('futur day : ' + str(future_day.hour * 100 + future_day.minute))
            print('now day : ' + str(day.hour * 100 + day.minute))
            """
            if (future_day.hour * 100 + future_day.minute <= day.hour * 100 + day.minute):
                notification.notify(
                    title="Pause",
                    message="Il est temps de faire une pause",
                    timeout=30
                )
                etatNotif = True
            else:
                time.sleep(5)
                print('Working hard...')
        else:
            time.sleep(5)
            print('In meeting...')