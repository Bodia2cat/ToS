import os
import sys
import subprocess

subprocess.call("clear")


i = 1

os.system("toilet {[?]} ")

command = input("? ")
while i:
	command = input("? ")

	os.system(command)

	if command == "m":
		os.system("python3 main.py -s")
	if command == "m --help":
		print("m - load system ")
	if command == "exit":
		exit()



