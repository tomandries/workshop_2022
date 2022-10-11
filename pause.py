import win32com.client
import datetime
from plyer import notification

# ouverture du calendrier Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calender = outlook.GetDefaultFolder(9)  # "9" est le calendrier Outlook

# affichage de la date
day = datetime.datetime.now()
print("Aujourd'hui, nous sommes le " + str(day.day) +
      "/" + str(day.month) + "/" + str(day.year))
print("Il est " + str(day.hour) + "h" + str(day.minute))

# extraction du planing du jour même
start_date = datetime.date(day.year, day.month, day.day)  # année, mois, jour
end_date = datetime.date(day.year, day.month, day.day+1)  # année, mois, jour

items = calender.Items  # récupération des rdv
select_items = []  # liste des rdv du jour

pause = datetime.timedelta(minutes=1)
future_day = day + pause


print("dans 1 minute(s) il sera : " +
      str(future_day.hour) + "h" + str(future_day.minute))


print("heure actuelle : " + str(day))
print("heure notif : " + str(future_day))

etatNotif = False
while etatNotif == False:
    day = datetime.datetime.now()
    if ((day.hour == future_day.hour) and (day.minute == future_day.minute)):
        # notification
        notification.notify(
            title="Pause",
            message="Il est l'heure de faire une pause",
            timeout=10,
            app_icon="clock.ico"
        )
        etatNotif = True


"""
for item in items:
    if start_date <= item.start.date() <= end_date:
        select_items.append(item)

# affichage des détails des rdv
for select_item in select_items:
    print("matière:", select_item.subject)
    print("endroit:", select_item.location)
    print("Heure de début:", select_item.start)
    print("Heure de fin:", select_item.end)
    print("Texte:", select_item.body)
    print("----")

"""
