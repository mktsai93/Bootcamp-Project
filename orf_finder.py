#!/usr/bin/env python2
from sys import argv
from seq_functions import *
import re

script, filename = argv

forward_sequence = file_to_sequence(filename)
reverse_complement = rev_comp_sequence(forward_sequence)

for1_orfs = find_orfs(sequence_to_codons(forward_sequence))
for2_orfs = find_orfs(sequence_to_codons(forward_sequence[1:]))
for3_orfs = find_orfs(sequence_to_codons(forward_sequence[2:]))

rev1_orfs = find_orfs(sequence_to_codons(reverse_complement))
rev2_orfs = find_orfs(sequence_to_codons(reverse_complement[1:]))
rev3_orfs = find_orfs(sequence_to_codons(reverse_complement[2:]))

# make a big list of lists
all_frames_orfs = [for1_orfs, for2_orfs, for3_orfs,
                   rev1_orfs, rev2_orfs, rev3_orfs]

for frame in all_frames_orfs:
    for orf in frame:
        print orf.indices()
