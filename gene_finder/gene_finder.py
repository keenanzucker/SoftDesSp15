# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: ALIX MCCABE AND KEENAN ZUCKER

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

dna = load_seq("./data/X73525.fa")

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    This doctest is sufficient to test this code - We decided we didn't need to add anything else

    you can use the dictionary to set up a "matching" matrix and just return matching(nucleotide)
    it's magic
    """
    nucl_matchings = {"A": "T", "T": "A", "G": "C", "C": "G"}
    return nucl_matchings[nucleotide]

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string

        We decided that these doctests were sufficient for our purposes and managed the 
        edge cases well

    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    reverse_strand = dna[::-1]

    comp = ''
    for nucl in reverse_strand:
         comp += get_complement(nucl)
    
    return comp

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'

    We decided to test more edge cases - in particilar if there is no stop codon or a stop
    codon out of frame

    >>> rest_of_ORF("ATGAGACTAGG")
    'ATGAGACTAGG'
    >>> rest_of_ORF("ATGAGACTGGG")
    'ATGAGACTGGG'
    """

    length = len(dna)

    #Finding the stop codons
    for l in range(0,length,3):
        if dna[l:l+3] == 'TAG':
            return dna[0:l]
        elif dna[l:l+3] == 'TGA':
            return dna[0:l]
        elif dna[l:l+3] == 'TAA':
            return dna[0:l]
    else:
        return dna[0:length]


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    We decided this doctest was sufficient to prove validity of our code

    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    all_orfs=[]

    #checks to see if reading frame is multiple of 3
    length = len(dna)
    length -= 1 if length%3 != 0 else 0
    length -= 1 if length%3 != 0 else 0

    i = 0

    #loops through reading frames that are multiples of 3, non-nested
    while i<length:
        if dna[i:i+3] == 'ATG':
            restORF = rest_of_ORF(dna[i:])
            if restORF == None:
                i += 3
                continue
            ORFlength = len(restORF)
            all_orfs.append(dna[i:ORFlength+i])
            i = i + ORFlength
        else: 
            i = i + 3
        #if no ORF is found, continue search

    return all_orfs

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']

    We added a test to ensure that our function doesn't return nested ORFs in the same frame.

    >>> find_all_ORFs("ATGCCCATGAACTAACATGCCGTAG")
    ['ATGCCCATGAAC', 'ATGCCG']
    """

    #First reading frame
    ORFFrame = find_all_ORFs_oneframe(dna)

    #second reading frame
    ORFFrame.extend(find_all_ORFs_oneframe(dna[1:]))

    #third reading frame
    ORFFrame.extend(find_all_ORFs_oneframe(dna[2:]))

    return ORFFrame


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']

    We implemented another test in order to check a longer, more complicated strand with ORFs in more frames
    in in more frames in the reverse direction

    >>> find_all_ORFs_both_strands("ATGCCCCCCTAACATGCCCCCCTAGCCATGCCCCCC")
    ['ATGCCCCCC', 'ATGCCCCCC', 'ATGCCCCCC', 'ATGTTAGGGGGGCAT', 'ATGGCTAGGGGGGCATGT']
    """
    allORFs = find_all_ORFs(dna)

    comp = get_reverse_complement(dna)

    #adds ORFs from reverse complement to forward strand
    allORFs.extend(find_all_ORFs(comp))

    return allORFs

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'

    In the above case study we implemented, the longest ORF IS in the compliment
    
    In the below, the longest ORF is in a non-original frame and is not terminated by a stop codon,
    which is completely plausible

    >>> longest_ORF("ATGCCGAATGCCATGCAATTGTAGCATATGCCTATTCGATAG")
    'ATGCCATGCAATTGTAGCATATGCCTATTCGATAG'
    """
    longest = ''
    all_ORFs = find_all_ORFs_both_strands(dna)
    
    for i in range (0 , len(all_ORFs)):
        if len(all_ORFs[i]) > len(longest):
            longest = all_ORFs[i]

    return longest

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF 
    
    there's no way to check this because it's randomly combined each time

    """
    longest = 0
    ListOfLongest = []

    #Loops through all trials, checking shuffled strings for ORFs
    for i in range (0, num_trials - 1):
        shuffled = shuffle_string(dna)

        longestShuffled = longest_ORF(shuffled)

        #appends found ORFs to list
        ListOfLongest.append(longestShuffled)

    for longestShuffled in ListOfLongest:
        #Finds the longest out of all longest ORFs
        if len(longestShuffled) > longest:
            longest = len(longestShuffled) 

    #Returns the threshold
    return longest
       
def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'

        We added a slightly longer doctest to ensure effectiveness

        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """

    ListAmino = []

    #loops through all dna codons, assigns amino acid letters from dictionary
    for i in range(0,len(dna)-1,3):
        codons = dna[i:i+3]
        if len(codons)==3:
            ListAmino.append(aa_table[codons])

    return ''.join(ListAmino)

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    all_ORF = find_all_ORFs_both_strands(dna)

    #Only returns amino acids longer than threshold
    return [coding_strand_to_AA(ORF) for ORF in all_ORF if len(ORF) > threshold]


"""if "__name__ == __main__":
tells the program what to run automatically when the program is initiated"""

print gene_finder(dna,longest_ORF_noncoding(dna,1500))

if __name__ == "__main__":
    import doctest          #doctest isjust a specific way of accessing the automatic programs
    doctest.testmod()

