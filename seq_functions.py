#!/usr/bin/env python2
import re

# Turn a sequence file into a single string
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

# Turn a sequence string into a list of 3-letter codons
def sequence_to_codons(sequence_str):
    codon_list = [ sequence_str[index:index+3] \
        for index in range(0, len(sequence_str), 3) ]
    return codon_list

# Return a string which is the reversed complement of the input string
def rev_comp_sequence(sequence_str):
    # Dictionary to define complement bases
    complement = {'A': 'T',
                  'T': 'A',
                  'C': 'G',
                  'G': 'C'}
    # Turn sequence string into a list of bases
    bases = list(sequence_str)
    # Switch each base in the list with its complement
    bases = [complement[base] for base in bases]
    # Join the list back into a single string
    complement_str = ''.join(bases)
    # Return the reverse of that string
    return complement_str[::-1]

class Orf(object):
    def __init__(self, first_index, last_index, codon_list):
        self.first_index = first_index
        self.last_index = last_index
        self.codon_list = codon_list
    def indices(self):
        return (self.first_index, self.last_index)

def find_orfs(codon_list):
    start_codon = re.compile('ATG')
    stop_codons = re.compile('TAA|TAG|TGA')
    orf_list = []
    started = False
    for index, codon in enumerate(codon_list):
        if not started and start_codon.match(codon):
            started = True
            tmp_list = []
            first_index = index
            tmp_list.append(codon)
        elif started and not stop_codons.match(codon):
            tmp_list.append(codon)
        elif started and stop_codons.match(codon):
            started = False
            tmp_list.append(codon)
            last_index = index
            orf_list.append(Orf(first_index, last_index, tmp_list))
    return orf_list
