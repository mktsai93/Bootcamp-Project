#!/usr/bin/env python2
from sys import argv
from seq_functions import *

script, filename = argv

forward_sequence = file_to_sequence(filename)
reverse_complement = rev_comp_sequence(forward_sequence)

class ReadingFrame(object):

    def __init__(self, input_seq):
        self.orfs = find_orfs(sequence_to_codons(input_seq))

for1_orfs = ReadingFrame(forward_sequence)
# make a big list of lists
#all_frames_orfs = [for1_orfs, for2_orfs, for3_orfs,
#                   rev1_orfs, rev2_orfs, rev3_orfs]

for orf in for1_orfs.orfs:
    print 'ORF at ' + str(orf.indices())
    print 'GC content: ' + str(orf.gc_content())
    print 'Translation:\n' + orf.translate_orf()
