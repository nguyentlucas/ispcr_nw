# ispcr_nw
ispcr_nw is a python package for CLI that does in silico PCR and Needleman-Wunsch global allignment in a series.

The package includes two functinal modules: **ispcr** and **nw**:
1. **ispcr** does in silico PCR on an assembly with a provided primer sequence.
2. **nw** does Needleman-Wunsch global allignment on two sequences to find the optimal allignment.

The whole package performs ispcr on two assemblies and align the produced amplicons. The help page is as follow:
```
usage: ispcr_nw.py [-h] -1 ASSEMBLY1 -2 ASSEMBLY2 -p PRIMERS -m MAX_AMPLICON_SIZE --match MATCH --mismatch MISMATCH --gap GAP

Perform in-silico PCR on two assemblies and align the amplicons

options:
  -h, --help            show this help message and exit
  -1 ASSEMBLY1          Path to the first assembly file
  -2 ASSEMBLY2          Path to the second assembly file
  -p PRIMERS            Path to the primer file
  -m MAX_AMPLICON_SIZE  Maximum amplicon size for isPCR
  --match MATCH         Match score to use in alignment
  --mismatch MISMATCH   Mismatch penalty to use in alignment
  --gap GAP             Gap penalty to use in alignment
```
The repo provides sample data in the `data` folder. If following command is ran:
```
$ ./amplicon_align.py -1 data/Pseudomonas_aeruginosa_PAO1.fna -2 data/Pseudomonas_protegens_CHA0.fna -p data/rpoD.fna -m 2000 --match 1 --mismatch=-1 --gap=-1
```
the expected output would be:
```
TCTCGGCGA-CGGTC-AG-CTCGACCTCG-CTTTCCAGGGCCGCCAGCTTCTGCTGGTTGCGCAGGATGT-CGTCGC
GCAGGCGCTCGATGGCCTCGGCGTACTT-CGGCTTG-CTCTT---CAGGACGCTGTCGACCCA-CTTCTCGT
CGGTCTCGTGGTTCGGGAACAGGCGCAGGAAGTCGGCACGCGGCATGCGCGCGTCACGCACGCAGAGCTGCATGATGGCGCGT
 TCCTG
GGCGCGCACGCCTTCCAGGGCGGAGCGCACGCGGGCGACCAGGGCGTCGAACTGCTTGGGCACCAGCTTGATCGGCATGAACA
 GCTCGGCCA-GGCCGGTGAGTTCGGCGGTGGCCTGCTTGCTGC-CGCGACCGTGCTTCTTCAGGGCCTT-CTTG
GCCTTGTCGAGCTGCTCGGAGACCGCGGTGAAA-CGCAG-GCGG
GCTTCTTCCGGATCCGGACCGCCGTCGCCTTCGTCGTCG-CTGTCGCT-GCTGTCGTCGC-T-TTCTTCTTC
CTCGTCGTCCTTCTCTTTCG-AGTCGGCGGAATCGTCCTTCAGGTTGACCGGCTCCACCTCTTCGGCGGGCAGGC---
TGCCGTCAT
CGGGATCGATATAGCCGCTGAGGACGTCGGAGAGGCGACCGCCTTCGGCGACGATGCGATTGTAGTCGGCCAGGATGCTG
TCCACCGTGCCCGGGAACTGGGCGATGGCGCTCATCACTTCGCGGATGCCTTCCTCGATG 
TCTCGGCGATC-TTCAAGCCT-G-TTTCGAC-TTCAAGAGCGGTCAGCTTCTGCTGGCAACGGATGATGTCCG-
GCTGCAGGCGGGCGATGGCTTCGGCGTACTTGC-TCTTGCCT-TTGGCCAGG--GC-GTCGGTCCAGCTT-TCATCCACT
TCGTTGCCCGGGAACTGGCGCAGGAAGTCGGCACGTGGCATGCGGGCATCACGCACGCAGAGCTGCATGATGGCGCGTTCCTG
 CTG
GCGCAGGCGATCCAGGGCACTGCGTACACGTTCAACCAGGCCTTCGAATTGCTTCGGAACCAGTTTGATCGGCATGAACAGTT
 CAGCCAGGGCCAG-CATTTCGGCGATGGCTTGCTTG-TTCTCGCGGCCGTGTTTCTTCAGCGCCTTGCGGGTGAC-T
TCCATCTGGTCGGCGACGGC-GCCAAAGCGCTGTGCGGCG-AT-GACCGGATCCGGACCGCTTTCGGCTTCTTCTTCGTCT
TCGGTCGCT-TC--CGCTTCTTCGTCTTCGCT-GTCGTCATCCGCTTTCGCGGTC-TTGG--T-GT-CGACA-G--G-
CGGCGGCACTTCGGCGGCAGGC-GGCGTAATGCCGTCATCCGGG
TCGATGTACCCGCTGAGAACGTCGGACAGGCGTCCACCTTCGGTGGTGACGCGAGTGTACTCGGAGAGGATG
TGATCAACCGTGCCAGGGAAGTGCGCGATTGCGCCCATCACTTCACGGATACCCTCTTCGATA 
368
```
