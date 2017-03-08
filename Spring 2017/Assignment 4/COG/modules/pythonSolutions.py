import numpy as np




humanDNA   = "CGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAACGAGATTGCCAGCACCGGG" \
			  "TATCATTCACCATTTTTCTTTTCGTTAACTTGCCGTCAGCCTTTTCTTTGACCTCTTCTTTCTGT"\
			  "TCATGTGTATTTGCTGTCTCTTAGCCCAGACTTCCCGTGTCCTTTCCACCGGGCCTTTGAGAGGT"\
			  "CACAGGGTCTTGATGCTGTGGTCTTCATCTGCAGGTGTCTGACTTCCAGCAACTGCTGGCCTGTG"\
			  "CCAGGGTGCAGCTGAGCACTGGAGTGGAGTTTTCCTGTGGAGAGGAGCCATGCCTAGAGTGGGAT"\
			  "GGGCCATTGTTCATG";

mouseDNA   = "CGCAATTTTTACTTAATTCTTTTTCTTTTAATTCATATATTTTTAATATGTTTACTATTAATGGTTATCATTCACCATTTAACTATTTGTTATTTTGACGTCATTTTTTTCTATTTCCTCTTTTTTCAATTCATGTTTATTTTCTGTATTTTTGTTAAGTTTTCACAAGTCTAATATAATTGTCCTTTGAGAGGTTATTTGGTCTATATTTTTTTTTCTTCATCTGTATTTTTATGATTTCATTTAATTGATTTTCATTGACAGGGTTCTGCTGTGTTCTGGATTGTATTTTTCTTGTGGAGAGGAACTATTTCTTGAGTGGGATGTACCTTTGTTCTTG";
unknownDNA = "CGCATTTTTGCCGGTTTTCCTTTGCTGTTTATTCATTTATTTTAAACGATATTTATATCATCGGGTTTCATTCACTATTTTTCTTTTCGATAAATTTTTGTCAGCATTTTCTTTTACCTCTTCTTTCTGTTTATGTTAATTTTCTGTTTCTTAACCCAGTCTTCTCGATTCTTATCTACCGGACCTATTATAGGTCACAGGGTCTTGATGCTTTGGTTTTCATCTGCAAGAGTCTGACTTCCTGCTAATGCTGTTCTGTGTCAGGGTGCATCTGAGCACTGATGTGGAGTTTTCTTGTGGATATGAGCCATTCATAGTGTGGGATGTGCCATAGTTCATG";

DNA_dict = {"human": humanDNA, "mouse": mouseDNA, "unknown": unknownDNA}

BASES = ["A", "T", "G", "C"]

def generate_random_sequence(lower_bound, upper_bound):
    # Determine random length
    sequence_length = np.random.randint(lower_bound, upper_bound)
    sequence_1 = ""

    for i in range(sequence_length):
        random_base = BASES[np.random.randint(len(BASES))]
        sequence_1 += random_base

    return sequence_1


def generate_random_sequences(lower_bound, upper_bound):

    # Determine random length
    sequence_length = np.random.randint(lower_bound, upper_bound)

    sequence_1 = ""
    sequence_2 = ""
    for i in range(sequence_length):
        random_base = BASES[np.random.randint(len(BASES))]
        sequence_1 += random_base

        if np.random.uniform() < 0.8:
            random_base = BASES[np.random.randint(len(BASES))]

        sequence_2 += random_base

    if np.random.uniform() < 0.1:
        sequence_2 += "A"

    return sequence_1, sequence_2


def problem1(sequence_1, sequence_2):
    hamming = 0
    score = 0.0

    if len(sequence_1) != len(sequence_2):
        return score

    for base1, base2 in zip(sequence_1, sequence_2):
        if base1 != base2:
            hamming += 1

    score = (len(sequence_1) - hamming) / len(sequence_2)

    return score


def problem2(species, sequence):
    genome = DNA_dict[species]
    if sequence not in genome:
        return ""

    positions = ""
    for genome_index in range(len(genome) - len(sequence)+1):
        genome_sequence = genome[genome_index:genome_index+len(sequence)]
        if sequence == genome_sequence:
            positions += " {}".format(genome_index+1)

    return positions


def problem3_helper(genome, user_sequence):
	best = 0

	for genome_index in range(len(genome) - len(user_sequence)+1):
		genome_sequence = genome[genome_index:genome_index+len(user_sequence)]

		score = problem1(genome_sequence, user_sequence)
		if score > best:
			best = score

	return best




def problem3(sequence):

	genome_scores = {"human" : 0, "mouse" : 0, "unknown" : 0}

	for species, genome in DNA_dict.items():
		genome_scores[species] = problem3_helper(genome, sequence)

	best_score = genome_scores["human"]
	if genome_scores["mouse"] > best_score:
		best_score = genome_scores["mouse"]

	if genome_scores["unknown"] > best_score:
		best_score = genome_scores["unknown"]

	best_matches = ["", "", ""]
	for species, genome_score in genome_scores.items():
		if genome_score == best_score:
			index = 0 if species == "human" else (1 if species == "mouse" else 2)
			best_matches[index] = species

	final_best = []
	for best_match in best_matches:
		if len(best_match) != 0:
			final_best.append(best_match)
	return final_best
