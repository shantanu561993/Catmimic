#!/usr/bin/python2.7
from optparse import OptionParser
from sys import argv
parser=OptionParser()
usage = "usage: %prog [options] arg1 "
parser = OptionParser(usage=usage)
parser.add_option("-f","--file",dest="filename",help="File which you want to print",metavar="FILE")
(options, args) = parser.parse_args()
if len(argv)==1:
    parser.print_help()

def Cat(filename):
    f=open(filename,'rU')
    for line in f:
        print line,
    
if __name__ == '__main__':
    Cat(options.filename)

