from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

data = open(from_file)
indata = data.read()

print "The input file is %d bytes long " % len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue"
raw_input()

output=open(to_file, 'w')
output.write(indata)

print "Alright, all done"
output.close
data.close
