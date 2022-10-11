# modules
import webbrowser
from win10toast_click import ToastNotifier

# function
page_url = 'http://google.com/'


def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Opening URL...')
    except:
        print('Failed to open URL. Unsupported variable type.')


# initialize
toaster = ToastNotifier()

# showcase
toaster.show_toast(
    "Ouvrir Google",  # title
    "Cliquer pour ouvrir le lien ! >>",  # message
    icon_path = "clock.ico",  # 'icon_path'
    duration = 10,  # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded = True,  # True = run other code in parallel; False = code execution will wait till notification disappears
    callback_on_click = open_url  # click notification to run function
)
