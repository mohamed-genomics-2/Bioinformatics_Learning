from Bio import Align

# 1. Define our sequences (Same as before, with the slight difference)
seq1 = "ACCTTGTCCTCTTTGCCC"
seq2 = "ACCTTGTCCTATTGCCC" 

# 2. Set up the Aligner (The "Machine")
aligner = Align.PairwiseAligner()

# 3. Configure the "Game Rules" (Scoring)
aligner.mode = 'global'  # We want to align the WHOLE sequence from start to end
aligner.match_score = 1.0
aligner.mismatch_score = -1.0
aligner.open_gap_score = -2.0  # Penalty for opening a gap
aligner.extend_gap_score = -1.0 # Penalty for making an existing gap longer

# 4. Run the alignment
# The aligner finds the best possible mathematical arrangement
alignments = aligner.align(seq1, seq2)

# 5. Show the results
print(f"Total alignments found: {len(alignments)}")
best_alignment = alignments[0]
print(f"Best Score: {best_alignment.score}")

print("\nVisual Alignment:")
print(best_alignment)