#!/usr/bin/env python2
from sys import argv
from seq_functions import *

script, filename = argv

full_sequence = file_to_sequence(filename)

forward_frame1 = sequence_to_codons(full_sequence)
forward_frame2 = sequence_to_codons(full_sequence[1:])
forward_frame3 = sequence_to_codons(full_sequence[3:])

