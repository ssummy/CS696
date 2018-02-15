"""
Homework 01
DO NOT RENAME THIS FILE OR ANY DEFINITIONS!
Place this file in your github repo inside of a folder titled "Homework".
"""


# String Functions
def fast_complement(dna):
    """
    Uses a dictionary to convert a DNA sequence into the complement strand.  C <--> G,  T <--> A
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    comps = {'C':'G','T':'A','A':'T','G':'C'}
    return[comps[key] for key in dna]

def remove_interval(s, start, stop):
    """
    Removes the interval of characters from a string or list inclusively, 0 based
    EX: remove_intervals('ABCDEFGHI', 2, 5) will return 'ABGHI'.
    :param s: a string
    :param start: a non-negative integer
    :param stop: a non-negative integer greater than the start integer.
    :return: a string
    """
    return s[:start]+s[stop+1:]
example = 'ABCDEFGHI'
test1 = remove_interval(example, 2, 5)

def kmer_list(s, k):
    """
    Generates all kmers of size k for a string s and store them in a list
    :param s: any string
    :param k: any integer greater than zero
    :return: a list of strings
    """
    return[s[i:i+k] for i in range(0,len(s)-k+1)]
ex = '123456'
kmers = kmer_list(ex, 3)
def kmer_set(s, k):
    """
    Generates all kmers of size k for a string s and store them in a set
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    return {s[i:i+k] for i in range(0, len(s)-k+1)}
tetst = kmer_set(ex, 3)

def kmer_dict(s, k):
    """
    Generates all kmers of size k for a string s and store them in a dictionary with the
    kmer(string) as the key and the number of occurances of the kmer as the value(int).
    :param s: any string
    :param k: any integer greater than zero
    :return: a set of strings
    """
    return {s[i:i+k]: kmer_list(s, k).count(s[i:i+k]) for i in range(0, len(s)-k+1)}
