#!/usr/bin/env python2
from sys import argv
from seq_functions import *
import re

script, filename = argv

forward_sequence = file_to_sequence(filename)
reverse_complement = rev_comp_sequence(forward_sequence)

forward_frame1 = sequence_to_codons(forward_sequence)
forward_frame2 = sequence_to_codons(forward_sequence[1:])
forward_frame3 = sequence_to_codons(forward_sequence[2:])

reverse_frame1 = sequence_to_codons(reverse_complement)
reverse_frame2 = sequence_to_codons(reverse_complement[1:])
reverse_frame2 = sequence_to_codons(reverse_complement[2:])

rev1_orfs = find_orfs(reverse_frame1)
for orf in rev1_orfs:
    print orf.indices()
