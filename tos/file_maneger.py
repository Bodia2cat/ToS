i = 1
import os
import time
import subprocess
while i:

	subprocess.call(["figlet", "TFile"])

	#атоброжение файлов
	os.system("ls")
	#интерфейс для управления 
	file_i = input(" command >_")
	os.system(file_i)
	#Отображение экрана
	time.sleep(2)
	subprocess.call("clear")