#! /usr/bin/python

import os,sys,inspect
import time
import datetime
import argparse
import subprocess

from scripts import genhashfile as create
from scripts import hash_macosx as hashM
from scripts import hash_linux as hashL
from scripts import hash_pc as hashP
from scripts.samma import samma_macosx as samma

def main():
	msg = 'Please enter a media file:\n'
	file = hashM.getInput(msg)
	file = file.rstrip()
	fileName = samma.getMediaInfoOutput(file)
	return

if __name__=='__main__':
	main()