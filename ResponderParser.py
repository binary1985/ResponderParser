#!/usr/bin/python

import sys

users={}

if len(sys.argv) < 3:
        print "Usage is: " +sys.argv[0]+" <input responder log> <output user file>"
        sys.exit()

with open(sys.argv[1]) as f:
        for line in f:
                if 'complete hash' in line:
                        if line.split(":")[3] not in users:
                                users[line.split(":")[3]] = line

userfile=open(sys.argv[2],"w")
for value in users.values():
        if '$' not in value:
                userfile.write(value)
