#! /usr/bin/python

import os,sys
import time
import datetime
import argparse
import subprocess

########################################################################################
######### Add your specifier to the list and direct the script to use it here ##########
########################################################################################
def main( hash, bool, path, filename, ext, alg, filesize=None, filetype=None, fileduration=None, filemuxrate=None, specifier='default', printbool=False, loc=None ):
	if(specifier == 'diva'):
		if (loc != None):
			diva(hash, bool, path, filename, ext, alg, printbool, loc)
		else:
			diva(hash, bool, path, filename, ext, alg, printbool)
	elif(specifier == 'samma'):
		if (loc != None):
			samma(hash, bool, path, files, ext, alg, filesize, filetype, fileduration, filemuxrate, printbool, loc)
		else:
			samma(hash, bool, path, files, ext, alg, filesize, filetype, fileduration, filemuxrate, printbool)
	else:
		if (loc != None):
			default(hash, bool, path, filename, ext, alg, printbool, loc)
		else:
			default(hash, bool, path, filename, ext, alg, printbool)
	return

########################################################################################
###########			Do not edit or add anything below this point			 ###########
########################################################################################
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

########################################################################################
######### Add the specification for your generator function to these functions #########
########################################################################################

def genExamplePrint( spec, details, arry ):
	if (spec == 'diva'):
		msg = 'This is what the diva file will look like when it is created and printed:\n'
		printStatement(msg, arry, details)
	# Add your own elif statements below this point
	elif (spec == 'samma'):
		msg = 'This is what the samma file will look like when it is created and printed:\n'
		print msg
		for i in arry:
			i = i.replace('\n', '')
			print i
		newmsg = '\nSummary:\n\tOutput Dir: \t\t' + details[0]
		newmsg += '\n\tExample File Name: \t' + details[1]
		newmsg += '\n\tOutput Ext: \t\t' + details[2]
		newmsg += '\n\tOutput Hash: \t\t' + details[3]
		newmsg += '\n\tSample Xml Name: \t' + details[4]
	# this is the default fallback ---> in other words, do not change anything below this
	else:
		msg = 'This is what the default file will look like when it is created and printed:\n'
		printStatement(msg, arry, details)
	return

def printSammaStatement( msg, arry, details ):
	return

# Do not edit this function
def printStatement( msg, arry, details ):
	print msg
	for i in arry:
		i = i.replace('\n', '')
		print i
	newmsg = '\nSummary:\n\tOutput Dir: \t\t' + details[0]
	newmsg += '\n\tExample File Name: \t' + details[1]
	newmsg += '\n\tFile Type: \t\t' + details[2]
	newmsg += '\n\tFile Hash: \t\t' + details[3]
	newmsg += '\n\tFile Size: \t\t' + details[4]
	newmsg += '\n\tFile Duration: \t\t' + details[5]
	newmsg += '\n\tFile Mux Rate: \t\t' + details[6]
	newmsg += '\n\tSample Xml Name: \t' + details[7]
	print newmsg
	return

def listPrintFunc():
	# Simply add your specification name to this array by using the list.append()
	list = []
	list.append('default')
	list.append('diva')
	list.append('samma')
	
	return list

########################################################################################
###########			Put all file generation functions below this point		 ###########
########################################################################################
def diva( hash, bool, path, files, ext, alg, printbool=False, loc=None ):
	'''
	diva generates the hash xml file necessary for transferring files to diva, this 
		function places the file it generates in the same location as the file it 
		got the hash from
	Uses the following functions:	None (does not use any external functions)
	'''
	filename = []
	count = 0
	if (bool == False):
		filename.append(files)
	else:
		filename = files
	for file in filename:
		if (bool == True):
			extension = "." + ext[count]
			mdhash = hash[count]
			fullpath = path[count]
			objName = file + extension
			algorithm = alg[count]
		else:
			extension = "." + ext
			mdhash = hash
			fullpath = path
			objName = file + extension
			algorithm = alg
		line1 = '<DIVAObjectDefinition>\n'
		line2 = '\t<objectName>' + objName + '</objectName>\n'
		line3 = '\t<fileList>\n'
		line4 = '\t\t<file\tchecksumType="' + algorithm.upper() + '"\n'
		line5 = '\t\t\tchecksumValue="' + mdhash + '">'+ objName + '</file>\n'
		line6 = '\t</fileList>\n'
		line7 = '</DIVAObjectDefinition>\n'
		if (loc != None):
			xmlName = loc + '/' + objName + '.xml'
		else:
			xmlName = fullpath + '/' + objName + '.xml'
		if (printbool == True):
			details = []
			details.append(fullpath)
			details.append(file)
			details.append(extension)
			details.append(algorithm)
			details.append(xmlName)
			lines = []
			lines.append(line1)
			lines.append(line2)
			lines.append(line3)
			lines.append(line4)
			lines.append(line5)
			lines.append(line6)
			lines.append(line7)
			genExamplePrint('diva', details, lines)
		else:
			f = os.open(xmlName, os.O_RDWR|os.O_CREAT)
			os.write(f, line1)
			os.close(f)

			with open(xmlName, 'a') as xml:
				xml.write(line2)
				xml.write(line3)
				xml.write(line4)
				xml.write(line5)
				xml.write(line6)
				xml.write(line7)
				xml.close()
		count += 1
	return

