#! /usr/bin/python

import os,sys
import time
import datetime
import argparse
import subprocess

import genhashfile as hashcreate

def main():
	if(len(sys.argv) == 1):
		msg = "Would you like to generate a hash for a single file or for multiple files?"
		multSing = ['Multiple', 'Single']
		option = multiOptions(msg, multSing)
		if (option == 0):
			print "Please note that it takes time to hash multiple files all at once on the same machine"
			multiPrompts()
		elif (option == 1):
			singlePrompts()
		else:
			raise ArgumentException("Error: bad argument")
	else:
		args, parser = usage()
		detArgs(args, parser)
	return

class ArgumentException(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def detArgs( args, parser ):
	if (args.printout == True):
		if (args.files != None or args.algorithm != None or args.specifier != None or args.location != None):
			raise ArgumentException('Error: bad argument')
		else:
			if (args.quiet == True):
				print "Sorry, there is no quiet option for the printout flag"
			else:
				pass
			filename = ['ACT319279_gospelLibraryAwareness2013_monitors_vfxShot_htcBuzz_2013.06.28', 'ACT319279_gospelLibraryAwareness2013_monitors_vfxShot_htcText_2013.06.28']
			alg = ['sha1', 'md5']
			hash = ['557c18f52ce82a7869fc193b91d1634eb212ba1b', '0e3d83025ce546c86971ea348878af99']
			path = ['/Volumes/Congo/DIVA/test/', '/Volumes/Congo/DIVA/test/']
			ext = ['tar', 'tar']
			loc = '/Volumes/Congo/DIVA/test/'
			list = hashcreate.listPrintFunc()
			showListNoPrompt(list)
			printbool = True
			count = 0
			maxCount = 2
			mIndex = len(list) - 1
			print '\nHere is what each of the output files will look like:'
			for spec in list:
				if (count == maxCount):
					count = 0
				hashcreate.main(hash[count], False, path[count], filename[count], ext[count], alg[count], spec, printbool, loc)
				count += 1
		sys.exit(0)
	elif (args.quiet == True):
		detQArgs(args, parser)
	elif (args.files != None):
		if (args.algorithm != None):
			if (args.specifier != None):
				if (args.location != None):
					length = len(args.files)
					if (length > 1):
						print "Please note that it takes time to hash multiple files all at once on the same machine"
						files = args.files
						for f in files:
							f = f.replace('\'', '')
						alg = args.algorithm
						spec = args.specifier
						location = args.location
						multiPrompts(files, alg[0], spec[0], location[0])
					elif (length == 1):
						files = args.files
						for f in files:
							f = f.replace('\'', '')
						alg = args.algorithm
						spec = args.specifier
						location = args.location
						singlePrompts(files[0], alg[0], spec[0], location[0])
					else:
						raise ArgumentException("Error: bad argument")
				else:
					length = len(args.files)
					if (length > 1):
						print "Please note that it takes time to hash multiple files all at once on the same machine"
						files = args.files
						for f in files:
							f = f.replace('\'', '')
						alg = args.algorithm
						spec = args.specifier
						multiPrompts(files, alg[0], spec[0])
					elif (length == 1):
						files = args.files
						for f in files:
							f = f.replace('\'', '')
						alg = args.algorithm
						spec = args.specifier
						singlePrompts(files[0], alg[0], spec[0])
					else:
						raise ArgumentException("Error: bad argument")
			elif (args.location != None):
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = args.algorithm
					spec = None
					location = args.location
					multiPrompts(files, alg[0], spec, location[0])
				elif (length == 1):
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = args.algorithm
					spec = None
					location = args.location
					singlePrompts(files[0], alg[0], spec, location[0])
				else:
					raise ArgumentException("Error: bad argument")
			else:
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = args.algorithm
					multiPrompts(files, alg[0])
				elif (length == 1):
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = args.algorithm
					singlePrompts(files[0], alg[0])
				else:
					raise ArgumentException("Error: bad argument")
		elif (args.specifier != None):
			if (args.location != None):
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = None
					spec = args.specifier
					location = args.location
					multiPrompts(files, alg, spec[0], location[0])
				elif (length == 1):
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = None
					spec = args.specifier
					location = args.location
					singlePrompts(files[0], alg, spec[0], location[0])
				else:
					raise ArgumentException("Error: bad argument")
			else:
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = None
					spec = args.specifier
					multiPrompts(files, alg, spec[0])
				elif (length == 1):
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					alg = None
					spec = args.specifier
					singlePrompts(files[0], alg, spec[0])
				else:
					raise ArgumentException("Error: bad argument")
		elif (args.location != None):
			length = len(args.files)
			if (length > 1):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				alg = None
				spec = None
				location = args.location
				multiPrompts(files, alg, spec, location[0])
			elif (length == 1):
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				alg = None
				spec = None
				location = args.location
				singlePrompts(files[0], alg, spec, location[0])
			else:
				raise ArgumentException("Error: bad argument")
		else:
			length = len(args.files)
			if (length > 1):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				multiPrompts(files)
			elif (length == 1):
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				singlePrompts(files[0])
			else:
				raise ArgumentException("Error: bad argument")
	elif (args.algorithm != None):
		if (args.specifier != None):
			if (args.location != None):
				msg = "Would you like to generate a hash for a single file or for multiple files?"
				multSing = ['Multiple', 'Single']
				option = multiOptions(msg, multSing)
				if (option == 0):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = None
					alg = args.algorithm
					spec = args.specifier
					location = args.location
					multiPrompts(files, alg[0], spec[0], location[0])
				elif (option == 1):
					files = None
					alg = args.algorithm
					spec = args.specifier
					location = args.location
					singlePrompts(files, alg[0], spec[0], location[0])
				else:
					raise ArgumentException("Error: bad argument")
			else:
				msg = "Would you like to generate a hash for a single file or for multiple files?"
				multSing = ['Multiple', 'Single']
				option = multiOptions(msg, multSing)
				if (option == 0):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = None
					alg = args.algorithm
					spec = args.specifier
					multiPrompts(files, alg[0], spec[0])
				elif (option == 1):
					files = None
					alg = args.algorithm
					spec = args.specifier
					singlePrompts(files, alg[0], spec[0])
				else:
					raise ArgumentException("Error: bad argument")
		elif (args.location != None):
			msg = "Would you like to generate a hash for a single file or for multiple files?"
			multSing = ['Multiple', 'Single']
			option = multiOptions(msg, multSing)
			if (option == 0):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = None
				alg = args.algorithm
				spec = None
				location = args.location
				multiPrompts(files, alg[0], spec, location[0])
			elif (option == 1):
				files = None
				alg = args.algorithm
				spec = None
				location = args.location
				singlePrompts(files, alg[0], spec, location[0])
			else:
				raise ArgumentException("Error: bad argument")
		else:
			msg = "Would you like to generate a hash for a single file or for multiple files?"
			multSing = ['Multiple', 'Single']
			option = multiOptions(msg, multSing)
			if (option == 0):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = None
				alg = args.algorithm
				multiPrompts(files, alg[0])
			elif (option == 1):
				files = None
				alg = args.algorithm
				singlePrompts(files, alg[0])
			else:
				raise ArgumentException("Error: bad argument")
	elif (args.specifier != None):
		if (args.location != None):
			msg = "Would you like to generate a hash for a single file or for multiple files?"
			multSing = ['Multiple', 'Single']
			option = multiOptions(msg, multSing)
			if (option == 0):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = None
				alg = None
				spec = args.specifier
				location = args.location
				multiPrompts(files, alg, spec[0], location[0])
			elif (option == 1):
				files = None
				alg = None
				spec = args.specifier
				location = args.location
				singlePrompts(files, alg, spec[0], location[0])
			else:
				raise ArgumentException("Error: bad argument")
		else:
			msg = "Would you like to generate a hash for a single file or for multiple files?"
			multSing = ['Multiple', 'Single']
			option = multiOptions(msg, multSing)
			if (option == 0):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = None
				alg = None
				spec = args.specifier
				multiPrompts(files, alg, spec[0])
			elif (option == 1):
				files = None
				alg = None
				spec = args.specifier
				singlePrompts(files, alg, spec[0])
			else:
				raise ArgumentException("Error: bad argument")
	elif (args.location != None):
		msg = "Would you like to generate a hash for a single file or for multiple files?"
		multSing = ['Multiple', 'Single']
		option = multiOptions(msg, multSing)
		if (option == 0):
			print "Please note that it takes time to hash multiple files all at once on the same machine"
			files = None
			alg = None
			spec = None
			location = args.location
			multiPrompts(files, alg, spec, location[0])
		elif (option == 1):
			files = None
			alg = None
			spec = None
			location = args.location
			singlePrompts(files, alg, spec, location[0])
		else:
			raise ArgumentException("Error: bad argument")
	else:
		raise ArgumentException('Error: bad argument')
	return

def detQArgs( args, parser ):
	if (args.files == None):
		raise ArgumentException('Error: missing argument')
	else:
		if (args.algorithm != None):
			if (args.specifier != None):
				if (args.location != None):
					files = []
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					algorithm = args.algorithm
					specifier = args.specifier
					location = args.location
					length = len(files)
					if (length > 1):
						multiNoPrompts(files, algorithm, specifier, location)
					else:
						newfile = files[0]
						singleNoPrompts(newfile, algorithm, specifier, location)
				else:
					files = []
					files = args.files
					for f in files:
						f = f.replace('\'', '')
					algorithm = args.algorithm
					specifier = args.specifier
					length = len(files)
					if (length > 1):
						multiNoPrompts(files, algorithm, specifier)
					else:
						newfile = files[0]
						singleNoPrompts(newfile, algorithm, specifier)
			elif (args.location != None):
				files = []
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				algorithm = args.algorithm
				specifier = None
				location = args.location
				length = len(files)
				if (length > 1):
					multiNoPrompts(files, algorithm, specifier, location)
				else:
					newfile = files[0]
					singleNoPrompts(newfile, algorithm, specifier, location)
			else:
				files = []
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				algorithm = args.algorithm
				length = len(files)
				if (length > 1):
					multiNoPrompts(files, algorithm)
				else:
					newfile = files[0]
					singleNoPrompts(newfile, algorithm)
		elif (args.specifier != None):
			if (args.location != None):
				files = []
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				algorithm = None
				specifier = args.specifier
				location = args.location
				length = len(files)
				if (length > 1):
					multiNoPrompts(files, algorithm, specifier, location)
				else:
					newfile = files[0]
					singleNoPrompts(newfile, algorithm, specifier, location)
			else:
				files = []
				files = args.files
				for f in files:
					f = f.replace('\'', '')
				algorithm = None
				specifier = args.specifier
				length = len(files)
				if (length > 1):
					multiNoPrompts(files, algorithm, specifier)
				else:
					newfile = files[0]
					singleNoPrompts(newfile, algorithm, specifier)
		elif (args.location != None):
			files = []
			files = args.files
			for f in files:
				f = f.replace('\'', '')
			algorithm = None
			specifier = None
			location = args.location
			length = len(files)
			if (length > 1):
				multiNoPrompts(files, algorithm, specifier, location)
			else:
				newfile = files[0]
				singleNoPrompts(newfile, algorithm, specifier, location)
		else:
			files = []
			files = args.files
			for f in files:
				f = f.replace('\'', '')
			length = len(files)
			if (length > 1):
				multiNoPrompts(files)
			else:
				newfile = files[0]
				singleNoPrompts(newfile)
	return

def detSamma( args, parser ):
	return

def detQSamma( args, parser ):
	return

def usage():
	parser = argparse.ArgumentParser(description='''This command is meant to generate a hash for
		the given files, it will also generate an xml file with the information taken from the file
		and it will place the xml file in the same place as the file that it used to generate the 
		hash''')
	parser.add_argument('-q', '--quiet', action="store_true", dest="quiet", help='''This allows this 
		command to be run in silent mode which means no prompts''')
	parser.add_argument('-f', '--files', nargs="+", dest="files", help='''This allows us to specify a 
		list of files to generate hashes for without the prompt asking for them, this flag is 
		mandatory in silent mode''')
	parser.add_argument('-s', '--specifier', nargs=1, dest="specifier", help='''This allows you to 
		specify which output file you want, depending on the settings you may also set some 
		parameters automatically''')
	parser.add_argument('-a', '--algorithm', nargs=1, dest="algorithm", help='''This lets you 
		select a different algorithm than the default md5''')
	parser.add_argument('-p', '--printout', action="store_true", dest="printout", help='''This should 
		allow a print out of available specifiers even in quiet mode, however, this flag cannot be 
		used with any other flag except the -q''')
	parser.add_argument('-l', '--location', nargs=1, dest="location", help='''This allows you to 
		specify an alternate location for the output files, default will always be in the same 
		location as the source files, the quiet mode only allows for one location for all the output 
		files''')
	parser.add_argument('-m', '--samma', action="store_true", dest="samma", help='''This is especially 
		for the samma output because it requires a bit more information to be sent to the output 
		than the core code typically provides''')
	args = parser.parse_args()
	return args, parser

def multiPrompts( arry=None, algorithm=None, specification=None, location=None ):
	'''
	multiPrompts handles generating hashes for multiple files all at once, as such it is 
		considerably longer than it's related function; this function takes the user 
		through prompts and handles all the files by the end, it even allows the user to 
		give individual specifiers to each file, that is, it allows the user to generate 
		a different output format for each file or the same output format for all files
	'''
	files = []
	hash = []
	filename = []
	ext = []
	path = []
	alg = []
	if (arry == None):
		msg = "Please enter a file that you wish to generate a hash for:\n"
		omsg = "(or \"Done\" to indicate there are no more files to add)\n"
		concat = msg + omsg
		doContinue = False
		while doContinue == False:
			nfile = getInput(concat)
			if (nfile == 'Done' or nfile == None or nfile == "Done" or nfile == 'done' or nfile == 'DONE' or nfile == "done" or nfile == "DONE"):
				doContinue == True
				break
			else:
				nfile = nfile.replace('\'', '')
				nfile = nfile.rstrip()
				files.append(nfile)
	else:
		for f in arry:
			files.append(f)
	alggen = False
	alg2gen = ''
	if (algorithm == None):
		newhsmsg = "Before we begin, would you like to generate using one algorithm for all the files or one per file?"
		newhsopt = ['All', 'One Per']
		newhschosen = multiOptions(newhsmsg, newhsopt)
		if (newhschosen == 0):
			alggen = True
			hsmsg = "Would you like to go with the default hash or use a different hash?\n(Default is md5):"
			hsopt = ['Default', 'Pick One']
			hschosen = multiOptions(hsmsg, hsopt)
			if (hschosen == 0):
				alg2gen = 'md5'
			else:
				hashlist = ['md5', 'sha1', 'sha256', 'sha', 'md2', 'md4', 'rmd160']
				hashmsg = 'These are the different hashes you can use:'
				printList(hashmsg, hashlist)
				shmsg = '\nWhich hash would you like to use?\n'
				tempalg2gen = getInput(shmsg)
				hsbool = isValidInput(tempalg2gen, hashlist)
				if (hsbool == False):
					alg2gen = 'md5'
				else:
					alg2gen = tempalg2gen
		else:
			alggen = False
	else:
		alggen = True
		alg2gen = algorithm
	startTime = None
	endTime = None
	for file in files:
		size = checkSize(file)
		if (size == True):
			print "\nPlease note that hashing can take some time, approximately 4 minutes per 20 GB of a file"
		else:
			pass
		print "\nFile Name: " + file
		if (alggen == True):
			tempalg = alg2gen
			startTime = startEndTimer()
			temphash = getHash(file, tempalg)
			endTime = startEndTimer()
			alg.append(tempalg)
		else:
			hsmsg = "Would you like to go with the default hash or use a different hash?\n(Default is md5):"
			hsopt = ['Default', 'Pick One']
			hschosen = multiOptions(hsmsg, hsopt)
			if (hschosen == 0):
				startTime = startEndTimer()
				temphash = getHash(file)
				endTime = startEndTimer()
				tempalg = 'md5'
				alg.append(tempalg)
			else:
				hashlist = ['md5', 'sha1', 'sha256', 'sha', 'md2', 'md4', 'rmd160']
				hashmsg = 'These are the different hashes you can use:'
				printList(hashmsg, hashlist)
				shmsg = '\nWhich hash would you like to use?\n'
				tempalg = getInput(shmsg)
				hsbool = isValidInput(tempalg, hashlist)
				if (hsbool == False):
					tempalg = 'md5'
					alg.append(tempalg)
				else:
					alg.append(tempalg)
				startTime = startEndTimer()
				temphash = getHash(file, tempalg)
				endTime = startEndTimer()
		totalTime = timerPrintout(startTime, endTime)
		hash.append(temphash)
		print "\nThis is the hash for your file: " + temphash
		print "This was generated with the " + tempalg.upper() + " algorithm"
		tempfilename = getFileName(file)
		filename.append(tempfilename)
		print "This is the name of your file: " + tempfilename
		tempext = getExtension(file)
		ext.append(tempext)
		print "This is your file's extension: " + tempext
		temppath = getPath(file)
		path.append(temppath)
		print "This is the path to your file: " + temppath
	if (specification == None):
		nmsg = "Would you like to enter a different specifier per file?"
		multiSpecs = yOrN(nmsg)
		if (multiSpecs == True):
			count = 0
			for name in filename:
				currentfile = "\nCurrent File: " + name + "\n"
				omsg = "Please type the specifier you wish to use for the output file or leave blank to use default "
				amsg = "(you may also type 'show' for a list of available specifiers):\n"
				concat = currentfile + omsg + amsg
				spec = getInput(concat)
				if (spec == 'show'):
					list = hashcreate.listPrintFunc()
					spec, printbool = showListPrompt(list)
				elif (spec == '' or spec == None):
					spec = 'default'
					printbool = False
				else:
					printbool = False
				while printbool == True:		
					print "\nSpecifier chosen: " + spec
					hashcreate.main(hash[0], False, path[0], name, ext[0], alg[0], spec, printbool)
					newmsg = "Is this the format you would like to use?"
					loopbool = yOrN(newmsg)
					if (loopbool == True):
						printbool = False
						break
					else:
						list = hashcreate.listPrintFunc()
						spec, printbool = showListPrompt(list)
				print "\nSpecifier chosen: " + spec
				if (location == None):
					locmsg = "Would you like to provide an alternate location to place the hash file?"
					altloc = yOrN(locmsg)
					if (altloc == True):
						nlocmsg = "\nPlease enter the file path where you would like to put the hash file:\n"
						loc = getInput(nlocmsg)
						loc = loc.rstrip()
						loc = loc.lstrip()
						loc += '/'
						try:
							locSplit = loc.split("/")
						except:
							raise ArgumentError('Error: invalid input')
						else:
							hashcreate.main(hash[count], False, path[count], name, ext[count], alg[count], spec, printbool, loc)
							print "\nYour file has been created and saved to: " + loc
					else:
						hashcreate.main(hash[count], False, path[count], name, ext[count], alg[count], spec, printbool)
						print "\nYour file has been created and saved to: " + path[count]
				else:
					loc = location
					hashcreate.main(hash[count], False, path[count], name, ext[count], alg[count], spec, printbool, loc)
					print "\nYour file has been created and saved to: " + loc
				print "Moving on..."
				count += 1
		else:
			omsg = "\nPlease type the specifier you wish to use for all the output files or leave blank to use default "
			amsg = "(you may also type 'show' for a list of available specifiers):\n"
			concat = omsg + amsg
			spec = getInput(concat)
			if (spec == 'show'):
				list = hashcreate.listPrintFunc()
				spec, printbool = showListPrompt(list)
			elif (spec == '' or spec == None):
				spec = 'default'
				printbool = False
			else:
				printbool = False
			while printbool == True:		
				print "\nSpecifier chosen: " + spec
				hashcreate.main(hash[0], False, path[0], filename[0], ext[0], alg[0], spec, printbool)
				newmsg = "Is this the format you would like to use?"
				loopbool = yOrN(newmsg)
				if (loopbool == True):
					printbool = False
					break
				else:
					list = hashcreate.listPrintFunc()
					spec, printbool = showListPrompt(list)
			print "\nSpecifier chosen: " + spec
			if (location == None):
				locmsg = "Would you like to provide an alternate location to place the hash file?"
				altloc = yOrN(locmsg)
				if (altloc == True):
					nlocmsg = "\nPlease enter the file path where you would like to put the hash file:\n"
					loc = getInput(nlocmsg)
					loc = loc.rstrip()
					loc = loc.lstrip()
					loc += '/'
					try:
						locSplit = loc.split("/")
					except:
						raise ArgumentError('Error: invalid input')
					else:
						hashcreate.main(hash, True, path, filename, ext, alg, spec, printbool, loc)
						print "\nYour files have been created and saved to: " + loc
				else:
					hashcreate.main(hash, True, path, filename, ext, alg, spec, printbool)
					print "\nYour files have been created and saved to: " + path[0]
			else:
				loc = location
				hashcreate.main(hash, True, path, filename, ext, alg, spec, printbool, loc)
				print "\nYour file has been created and saved to: " + loc
	else:
		print specification
		spec = specification
		if (location == None):
			locmsg = "Would you like to provide an alternate location to place the hash file?"
			altloc = yOrN(locmsg)
			if (altloc == True):
				nlocmsg = "\nPlease enter the file path where you would like to put the hash file:\n"
				loc = getInput(nlocmsg)
				loc = loc.rstrip()
				loc = loc.lstrip()
				loc += '/'
				try:
					locSplit = loc.split("/")
				except:
					raise ArgumentError('Error: invalid input')
				else:
					hashcreate.main(hash, True, path, filename, ext, alg, spec, False, loc)
					print "\nYour files have been created and saved to: " + loc
			else:
				hashcreate.main(hash, True, path, filename, ext, alg, spec, False)
				print "\nYour files have been created and saved to: " + path[0]
		else:
			loc = location
			hashcreate.main(hash, True, path, filename, ext, alg, spec, False, loc)
			print "\nYour file has been created and saved to: " + loc
	print "Everything has been completed. Ending now."
	return

def multiNoPrompts( arry, algorithm=None, specification=None, location=None ):
	files = []
	for f in arry:
		files.append(f)
	hash = []
	if (algorithm == None):
		alg2gen = 'md5'
	else:
		alg2gen = algorithm[0]
	alg = []
	if (specification == None):
		spec = 'default'
	else:
		spec = specification[0]
	path = []
	if (location == None):
		loc = None
	else:
		loc = location[0]
		loc = loc.rstrip()
	filename = []
	ext = []
	for file in files:
		temphash = getHash(file, alg2gen)
		tempfilename = getFileName(file)
		tempext = getExtension(file)
		temppath = getPath(file)
		
		alg.append(alg2gen)
		hash.append(temphash)
		filename.append(tempfilename)
		ext.append(tempext)
		path.append(temppath)
	hashcreate.main(hash, True, path, filename, ext, alg, spec, False, loc)
	return

def singlePrompts( file=None, algorithm=None, specification=None, location=None ):
	'''
	singlePrompts is as the name suggests: doing the hash for only one file and doing it 
		with prompts, this creates everything necessary to create a hash file and sends 
		the information to the genhashfile.py to parse
	'''
	if (file == None):
		msg = "Please enter the file you wish to generate a hash for:\n"
		file = getInput(msg)
		file = file.replace('\'', '')
		file = file.rstrip()
	else:
		file = file.rstrip()
	size = checkSize(file)
	if (size == True):
		print "Please note that hashing can take some time, approximately 4 minutes per 20 GB of a file"
	else:
		print "Please note that hashing can take some time, but files under 20 GB should take less than 4 minutes to hash"
	startTime = None
	endTime = None
	if (algorithm == None):
		hsmsg = "Would you like to go with the default hash or use a different hash?\n(Default is md5):"
		hsopt = ['Default', 'Pick One']
		hschosen = multiOptions(hsmsg, hsopt)
		if (hschosen == 0):
			startTime = startEndTimer()
			hash = getHash(file)
			endTime = startEndTimer()
			alg = 'md5'
		else:
			hashlist = ['md5', 'sha1', 'sha256', 'sha', 'md2', 'md4', 'rmd160']
			hashmsg = 'These are the different hashes you can use:'
			printList(hashmsg, hashlist)
			shmsg = '\nWhich hash would you like to use?\n'
			alg = getInput(shmsg)
			hsbool = isValidInput(alg, hashlist)
			if (hsbool == False):
				alg = 'md5'
			else:
				pass
			startTime = startEndTimer()
			hash = getHash(file, alg)
			endTime = startEndTimer()
	else:
		alg = algorithm
		startTime = startEndTimer()
		hash = getHash(file, alg)
		endTime = startEndTimer()
	totalTime = timerPrintout(startTime, endTime)
	print "\nThis is the hash for your file: " + hash
	print "This was generated with the " + alg.upper() + " algorithm"
	filename = getFileName(file)
	print "This is the name of your file: " + filename
	ext = getExtension(file)
	print "This is your file's extension: " + ext
	path = getPath(file)
	print "This is the path to your file: " + path
	if (specification == None):
		omsg = "\nPlease type the specifier you wish to use for the output file or leave blank to use default "
		amsg = "(you may also type 'show' for a list of available specifiers):\n"
		concat = omsg + amsg
		spec = getInput(concat)
		if (spec == 'show'):
			list = hashcreate.listPrintFunc()
			spec, printbool = showListPrompt(list)
		elif (spec == '' or spec == None):
			spec = 'default'
			printbool = False
		else:
			printbool = False
		while printbool == True:		
			print "\nSpecifier chosen: " + spec
			hashcreate.main(hash, False, path, filename, ext, alg, spec, printbool)
			newmsg = "Is this the format you would like to use?"
			loopbool = yOrN(newmsg)
			if (loopbool == True):
				printbool = False
				break
			else:
				list = hashcreate.listPrintFunc()
				spec, printbool = showListPrompt(list)
	else:
		spec = specification
		printbool = False
	print "\nSpecifier chosen: " + spec
	if (location == None):
		locmsg = "Would you like to provide an alternate location to place the hash file?"
		altloc = yOrN(locmsg)
		if (altloc == True):
			nlocmsg = "\nPlease enter the file path where you would like to put the hash file:\n"
			loc = getInput(nlocmsg)
			loc = loc.rstrip()
			loc = loc.lstrip()
			loc += '/'
			try:
				locSplit = loc.split("/")
			except:
				raise ArgumentError('Error: invalid input')
			else:
				hashcreate.main(hash, False, path, filename, ext, alg, spec, printbool, loc)
				print "\nYour file has been created and saved to: " + loc
		else:
			hashcreate.main(hash, False, path, filename, ext, alg, spec, printbool)
			print "\nYour file has been created and saved to: " + path
	else:
		loc = location
		hashcreate.main(hash, False, path, filename, ext, alg, spec, printbool, loc)
		print "\nYour file has been created and saved to: " + loc
	print "Ending now"
	return

def singleNoPrompts( file, algorithm=None, specification=None, location=None ):
	'''
	singleNoPrompts handles all the quiet options of this script, basically if it is only 
		passed the file then it assumes defaults for everything else, otherwise it will 
		insert the information where it is needed and produce the proper output
	'''
	file = file.rstrip()
	if (algorithm == None):
		hash = getHash(file)
		alg = 'md5'
	else:
		alg = algorithm[0]
		hash = getHash(file, alg)
	filename = getFileName(file)
	ext = getExtension(file)
	path = getPath(file)
	if (specification == None):
		spec = 'default'
	else:
		spec = specification[0]
	if (location == None):
		loc = None
		hashcreate.main(hash, False, path, filename, ext, alg, spec, False, loc)
	else:
		loc = location[0]
		loc = loc.rstrip()
		hashcreate.main(hash, False, path, filename, ext, alg, spec, False, loc)
	return

def isValidInput( input, args ):
	'''
	isValidInput can ensure that the user entered something within the allowable range, 
		returns false if user did not enter something in the allowable limits
	'''
	if input in args:
		return True
	else:
		return False

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

def getInput( msg ):
	'''
	getInput simply prints the message it is passed and gets the user input
	'''
	userInputVar = raw_input(msg)	
	return userInputVar

def get_size(file):
	'''
	get_size only gets and returns the size, in bytes, of the folder that is passed to it
	'''
	total_size = 0
	total_size += os.path.getsize(file)
	return total_size

def checkSize( file ):
	'''
	checkSize checks the size of the given folder or path and returns true if the folder or file is over 300 GB
		or false if it is not
	Note: currently does not support relative paths
	Uses the following functions:	size.get_size (from getSize.py in testModules)
	'''
	maxSize = 20000000000
	fileSize = get_size(file)
	if (fileSize > maxSize):
		return True
	else:
		return False

def showListNoPrompt ( list ):
	'''
	showListNoPrompt simply shows the list of available specifiers, this function is 
		available for the use of quiet mode functions
	'''
	print "\nThese are the available specifiers:\n"
	for i in list:
		print "\t- " + i
	return

def showListPrompt( list ):
	'''
	showListPrompt shows the list of available specifiers and allows you to enter the one 
		you would like to see or use
	'''
	print "\nThese are the available specifiers:\n"
	for i in list:
		print "\t- " + i
	line1 = "\nIf you would like to see a sample of one of the output formats shown above"
	line2 = " then enter a -s followed by the name of the format you would like to see,"
	line3 = " otherwise please enter the name of the format you would like to use:\n"
	concat = line1 + line2 + line3
	newspec = getInput(concat)
	if (newspec[:2] == '-s'):
		specSplit = newspec.split(' ')
		spec = specSplit[1]
		printbool = True
	else:
		spec = newspec.rstrip()
		spec = spec.lstrip()
		printbool = False
	return spec, printbool

def printList( msg, arry ):
	'''
	printList just prints an array that is passed to it
	'''
	print "\n" + msg + "\n"
	for i in arry:
		print "\t- " + i
	return

def getExtension( file ):
	'''
	getExtension gets the extension from the file that is provided, it makes sure to take 
		the period off of it and it returns the ext that it got
	'''
	fileSplit = file.split("/")
	mIndex = len(fileSplit) - 1
	filename = fileSplit[mIndex]
	nameSplit = filename.split(".")
	aIndex = len(nameSplit) - 1
	ext = nameSplit[aIndex]
	return ext

def getFileName( file ):
	'''
	getFileName gets the name of the file that is provided, the file that is provided 
		should have the complete file path with it when it is given to this function
	'''
	fileSplit = file.split("/")
	mIndex = len(fileSplit) - 1
	name = fileSplit[mIndex]
	nameSplit = name.split(".")
	del nameSplit[-1]
	filename = ".".join(nameSplit)
	return filename

def getPath( file ):
	'''
	getPath gets the file path from the file provided, the file that is given to this 
		function should have the file path with it when it is passed in
	'''
	fileSplit = file.split("/")
	del fileSplit[-1]
	fileSplit.append('')
	path = "/".join(fileSplit)
	path = path.rstrip()
	return path

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

def getHash( file, alg='md5' ):
	'''
	getHash returns the hash tag for the given file
	Uses the following functions:	subprocess.Popen, subprocess.communicate
	'''
	if (alg == 'md5' or alg == 'sha' or alg == 'md2' or alg == 'md4' or alg == 'mdc2' or alg == 'rmd160'):
		out = subprocess.Popen(['openssl', alg, file], stdout=subprocess.PIPE).communicate()[0]
		outSplit = out.split('=')
		maxIndex = len(outSplit) - 1
		apitem = outSplit[maxIndex].lstrip()
		hash = apitem.replace('\n', '')
	elif (alg[:3] == 'sha'):
		alg = alg[3:]
		out = subprocess.Popen(['shasum', '-a', alg, file], stdout=subprocess.PIPE).communicate()[0]
		outSplit = out.split(' ')
		apitem = outSplit[0].lstrip()
		hash = apitem.rstrip()
	else:
		raise ArgumentException('Error: unknown hash type')
	return hash

if __name__=='__main__':
	main()