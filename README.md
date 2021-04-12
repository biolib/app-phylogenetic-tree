# Phylogenetic-Tree
This tool returns a distance phylogenetic tree from a multi FASTA file as input. First, it aligns the input sequences with MUSCLE and calculates a distance matrix of the alignment to build the tree. Finally, it draws the phylogenetic tree.

#### ####

**Input:** A FASTA file with three or more sequences. The sequences can be DNA, RNA or protein. 

**Output:** The phylogenetic tree is build in either Neighbor-Joining approach or UPGMA approach. 

### Example: 

**Input:**

```
>sequence1
ACTCCCCGTGCGCGCCCGGCCCGTAGCGTCCTCGTCGCCGCCCCTCGTCTCGCAGCCGCAGCCCGCGTGG
ACGCTCTCGCCTGAGCGCCGCGGACTAGCCCGGGTGGCC
>sequence2
CAGTCCGGCAGCGCCGGGGTTAAGCGGCCCAAGTAAACGTAGCGCAGCGATCGGCGCCGGAGATTCGCGA
ACCCGACACTCCGCGCCGCCCGCCGGCCAGGACCCGCGGCGCGATCGCGGCGCCGCGCTACAGCCAGCCT
CACTGGCGCGCGGGCGAGCGCACGGGCGCTC
>sequence3
CACGACAGGCCCGCTGAGGCTTGTGCCAGACCTTGGAAACCTCAGGTATATACCTTTCCAGACGCGGGAT
CTCCCCTCCCC
>sequence4
CAGCAGACATCTGAATGAAGAAGAGGGTGCCAGCGGGTATGAGGAGTGCATTATCGTTAATGGGAACTTC
AGTGACCAGTCCTCAGACACGAAGGATGCTCCCTCACCCCCAGTCTTGGAGGCAATCTGCACAGAGCCAG
TCTGCACACC
```

**Output:**

![phylogenetic tree](images/tree.png)