def samma( hash, bool, path, files, ext, alg, filesize, filetype, fileduration, filemuxrate, printbool=False, loc=None ):
	'''
	samma generates the hash xml file for multifile objects, it is necessary for 
		transferring files to diva, this function places the file it generates in 
		the same location as the file it got the hash from
	Uses the following functions:	None (does not use any external functions)
	'''
	count = 0
	titleLine = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
	line1 = '<SammaSolo>\n'
	line2 = '\t<Settings>\n'
	line3 = '\t\t<Details>\n'
	line4 = '\t\t\t<GeneratedBy>Genhash Script</GeneratedBy>\n'
	line5 = '\t\t</Details>\n'
	line6 = '\t</Settings>\n'
	line7 = '\t<EncodedFiles>\n'
	line8 = '\t</EncodedFiles>\n'
	line9 = '\t<Metadata>\n'
	line10 = '\t</Metadata>\n'
	line11 = '</SammaSolo>\n'
	
	xmlName = ''

	if (printbool == False):
		f = os.open(xmlName, os.O_RDWRlos.O_CREAT)
		os.write(f, titleLine)
		os.write(f, line1)
		os.write(f, line2)
		os.write(f, line3)
		os.write(f, line4)
		os.write(f, line5)
		os.write(f, line6)
		os.write(f, line7)
		os.close(f)

	for file in files:
		extension = '.' + ext[count]
		shash = hash[count]
		fullpath = path[count]
		size = filesize[count]
		type  = filetype[count]
		fullFileName = fullpath + file + extension

		linefile = '\t\t<File' + str(count) + '>\n'
		linefilename = '\t\t\t<Filename>' + fullFileName + '</Filename>\n'
		linetype = '\t\t\t<Type>' + type + '</Type>\n'
		linesdig = '\t\t\t<ShaDigest>' + shash + '</ShaDigest>\n'
		linefilesize = '\t\t\t<FileSize>' + size + '</FileSize>\n'
		lineduration = '\t\t\t<Duration>' + duration + '</Duration>\n'
		lineavmux = '\t\t\t<AverageMuxRate>' + muxrate + '</AverageMuxRate>\n'
		linefileclose = '\t\t<File' + str(count) + '>\n'

		if (printbool == True):
			printLines = []
			details = []
			printLines.append(titleLine)
			printLines.append(line1)
			printLines.append(line2)
			printLines.append(line3)
			printLines.append(line4)
			printLines.append(line5)
			printLines.append(line6)
			printLines.append(line7)
			printLines.append(linefile)
			printLines.append(linefilename)
			printLines.append(linetype)
			printLines.append(linesdig)
			printLines.append(linefilesize)
			printLines.append(lineduration)
			printLines.append(lineavmux)
			printLines.append(linefileclose)
			printLines.append(line8)
			printLines.append(line9)
			printLines.append(line10)
			printLines.append(line11)
			details.append()
			details.append(fullFileName)
			details.append(type)
			details.append(shash)
			details.append(size)
			details.append(duration)
			details.append(muxrate)
			details.append(xmlName)
		else:
			with open(xmlName, 'a') as xml:
				xml.write(linefile)
				xml.write(linefilename)
				xml.write(linetype)
				xml.write(linesdig)
				xml.write(linefilesize)
				xml.write(lineduration)
				xml.write(lineavmux)
				xml.write(linefileclose)
		count += 1
	with open(xmlName, 'a') as x:
		x.write(line8)
		x.write(line9)
		x.write(line10)
		x.write(line11)
	return

def default( hash, bool, path, files, ext, alg, printbool=False, loc=None ):
	'''
	default is the default settings for the hash script, it will generate this file unless 
		otherwise specified; this will always put the file it generates in the same 
		location as the file it used to generate the hash
	Uses the following functions:		currentTime
	'''
	format = '%Y-%m-%d %H:%M:%S'
	time = currentTime(format)
	filename = []
	count = 0
	if (bool == False):
		filename.append(files)
	else:
		filename = files
	for file in filename:
		if (bool == True):
			extension = "." + ext[count]
			mdhash = hash[count]
			fullpath = path[count]
			algorithm = alg[count]
		else:
			extension = "." + ext
			mdhash = hash
			fullpath = path
			algorithm = alg
		line1 = '<hashFile>\n'
		line2 = '\t<objectExt>' + extension + '\n'
		line3 = '\t<fileInfo>\n'
		line4 = '\t\t<hashckt\tchecksumType="' + algorithm.upper() + '"></hashckt>\n'
		line5 = '\t\t<hashckv\tchecksumValue="' + mdhash + '"></hashckv>\n'
		line6 = '\t\t<hashfn\tfilename="' + file + '"></hashfn>\n'
		line7 = '\t\t<timeHashed>' + time + '</timeHashed>\n'
		line8 = '\t</fileInfo>\n'
		line9 = '</hashFile>\n'
		if (loc != None):
			fName = loc + '/' + file + '.xml'
		else:
			fName = fullpath + '/' + file + '.xml'
		if (printbool == True):
			details = []
			details.append(fullpath)
			details.append(file)
			details.append(extension)
			details.append(algorithm)
			details.append(fName)
			lines = []
			lines.append(line1)
			lines.append(line2)
			lines.append(line3)
			lines.append(line4)
			lines.append(line5)
			lines.append(line6)
			lines.append(line7)
			lines.append(line8)
			lines.append(line9)
			genExamplePrint('default', details, lines)
		else:
			f = os.open(fName, os.O_RDWR|os.O_CREAT)
			os.write(f, line1)
			os.close(f)

			with open(fName, 'a') as x:
				x.write(line2)
				x.write(line3)
				x.write(line4)
				x.write(line5)
				x.write(line6)
				x.write(line7)
				x.write(line8)
				x.write(line9)
				x.close()
		count += 1
	return
########################################################################################
###########			Do not edit or add anything below this point			 ###########
########################################################################################
if __name__=='__main__':
	main()