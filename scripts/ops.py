#! /usr/bin/python

import locale
import os,sys,inspect
import time, re
import datetime, socket
import argparse
import subprocess
import commands

def get_file_size( start_path = '.', printTime=False ):
	start = startEndTimer()
	total_size = os.path.getsize(start_path)
	end = startEndTimer()
	if printTime == True:
		print timerPrintout(start, end)
	else:
		pass
	return total_size

def get_folder_size( start_path = '.', printTime=False ):
	total_size = 0
	count = 0
	start = startEndTimer()
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			s = os.stat(fp)
			fileSize = s.st_size
			total_size += fileSize
			if f[:1] == '.':
				pass
			else:
				count += 1
		for d in dirnames:
			count += 1
	end = startEndTimer()
	if printTime == True:
		print timerPrintout(start, end)
	else:
		pass
	return total_size, count

def get_finder_file_size( start_path='.', printTime=False ):
	total_size = 0
	path = '\'' + start_path + '\'/..namedfork/rsrc'
	cmd = 'perl -e \'print -s @ARGV[0]\' ' + path
	start = startEndTimer()
	out = commands.getstatusoutput(cmd)
	for o in out:
		if o == '':
			continue
		elif o == 0 or o =='0':
			continue
		else:
			total_size += int(o)
	end = startEndTimer()
	if printTime == True:
		print timerPrintout(start, end)
	else:
		pass
	return total_size

def get_finder_folder_size( start_path='.', printTime=False ):
	total_size = 0
	start = startEndTimer()
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			path = '\'' + fp + '\'/..namedfork/rsrc'
			cmd = 'perl -e \'print -s @ARGV[0]\' ' + path
			out = commands.getstatusoutput(cmd)
			for o in out:
				if o == '':
					continue
				elif o == 0 or o =='0':
					continue
				else:
					total_size += int(o)
	end = startEndTimer()
	if printTime == True:
		print timerPrintout(start, end)
	else:
		pass
	return total_size

def getServer():
	vols = os.listdir('/Volumes/')
	if 'yellow' in vols:
		return 'yellow'
	elif 'Congo' in vols:
		return 'Congo'
	else:
		print 'Server not mounted'
		sys.exit(2)

class ArgumentException(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def currentTime( format=None ):
	'''
	currentTime simply gives us the current time, you can pass in a format that you would 
		like if the default isn't what you want
	'''
	if (format == None):
		timeFormat = '%Y-%m-%d %H:%M:%S'
	else:
		timeFormat = format
	time = datetime.datetime.now().strftime(timeFormat)
	return time

def timerPrintout( start, end ):
	'''
	timerPrintout subtracts the start time from the end time to give us a total time that 
		the task took to run, eventually it will print in human readable format...
	'''
	startTime = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
	endTime = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
	totalTime = endTime - startTime
	msg = "Your task took " + str(totalTime) + " minutes to complete"
	print msg
	return totalTime

def startEndTimer( format=None ):
	'''
	startEndTimer gives us the current time with the format that is specified within the 
		function, it gives us this time to use as either the start or end time for the 
		timer function
	'''
	if (format == None):
		timeFormat = '%Y-%m-%d %H:%M:%S'
	else:
		timeFormat = format
	time = datetime.datetime.now().strftime(timeFormat)
	return time

def multiOptions( msg, arry ):
	'''
	multiOptions provides a ui for selecting an option out of a list, you provide the 
		message to ask and the array to check for an it outputs the option that was 
		selected
	'''
	print "\n" + msg + "\n"
	count = 1
	for i in arry:
		print "\t" + str(count) + "- " + i
		count += 1
	message = "\nEnter the number of the option you want:\n"
	try:
		option = getInput(message)
		num = int(option)
		num -= 1
	except:
		num = 0
	return num

def printList( msg, arry ):
	'''
	printList just prints an array that is passed to it
	'''
	print "\n" + msg + "\n"
	for i in arry:
		print "\t- " + i
	return

def printNumList( msg, arry ):
	'''
	printList simply prints out a message and an array
	'''
	count = 0
	print "\n" + msg + "\n"
	for i in arry:
		print "\t" + str(count) + ". " + i
		count += 1
	return

def getInput( msg ):
	'''
	getInput simply prints the message it is passed and gets the user input
	'''
	print msg
	userInputVar = raw_input()
	return userInputVar

def yOrN( msg ):
	'''
	yOrN is a yes or no prompt, input the question and get back true if yes and false if no, 
		also defaults to false if you give it something that isn't allowed
	'''
	print "\n" + msg + "\n"
	message = "Enter 'Y' or 'N' for yes or no:\n"
	option = getInput(message)
	if (option == 'Y' or option == 'y' or option == 'Yes' or option == 'yes'):
		return True
	elif (option == 'N' or option == 'n' or option == 'No' or option == 'no'):
		return False
	else:
		print "Invalid option, returning 'false'."
		return False

def isValidInput( input, args ):
	'''
	isValidInput can ensure that the user entered something within the allowable range, 
		returns false if user did not enter something in the allowable limits
	'''
	if input in args:
		return True
	else:
		return False

def submitTractor( alfFileName ):
	command = "/Applications/Pixar/tractor-blade-1.6.5/tractor-spool.py " + alfFileName
	os.system(command)
	return