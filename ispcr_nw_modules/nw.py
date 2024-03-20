#!/usr/bin/env python3

def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
	
	# Inititate a matrix
	matrix = []
	for i in range(len(seq_a)+1):
		row=[[] for _ in range(len(seq_b)+1)]
		matrix.append(row)

	# for row in matrix:
	# 	print(row)
	#--------------------------------------------------------	
	# NW
	## gap left-most row and top-most row
	gap_number = 0
	for i in range(len(seq_a)+1):
		matrix[i][0] = [gap_number]
		gap_number-=1
	gap_number = 0
	for i in range(len(seq_b)+1):
		matrix[0][i] = [gap_number]
		gap_number-=1

	# for row in matrix:
	# 	print(row)
	## filling up the rest of the cells
	for i in range(len(seq_a)):
		for j in range(len(seq_b)):
			a_coordinate = i+1
			b_coordinate = j+1
			horizontal_gap_score = matrix[i+1][j][0] + gap
			vertical_gap_score = matrix[i][j+1][0] + gap
			if seq_a[i] == seq_b[j]:
				match_score = matrix[i][j][0] + match
			else:
				match_score = matrix[i][j][0] + mismatch
			# finding highest score
			score_list = [horizontal_gap_score, vertical_gap_score, match_score]
			#print(score_list)
			high_score = score_list[0]
			for a in range(len(score_list)):
				if score_list[a] > high_score:
					high_score = score_list[a]
			#print(high_score)
			# fill in cell
			matrix[a_coordinate][b_coordinate] = [high_score]
	final_score=matrix[len(seq_a)][len(seq_b)][0]
	# print(final_score)
	# for row in matrix:
	# 	print(row)
	#print(matrix[len(seq_a)])
	## trace back
	horizontal_seq_reverse=""
	vertical_seq_reverse=""
	k = len(seq_a)
	h = len(seq_b)
	while  h>0 or k>0:
		if (matrix[k][h][0] == matrix[k-1][h-1][0] +1) and (seq_a[k-1] == seq_b[h-1]):
			vertical_seq_reverse+=seq_a[k-1]
			horizontal_seq_reverse+=seq_b[h-1]
			k-=1
			h-=1
			# print("a")
		elif (matrix[k][h][0] == matrix[k-1][h-1][0] -1) and (seq_a[k-1] != seq_b[h-1]):
			vertical_seq_reverse+=seq_a[k-1]
			horizontal_seq_reverse+=seq_b[h-1]
			k-=1
			h-=1
			# print("b")
		elif matrix[k][h][0] == matrix[k-1][h][0] -1:
			vertical_seq_reverse+=seq_a[k-1]
			horizontal_seq_reverse+="-"
			k-=1
			# print("d")
		elif matrix[k][h][0] == matrix[k][h-1][0] -1:
			vertical_seq_reverse+="-"
			horizontal_seq_reverse+=seq_b[h-1]
			h-=1
			# print("c")
		
	# print(horizontal_seq_reverse)
	# print(vertical_seq_reverse)
	horizontal_seq_forward = horizontal_seq_reverse[::-1]
	vertical_seq_forward = vertical_seq_reverse[::-1]
	# print(horizontal_seq_forward)
	# print(vertical_seq_forward)
	# print(final_score)
	return (vertical_seq_forward, horizontal_seq_forward), final_score
	#--------------------------------------------------------

# 	# Calling algo with test case
# needleman_wunsch("TAGTCAT", "TATCAAT", 1, -1, -1)