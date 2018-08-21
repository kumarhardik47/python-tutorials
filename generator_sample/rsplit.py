import os

wwwlog     = open("access-log")
for line in wwwlog:
	print line
	bytecolumn = line.rsplit(None,1)[1]
	print bytecolumn

#bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
