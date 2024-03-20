#!/usr/bin/env python3

import argparse
import ispcr_nw

p = argparse.ArgumentParser(description="Perform in-silico PCR on two assemblies and align the amplicons")
    
p.add_argument('-1', dest="ASSEMBLY1", required=True, help="Path to the first assembly file")
p.add_argument('-2', dest="ASSEMBLY2", required=True, help="Path to the second assembly file")
p.add_argument('-p', dest="PRIMERS", required=True, help="Path to the primer file")
p.add_argument('-m', dest="MAX_AMPLICON_SIZE", type=int, required=True, help="Maximum amplicon size for isPCR")
p.add_argument('--match', dest="MATCH", type=int, required=True, help="Match score to use in alignment")
p.add_argument('--mismatch', dest="MISMATCH", type=int, required=True, help="Mismatch penalty to use in alignment")
p.add_argument('--gap', dest="GAP", type=int, required=True, help="Gap penalty to use in alignment")

args = p.parse_args()

# print(args)
# print(args.ASSEMBLY1)
#------------------------------------------------
amplicon_1 = ispcr_nw.ispcr(args.PRIMERS, args.ASSEMBLY1, args.MAX_AMPLICON_SIZE).strip().split('\n')[1]
# print(amplicon_1)
amplicon_2 = ispcr_nw.ispcr(args.PRIMERS, args.ASSEMBLY2, args.MAX_AMPLICON_SIZE).strip().split('\n')[1]
# print(amplicon_2)
amplicon_2_compl = ""
for base in amplicon_2:
	if base=="A":
		amplicon_2_compl+="T"
	if base=="T":
		amplicon_2_compl+="A"
	if base=="G":
		amplicon_2_compl+="C"
	if base=="C":
		amplicon_2_compl+="G"
amplicon_2_rev_compl=amplicon_2_compl[::-1]
#-----------
FF, FF_score = ispcr_nw.needleman_wunsch(amplicon_1, amplicon_2, args.MATCH, args.MISMATCH, args.GAP)
# print(FF_score)
FR, FR_score = ispcr_nw.needleman_wunsch(amplicon_1, amplicon_2_rev_compl, args.MATCH, args.MISMATCH, args.GAP)
# print(FR_score)

if FF_score>FR_score:
	print(FF[0])
	print(FF[1])
	print(FF_score)
else:
	print(FR[0])
	print(FR[1])
	print(FR_score)