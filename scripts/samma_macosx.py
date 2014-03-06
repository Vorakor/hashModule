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
from mediaInfoWrapper.scripts import mediaInfoWrapper as miWrap

# This is no longer a standalone function, it is simply additional functions to handle samma output
class SammaObject:
	'This is for the Samma system in particular'
	def __init__(self):
		self.spec = 'samma'
		self.printbool = False
		self.files = []
		self.filenames = []
		self.ext = []
		self.mdhash = []
		self.shahash = []
		self.path = []
		self.filesize = []
		self.filetype = []
		self.duration = []
		self.muxrate = []
		self.name = ''
		self.location = ''
	
	def __add__(self, multiObj):
		self.files.append(multiObj.file)
		self.filenames.append(multiObj.filename)
		self.ext.append(multiObj.extension)
		self.mdhash.append(multiObj.mdhash)
		self.shahash.append(multiObj.shahash)
		self.path.append(multiObj.path)
		self.filesize.append(multiObj.filesize)
		self.filetype.append(multiObj.filetype)
		self.duration.append(multiObj.duration)
		self.muxrate.append(multiObj.muxrate)
	
	def setLocation(self, multiObj):
		self.location = multiObj.loc
	
	def setName(self, name):
		self.name = name
	
	def setPrintBool(self, printbool):
		if isinstance(printbool, bool):
			self.printbool = printbool
		else:
			self.printbool = False

class MultiFileObject( SammaObject ):
	'''This is a hash object for the samma system, this gets hashes and other information per file 
	of the multi-file object'''
	def __init__(self, file):
		self.spec = 'samma'
		self.file = file
		self.algorithms = ['md5', 'sha1']
		self.mdhash = ''
		self.shahash = ''
		self.extension = ''
		self.filename = ''
		self.path = ''
		self.filesize = ''
		self.filetype = ''
		self.duration = ''
		self.muxrate = ''
		__addPathDetails()
		__addSammaDetails()
		__getHashes()
	
	def __addPathDetails(self):
		filePath, temp = os.path.split(self.file)
		if 'imx' in temp:
			tempName, tempExt = os.path.splitext(temp)
			fileName, anOtherTempExt = os.path.splitext(tempName)
			fileExtension = anOtherTempExt + tempExt
		else:
			fileName, fileExtension = os.path.splitext(temp)
		self.extension = fileExtension
		self.filename = fileName
		self.path = filePath
	
	def __addSammaDetails(self):
		#mIWrap( quiet, file, all=None, category=None, detailRequests=None )
		detail_requests = ['General;FileExtension', 'General;FileSize', 'General;Duration', 'General;OverallBitRate']
		generalDict, vid, aud, text, image, menu = miWrap(False, self.file, False, 'General', detail_requests)
		for k, v in generalDict.iteritems():
			if k == 'FileExtension':
				self.filetype = v
			elif k == 'FileSize':
				self.filesize = v
			elif k == 'Duration':
				self.duration = v
			elif k == 'OverallBitRate':
				self.muxrate = v
			else:
				raise ghOps.ArgumentException('Error: failed here!  Didn\'t get detail requests __addSammaDetails()')
	
	def __getHashes(self):
		out = subprocess.Popen(['openssl', self.algorithms[0], self.file], stdout=subprocess.PIPE).communicate()[0]
		outSplit = out.split('=')
		maxIndex = len(outSplit) - 1
		apitem = outSplit[maxIndex].lstrip()
		self.mdhash = apitem.replace('\n', '')
		out = subprocess.Popen(['shasum', '-a', '1', self.file], stdout=subprocess.PIPE).communicate()[0]
		outSplit = out.split(' ')
		apitem = outSplit[0].lstrip()
		self.shahash = apitem.rstrip()

if __name__=='__main__':
	main()