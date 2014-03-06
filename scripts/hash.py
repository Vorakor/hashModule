#! /usr/bin/python

import locale
import os,sys,inspect
import time, re
import datetime, socket
import argparse
import subprocess
import commands

import genhashfile as create
from config import *
import ops as ghOps
import samma_macosx as samma

def main():
	'''
	main is the entry point for the entire script
	'''
	if(len(sys.argv) == 1):
		msg = "Would you like to generate a hash for a single file or for multiple files?"
		multSing = ['Multiple', 'Single']
		option = ghOps.multiOptions(msg, multSing)
		if option == 0:
			genHash(True)
		elif option == 1:
			genHash(False)
		else:
			raise ArgumentException("Error: bad argument")
	else:
		args, parser = usage()
		detArgs(args, parser)
	return

def detArgs( args, parser ):
	'''
	detArgs uses all of the arguments it is given and prompts for anything it doesn't have, it does 
		the same thing as genHash except that genHash assumes the only thing we have decided is 
		whether or not we are doing multiple files
	'''
	distRend = None
	files = []
	spec = ''
	printbool = None
	algorithm = ''
	loc = ''
	sammaOut = None
	if args.quiet == True:
		if not args.files:
			raise ghOps.ArgumentException('Error: Cannot run quiet without files! detArgs() line: ' + str(lineno()))
		else:
			files = args.files
			if not args.specifier:
				spec = 'default'
			else:
				spec = args.specifier[0]
			sammaOut = args.samma
			if not args.algorithm:
				algorithm = 'md5'
			else:
				algorithm = args.algorithm[0]
			distRend = args.distrender
			if not args.location:
				pass
			else:
				loc = args.location[0]
			printbool = args.printout
	else:
		if not args.files:
			files = getFiles()
		else:
			files = args.files
		sammaOut = checkSamma()
		if not args.specifier:
			spec = detSpecifier()
		else:
			spec = args.specifier[0]
		distRend = detDistRend()
		if not args.algorithm:
			algorithm = detAlgorithm()
		else:
			algorithm = args.algorithm[0]
		printbool = detPrintBool()
		if not args.location:
			loc = detLocation()
		else:
			loc = args.location[0]
	if sammaOut == True:
		objName = detObjName(args.quiet)
		sammaObject = samma.SammaObject()
		for f in files:
			multiObject = samma.MultiFileObject(f)
			sammaObject += multiObject
		sammaobj.setLocation(loc)
		sammaobj.setPrintBool(printbool)
		sammaobj.setName(objName)
		create.main(sammaobj)
	elif distRend == True:
		cmdArry = []
		for f in files:
			if args.quiet == True:
				cmd = GENHASHEXE + ' -q -a ' + algorithm + ' -sp ' + spec + ' -l ' + loc + ' -f ' + f
				cmdArry.append(cmd)
			else:
				cmd = GENHASHEXE + ' -a ' + algorithm + ' -sp ' + spec + ' -l ' + loc + ' -f ' + f
				cmdArry.append(cmd)
		#Now connect to some sort of task engine and send off all of the tasks
	else:
		for f in files:
			object = HashObject(f, spec, algorithm, loc)
			object.setPrintBool(printbool)
			object.getHash()
			create.main(object)
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
	parser.add_argument('-sp', '--specifier', nargs=1, dest="specifier", help='''This allows you to 
		specify which output file you want, depending on the settings you may also set some 
		parameters automatically''')
	parser.add_argument('-a', '--algorithm', nargs=1, dest="algorithm", help='''This lets you 
		select a different algorithm than the default md5''')
	parser.add_argument('-l', '--location', nargs=1, dest="location", help='''This allows you to 
		specify an alternate location for the output files, default will always be in the same 
		location as the source files, the quiet mode only allows for one location for all the output 
		files''')
	parser.add_argument('-p', '--printout', action="store_true", dest="printout", help='''This should 
		allow a print out of available specifiers even in quiet mode, however, this flag cannot be 
		used with any other flag except the -q''')
	parser.add_argument('-sa', '--samma', action="store_true", dest="samma", help='''This is especially 
		for the samma output because it requires a bit more information to be sent to the output 
		than the core code typically provides''')
	parser.add_argument('-dr', '--distributed-rendering', action="store_true", dest="distrender", 
		help='''This is meant to enable genhash to use distributed rendering which will speed up 
		processing on large numbers of files''')
	args = parser.parse_args()
	return args, parser

def lineno():
    '''Returns the current line number in the program'''
    return inspect.currentframe().f_back.f_lineno

def genHash( multi ):
	'''
	genHash takes the information it is given and creates an object to stick it all in, then it 
		sends that object to the output file
	'''
	distRend = None
	files = []
	spec = ''
	printbool = None
	algorithm = ''
	loc = None
	sammaOut = None
	if multi == True:
		sammaOut = checkSamma()
		if sammaOut == False:
			distRend = detDistRend()
			files = getFiles()
			spec = detSpecifier() 
			algorithm = detAlgorithm()
			loc = detLocation()
			if distRend == True:
				cmdArry = []
				for f in files:
					cmd = GENHASHEXE + ' -a ' + algorithm + ' -sp ' + spec + ' -l ' + loc + ' -f ' + f
					cmdArry.append(cmd)
			else:
				for f in files:
					if not loc or loc == None or loc == '':
						object = HashObject(f, spec, algorithm)
					else:
						object = HashObject(f, spec, algorithm, loc)
					object.setPrintBool(printbool)
					object.getHash()
					create.main(object)
		else:
			files = getFiles()
			loc = detLocation()
			objName = detObjName() #This is only for Samma
			printbool = detPrintBool()
			sammaobj = samma.SammaObject()
			for f in files:
				multiobj = samma.MultiFileObject(f)
				sammaobj += multiobj
			sammaobj.setLocation(loc)
			sammaobj.setPrintBool(printbool)
			sammaobj.setName(objName)
			create.main(sammaobj)
	else:
		printbool = detPrintBool()
		files = getFiles()
		spec = detSpecifier()
		algorithm = detAlgorithm()
		loc = detLocation()
		for f in files:
			if not loc or loc == None or loc == '':
				object = HashObject(f, spec, algorithm)
			else:
				object = HashObject(f, spec, algorithm, loc)
			object.setPrintBool(printbool)
			object.getHash()
			create.main(object)
	return

