# genlog.py
#
# Sum up the bytes transferred in an Apache server log using
# generator expressions

wwwlog     = open("access-log")

bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog)
print type(bytecolumn)


byte = [line.rsplit(None,1)[1] for line in wwwlog]
print type(byte)
bytes      = (int(x) for x in bytecolumn if x != '-')
print bytes
print "Total", sum(bytes)
