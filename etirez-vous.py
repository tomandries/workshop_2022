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
from plyer import notification
import time

while True:
    # notification
    notification.notify(
        title="Etirez-vous",
        message="Prenez deux petites minutes pour vous étirez",
        timeout=10,
        app_icon="setirer.ico"
    )
    # pause de 30 minutes
    time.sleep(1800)
