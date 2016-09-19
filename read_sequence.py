#!/usr/bin/env python2
from sys import argv

script, filename = argv

def file_to_sequence(filename):
	sequence_file = open(filename, 'r')
	sequence_lines = sequence_file.readlines()
	sequence_file.close()
	
	# Remove the header
	sequence_lines.pop(0)
	# Remove line endings
	sequence_lines = [i.strip('\r\n') for i in sequence_lines]
	# Concatenate lines into a single string
	sequence_str = ''.join(map(str, sequence_lines))

	return sequence_str
	
def sequence_to_codons(sequence_str):
	codon_list = [ sequence_str[index:index+3] for index in range(0, len(sequence_str), 3) ]
	return codon_list
	

codons = sequence_to_codons(file_to_sequence(filename))
print codons
