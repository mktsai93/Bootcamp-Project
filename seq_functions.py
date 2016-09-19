#!/usr/bin/env python2

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
    codon_list = [ sequence_str[index:index+3] \
        for index in range(0, len(sequence_str), 3) ]
    return codon_list

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
