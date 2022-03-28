#!/usr/bin/python3
import difflib
import sys

try:
    textfile1=sys.argv[1]
    textfile2=sys.argv[2]
except Exception as e:
    print('Error:' + e)
    print('Usage: xx.py filename1 filename2')
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text=fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except Exception as e:
        print('Read file Error: %s' % e)
        sys.exit()

text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print (d.make_file(text1_lines, text2_lines))