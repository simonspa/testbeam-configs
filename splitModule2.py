#!/usr/bin/python
#python splitModule2.py -i D4028/dacParameters_D4028_ia25-trim40-2016-04.dat -g 19
#python splitModule2.py -i D4028/trimParameters_D4028_ia25-trim40-2016-04.dat -g 4160

import sys, getopt

def main(argv):
    filename = ''
    lines_per_file = 0

    try:
        opts, args = getopt.getopt(argv,"hi:g:",["ifile=","lines_per_file="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -g <lines_per_file>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-g", "--lines_per_file"):
            lines_per_file = int(arg)

    with open(filename,'r') as f:
        lines = f.readlines()

    for o in range(len(lines)):
        if lines!=[]: 
            with open(f.name.split("_")[0] +"_C" + str(o) + '.dat','w') as NewFile:
                for i in range(lines_per_file):
                    if lines!=[]:NewFile.write(lines.pop(0))
                

if __name__ == "__main__":
   main(sys.argv[1:])

