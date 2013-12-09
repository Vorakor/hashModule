=================================
|	HASH GENERATOR README	|
=================================
*************************
*	INSTALLATION	*
*************************
Because this is a python package there are a few things that need to happen before this command can be run.  Now, you should have been given the entire folder that the command was developed in, so the environment is mostly set up, you just need to add it to your $PATH and $PYTHONPATH variables.

Firstly you need to create a folder to contain the files in.  Please ensure that this file is in its permanent home, that is, somewhere it can live and never leave.  Once you have it created, get the code off of this repository (Note: this assumes that you have Python, at least 2.7, installed on the machine you are trying to run the command on):

MACOSX:
	On mac it is relatively simple to install this script, this is primarily because the script was originally designed and intended for use on the mac environment, however, it was developed to be more platform independent than anything else so it works well on all windows, linux, and mac.  Other reasons is that mac comes pre-installed with a lot of the things this script needs to run like Python 2.7.
	
	To install you simply need to go to each individual user's .bashrc file; this is located in each user's home directory, and it is a hidden file so you may want to open it from the command line using: 'open -a <yourTextEditorHere> <pathToHomeDir>/.bashrc'.
	
	Once you have it open, simply copy and paste the following lines into it:
	
if [ -f /Volumes/$SERVER/RESOURCE/UMS/hashModule/hashModule_macosx.sh ]; then
	source /Volumes/$SERVER/RESOURCE/UMS/hashModule/hashModule_macosx.sh
fi

	Now, you will need to change the path to the hashModule folder (the folder this readme is contained in), depending on wherever you put it, but that hashModule_macosx.sh script has all the information the Macintosh OS needs to run the script.  Easy right?  So just make sure the file path in the lines above points to the hashModule_macosx.sh file and you are done.

LINUX:
	On linux it is also relatively simple to install this script, this is primarily because the mac and linux environments are so similar.  And, like mac, linux comes pre-installed with a lot of the things this script needs to run like Python 2.7.
	
	To install you simply need to go to each individual user's .bashrc file; this is located in each user's home directory, and it is a hidden file so you may want to open it from the command line using: 'open -a <yourTextEditorHere> <pathToHomeDir>/.bashrc'.
	
	Once you have it open, simply copy and paste the following lines into it:
	
if [ -f /hashModule/hashModule_linux.sh ]; then
	source /hashModule/hashModule_linux.sh
fi

	Now, you will need to change the path to the hashModule folder (the folder this readme is contained in), depending on wherever you put it, but that hashModule_linux.sh script has all the information the Linux OS needs to run the script.  Easy right?  So just make sure the file path in the lines above points to the hashModule_linux.sh file and you are done.

WINDOWS:
	On windows you need to add the python path and some other things to your $PATH environment variable, however, this is slightly different depending on which version of the windows operating system you are using, please see below:
	
	---> Windows 7 & Windows Vista --->	
	To do this, on either Windows 7 or Vista, you need to go to 'My Computer', it is either on your desktop or in your start menu.
	
	Once you have that open you need to click 'System Properties' located just under the navigation bar near the top of the window, then on the left hand side of the window that opens you need to select the 'Advanced System Settings' from the list of options.
	
	This should open a window titled 'System Properties', select the 'Advanced' tab and look for a button near the bottom labeled 'Environment Variables...', click that button.
	
	---> Windows XP & Windows 2000 --->
	To do this, on Windows XP or 2000, you need to go to 'My Computer', it is located on your desktop or in your start menu.
	
	You need to right click on 'My Computer' and select 'Properties', this should open the 'System Properties' window and then you need to click on the 'Advanced' tab, and from there you need to click on the 'Environment Variables...' button.
			
	v--- From here on out it is the same for both operating systems. ---v
	
	Now, in the window that opens you need to go to the bottom half of it that is labeled 'System Variables', scroll down until you reach 'Path' and then select it and click the edit button.
	
	There are two things in here that you need to look for, first is the path to the python executable, it should look like this: 'C:\Python27;' if it isn't there then add it exactly as it is typed in this readme.
	
	The second thing you want, to add this time, is the path to the exe folder in the folder with this readme, for example, on the computer this was developed for windows on, the path the the exe folder was:
	
		C:\Users\<username>\Documents\Python\UMS\hashModule\exe

	You do not have to put it in the same place, but that was where it was put on that particular machine.  That is what you need to add to your path environment variable.
	
	After you have added both of those you need to create a new variable, so click the 'new...' button beneath the 'System Variables' half of the window, the title of the variables is 'PYTHONPATH' and the contents of that are as follows:
	
		C:\Python27\Lib;C:\Python27\DLLs;C:\Python27\Lib\lib-tk;

	And on the end of that is the path to this readme file, for example:

		C:\Users\<username>\Documents\Python\UMS\hashModule

	That was the path on the machine that was used to develop this script for windows, you will notice the only difference from above is that it doesn't direct you to the exe folder, that is because this script is already set up and has all the right scripts in the right places for this to work with just the limited instructions given here.  So please don't change anything in the file structure, Python is rather picky about it's module setup.
	
	Now, you only have one file to edit as soon as all of that is done, and that is the .bat file, this file should be named genhash.bat and it should be inside of the exe directory, go ahead and open it up in your favorite text editor, the only thing you need to change in here is the path to the hash_pc.py script, now, currently relative paths do not work, but absolute paths do, so enter in the full path to the file; once you change that you can enter in 'genhash' at the command prompt and it will run the script!

