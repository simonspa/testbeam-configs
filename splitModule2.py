#!/usr/bin/python

import sys, getopt

def main(argv):
    filename = ''
    granularity = 0

    try:
        opts, args = getopt.getopt(argv,"hi:g:",["ifile=","granularity="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -g <granularity>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-g", "--granularity"):
            granularity = int(arg)

    with open(filename,'r') as f:
        lines = f.readlines()

    for o in range(len(lines)):
        if lines!=[]: 
            with open(f.name.split("_")[0] +"_C" + str(o) + '.dat','w') as NewFile:
                for i in range(granularity):
                    if lines!=[]:NewFile.write(lines.pop(0))
                

if __name__ == "__main__":
   main(sys.argv[1:])

