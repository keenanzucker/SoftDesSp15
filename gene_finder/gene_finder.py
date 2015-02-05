# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: ALIX MCCABE, KEENAN ZUCKER (PAIR PROGRAMMING WIZARDS)

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

    you can use the dictionary to set up a "matching" matrix and just return matching(nucleotide)
    it's magic
    """
    if nucleotide == "A":
        return 'T'    
    elif nucleotide == "G":
        return 'C'
    elif nucleotide == "T":
        return 'A'
    elif nucleotide == "C":
        return 'G'

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    li = list(dna)
    y = len(dna)

    li = li[::-1]

    i = 0

    while i < y:
        if li[i] == "A":
            li[i] = 'T'    
        elif li[i] == "G":
            li[i] = 'C'
        elif li[i] == "T":
            li[i] = 'A'
        elif li[i] == "C":
            li[i] = 'G'
        i = i+1

    """dna.replace("A","T") 
    dna.replace("T","A")
    dna.replace("G","C")
    dna.replace("C","G")"""
    # TODO: implement this
    
    return "".join(li)

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
    >>> rest_of_ORF("ATGAGACTAGG")
    'ATGAGACTAGG'
    >>> rest_of_ORF("ATGAGACTGGG")
    'ATGAGACTGGG'
    """

    li = dna
    y = len(dna)

    for l in range(0,y,3):
        if li[l:l+3] == 'TAG':
            return li[0:l]
        elif li[l:l+3] == 'TGA':
            return li[0:l]
        elif li[l:l+3] == 'TAA':
            return li[0:l]
    else:
        return li[0:y]

#print rest_of_ORF("ATGAGATAGG")
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    all_orfs=[]

    length = len(dna)
    length -= 1 if length%3 != 0 else 0
    length -= 1 if length%3 != 0 else 0

    i = 0

    #for i in range(0,length,3):
    while i<length:
        if dna[i:i+3] == 'ATG':
            y = rest_of_ORF(dna[i:])
            if y == None:
                i += 3
                continue
            x = len(y)
            all_orfs.append(dna[i:x+i])
            i = i + x
        else: 
            i = i + 3

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


    x = find_all_ORFs_oneframe(dna)

    y = find_all_ORFs_oneframe(dna[1:])

    z = find_all_ORFs_oneframe(dna[2:])

    l = [x,y,z]

    allORFs = [item for sublist in l for item in sublist]

    return allORFs
#print find_all_ORFs("ATGCCCATGAACTAACATGCCGTAG")

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
    x = find_all_ORFs(dna)

    comp = get_reverse_complement(dna)
    
    y = find_all_ORFs(comp)

    l = [x,y]
    allORFsBoth = [item for sublist in l for item in sublist]

    return allORFsBoth

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
    y = []

    for i in range (0, num_trials - 1):
        x = shuffle_string(dna)

        z = longest_ORF(x)

        y.append(z)

    for z in y:
        if len(z) > longest:
            longest = len(z) 

    return longest
       # print longest_ORFs 

    #length = len(str(longest_ORF(string))

#print longest_ORF_noncoding("ATGCGAATGTAGCATCAAA", 1500)

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    y = []
    for i in range(0,len(dna)-1,3):
        x = dna[i:i+3]
        if len(x)==3:
            #print aa_table[x]
            y.append(aa_table[x])
        else:
            continue

    return ''.join(y)

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

    return [coding_strand_to_AA(ORF) for ORF in all_ORF if len(ORF) > threshold]


"""if "__name__ == __main__":
tells the program what to run automatically when the program is initiated"""

print gene_finder(dna,longest_ORF_noncoding(dna,1500))

if __name__ == "__main__":
    import doctest          #doctest isjust a specific way of accessing the automatic programs
    doctest.testmod()