*****************************************
*	SETTING UP CUSTOM OUTPUTS	*
*****************************************
	The first thing you want to do is look inside of the scripts folder in the installation directory for this script, inside of that folder you should find a file named genhashfile.py, you need to open this for editing.
	Inside this file there are four functions that you need to change.  WARNING: Do not change anything else in this file and do not change any other file, these are set up so that the only file you have to edit is the genhashfile and in that you only need to edit a few things.

	---------------------------------
	|	First Step: Main()	|
	---------------------------------
		The first function you need to change is the main() at the very top of the file, in this you simply need to add your new specifier, which will be the name of your output function, to add this to the list simply put your cursor in front of the 'else:' that is below the 'if(specifier == 'diva'):' or 'elif(specifier == '<whateverYouHaveAddedAlready>'):' and hit enter to put the 'else:' on a new line.
		Now, also note, and this is VERY important, python actually requires whitespace to work, so when you move the 'else:' to a new line make sure it is EXACTLY as far out as the 'if(specifier == 'diva'):' that you see above it.
		So here's what the file should look like when you open it:

		if(specifier == 'diva'):
			if (loc != None):
				diva(hash, bool, path, filename, ext, alg, printbool, loc)
			else:
				diva(hash, bool, path, filename, ext, alg, printbool)
		else:
			if (loc != None):
				default(hash, bool, path, filename, ext, alg, printbool, loc)
			else:
				default(hash, bool, path, filename, ext, alg, printbool)

		Here is what it should look like after you have followed instructions precisely:

		if(specifier == 'diva'):
			if (loc != None):
				diva(hash, bool, path, filename, ext, alg, printbool, loc)
			else:
				diva(hash, bool, path, filename, ext, alg, printbool)
		<<<See! There's a space here now!>>>
		else:
			if (loc != None):
				default(hash, bool, path, filename, ext, alg, printbool, loc)
			else:
				default(hash, bool, path, filename, ext, alg, printbool)

		Now you need to add the following in the space that you created:

		elif(specifier == '<whateverYourNewFunctionNameIs>'):
			if (loc != None):
				<whateverYourNewFunctionNameIs>(hash, bool, path, filename, ext, alg, printbool, loc)
			else:
				<whateverYourNewFunctionNameIs>(hash, bool, path, filename, ext, alg, printbool)

		Remember not to touch anything else in that function, do not delete anything, just add your new output formats, and be sure to include all the parameters listed above, EVEN if you don't need to use all of them.

	-----------------------------------------
	|	Second Step: GenExamplePrint()	|
	-----------------------------------------
		Next function you need to edit is genExamplePrint, in this function you need to add your own special message for your function output, this function and the one beneath it will allow you to see a sample printout of your output format in the main execution script, all you need to do to this script is find the 'else:' or 'elif(spec == '<whateverYouHaveAddedAlready>'):' and put it down a line, then add the following:

		elif (spec == '<whateverYourNewFunctionNameIs>'):
			msg = 'Whatever text you would like displayed when a sample printout of this output format is generated, you can probably follow the same format of the other messages and just do "This is what the <whateverYourNewFunctionNameIs> file will look like when it is created and printed:\n" if you have nothing special to put, just make sure you add the newline character to the end:\n'

	-----------------------------------------
	|	Third Step: ListPrintFunc()	|
	-----------------------------------------
		The next function to edit is the easiest, the function is called: 'listPrintFunc()', the only thing to do with this is to just add 'list.append('<whateverYourNewFunctionNameIs>')' to the list of 'list.append' stuff, with this one it doesn't matter if you put it before 'list.append('diva')', after 'list.append('default')', or anywhere in between, all this function does is provide a list of specifiers to the core code.  So the order doesn't matter in this function

	-------------------------------------------------
	|	Final Step: Custom Output Function	|
	-------------------------------------------------
		Now, last but not least, is the actual output function itself.  For this I would recommend copying one of the functions that is already there and using it as a template, because really the only parts of the output formats you should be worrying about changing is the 'line' stuff, the name of the file, and the printbool stuff.
		So that is to say all the stuff as follows:
		---- LINE ----
		'Line':

			line1 = '<DIVAObjectDefinition>\n'
			line2 = '\t<objectName>' + objName + '</objectName>\n'
			line3 = '\t<fileList>\n'
			line4 = '\t\t<file\tchecksumType="' + algorithm.upper() + '"\n'
			line5 = '\t\t\tchecksumValue="' + mdhash + '">\n'
			line6 = '\t\t' + objName + '\n'
			line7 = '\t\t</file>\n'
			line8 = '\t</fileList>\n'
			line9 = '</DIVAObjectDefinition>\n'

		And this too for the 'line' stuff:

			xml.write(line2)
			xml.write(line3)
			xml.write(line4)
			xml.write(line5)
			xml.write(line6)
			xml.write(line7)
			xml.write(line8)
			xml.write(line9)
		This part of the function is what determines what your output file will look like, so this is probably the most important thing to change, if you need to add lines then make sure that you add the new line and number to the 'xml.write(line)' part of the function.

		---- NAME ----
		Name of file:

			objName = file + extension

		This will change the name of the file that is generated.  And this too for the name:

			if (loc != None):
				xmlName = loc + '/' + objName + '.xml'
			else:
				xmlName = fullpath + '/' + objName + '.xml'
		This will allow you to create a file with a different extension, both the 'diva' and 'default' specifiers output an xml file, however, you may wish to output something else, and that is totally fine as well.

		---- PRINTBOOL ----
		'Printbool' stuff:

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
				lines.append(line8)
				lines.append(line9)
				genExamplePrint('<whateverYourNewFunctionNameIs>', details, lines)
		This particular part of your function is what determines the sample printout of your output, so this one of all of them needs to be pretty flushed out, all you really need to do is put all of your lines from above into an array and your details (hash, path, name, algorithm, extension, file name), into an array and pass all of that with the specifier to the genExamplePrint function.

	And after you have changed all of that, then your new output format will show up as an option in the script!  So just make sure that this is the only file that you change.

*****************
*	NOTES	*
*****************
Usage:
genhashm [-h] [-q] [-f FILES [FILES ...]] [-s SPECIFIER] [-a ALGORITHM]
                [-p] [-l LOCATION]

This command is meant to generate a hash for the given files, it will also
generate an xml file with the information taken from the file and it will
place the xml file in the same place as the file that it used to generate the
hash

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           This allows this command to be run in silent mode
                        which means no prompts
  -f FILES [FILES ...], --files FILES [FILES ...]
                        This allows us to specify a list of files to generate
                        hashes for without the prompt asking for them, this
                        flag is mandatory in silent mode
  -s SPECIFIER, --specifier SPECIFIER
                        This allows you to specify which output file you want,
                        depending on the settings you may also set some
                        parameters automatically
  -a ALGORITHM, --algorithm ALGORITHM
                        This lets you select a different algorithm than the
                        default md5
  -p, --printout        This should allow a print out of available specifiers
                        even in quiet mode, however, this flag cannot be used
                        with any other flag except the -q
  -l LOCATION, --location LOCATION
                        This allows you to specify an alternate location for
                        the output files, default will always be in the same
                        location as the source files, the quiet mode only
                        allows for one location for all the output files
