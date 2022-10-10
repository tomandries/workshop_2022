from plyer import notification
import time

while True:
    # notification
    notification.notify(
        title="Posture",
        message="Faîtes attention à votre dos",
        timeout=10,
        app_icon="dos.ico"
    )
    # pause de 30 minutes
    time.sleep(1800)
