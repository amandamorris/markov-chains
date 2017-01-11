#from markov.py import *
import re


def open_file(filename):
    script = open(filename)

    speech_only = []
    for line in script:
        #print line
        line = line.strip()
        if line:
            if line[0] != "[" and line[0] != "(":
                speech_only.append(line)
    for line in speech_only:
        m = re.search('\((.*?)\)', line)
        if m:
            print m.group(0)
    #print speech_only

open_file("friends.txt")

# \((.*?)\)