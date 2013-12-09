#! /usr/bin/python

import os,sys,inspect
import time
import datetime
import argparse
import subprocess

from hashModule.scripts import genhashfile as create
from hashModule.scripts import hash_macosx as hmMain

# Allow this printout for a single or multifile object

def main( arguments=None, par=None ):
	if (arguments == None or par == None):
		if (len(sys.argv) == 1):
			msg = 'Is this for multi-file objects or just for the samma output?'
			objOut = ['Objects','Output']
			option = hmMain.multiOptions(msg, objOut)
			if (option == 0):
				multiPrompts(False)
			elif (option == 1):
				singlePrompts(False)
		else:
			args, parser = usage()
			detArgs(args, parser)
	else:
		detArgs(arguments, par)
	return

def getInfoSaveLoc():
	file = inspect.getfile(inspect.currentframe())
	filename = os.path.realpath(file)
	fSplit = filename.split('/')
	del fSplit[-1]
	name = '/'.join(fSplit)
	name += '/mediaInfo/'
	return name

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

global SERVER
SERVER = getServer()

global SPECIFIER
SPECIFIER = 'samma'

global INFOSAVE
INFOSAVE = getInfoSaveLoc()

def detArgs( args, parser ):
	# Rewrite printout section for the special samma printout only, this entire script only works for that output
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
			list = create.listPrintFunc()
			showListNoPrompt(list)
			printbool = True
			count = 0
			maxCount = 2
			mIndex = len(list) - 1
			print '\nHere is what each of the output files will look like:'
			for spec in list:
				if (count == maxCount):
					count = 0
				create.main(hash[count], False, path[count], filename[count], ext[count], alg[count], spec, printbool, loc)
				count += 1
		sys.exit(0)
	elif (args.quiet == True):
		detQArgs(args, parser)
	elif (args.files != None):
		if (args.algorithm != None):
			# Specifier no longer applies, this only has one specifier and that is samma
			if (args.location != None):
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					alg = args.algorithm
					spec = SPECIFIER
					location = args.location
					multiPrompts(files, alg[0], spec, location[0])
				elif (length == 1):
					files = args.files
					alg = args.algorithm
					spec = SPECIFIER
					location = args.location
					singlePrompts(files[0], alg[0], spec, location[0])
				else:
					raise ArgumentException("Error: bad argument")
			else:
				length = len(args.files)
				if (length > 1):
					print "Please note that it takes time to hash multiple files all at once on the same machine"
					files = args.files
					alg = args.algorithm
					multiPrompts(files, alg[0])
				elif (length == 1):
					files = args.files
					alg = args.algorithm
					singlePrompts(files[0], alg[0])
				else:
					raise ArgumentException("Error: bad argument")
		elif (args.location != None):
			length = len(args.files)
			if (length > 1):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = args.files
				alg = None
				spec = SPECIFIER
				location = args.location
				multiPrompts(files, alg, spec, location[0])
			elif (length == 1):
				files = args.files
				alg = None
				spec = SPECIFIER
				location = args.location
				singlePrompts(files[0], alg, spec, location[0])
			else:
				raise ArgumentException("Error: bad argument")
		else:
			length = len(args.files)
			if (length > 1):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = args.files
				multiPrompts(files)
			elif (length == 1):
				files = args.files
				singlePrompts(files[0])
			else:
				raise ArgumentException("Error: bad argument")
	elif (args.algorithm != None):
		if (args.location != None):
			msg = "Would you like to generate a hash for a single file or for multiple files?"
			multSing = ['Multiple', 'Single']
			option = multiOptions(msg, multSing)
			if (option == 0):
				print "Please note that it takes time to hash multiple files all at once on the same machine"
				files = None
				alg = args.algorithm
				spec = SPECIFIER
				location = args.location
				multiPrompts(files, alg[0], spec, location[0])
			elif (option == 1):
				files = None
				alg = args.algorithm
				spec = SPECIFIER
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
	elif (args.location != None):
		msg = "Would you like to generate a hash for a single file or for multiple files?"
		multSing = ['Multiple', 'Single']
		option = multiOptions(msg, multSing)
		if (option == 0):
			print "Please note that it takes time to hash multiple files all at once on the same machine"
			files = None
			alg = None
			spec = SPECIFIER
			location = args.location
			multiPrompts(files, alg, spec, location[0])
		elif (option == 1):
			files = None
			alg = None
			spec = SPECIFIER
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
			if (args.location != None):
				files = []
				files = args.files
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
				algorithm = args.algorithm
				length = len(files)
				if (length > 1):
					multiNoPrompts(files, algorithm)
				else:
					newfile = files[0]
					singleNoPrompts(newfile, algorithm)
		elif (args.location != None):
			files = []
			files = args.files
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
			length = len(files)
			if (length > 1):
				multiNoPrompts(files)
			else:
				newfile = files[0]
				singleNoPrompts(newfile)
	return

def usage():
	parser = argparse.ArgumentParser(description='''This command is meant to generate a hash for
		the given files, it will generate the needed data for the samma output in the genhashfile 
		script, this is configured to handle multi-file objects too''')
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
	parser.add_argument('-dr', '--distributed-rendering', action="store_true", dest="distrender", 
		help='''This is meant to enable genhash to use distributed rendering which will speed up 
		processing on large numbers of files''')
	parser.add_argument('-o', '--object', action="store_true", dest="object", help='''This is meant 
		to specify that everything following is an object, this flag only works in quiet mode and 
		it will only work for one object at a time''')
	args = parser.parse_args()
	return args, parser

def getMediaInfoOutput( file ):
	'''
	getMediaInfoOutput simply runs mediainfo on a given file and then saves the output to a specific 
		place, it also passes back the name / location of that file so that it can be used for 
		reference so that we can get the information we need out of this file
	'''
	mediafile = checkFile(file)
	if (mediafile == False):
		createdFile = None
	else:
		fSplit = file.split('/')
		fSplit = filter(None, fSplit)
		mIndex = len(fSplit) - 1
		fileSplit = fSplit[mIndex].split('.')
		fName = fileSplit[0]
		fileName = fName.replace(' ', '_')
		out = subprocess.Popen(['mediainfo', '-f', file], stdout=subprocess.PIPE).communicate()[0]
		createdFile = INFOSAVE + fileName + '_mediainfo_printout.txt'
		f = os.open(createdFile, os.O_RDWR|os.O_CREAT)
		os.write(f, out)
		os.close(f)	
	return createdFile

def checkFile( file ):
	'''
	checkFile simply checks a given file for whether or not it is a media file
	'''
	ext = ['mkv','mka','mks','ogg','ogm','avi','wav','mpeg','mpg','vob','mp4','mpgv','mpv','m1v','m2v','mp2','mp3','asf','wma','wmv','qt','mov','rm','rmvb','ra','ifo','ac3','dts','aac','ape','mac','flac','dat','aiff','aifc','au','iff','paf','sd2','irca','w64','mat','pvf','xi','sds','avr']
	fileExt = file[-3:]
	if fileExt in ext:
		return True
	else:
		return False

if __name__=='__main__':
	main()