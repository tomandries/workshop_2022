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
from datetime import datetime
import screen_brightness_control as sbc

# get current brightness  value
current_brightness = sbc.get_brightness()
print(current_brightness)

# get the brightness of the primary display
primary_brightness = sbc.get_brightness(display=0)
print(primary_brightness)


while True:
    # notification
    primary_brightness = sbc.get_brightness(display=0)
    if primary_brightness == [100]:
        print("ici")
        notification.notify(
            title="Luminosité très forte !",
            message="Faîtes attention à vos yeux.",
            timeout=10,
            app_icon="oeilPleure.ico"
        )
        # pause de 1h
        time.sleep(3600)