tetst = kmer_dict(ex, 3)
# Reading Files
def head(file_name):
    """
    Prints the FIRST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    import os
    f = open(file_name)
    line = f.readline()
    count = 1
    while(line and count < 11):
        print(line)
        line = f.readline()
        count = count + 1
    return None
#f10 = head('t.txt')
def tail(file_name):
    """
    Prints the LAST 10 lines of a file
    :param file_name: a string
    :return: None
    """
    import os
    f = open(file_name)
    line = f.readline()
    lines = 10*[None]
    head = 0
    while(line):
        lines[head] = line
        head = (head+1)%10
        line = f.readline()
    for i in range(0, 10):
        #head = (head+1)%10
        print(lines[head])
        head = (head+1)%10
    return None
#l10 = tail('t.txt')
def print_even(file_name):
    """
    Prints the even numbered lines of a file
    :param file_name: a string
    :return: None
    """
    import os
    f = open(file_name)
    line = f.readline().strip()
    mod2 = 1
    while(line):
        if(mod2 == 0):
            print(line)
        line = f.readline().strip()
        mod2 = (mod2+1)%2
    return None
test = print_even('C:\\Users\stesu\OneDrive\Documents\Spring2018\BIO\\test_files\proper_fasta.fasta')
def csv_list(file_name):
    """
    Read in a CSV file to a 2D array (In python it is a list of lists)
    :param file_name: a string
    :return: a list of lists
    """
    import csv
    retlist = []
    with open(file_name) as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            retlist.append(line)
    return retlist
test = csv_list('c.csv')
def get_csv_column(file_name, column):
    """
    Reads in a CSV file and returns a list of values belonging to the column specified
    :param file_name: a string
    :param column: a positive integer
    :return: a list
    """
    import csv
    retlist = []
    mod2 = 1
    with open(file_name) as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            retlist.append(line[column])
    return retlist
test = get_csv_column('c.csv', 2)
def fasta_seqs(file_name):
    """
    Reads in a FASTA file and returns a list of only the sequences
    :param file_name: a string
    :return: a list of strings
    """
    import os
    f = open(file_name)
    line = f.readline()
    seqs = []
    totseqs = 0
    curseq = line.strip()
    while (line):
        while(line and not line.startswith('>')):
            curseq = curseq + line.strip()
            line = f.readline()
        line = f.readline()
        if(curseq and not curseq.startswith('>')):
            seqs.append(curseq)
        curseq = ''
    return seqs

def fasta_headers(file_name):
    """
    Reads in a FASTA file and returns a list of only the headers (Lines that start with ">")
    :param file_name: a string
    :return: a list of strings
    """
    import os
    f = open(file_name)
    line = f.readline()
    headers = []
    while (line):
        if(line.startswith('>')):
            headers.append(line.strip())
        line = f.readline()
    return headers
headers = fasta_headers('C:\\Users\stesu\OneDrive\Documents\Spring2018\BIO\\test_files\\tricky_fasta.fasta')
tailers = fasta_seqs('C:\\Users\stesu\OneDrive\Documents\Spring2018\BIO\\test_files\\tricky_fasta.fasta')
def fasta_dict(file_name):
    """
    Reads in a FASTA file and returns a dictionary of the format {header: sequence, ...}, where
    the sequence headers are keys and the sequence is the value
    :param file_name: a string
    :return: a dictionary
    """
    return dict(zip(fasta_headers(file_name), fasta_seqs(file_name)))

headers = fasta_dict('C:\\Users\\stesu\\OneDrive\\Documents\\Spring2018\BIO\\test_files\\tricky_fasta.fasta')

def fastq_to_fasta(file_name, new_name=None):
    """
    Reads in a FASTQ file and writes it to a new FASTA file. This definition should also
    keep the same file name and change the extension to from .fastq to .fasta if new_name is not specified.
    EX: fastq_to_fasta('ecoli.fastq') should write to a new file called ecoli.fasta
    :param file_name: a string
    :param new_name: a string
    :return: None
    """
    import os
    f = open(file_name)
    line = f.readline().strip()
    dict = {}
    while(line):
        if(line.startswith('@')):
            key = line.strip()
            value = f.readline().strip()
            line = f.readline().strip()
            while(not line.startswith('+')):
                value = value + line
                line = f.readline().strip()
            if(key and value):
                dict[key] = value
        line = f.readline().strip()
    return dict
testDict = fastq_to_fasta('C:\\Users\stesu\OneDrive\Documents\Spring2018\BIO\\test_files\proper_fastq.fastq')
# Transcription and Translation
def reverse_complement(dna):
    """
    Returns the strand of DNA that is the reverse complement of the sequence given
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, T, A, and G
    """
    comps = {'C': 'G', 'T': 'A', 'A': 'T', 'G': 'C'}
    return ''.join([comps[key] for key in dna[::-1]])
DNA = 'AAAATTTTTTGGGGGCCCC'
compl = reverse_complement(DNA)



def transcribe(dna):
    """
    Transcribes a string of DNA into RNA
    :param dna: a string containing only the characters C, T, A, and G
    :return: a string containing only the characters C, U, A, and G
    """
    return ''.join([letter if letter is not 'T' else 'U' for letter in dna])
transcript = transcribe(DNA)

def translate(rna):
    """
    Translates the strand of RNA given into its amino acid composition.
    DO NOT INCLUDE * IN YOUR RETURN STRING
    :param rna: a string containing only the characters C, U, A, and G
    :return: a string containing only the characters G, A, L, M, F, W, K, Q, E, S, P, V, I, C, Y, H, R, N, D, and T
    """
    RNA_CODON_TABLE = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
           "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
           "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
           "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
           "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
           "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
           "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
           "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
           "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
           "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
           "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
           "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
           "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
           "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
           "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
           "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}
    return ''.join([RNA_CODON_TABLE[rna[i:i+3]] if RNA_CODON_TABLE[rna[i:i+3]] is not "*" and len(RNA_CODON_TABLE[rna[i:i+3]]) is 3 else '' for i in range(0, len(rna)-2, 3)])
SPICY = translate('UCAUAAUAGCCGAUUUGUUAC')

def reading_frames(dna):
    """
    Generates a list of all 6 possible reading frames for a given strand of DNA
    For the non-biologists: https://en.wikipedia.org/wiki/Open_reading_frame
    :param dna: a string containing only the characters C, T, A, and G
    :return: a list of 6 strings containing only C, T, A, and G
    """
    frames = []
    frames.append(dna)
    frames.append(dna[1:])
    frames.append(dna[2:])
    rc = reverse_complement(dna)
    frames.append(rc)
    frames.append(rc[1:])
    frames.append(rc[2:])
    return frames
frames = reading_frames('AAAATTTCCG')
DNA = 'ACGCT'
compl = fast_complement(DNA)









quitter = 0