def checkSamma():
	msg = 'Do you want the output for a Samma multi-file object?'
	return ghOps.yOrN(msg)

def detDistRend():
	msg = 'Would you like to split up the hash generation across a distributed system?'
	return ghOps.yOrN(msg)

def getFiles():
	files = []
	doneArry = ['Done', 'DONE', 'D', 'done', 'd']
	doContinue = False
	while doContinue == False:
		msg = '\nPlease enter a file that you would like to generate a hash for-\n '
		msg += 'Note: enter \'Done\' to indicate that you are done adding files\n\t'
		selection = ghOps.getInput(msg).rstrip().lstrip()
		if selection in doneArry:
			doContinue = True
			break
		else:
			files.append(selection)
	return files

def detSpecifier():
	specifier = ''
	arry = create.listPrintFunc()
	listmsg = 'These are the available specifiers:'
	ghOps.printList(listmsg, arry)
	valid = False
	while valid == False:
		msg = '\nWhich specifier would you like to use? (This specifier determines what output file you are going to use):'
		specifier = ghOps.getInput(msg)
		valid = ghOps.isValidInput(specifier, arry)
		if valid == True:
			break
		else:
			print 'Sorry, that is not a valid specifier, please choose a specifier from the list that was provided above'
	return specifier

def detAlgorithm():
	alg = ''
	allowable = ['md5','md2','md4','mdc2','rmd160', 'sha', 'sha1', 'sha256', 'sha384', 'sha512']
	allmsg = 'Here is a list of the hashing algorithms this script supports: '
	ghOps.printList(allmsg, allowable)
	valid = False
	while valid == False:
		msg = '\nWhat algorithm would you like to use to generate your hash for the file you provided?'
		alg = ghOps.getInput(msg)
		valid = verifyAlgorithm(alg)
		if valid == True:
			break
		else:
			print 'Sorry, that is not a valid algorithm, please choose an algorithm from the list that was provided above'
	return alg

def detLocation():
	loc = ''
	msg = 'Would you like to place the output files in a different location than where the their source files are located?'
	selection = ghOps.yOrN(msg)
	if selection == False:
		return None
	else:
		newmsg = 'Please input the file path now: '
		loc = ghOps.getInput(newmsg).rstrip().lstrip()
		return loc

def detPrintBool():
	msg = 'Would you like a sample output? (This script will produce a sample in the terminal window and then end)'
	return ghOps.yOrN(msg)

def verifyAlgorithm( input ):
	allowable = ['md5','md2','md4','mdc2','rmd160', 'sha', 'sha1', 'sha256', 'sha384', 'sha512']
	testVal = input.lower()
	if testVal in allowable:
		return True
	else:
		return False

class HashObject:
	'This is for the creation of a hash object, that can be sent to the genhashfile.py later'
	def __init__(self, file, specification=None, alg=None, loc=None):
		if specification == None:
			self.spec = ''
		else:
			self.spec = specification
		self.file = file
		if alg == None:
			self.algorithm = ''
		else:
			self.algorithm = alg
		self.hash = ''
		self.printbool = False
		self.extension = ''
		self.filename = ''
		self.path = ''
		self.__addPathDetails()
		if loc == None:
			self.location = self.path
		else:
			if loc == 'path' or not loc or loc == '':
				self.location = self.path
			else:
				self.location = loc
	
	def __addPathDetails(self):
		filePath, temp = os.path.split(self.file)
		fileName, fileExtension = os.path.splitext(temp)
		self.extension = fileExtension
		self.filename = fileName
		self.path = filePath
	
	def setSpec(self, specification):
		self.spec = specification
	
	def setAlg(self, algorithm):
		self.algorithm = algorithm
	
	def setLoc(self, location):
		if location == 'path':
			self.location = self.path
		else:
			self.location = location
	
	def setPrintBool(self, printbool):
		if isinstance(printbool, bool):
			self.printbool = printbool
		else:
			self.printbool = False
	
	def getHash(self):
		if (self.algorithm == 'md5' or self.algorithm == 'sha' or 
			self.algorithm == 'md2' or self.algorithm == 'md4' or 
			self.algorithm == 'mdc2' or self.algorithm == 'rmd160'):
			out = subprocess.Popen(['openssl', self.algorithm, self.file], stdout=subprocess.PIPE).communicate()[0]
			outSplit = out.split('=')
			maxIndex = len(outSplit) - 1
			apitem = outSplit[maxIndex].lstrip()
			self.hash = apitem.replace('\n', '')
		elif (self.algorithm[:3] == 'sha'):
			alg = self.algorithm[3:]
			out = subprocess.Popen(['shasum', '-a', alg, self.file], stdout=subprocess.PIPE).communicate()[0]
			outSplit = out.split(' ')
			apitem = outSplit[0].lstrip()
			self.hash = apitem.rstrip()
		else:
			raise ghOps.ArgumentException('Error: unknown hash type ---> getHash() line: ' + str(lineno()))

if __name__=='__main__':
	main()