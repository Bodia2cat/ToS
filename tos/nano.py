import os
import subprocess

subprocess.call("clear")
file = input("File name: ")
os.system("nano " + file)
