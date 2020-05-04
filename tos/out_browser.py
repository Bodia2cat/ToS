import subprocess
import os
import webbrowser

web = input("url: ")
try:
    webbrowser.open("http://" + web)
except:
    webbrowser.open("https://" + web)
