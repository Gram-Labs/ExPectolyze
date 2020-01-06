# logger.py

import time, sys

class logger:
	def __init__(self):
		self.colors = {
			"error" 		: "\033[91m",
			"success" 		: "\033[92m",
			"info" 			: "\033[96m",
			"debug" 		: "\033[95m",
			"yellow" 		: "\033[93m",
			"lightpurple" 	: "\033[94m",
			"lightgray" 	: "\033[97m",
			"clear"			: "\033[00m"
		}

	def log(self, message="", color="", file="", shown=True, showtime=True, nocolor=""):
		currentTime = time.strftime("%H:%M:%S")

		try:
			colorString = self.colors[color]
		except:
			colorString = ""

		if showtime:
			timestring = "[%s] " % currentTime
		else:
			timestring = ""

		messageString = str(message) + self.colors['clear']
		noColorString = str(message)

		if nocolor:
			messageString += "%s" % nocolor 
			noColorString += "%s" % nocolor 

		finalString = "%s%s%s\n" % (timestring, colorString, str(messageString))
		noColorFinalString = "%s%s\n" % (timestring, str(noColorString))

		sys.stdout.write(finalString)
		sys.stdout.flush()

		if file:
			with open(file, "a") as f:
				f.write(noColorFinalString)