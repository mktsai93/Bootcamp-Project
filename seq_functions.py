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


def find_orfs(codon_list):
    start_codon = re.compile('ATG')
    stop_codons = re.compile('TAA|TAG|TGA')
    started = False
    for index, codon in enumerate(codon_list):
        if not started and start_codon.match(codon):
            started = True
            print index, codon, 'start'
        elif started and not stop_codons.match(codon):
            print index, codon
        elif started and stop_codons.match(codon):
            started = False
            print index, codon, 'stop'
