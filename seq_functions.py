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

# Translate a list of codons into a string of amino acids
def translate(codon_list):
    codon_to_aa = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
                   'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
                   'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
                   'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'TGA': '*',
                   'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
                   'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                   'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                   'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                   'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
                   'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                   'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                   'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                   'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
                   'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                   'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                   'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    aa_list = [codon_to_aa[codon] for codon in codon_list]
    return ''.join(aa_list)


# Class to hold and return information about individual ORFs
class Orf(object):

    def __init__(self, first_index, last_index, codon_list):
        self.first_index = first_index
        self.last_index = last_index
        self.codon_list = codon_list
        self.sequence_str = ''.join(self.codon_list)

    def indices(self):
        return (self.first_index, self.last_index)

    def gc_content(self):
        self.count_g = self.sequence_str.count('G')
        self.count_c = self.sequence_str.count('C')
        self.seq_length = len(self.sequence_str)
        return (float(self.count_g) + \
                float(self.count_c)) / \
                float(self.seq_length)

    def codon_bias(self):
        pass

    def translate_orf(self):
        self.aa_seq = translate(self.codon_list)
        return self.aa_seq

# Find ORFs in a list of codons and turn them into a list of Orf objects
def find_orfs(codon_list):
    # Regex to identify start and stop codons
    start_codon = re.compile('ATG')
    stop_codons = re.compile('TAA|TAG|TGA')
    orf_list = []
    # The 'started' variable is a switch to identify when the functions
    # is reading through an ORF
    started = False
    for index, codon in enumerate(codon_list):
        # When a start codon is found, start recording codons
        if not started and start_codon.match(codon):
            started = True
            tmp_list = []
            first_index = index
            tmp_list.append(codon)
        # Record all the codons after the start codon
        elif started and not stop_codons.match(codon):
            tmp_list.append(codon)
        # When a stop codon is found, stop recording codons,
        # build an Orf object, and add it to the list.
        elif started and stop_codons.match(codon):
            started = False
            tmp_list.append(codon)
            last_index = index
            orf_list.append(Orf(first_index, last_index, tmp_list))
    return orf_list
