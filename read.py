import os
filename="pscp.exe"
name,separator,extension = filename.partition('.')
file=open("pscp.exe", 'r')
i=1
var = ""
while i<=2:
	str = file.read(1)
	hexvalue = hex(ord(str))
	bytevalue = format(ord(str), "x")
	#print bytevalue
	tocaps=bytevalue.upper()
	var=var+tocaps
	i=i+1
print var
i=1
