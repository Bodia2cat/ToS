#-----------------------#
i = 10 				    #	
#-----------------------#
import subprocess		#
import time				#
import os				#	
import requests			#-------------#
from terminaltables import SingleTable#
#-------------------------------------#

#log function

def log():
	log = datetime.datetime.now().time()
	handle = open(".log.txt", "w")
	handle.write(str(log) + "; " + sys.platform + "; " + str(sys.argv))	
	handle.close()

#console function
def console():
	table_data = [
		['xterm edition(bash) [1] ', 'ToS console(Tonsole) [2] ', 'exit', ]
	]
	table = SingleTable(table_data)
	while i == 10:
		print(table.table)

		con_in = input("ToS >_")
		if con_in == "1":
			subprocess.call(["xterm"])
		if con_in == "2":
			os.system("python3 Tonsole.py")
			time.sleep(2)
		if con_in == "3":
			print("Ok, I exit from system beacose exit from this menu is not avaible....")
			time.sleep(2)
			exit()
		time.sleep(2)
		subprocess.call("clear")

#system function
def system():
	table_data = [
		['console [1]', 'shutdown [2] ', 'extra shutdown [3] ', 'SePy [4] ', ],
		['webbrowser [5] ', 'apache2 [6] ', 'Arduino ide [7] ', 'ssh [8]', ],
		['file maneger [9] ', 'ngrok start [10] ', 'myserver [11] ']
	]
	table = SingleTable(table_data)

	while i == 10: 
		os.system("figlet       menu         ")
		print(table.table)
		time.sleep(2)
		sys_in = input("ToS >_")
		if sys_in == "1":
			console()
		if sys_in == "2":
			log_s = datetime.datetime.now().time()
			handle = open(".log_s.txt", "w")
			handle.write("Shutdown was: " + str(log_s) + "; " + sys.platform + "; ")	
			handle.close()
			subprocess.call("clear")
			print("Good bye......")
			time.sleep(2)
			exit()
		if sys_in == "3":
			exit()
		if sys_in == "4":
			os.system("python3 search2.py")
		if sys_in == "5":
			web = input("what url? ")
			code = subprocess.call(['w3m', web])
		if sys_in == "6":
			print("ok")
			os.system("sudo service apache2 start")
		if sys_in == "7":
			code = subprocess.call("arduino")
		if sys_in == "8":
			os.system("sudo service ssh start")
		if sys_in == "9":
			os.system("python3 file_maneger.py")
		if sys_in == "10":
			os.system("./ngrok http 80")
		if sys_in == "11":
			os.system("myserver start")
		else:
			pass
		#loop for image
		time.sleep(1)
		subprocess.call("clear")

#install 
import datetime
import sys
try:
	if sys.argv[1]=="-nl":
		subprocess.call("clear")
		print("-----------------Tos---------------------")
		import time
		time.sleep(2)
		subprocess.call("clear")

		a = 'test_a'



		table_data = [
		    ['num', 'var.'],
		    ['1. ', 'live'],
		    ['2. ', 'exit'],
		]
		table = SingleTable(table_data)
		print(table.table)
		os.system("figlet TBoot")
		numinstall = input(">_")
		if numinstall == "1":
			subprocess.call("clear")
			system()
		if numinstall == "2":
			exit()
		else:
			print("Error")
	if sys.argv[1]=="-s":
		log()
		subprocess.call("clear")
		print("-----------------Tos---------------------")
		time.sleep(2)
		subprocess.call("clear")

		a = 'test_a'
		os.system("figlet TBoot")
		table_data = [
		    ['num', 'text'],
		    ['1. ', 'live'],
		    ['2. ', 'exit'],
		]
		table = SingleTable(table_data)
		print(table.table)

		numinstall = input(">_")
		if numinstall == "1":
			subprocess.call("clear")
			system()
		if numinstall == "2":
			exit()
		else:
			print("Error")
	if sys.argv[1]=="-ex":
		def system():
			table_data = [
				['console [1]', 'shutdown [2] ', 'extra shutdown [3] ', 'SePy [4] ', ],
				['webbrowser [5] ', 'apache2 [6] ', 'Arduino ide [7] ', 'ngrok [8] ']
			]
			table = SingleTable(table_data)

			while i == 10: 
				print(table.table)
				time.sleep(2)
				sys_in = input("ToS >_")
				if sys_in == "1":
					console()
				if sys_in == "2":
					subprocess.call("clear")
					print("Good bye......")
					time.sleep(2)
					exit()
				if sys_in == "3":
					exit()
				if sys_in == "4":
					os.system("python3 search2.py")
				if sys_in == "5":
					web = input("what url? ")
					code = subprocess.call(['w3m', web])
				if sys_in == "6":
					print("ok")
					os.system("sudo service apache2 start")
				if sys_in == "7":
					code = subprocess.call("arduino")
				if sys_in == "8":
					os.system("./ngrok http 80")
				else:
					pass
				#loop for image
				time.sleep(2)
				subprocess.call("clear")
		system()
except:
	print("Out of arguments!!! ")
