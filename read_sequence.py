#!/usr/bin/env python2
from sys import argv

script, filename = argv

def file_to_string(filename):
	sequence_file = open(filename, 'r')

	sequence_lines = sequence_file.readlines()

	sequence_lines.pop(0)
	sequence_lines = [i.strip('\r\n') for i in sequence_lines]

	sequence_str = ''.join(map(str, sequence_lines))

	return sequence_str
	
print file_to_string(filename)
