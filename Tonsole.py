i = 1
import os
import subprocess
while i:
	#базовые команды bash
	file_i = input(">_")
	os.system(file_i)
	if file_i == "exit":
		exit()
	if file_i == "apache2 start":
		os.system("sudo service apache2 start")
	if file_i == "apache2 stop":
		os.system("sudo service apache2 stop")