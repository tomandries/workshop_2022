# commande à taper en ligne de commande après la sauvegarde de ce fichier:
# python setup.py build

from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "interface.py", icon = "logo.ico")
]
  
buildOptions = dict( 
        includes = ["os","tkinter", "tkinter.filedialog", "smtplib", "email.mime.multipart", "email.mime.text", "dotenv", "threading", "turtle", "win32com.client",
         "datetime", "time", "plyer", "ctypes", "win10toast_click", "screen_brightness_control", "subprocess", "notifications"],
        include_files = ["logo.ico", "clock.ico", "dos.ico", "oeilPleure.ico", "setirer.ico", "testfinal.py"]
)
  
setup(
    name = "SmileTime ☺",
    version = "1.0",
    description = "Application de bien-être au travail",
    author = "Groupe 1",
    options = dict(build_exe = buildOptions),
    executables = executables
)