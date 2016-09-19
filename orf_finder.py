#!/usr/bin/env python2
from sys import argv
from seq_functions import *

script, filename = argv

full_sequence = file_to_sequence(filename)
reverse_complement = rev_comp_sequence(full_sequence)

forward_frame1 = sequence_to_codons(full_sequence)
forward_frame2 = sequence_to_codons(full_sequence[1:])
forward_frame3 = sequence_to_codons(full_sequence[3:])

reverse_frame1 = sequence_to_codons(reverse_complement)
reverse_frame2 = sequence_to_codons(reverse_complement[1:])
reverse_frame2 = sequence_to_codons(reverse_complement[2:])

print "forward frame 1:"
print forward_frame1
print "reverse frame 1:"
print reverse_frame1
