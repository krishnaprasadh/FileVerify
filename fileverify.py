import os
print "File Verify Version 1.0 - Krishnaprasadh.R\n"
for filename in os.listdir(os.getcwd()):
	name,separator,extension = filename.partition('.')
	#print(filename)
	i=1
	string = ""
	bytestoread=2
	file=open(filename,'r')
	while i<=bytestoread:
		str = file.read(1)
		hexvalue = hex(ord(str))
       	        bytevalue = format(ord(str), "x")
       		#print bytevalue
		tocaps=bytevalue.upper()
        	string=string+tocaps
		#print string
        	i=i+1
		if((extension == "exe" and string == "4D5A") or (extension == "jpg" and string == "FFD8") or (extension == "jpeg" and string == "FFD8")):
			result="FileMatch[OK]"
		#if((extension != "exe") or (extension != "jpg") or (extension != "jpeg")):
			#result="ExtensionsNotFound[??]"
		else:
			result="FileMisMatch[!!]"
	print(filename+" ---> "+result)
