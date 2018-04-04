import os
print "--------------------------------------------"
print "File Verify Version 1.0 - Krishnaprasadh.R"
print "--------------------------------------------"
extensions=('exe','jpg','jpeg')
signatures=('4D5A','FFD8','FFD8')
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
		if(extension == extensions[0] and string == signatures[0]):
			result="FileMatch[OK]"
		elif(extension == extensions[1] and string == signatures[1]):
			result="FileMatch[OK]"
		elif(extension == extensions[2] and string == signatures[2]):
			result="FileMatch[OK]"
		else:
			result="FileMisMatch[!!]"
	print(filename+" ---> "+result)
