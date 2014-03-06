#! /usr/bin/python

import locale
import os,sys,inspect
import time, re
import datetime, socket
import argparse
import subprocess
import commands

from config import *
import ops as ghOps

def main( hashObject ):
	specifier = hashObject.spec
	if(specifier == 'diva'):
		diva(hashObject)
	elif(specifier == 'samma'):
		samma(hashObject)
	else:
		default(hashObject)
	return

class Sample:
	'This is for the creation of a sample object that can later be printed out'
	def __init__(self, specification):
		self.spec = specification
		self.summary = ''
		self.msg = 'This is what the ' + self.spec + ' file will look like when it is created and printed:\n'
	
	def addBasicDetails(self, outDir, fileName, hash, xmlName):
		self.outputDir = outDir
		self.fileName = fileName
		self.hash = hash
		self.xmlName = xmlName
	
	def addSammaDetails(self, mdhash, fileType, fileSize, duration, muxRate):
		self.mdhash = mdhash
		self.fileType = fileType
		self.size = fileSize
		self.duration = duration
		self.muxrate = muxRate

	def detPrintArry(self, objectName=None, algorithm=None, fullFileName=None, count=0, time=None, extension=None):
		self.arry = []
		if self.spec == 'diva':
			self.arry.append('<DIVAObjectDefinition>\n')
			self.arry.append('\t<objectName>' + objectName + '</objectName>\n')
			self.arry.append('\t<fileList>\n')
			self.arry.append('\t\t<file\tchecksumType="' + algorithm.upper() + '"\n')
			self.arry.append('\t\t\tchecksumValue="' + self.hash + '">'+ objectName + '</file>\n')
			self.arry.append('\t</fileList>\n')
			self.arry.append('</DIVAObjectDefinition>\n')
		elif self.spec == 'samma':
			self.arry.append('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
			self.arry.append('<SammaSolo>\n')
			self.arry.append('\t<Settings>\n')
			self.arry.append('\t\t<Details>\n')
			self.arry.append('\t\t\t<GeneratedBy>\n')
			self.arry.append('\t\t\t\t<ScriptName>Genhash Script</ScriptName>\n')
			self.arry.append('\t\t\t\t<ScriptVersion>' + GENHASHVERSION + '</ScriptVersion>\n')
			self.arry.append('\t\t\t</GeneratedBy>\n')
			self.arry.append('\t\t</Details>\n')
			self.arry.append('\t</Settings>\n')
			self.arry.append('\t<EncodedFiles>\n')
			self.arry.append('\t\t<File' + str(count) + '>\n')
			self.arry.append('\t\t\t<Filename>' + fullFileName + '</Filename>\n')
			self.arry.append('\t\t\t<Type>' + self.fileType + '</Type>\n')
			self.arry.append('\t\t\t<ShaDigest>' + self.hash + '</ShaDigest>\n')
			self.arry.append('\t\t\t<FileSize>' + self.size + '</FileSize>\n')
			self.arry.append('\t\t\t<Duration>' + self.duration + '</Duration>\n')
			self.arry.append('\t\t\t<AverageMuxRate>' + self.muxrate + '</AverageMuxRate>\n')
			self.arry.append('\t\t\t<MDDigest>' + self.mdhash + '</MDDigest>\n')
			self.arry.append('\t\t<File' + str(count) + '>\n')
			self.arry.append('\t</EncodedFiles>\n')
			self.arry.append('\t<Metadata>\n')
			self.arry.append('\t</Metadata>\n')
			self.arry.append('</SammaSolo>\n')
		else:
			self.arry.append('<hashFile>\n')
			self.arry.append('\t<objectExt>' + extension + '\n')
			self.arry.append('\t<fileInfo>\n')
			self.arry.append('\t\t<hashckt\tchecksumType="' + algorithm.upper() + '"></hashckt>\n')
			self.arry.append('\t\t<hashckv\tchecksumValue="' + self.hash + '"></hashckv>\n')
			self.arry.append('\t\t<hashfn\tfilename="' + self.fileName + '"></hashfn>\n')
			self.arry.append('\t\t<timeHashed>' + time + '</timeHashed>\n')
			self.arry.append('\t</fileInfo>\n')
			self.arry.append('</hashFile>\n')

	def printStatement(self):
		print self.msg
		for i in self.arry:
			i = i.replace('\n', '')
			print i
		self.summary = '\nSummary:\n\tOutput Dir: \t\t' + self.outputDir
		self.summary += '\n\tExample File Name: \t' + self.fileName
		self.summary += '\n\tFile Hash: \t\t' + self.hash
		self.summary += '\n\tSample Xml Name: \t' + self.xmlName
		print self.summary
	
	def printSammaStatement(self):
		print self.msg
		for i in self.arry:
			i = i.replace('\n', '')
			print i
		self.summary = '\nSummary:\n\tOutput Dir: \t\t' + self.outputDir
		self.summary += '\n\tExample File Name: \t' + self.fileName
		self.summary += '\n\tFile Type: \t\t' + self.fileType
		self.summary += '\n\tFile Hash: \t\t' + self.hash
		self.summary += '\n\tFile Size: \t\t' + self.size
		self.summary += '\n\tFile Duration: \t\t' + self.duration
		self.summary += '\n\tFile Mux Rate: \t\t' + self.muxrate
		self.summary += '\n\tSample Xml Name: \t' + self.xmlName
		print self.summary

def genExamplePrint( sampleObject ):
	spec = sampleObject.spec
	if (spec == 'diva'):
		sampleObject.printStatement()
	elif (spec == 'samma'):
		sampleObject.printSammaStatement()
	else:
		sampleObject.printStatement()
	return

def listPrintFunc():
	glist = []
	glist.append('default')
	glist.append('diva')
	glist.append('samma')
	return glist

def diva( object ):
	'''
	diva generates the hash xml file necessary for transferring files to diva, this 
		function places the file it generates in the same location as the file it 
		got the hash from, unless the user has specified otherwise
	'''
	objFile = object.filename
	ext = object.extension
	objHash = object.hash
	path = object.path
	alg = object.algorithm
	printbool = object.printbool
	objName = objFile + ext
	line1 = '<DIVAObjectDefinition>\n'
	line2 = '\t<objectName>' + objName + '</objectName>\n'
	line3 = '\t<fileList>\n'
	line4 = '\t\t<file\tchecksumType="' + alg.upper() + '"\n'
	line5 = '\t\t\tchecksumValue="' + objHash + '">'+ objName + '</file>\n'
	line6 = '\t</fileList>\n'
	line7 = '</DIVAObjectDefinition>\n'
	if hasattr(object, 'location'):
		loc = object.location
		objName += '.xml'
		xmlName = os.path.join(loc, objName)
	else:
		objName += '.xml'
		xmlName = os.path.join(path, objName)
	if (printbool == True):
		divaSample = Sample('diva')
		divaSample.addBasicDetails(path, objFile, objHash, xmlName)
		divaSample.detPrintArry(objName, alg)
		genExamplePrint(divaSample)
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
	return

def samma( object ):
	'''
	samma generates the hash xml file for multifile objects, it is necessary for 
		transferring files to diva, this function places the file it generates in 
		the same location as the file it got the hash from
	'''
	printbool = object.printbool
	files = object.files
	ext = object.ext
	mdhash = object.mdhash
	shahash = object.shahash
	path = object.path
	filesize = object.filesize
	filetype = object.filetype
	duration = object.duration
	muxrate = object.muxrate
	objName = object.name

	count = 0
	titleLine = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
	line1 = '<SammaSolo>\n'
	line2 = '\t<Settings>\n'
	line3 = '\t\t<Details>\n'
	line4 = '\t\t\t<GeneratedBy>\n'
	line4_2 = '\t\t\t\t<ScriptName>Genhash Script</ScriptName>\n'
	line4_5 = '\t\t\t\t<ScriptVersion>' + GENHASHVERSION + '</ScriptVersion>\n'
	line4_9 = '\t\t\t</GeneratedBy>\n'
	line5 = '\t\t</Details>\n'
	line6 = '\t</Settings>\n'
	line7 = '\t<EncodedFiles>\n'
	line8 = '\t</EncodedFiles>\n'
	line9 = '\t<Metadata>\n'
	line10 = '\t</Metadata>\n'
	line11 = '</SammaSolo>\n'

	xmlName = ''
	if hasattr(object, 'location'):
		loc = object.location
		objName += '.xml'
		xmlName = os.path.join(loc, objName)
	else:
		objName += '.xml'
		xmlName = os.path.join(path, objName)
	if (printbool == False):
		f = os.open(xmlName, os.O_RDWR|os.O_CREAT)
		os.write(f, titleLine)
		os.write(f, line1)
		os.write(f, line2)
		os.write(f, line3)
		os.write(f, line4)
		os.write(f, line5)
		os.write(f, line6)
		os.write(f, line7)
		os.close(f)

	for f in files:
		extension = '.' + ext[count]
		mhash = mdhash[count]
		shash = shahash[count]
		fullpath = path[count]
		size = filesize[count]
		objType  = filetype[count]
		dur = duration[count]
		muxr = muxrate[count]
		fullFileName = fullpath + f + extension

		linefile = '\t\t<File' + str(count) + '>\n'
		linefilename = '\t\t\t<Filename>' + fullFileName + '</Filename>\n'
		linetype = '\t\t\t<Type>' + objType + '</Type>\n'
		linesdig = '\t\t\t<ShaDigest>' + shash + '</ShaDigest>\n'
		linefilesize = '\t\t\t<FileSize>' + size + '</FileSize>\n'
		lineduration = '\t\t\t<Duration>' + dur + '</Duration>\n'
		lineavmux = '\t\t\t<AverageMuxRate>' + muxr + '</AverageMuxRate>\n'
		linefileclose = '\t\t<File' + str(count) + '>\n'

		if (printbool == True):
			sammaSample = Sample('samma')
			sammaSample.addBasicDetails(fullpath, f, shash, xmlName)
			sammaSample.addSammaDetails(mhash, objType, size, duration, muxrate)
			sammaSample.detPrintArry(None, None, fullFileName, count)
			genExamplePrint(sammaSample)
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

def default( object ):
	'''
	default is the default settings for the hash script, it will generate this file unless 
		otherwise specified; this will always put the file it generates in the same 
		location as the file it used to generate the hash
	'''
	format = '%Y-%m-%d %H:%M:%S'
	time = ghOps.currentTime(format)
	objFile = object.filename
	extension = object.extension
	objHash = object.hash
	path = object.path
	alg = object.algorithm
	printbool = object.printbool
	line1 = '<hashFile>\n'
	line2 = '\t<objectExt>' + extension + '\n'
	line3 = '\t<fileInfo>\n'
	line4 = '\t\t<hashckt\tchecksumType="' + alg.upper() + '"></hashckt>\n'
	line5 = '\t\t<hashckv\tchecksumValue="' + objHash + '"></hashckv>\n'
	line6 = '\t\t<hashfn\tfilename="' + objFile + '"></hashfn>\n'
	line7 = '\t\t<timeHashed>' + time + '</timeHashed>\n'
	line8 = '\t</fileInfo>\n'
	line9 = '</hashFile>\n'
	if hasattr(object, 'location'):
		loc = object.location
		objName += '.xml'
		xmlName = os.path.join(loc, objName)
	else:
		objName += '.xml'
		xmlName = os.path.join(path, objName)
	if (printbool == True):
		defaultSample = Sample('default')
		defaultSample.addBasicDetails(path, objFile, objHash, xmlName)
		defaultSample.detPrintArry(None, alg, None, 0, time, extension)
		genExamplePrint(defaultSample)
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
	return

if __name__=='__main__':
	main()