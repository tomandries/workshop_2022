import win32com.client
import datetime

# ouverture du calendrier Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
calender = outlook.GetDefaultFolder(9) # "9" est le calendrier Outlook

# affichage de la date
date = datetime.date.today()
print("Aujourd'hui, nous sommes le " + str(date.day) + "/" + str(date.month) + "/" + str(date.year))

# extraction du planing du jour même
start_date = datetime.date(date.year, date.month, date.day) # année, mois, jour
end_date = datetime.date(date.year, date.month, date.day+1) # année, mois, jour

items = calender.Items # récupération des rdv
select_items = [] # liste des rdv du jour

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

