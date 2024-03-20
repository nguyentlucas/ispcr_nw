#!/usr/bin/env python3

import subprocess

def ispcr(primer_file: str, assembly_file: str, max_amplicon_size: int) -> str:
	#block1
	shell_command = "blastn -query " + primer_file + " -subject " + assembly_file + " -task blastn-short -outfmt '6 std qlen' | awk '$3>=80 && $4==$13'"
	step_one_result = subprocess.run([shell_command], capture_output=True, text=True, shell=True, executable="/bin/bash")
	sorted_hits = [ele.split("\t") for ele in step_one_result.stdout.strip().split("\n")]
	# print(sorted_hits)
	#block2
	paired_hits=[]
	for i in range(len(sorted_hits)):
		primer_name_1, _, _, _, _, _, _, _, five_prime_1, three_prime_1, *_ = sorted_hits[i]
		for j in range(i+1, len(sorted_hits)):
			primer_name_2, _, _, _, _, _, _, _, five_prime_2, three_prime_2, *_ = sorted_hits[j]
			if primer_name_1 == primer_name_2:
				break
			elif abs(int(three_prime_2) - int(three_prime_1)) > max_amplicon_size:
				break
			elif ((int(three_prime_1)-int(five_prime_1)) > 0) and (int(five_prime_1)<int(five_prime_2)):
				paired_hits.append((sorted_hits[i],sorted_hits[j]))
			elif ((int(three_prime_1)-int(five_prime_1)) < 0) and (int(five_prime_1)>int(five_prime_2)):
				paired_hits.append((sorted_hits[i],sorted_hits[j]))
	#print(paired_hits)
	#block3
	file = open("bed_file", 'w')
	line=""
	for pair in paired_hits:
		if int(pair[0][9]) - int(pair[0][8]) > 0:
			_, contig, _, _, _, _, _, _, five_prime_1, three_prime_1, *_ = pair[0]
			_, _, _, _, _, _, _, _, five_prime_2, three_prime_2, *_ = pair[1]
			line= line + contig + "\t" + three_prime_1 + "\t" + str(int(three_prime_2)-1) + "\n"
		else:
			_, contig, _, _, _, _, _, _, five_prime_1, three_prime_1, *_ = pair[1]
			_, _, _, _, _, _, _, _, five_prime_2, three_prime_2, *_ = pair[0]
			line= line + contig + "\t" + three_prime_1 + "\t" + str(int(three_prime_2)-1) + "\n"
	file.write(line.strip())
	file.close()
	#print(line)
	seqtk_comm = "seqtk subseq " + assembly_file + " " + "bed_file"
	result_3 = subprocess.run([seqtk_comm], capture_output=True, text=True, shell=True, executable="/bin/bash")
	#print(result_3.stdout)
	return(result_3.stdout)

# test call
# ispcr("../data/rpoD.fna", "../data/Pseudomonas_protegens_CHA0.fna", 2000)