#! /usr/bin/python

import locale
import os,sys,inspect
import time, re
import datetime, socket
import argparse
import subprocess
import commands

import ops as ghOps

SERVER = ghOps.getServer()

GENHASHVERSION = '2.0.0'

GENHASHMEXE = '/Volumes/' + SERVER + '/RESOURCE/standalone/hashModule/exe/genhashm'

GENHASHLEXE = '/Volumes/Congo/RESOURCE/standalone/hashModule/exe/genhashl'

GENHASHWINEXE = '\\RESOURCE\\standalone\\hashModule\\exe\\genhash'